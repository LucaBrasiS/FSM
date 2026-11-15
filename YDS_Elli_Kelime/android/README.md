# Android paketi (Basamak.apk)

Uygulama, önceki KELIME 0.4.0 uygulamasının WebView kabuğuyla paketlenir. Kabuk `assets/www/index.html` dosyasını
açar; ses (`KelimeApp.speak`, `KelimeApp.stop`) ve geri tuşu (`window.kelimeBack`) köprülerini sağlar.

- `base/`: KELIME 0.4.0 APK'sından alınan kabuk dosyaları (manifest, classes.dex, resources.arsc, uyarlanabilir simge).
- `build_apk.py`: manifesti yeni paket adı (`com.nefata.basamak`) ve uygulama adıyla (`Basamak`) yeniden yazar,
  renkleri günceller, `index.html` ve simgeleri ekler; imzasız APK üretir.
- `v2sign.py`: APK Signature Scheme v2 ile imzalar (Python `cryptography` paketi gerekir).
- `icons/`: başlatıcı simgeleri.

```
python3 android/build_apk.py android/base index.html android/icons /tmp/Basamak-unsigned.apk
python3 android/v2sign.py ANAHTAR.p12 PAROLA /tmp/Basamak-unsigned.apk dist/Basamak.apk
```

İmza anahtarı (`basamak-release.p12`) depoda tutulmaz. Güncellemelerin eski kurulumun üzerine yüklenebilmesi için
her sürüm aynı anahtarla imzalanmalıdır; anahtarı ve parolasını güvenli bir yerde saklayın.
