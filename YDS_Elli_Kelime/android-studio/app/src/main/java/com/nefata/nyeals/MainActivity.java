package com.nefata.nyeals;

import android.app.Activity;
import android.content.res.Configuration;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import android.window.OnBackInvokedCallback;
import android.window.OnBackInvokedDispatcher;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Locale;

/**
 * Nyeals'ın Android kabuğu. Uygulamanın kendisi assets/www/index.html içindeki tek dosyalık web sayfasıdır;
 * bu sınıf onu bir WebView'de açar ve üç köprü sağlar:
 *   - KelimeApp.speak(metin, hız) ve KelimeApp.stop(): kelimeleri cihazın konuşma motoruyla okur,
 *   - KelimeApp.bar(renk): tema değişince durum çubuğunun arkasındaki zemini boyar,
 *   - geri tuşu: sayfadaki window.kelimeBack() bir önceki ekrana döner; ana menüdeyse uygulama arka plana geçer.
 * Sayfa https://appassets.androidplatform.net/ adresinden sunulur gibi görünür ama her istek paketin içinden
 * karşılanır; uygulama internete bağlanmaz (INTERNET izni de yoktur).
 */
public class MainActivity extends Activity implements TextToSpeech.OnInitListener {
    private static final String HOST = "appassets.androidplatform.net";
    private static final String START = "https://" + HOST + "/index.html";

    private FrameLayout root;
    private WebView web;
    private TextToSpeech tts;
    private boolean ttsReady;
    private OnBackInvokedCallback backCallback;

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);

        root = new FrameLayout(this);
        root.setBackgroundColor(getColor(R.color.app_bg));
        web = new WebView(this);
        web.setBackgroundColor(getColor(R.color.app_bg));
        web.setOverScrollMode(View.OVER_SCROLL_NEVER);
        root.addView(web, new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        setContentView(root);

        // Android 15 ve sonrası uygulamayı kenardan kenara çizer: durum ve gezinme çubuklarının payı dolgu olarak verilir.
        root.setOnApplyWindowInsetsListener((v, insets) -> {
            int l, t, r, b;
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
                android.graphics.Insets i = insets.getInsets(WindowInsets.Type.systemBars() | WindowInsets.Type.displayCutout() | WindowInsets.Type.ime());
                l = i.left; t = i.top; r = i.right; b = i.bottom;
            } else {
                l = insets.getSystemWindowInsetLeft(); t = insets.getSystemWindowInsetTop();
                r = insets.getSystemWindowInsetRight(); b = insets.getSystemWindowInsetBottom();
            }
            v.setPadding(l, t, r, b);
            return insets;
        });

        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);                     // ilerleme localStorage'da tutulur
        s.setMediaPlaybackRequiresUserGesture(false);
        s.setTextZoom(100);                               // sistem yazı boyutu yerleşimi bozmasın
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(false);

        web.addJavascriptInterface(new Kopru(), "KelimeApp");
        web.setWebViewClient(new WebViewClient() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
                Uri u = request.getUrl();
                if (HOST.equals(u.getHost())) {
                    String path = u.getPath();
                    if (path == null || path.isEmpty() || "/".equals(path)) path = "/index.html";
                    try {
                        InputStream in = getAssets().open("www" + path);
                        return new WebResourceResponse(mime(path), "UTF-8", in);
                    } catch (IOException e) {
                        return empty(404, "Not Found");
                    }
                }
                return empty(403, "Blocked");               // paketin dışına hiçbir istek çıkmaz
            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                return !HOST.equals(request.getUrl().getHost());
            }
        });

        tts = new TextToSpeech(this, this);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            backCallback = this::goBack;
            getOnBackInvokedDispatcher().registerOnBackInvokedCallback(OnBackInvokedDispatcher.PRIORITY_DEFAULT, backCallback);
        }

        if (state == null || web.restoreState(state) == null) web.loadUrl(START);
    }

    private static String mime(String path) {
        String p = path.toLowerCase(Locale.ROOT);
        if (p.endsWith(".html")) return "text/html";
        if (p.endsWith(".js")) return "application/javascript";
        if (p.endsWith(".css")) return "text/css";
        if (p.endsWith(".json") || p.endsWith(".webmanifest")) return "application/json";
        if (p.endsWith(".svg")) return "image/svg+xml";
        if (p.endsWith(".png")) return "image/png";
        if (p.endsWith(".woff2")) return "font/woff2";
        return "application/octet-stream";
    }

    private static WebResourceResponse empty(int code, String reason) {
        return new WebResourceResponse("text/plain", "UTF-8", code, reason, new HashMap<String, String>(), new ByteArrayInputStream(new byte[0]));
    }

    /** Geri: sayfa bir önceki ekrana dönebiliyorsa döner; ana menüdeyse uygulama arka plana geçer (ilerleme kaybolmaz). */
    private void goBack() {
        web.evaluateJavascript("(window.kelimeBack && window.kelimeBack()) ? 'ok' : 'no'", value -> {
            if (value == null || !value.contains("ok")) moveTaskToBack(true);
        });
    }

    @Override
    @SuppressWarnings("deprecation")
    public void onBackPressed() {                           // Android 12 ve öncesi
        goBack();
    }

    @Override
    public void onInit(int status) {
        if (status != TextToSpeech.SUCCESS) return;
        int r = tts.setLanguage(Locale.US);
        ttsReady = r != TextToSpeech.LANG_MISSING_DATA && r != TextToSpeech.LANG_NOT_SUPPORTED;
    }

    /** Sayfanın çağırdığı köprü (window.KelimeApp). Çağrılar WebView'in kendi iş parçacığından gelir. */
    private final class Kopru {
        @JavascriptInterface
        public void speak(String text, float rate) {
            if (!ttsReady || text == null) return;
            tts.setSpeechRate(rate > 0 ? rate : 1f);
            tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, "nyeals");
        }

        @JavascriptInterface
        public void stop() {
            if (tts != null) tts.stop();
        }

        /** Tema zemini: boş metin varsayılan renge döner. Durum çubuğu simgeleri zeminin açıklığına göre seçilir. */
        @JavascriptInterface
        public void bar(final String hex) {
            runOnUiThread(() -> {
                int c = getColor(R.color.app_bg);
                boolean set = false;
                if (hex != null && !hex.isEmpty()) {
                    try { c = Color.parseColor(hex); set = true; } catch (IllegalArgumentException ignored) { }
                }
                root.setBackgroundColor(c);
                web.setBackgroundColor(c);
                boolean night = (getResources().getConfiguration().uiMode & Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES;
                boolean light = set ? Color.luminance(c) > 0.5f : !night;
                lightBars(light);
            });
        }
    }

    @SuppressWarnings("deprecation")
    private void lightBars(boolean light) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            WindowInsetsController ic = getWindow().getInsetsController();
            if (ic != null) {
                int mask = WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS | WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS;
                ic.setSystemBarsAppearance(light ? mask : 0, mask);
            }
        } else {
            View d = getWindow().getDecorView();
            int f = d.getSystemUiVisibility();
            int bit = View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR | (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O ? View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR : 0);
            d.setSystemUiVisibility(light ? (f | bit) : (f & ~bit));
        }
    }

    @Override
    protected void onSaveInstanceState(Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);
    }

    @Override
    protected void onPause() {
        if (tts != null) tts.stop();
        web.onPause();
        super.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        web.onResume();
    }

    @Override
    protected void onDestroy() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU && backCallback != null) {
            getOnBackInvokedDispatcher().unregisterOnBackInvokedCallback(backCallback);
        }
        if (tts != null) { tts.stop(); tts.shutdown(); }
        root.removeView(web);
        web.destroy();
        super.onDestroy();
    }
}
