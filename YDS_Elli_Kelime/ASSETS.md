# Görseller ve içerik kaynakları

## Çizimler: Fluent Emoji (düz stil)

- Sahibi: Microsoft Corporation, https://github.com/microsoft/fluentui-emoji
- Lisans: MIT. Ticari kullanım dahil ücretsizdir; tek koşul telif ve lisans notunun kopyalarda yer almasıdır.
  Lisans metni `assets/FLUENT-EMOJI-LICENSE.txt` dosyasında ve derlenen `index.html` içinde yorum olarak bulunur.
- Alındığı paket: npm `@iconify-json/fluent-emoji-flat` 1.2.6. Uygulamada 137 çizim kullanılır.
- `data/art-picks.json`: hangi ünite, arayüz yeri ya da kelime için hangi çizimin seçildiği (ilk bulunan aday kullanılır).
- `data/art.json`: seçilen çizimlerin SVG gövdeleri; `src/build.py` bunları `index.html` içine gömer.

Çizimler değiştirilmeden kullanılmıştır. Uygulama simgesi (`icon.svg` ve PNG türevleri) bu proje için çizilmiştir.

## Gramer soruları ve konu özetleri

`data/gramer.json`, önceki KELIME uygulamasının (0.4.0) gramer bankasından alınmıştır: 18 konu, konu başına 30 beş şıklı soru.
Sorular her konuda zorluk sırasına dizilmiş ve onar soruluk üç teste bölünmüştür. Ünite sırası gramer kitaplarının
alışılmış konu akışını izler; herhangi bir kitabın metni ya da alıştırması kopyalanmamıştır.

## Kelimeler

150 kelimelik demo seti, örnek cümleleri ve çevirileriyle birlikte bu proje için yazılmıştır (`src/app.src.html` içinde).
