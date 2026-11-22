# Play Console: Nyeals kapalı test kurulumu

Bu belge Play Console'da doldurulacak her alanın hazır cevabını içerir. Dosyalar: `Nyeals-1.0.0.aab`, `simge-512.png`,
`one-cikan-1024x500.png` ve `1-…7-*.png` (1080x1920 telefon ekranları).

## 1. Uygulama oluştur

- Uygulama adı: **Nyeals**
- Varsayılan dil: **Türkçe – tr-TR**
- Uygulama mı oyun mu: **Uygulama**
- Ücretsiz mi ücretli mi: **Ücretsiz** (sonradan ücretliye çevrilemez; uygulama içi satın alma eklenebilir)
- Beyanlar: Geliştirici Program Politikaları ve ABD ihracat yasaları kutuları işaretlenir.

## 2. Kapalı test sürümü

Test ve yayınla > Test > **Kapalı test** > (varsayılan "Alfa" kanalı) > Yeni sürüm oluştur.
- Play Uygulama İmzalama: **Google'ın oluşturduğu imza anahtarını kullan** (varsayılan). Yüklediğimiz dosyanın imzası
  "yükleme anahtarı" olur; sonraki her sürüm aynı anahtarla imzalanmalıdır.
- App bundle: `Nyeals-1.0.0.aab` (paket `com.nefata.nyeals`, sürüm kodu 1, sürüm adı 1.0.0)
- Sürüm adı: `1.0.0`
- Sürüm notu (tr-TR):

  > İlk deneme sürümü. Günde 10 kelime, beş kelime oyunu, A1 gramer üniteleri. Gördüğünüz her sorunu bize yazın.

- Testçiler sekmesi: var olan e-posta listesini seçin, **geri bildirim adresi** olarak kendi e-postanızı yazın, kaydedin.
- Ülkeler: Türkiye (ya da tümü).

## 3. Mağaza girişi (Büyüme > Mağaza varlığı > Ana mağaza girişi)

- **Uygulama adı** (en çok 30): `Nyeals: Oyunla İngilizce`
- **Kısa açıklama** (en çok 80): `Günde 10 kelime, kısa oyunlar ve A1'den başlayan gramer. İngilizceye kolay başla.`
- **Tam açıklama**:

```
Nyeals ile İngilizceye en baştan, oynayarak başla.

Her gün 10 yeni kelime: önce resmi ve örnek cümlesiyle tanışırsın, sonra kısa sorularla pekiştirirsin.
Seviye testi yok; herkes A1'in en kolay kelimeleriyle başlar: elma, su, kedi, ev, okul…

• Günde 10 kelime, yaklaşık 6 dakika
• Beş kelime oyunu: Balon patlat, Hafıza kartları, Eşleşme mi?, Hızlı tur, Hangi tür?
• A1 gramer üniteleri: am / is / are, a / an, this / that, can, geniş zaman
• Bilemediğin kelimeler ertesi gün yeniden gelir, öğrendiklerin aralıklarla tekrar edilir
• Lokum adında küçük bir arkadaş ve her gün kutudan çıkan bir çıkartma
• İstersen siyah tema: siyah, gri ve beyaz, çıkartmasız
• Kelimeleri telefonunun kendi sesiyle dinleyebilirsin

İnternet gerekmez, reklam yok, hesap açman gerekmez. İlerlemen yalnız telefonunda saklanır.
```

- **Uygulama simgesi**: `simge-512.png`
- **Öne çıkan görsel**: `one-cikan-1024x500.png`
- **Telefon ekran görüntüleri** (2–8): `1-ana-menu.png` … `7-siyah-tema.png`
- Kategori: **Eğitim**. Etiketler: Dil öğrenme, Eğitici oyunlar.
- İletişim e-postası: geliştirici e-postanız. Web sitesi: boş bırakılabilir.

## 4. Uygulama içeriği (Politika > Uygulama içeriği)

- **Gizlilik politikası**: Drive'daki herkese açık "Nyeals gizlilik politikası" belgesinin bağlantısı.
- **Reklamlar**: Hayır, uygulamada reklam yok.
- **Uygulama erişimi**: Tüm işlevler özel erişim gerektirmez.
- **İçerik derecelendirmesi** (IARC anketi): kategori **Eğitim / Başvuru**; şiddet, cinsellik, küfür, kumar, uyuşturucu,
  kullanıcı etkileşimi, konum paylaşımı, dijital satın alma sorularının hepsine **Hayır**. Beklenen sonuç: 3+ / Herkes.
- **Hedef kitle ve içerik**: yaş grupları **13–15, 16–17, 18 ve üzeri**. (13 yaş altını seçmek Aile Politikası şartlarını getirir.)
  "Uygulama çocukların ilgisini çekebilir mi?" sorusuna dürüst cevap: maskot ve çıkartmalar nedeniyle **Evet** denebilir;
  bu durumda Google ek bilgi isteyebilir.
- **Veri güvenliği**: "Uygulamanız zorunlu kullanıcı veri türlerinden herhangi birini topluyor veya paylaşıyor mu?" → **Hayır**.
  (İlerleme yalnız cihazda saklanır, hiçbir veri cihazdan çıkmaz; internet izni yoktur.)
- **Devlet uygulaması**: Hayır. **Finansal özellikler**: Yok. **Sağlık**: Yok. **Haber**: Hayır.

## 5. Kapalı testi incelemeye gönder

Yayın genel bakışı > değişiklikleri incelemeye gönder. İlk inceleme birkaç gün sürebilir. Onaylanınca testçiler
katılım bağlantısından katılıp uygulamayı Play Store'dan indirir. 14 gün boyunca en az 12 testçi kayıtlı kalmalı.

## Yeni sürüm yüklerken

`app/build.gradle` içinde `versionCode` bir artırılır, `./gradlew bundleRelease` ile yeni AAB üretilir ve aynı kapalı test
kanalına yeni sürüm olarak yüklenir.
