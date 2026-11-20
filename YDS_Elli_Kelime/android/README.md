# Android paketi (Nyeals.apk)

Uygulama, önceki KELIME 0.4.0 uygulamasının WebView kabuğuyla paketlenir. Kabuk `assets/www/index.html` dosyasını
açar; ses (`KelimeApp.speak`, `KelimeApp.stop`) ve geri tuşu (`window.kelimeBack`) köprülerini sağlar.

- `base/`: KELIME 0.4.0 APK'sından alınan kabuk dosyaları (manifest, classes.dex, resources.arsc, uyarlanabilir simge).
- `build_apk.py`: manifesti yeni paket adı (`com.nefata.nyeals`) ve uygulama adıyla (`Nyeals`) yeniden yazar,
  renkleri günceller, `index.html` ve simgeleri ekler; imzasız APK üretir.
  Kısa titreşimler (`navigator.vibrate`) için manifeste `android.permission.VIBRATE` izni de eklenir (kurulumda verilen olağan izin).
- `v2sign.py`: APK Signature Scheme v2 ile imzalar (Python `cryptography` paketi gerekir).
- `icons/`: başlatıcı simgeleri.

```
python3 android/build_apk.py android/base index.html android/icons /tmp/Nyeals-unsigned.apk
python3 android/v2sign.py ANAHTAR.p12 PAROLA /tmp/Nyeals-unsigned.apk dist/Nyeals.apk
```

İmza anahtarı (`basamak-release.p12`) depoda tutulmaz. Güncellemelerin eski kurulumun üzerine yüklenebilmesi için
her sürüm aynı anahtarla imzalanmalıdır; anahtarı ve parolasını güvenli bir yerde saklayın.
