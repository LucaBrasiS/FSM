# Görseller ve içerik kaynakları

## Çizimler: Fluent Emoji (düz stil)

- Sahibi: Microsoft Corporation, https://github.com/microsoft/fluentui-emoji
- Lisans: MIT. Ticari kullanım dahil ücretsizdir; tek koşul telif ve lisans notunun kopyalarda yer almasıdır.
  Lisans metni `assets/FLUENT-EMOJI-LICENSE.txt` dosyasında ve derlenen `index.html` içinde yorum olarak bulunur.
- Alındığı paket: npm `@iconify-json/fluent-emoji-flat` 1.2.6. Uygulamada 238 çizim kullanılır.
- `data/art-picks.json`: hangi ünite, arayüz yeri ya da kelime için hangi çizimin seçildiği (ilk bulunan aday kullanılır).
- `data/art.json`: seçilen çizimlerin SVG gövdeleri; `src/build.py` bunları `index.html` içine gömer.

Çizimler değiştirilmeden kullanılmıştır; çıkartmalarda yalnızca çevrelerine beyaz kenar, koyu dış çizgi ve gölge eklenir
(kalıp kesim görünümü, SVG filtresiyle çalışma anında). Uygulama simgesi (`icon.svg` ve PNG türevleri) bu proje için çizilmiştir.

## Bu proje için çizilenler

- **Lokum** (maskot): pudra şekerli bir lokum küpü; altı poz ve altı tat (renk). `src/app.src.html` içinde `lok()`, düz SVG.
- **Sürpriz kutusu**: mor kutu, sarı kurdele ve fiyonk; kapağı ayrı çizildiği için açılışta uçar. `giftArt()`.
- **Parıltı, kalp ve konfeti parçaları**, dolu ve boş yıldızlar, damga kartı noktaları: kodla çizilir.
- Öneri uygulama simgesi `sanat/oneri-ikon-lokum.svg` (henüz kullanılmıyor). Gemini istemleri `sanat/gemini-gorseller.md` içinde.

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

Uygulamada ses dosyası yoktur. Ses efektlerinin hepsi çalışma anında WebAudio ile üretilir (`src/app.src.html` içindeki
`SFX`); telif gerektiren bir kayıt kullanılmaz. Kelimelerin okunması cihazın kendi konuşma sesiyle yapılır.

- Düğmeler işine göre çalar: ileri giden yukarı, geri ve kapat aşağı, ötekiler nötr.
- Cevaptan sonra Devam: kart kayıp gider ("fşşt"); tur içinde bölüm değişince ayrı bir geçiş sesi ("fiuv").
- Doğru sesi bölüme göre çalgı değiştirir: kelime marimba, gramer zil, bağlaç pizzicato, fiil taraması kalimba (turda
  20 adım boyunca bir oktav tırmanır). Yanlışta "boing" her seferinde biraz farklı perdede.
- Seri rozeti (x3, x5, x10…) belirince ayrı kutlama; gün serisi artınca bir kez "alev".
- Sürpriz kutu: her dokunuşta uzayan trampet, kutu büyür ve daha sert sallanır; açılışta zil ve tada. Albüm dolduysa
  tekrar gelen çıkartmaya daha hafif bir kutlama.
- Yeni kelime kartında kelime ve kazanılan çıkartmanın İngilizce adı kendiliğinden okunur (Ayarlar'dan kapatılır).
- Lokum'a dokununca kıkırdar ("hi-hi-hi"); eşleşme oyununda doğru "eşleşiyor" zil, doğru "eşleşmiyor" kayan bir "fşş";
  ödülde çıkartma yapışırken tada'nın içinde yumuşak bir "tap". Albümdeki çıkartmaya dokununca İngilizce adı okunur.

Bu sesler, görsel yargıç ajanın (İlya) ses anları değerlendirmesine göre seçildi; arka plan müziği, boşta kalma uyarısı ve
hafıza kartlarında konuma göre nota bilerek eklenmedi.

## Çıkartmalar

Sürpriz kutudan çıkan 24 çıkartma da Fluent Emoji çizimleridir (`data/art-picks.json` içinde `stk-` ile başlayanlar).
Kutudan sırayla üç oyundan biri çıkar: balon patlat, hafıza kartları, eşleşme mi?
