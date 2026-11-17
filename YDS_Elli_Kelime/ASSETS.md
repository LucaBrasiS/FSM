# Görseller ve içerik kaynakları

## Çizimler: Fluent Emoji (düz stil)

- Sahibi: Microsoft Corporation, https://github.com/microsoft/fluentui-emoji
- Lisans: MIT. Ticari kullanım dahil ücretsizdir; tek koşul telif ve lisans notunun kopyalarda yer almasıdır.
  Lisans metni `assets/FLUENT-EMOJI-LICENSE.txt` dosyasında ve derlenen `index.html` içinde yorum olarak bulunur.
- Alındığı paket: npm `@iconify-json/fluent-emoji-flat` 1.2.6. Uygulamada 154 çizim kullanılır.
- `data/art-picks.json`: hangi ünite, arayüz yeri ya da kelime için hangi çizimin seçildiği (ilk bulunan aday kullanılır).
- `data/art.json`: seçilen çizimlerin SVG gövdeleri; `src/build.py` bunları `index.html` içine gömer.

Çizimler değiştirilmeden kullanılmıştır. Uygulama simgesi (`icon.svg` ve PNG türevleri) bu proje için çizilmiştir.

## Gramer üniteleri

İki kaynaktan oluşur:

- `data/kitap/k01.json` … `k34.json`: bir gramer kitabının içindekiler sayfasındaki 34 başlığın sırasını izleyen üniteler.
  Kitaptan yalnızca konu başlıkları alınmıştır; konu özetleri, sorular, açıklamalar ve okuma parçaları bu proje için
  yazılmıştır. Her ünitede zorluk sırasına dizilmiş 30 beş şıklı soru vardır (34. ünite: altı okuma parçası ve otuz soru).
- `data/gramer.json`: önceki KELIME uygulamasının (0.4.0) YDS düzeyi gramer bankası; 18 konu, konu başına 30 soru.

Sorular uygulamada onar soruluk üç teste bölünür; günün grameri, karışık test ve ara tekrar testleri aynı havuzdan beslenir.

## Kelimeler

293 kelimelik liste (B1 – alt B2, YDS metinlerinde sık geçen kelimeler), örnek cümleleri ve çevirileriyle birlikte bu proje
için yazılmıştır (`data/kelimeler.txt`).

## Fiil taraması

`data/fiiller.txt`: A1'den B1'e 586 fiil (A1 120, A2 175, B1 291; 51'i öbek fiil), Türkçe karşılıklarıyla bu proje için
yazılmıştır. Düzeyler yaklaşıktır; herhangi bir yayınevinin kelime listesi kopyalanmamıştır. Dördüncü alan, anlamı yakın
olduğu için aynı soruda şık olarak yan yana gelmemesi gereken fiilleri tutar.

## Sesler

Uygulamada ses dosyası yoktur. Ses efektlerinin hepsi (dokunma, doğru, yanlış, eşleşme, balon, kutlama) çalışma anında
WebAudio ile üretilir (`src/app.src.html` içindeki `SFX`); telif gerektiren bir kayıt kullanılmaz. Kelimelerin okunması
cihazın kendi konuşma sesiyle yapılır.

## Çıkartmalar

Sürpriz kutudan çıkan 24 çıkartma da Fluent Emoji çizimleridir (`data/art-picks.json` içinde `stk-` ile başlayanlar).
