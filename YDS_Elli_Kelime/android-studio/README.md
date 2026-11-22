# Nyeals · Android Studio projesi (Play Store için AAB)

Play Store yeni uygulamalarda APK değil **AAB** (Android App Bundle) ve **API 36** hedefi ister. Bu proje onu üretir.
`android/` klasöründeki eski yol (KELIME kabuğunu yeniden paketleyen `build_apk.py`) yalnız elden kurulan deneme APK'sı içindir.

## Ne var?

- `app/src/main/java/com/nefata/nyeals/MainActivity.java`: tek ekranlık kabuk. Uygulamanın kendisi olan `index.html`'i bir
  WebView'de açar; kelimeleri cihazın konuşma motoruyla okur (`KelimeApp.speak / stop`), geri tuşunu sayfaya iletir
  (`window.kelimeBack`), tema değişince durum çubuğunun zeminini boyar (`KelimeApp.bar`).
- `app/build.gradle`: paket kimliği `com.nefata.nyeals`, `minSdk 24`, `targetSdk 36`. Derleme sırasında depodaki
  `../index.html` pakete kopyalanır (yedek Google Fonts bağlantısı çıkarılır; uygulama internete bağlanmaz).
- İzinler: yalnız `VIBRATE`. `INTERNET` izni yoktur.
- Kütüphane bağımlılığı yoktur (AndroidX bile); yalnız Android'in kendi sınıfları kullanılır.

## Derleme

1. Önce uygulamayı üretin: depo kökünde `python3 src/build.py` (`index.html` güncellenir).
2. Android Studio'da **bu klasörü** (`android-studio`) açın. İlk açılışta Android SDK 36'yı indirmeyi ve lisansını kabul etmeyi önerir.
3. İmza için `keystore.properties.example` dosyasını `keystore.properties` adıyla kopyalayıp doldurun.
   Anahtar dosyası ve parolası depoya girmez; `.gitignore` bunları dışarıda tutar.
4. **Build > Generate Signed App Bundle** ya da komut satırından:

   ```
   ./gradlew bundleRelease
   ```

   Çıktı: `app/build/outputs/bundle/release/app-release.aab`

Elden kurmak için APK: `./gradlew assembleRelease` → `app/build/outputs/apk/release/app-release.apk`.

## Play Console'a yükleme

1. Play Console > **Uygulama oluştur** (ad: Nyeals). Paket kimliği ilk yüklemeyle kesinleşir ve **bir daha değişmez**: `com.nefata.nyeals`.
2. **Test > Kapalı test** > yeni sürüm oluştur > `app-release.aab` dosyasını yükle. Play Uygulama İmzalama'yı kabul edin;
   elinizdeki anahtar "yükleme anahtarı" olur ve sonraki her sürüm aynı anahtarla imzalanmalıdır.
3. Testçi listesini ekleyin, katılım bağlantısını paylaşın.
4. Mağaza girişi için gerekenler: kısa ve uzun açıklama, ekran görüntüleri, 512 px simge, gizlilik politikası adresi
   (taslak: depo kökünde `GIZLILIK.md`), veri güvenliği formu ("veri toplanmıyor"), yaş derecelendirme anketi.

## Her yeni sürümde

`app/build.gradle` içindeki `versionCode` bir artırılır (1, 2, 3…); Play aynı numarayı iki kez kabul etmez. `versionName` görünen addır.

## Bilinen durum

Kabuk kodu Android 16 sınıflarına karşı derleme denetiminden geçti; gerçek AAB derlemesi ve telefonda deneme henüz yapılmadı.
İlk derlemede bakılacaklar: sesli okuma, geri tuşu, titreşim, durum çubuğunun altında kalan içerik olmaması.
