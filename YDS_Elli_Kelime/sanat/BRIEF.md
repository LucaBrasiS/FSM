# Basamak · Sanat değerlendirmesi görev tanımı

Sen bu uygulamanın sanat yönetmeni ve illüstratörüsün. Görevin üç parça:

1. Uygulamanın görsel dünyasını dürüstçe değerlendirmek.
2. Öncelik sırasına dizilmiş, uygulanabilir öneriler yazmak.
3. Gerekiyorsa sürpriz adımı için özgün görseller üretmek. Gemini kullanabilirsin.

Uygulamanın kaynağını değiştirmiyorsun. Önerileri geliştirme oturumu uygulayacak; bu yüzden her öneri, okuyan biri hiçbir şey sormadan uygulayabileceği kadar somut olmalı.

## Uygulama ve kullanıcısı

- **Basamak**, YDS'ye hazırlanan ve A2–B1'den B2'ye çıkmak isteyen 16–30 yaş Türk öğrenciler için bir İngilizce uygulaması. Yalnızca dokunma ve sürükle-bırak kullanılır, klavye yoktur. Arayüz Türkçedir.
- Bölümler:
  - **Günlük kelime:** günde 10 yeni kelime (Necip: kelime az, oyun çok). Tanıtım kartları, beş şıklı sorular; her 5 kelimede bir ara görev (eşleştirme, cümle ya da mola oyunu), 10. kelimeden sonra sürpriz kutu, gün sonu kontrolünden sonra günün oyunu.
  - **Oyunlar:** Balon patlat, Hafıza kartları, Eşleşme mi?, Hızlı tur (20 saniye), Hangi tür? (fiil, isim, sıfat, zarf). Kelime ekranındaki Oyun odasında istenildiği kadar oynanır.
  - **Sürpriz kutu:** günde bir kez, 10. kelimeden sonra çıkar. Üç dokunuşla açılır; içinden *Balon patlat* ya da *Hafıza kartları* oyunu çıkar. Oyun bitince albüme bir çıkartma eklenir.
  - **Gramer:** 52 ünite.
  - **Bağlaç atölyesi:** kartlar, üç alıştırma ve *Ayır* oyunu.
  - **Fiil taraması:** A1–B1 arası 586 fiil.
- Sahibinin istekleri, kendi sözleriyle:
  - "daha renkli"
  - 16–30 yaşa hitap etsin
  - sesler "tatlı, uyandırıcı, komik" olsun
  - sürpriz adımının tek amacı kullanıcıyı eğlendirmek
  - en son: "paneli okumak zor, her şey ortada gibi duruyor". Bunun üzerine Bugün ve Kelime ekranları sadeleştirildi. **Bu iki ekrana yeni öğe eklemeyi önerme.**

## Var olan görsel dil

- Tek HTML dosyası. Kalın koyu çizgiler, düz dolgular, sert ofset gölgeler ve kelime türüne göre renk kodu var. Başlıklarda Bricolage Grotesque, metinde DM Sans kullanılıyor. Bütün renk ve ölçü tokenları (açık ve koyu tema) `tasarim/tokenlar.css` içinde.
- Çizimlerin hepsi Microsoft Fluent Emoji Flat (MIT lisansı), SVG olarak gömülü: sekme ve ünite simgeleri, her kelimeye bir küçük resim, hediye kutusu ve 24 çıkartma. Hangi çizimin nerede kullanıldığı `tasarim/gorsel-secimleri.json` dosyasında.
- Balonlar, hafıza kartları ve konfeti yalnızca CSS ile çiziliyor. Hareketlerin listesi `tokenlar.css` dosyasının sonunda.
- Ekrandaki boyutlar:

  | Öğe | Boyut |
  |---|---|
  | Hediye kutusu | 112 px |
  | Ödül ekranındaki çıkartma | 104 px |
  | Albümdeki çıkartma | 36 px |
  | Kahraman alanı görselleri | 44–56 px |
  | Kelime görseli | 40 px |
  | Ünite simgesi | 40 px / 28 px |
  | Sekme simgesi | 24 px |

- Çıkartmalar aynı zamanda kelime öğretir: her birinin altında İngilizce adı ve Türkçesi yazar (örneğin *otter*, su samuru).

## Paketteki dosyalar

| Yol | İçerik |
|---|---|
| `uygulama/Basamak.html` | Uygulamanın son hali. Tarayıcıda açılır, sunucu gerekmez. |
| `ekranlar/01…34-*.png` | Bütün ana ekranlar, 390×844, 2×. 29–34 koyu tema. |
| `ekranlar/paftalar/` | Beşerli genel bakış paftaları. **Buradan başla.** |
| `ekran-cek.js` | Ekranları yeniden çeker: `node ekran-cek.js [html] [klasör]`. Node ve Playwright gerekir. |
| `tasarim/tokenlar.css` | Renkler, yazı tipleri, köşeler, gölgeler, hareketler. |
| `tasarim/gorsel-secimleri.json` | Hangi emoji nerede; 24 çıkartmanın adları. |
| `on-calisma/` | Yarım kalmış ilk değerlendirmeden kalan üç mock-up (aşağıya bak). |

Depodan çalışıyorsan:

- `uygulama/Basamak.html` yerine `YDS_Elli_Kelime/index.html`'i kullan.
- Tokenlar `src/app.src.html` dosyasının başındaki `:root` bloğunda.
- Emoji seçimleri `data/art.json` içinde.
- Ekranları `YDS_Elli_Kelime/sanat/ekran-cek.js` ile çek.

### Uygulamada gezinmek için

- **Kelime** sekmesi → **Ayarlar ve deneme** bölümünde iki tür düğme var:
  - Her soru türünü ve iki oyunu doğrudan açan deneme düğmeleri.
  - Demo araçları: *Ertesi güne geç*, *Bugünü otomatik bitir*, *Fiil taramasını otomatik doldur*.
- Gerçek akışta sürpriz kutu 10. kelimeden sonra çıkar.
- Playwright ile gezeceksen:
  - Hareketli öğelere (kutu, balonlar) `click({force:true})` ile tıkla.
  - `addInitScript` içinde `localStorage`'a dokunma; sayfa bazı yüklemelerde boş depolamayla açılıyor. Durumu sayfa yüklendikten sonra `page.evaluate` ile yaz.

## İstenen

### 1. Değerlendirme

Türkçe yaz, dosya adı `DEGERLENDIRME.md`. Bölümler:

1. **Genel izlenim:** 4–5 cümle.
2. **İyi olanlar, dokunmayalım.**
3. **Sorunlar ve öneriler:** etkiye göre sıralı bir tablo. Sütunlar: *ekran / sorun / öneri / emek (küçük, orta, büyük)*.
   - Önerileri mümkün olduğunca var olan tokenlarla yaz: hangi öğe, hangi boyut, renk ya da boşluk.
   - En fazla bir düzine güçlü madde yeter.
   - Ekran görüntüsünde gördüğünle tahmin ettiğini ayır.
4. **Sürpriz adımı ve çıkartmalar:** kutunun açılışı, oyunlar, ödül anı ve albüm gerçekten sevindiriyor mu? Bunları özel kılmak için ne yapılabilir (maskot, temalı çıkartma seti, daha iyi bir açılış anı…)? Her fikir için, var olan emoji ve CSS ile yapılabilir mi, yoksa yeni çizim mi gerekir, yaz.
5. **Üretilecek görseller:** aşağıdaki listeye ya da açıkça "gerek yok" yazısına bağlantı ver.
6. **Mock-up dosyaları:** hazırladıysan.
7. **Ön çalışmaya bakış:** kendi değerlendirmeni bitirdikten sonra `on-calisma/` içindekilere bak. Katıldığın ve katılmadığın yerleri bir paragrafta yaz.

Kısa ve açık cümleler kullan; tablolar hariç yaklaşık 900 kelime.

### 2. Özel görseller

Özel görsel yalnızca emoji setinden açıkça daha iyi olacaksa gerekir. Emoji setinin doğru seçim olduğunu düşünüyorsan bunu açıkça söylemek de iyi bir cevaptır.

Görsel üreteceksen teslim biçimi şöyle; geliştirme oturumu bunu doğrudan uygulamaya bağlayacak:

- Dosyalar `gorseller/` klasörüne gelir. Her biri 512×512, saydam zeminli PNG olmalı. Dosya adı uygulamadaki anahtarla aynı olsun:
  - var olan bir çıkartmanın yerine geçiyorsa `stk-otter.png`
  - yeni bir anahtarsa `stk-yeni-ad.png` ya da `gift.png`
- `gorseller/liste.json` dosyası bir dizi olmalı. Her öğenin alanları:

  ```json
  {"dosya": "stk-otter.png", "anahtar": "stk-otter", "nerede": "ödül ekranı + albüm",
   "gosterim_px": [104, 36], "en": "otter", "tr": "su samuru", "istem": "…kullandığın İngilizce istem…"}
  ```

  `en` ve `tr` yalnızca çıkartmalar için zorunludur.
- **Stil kilidi:** bütün setin istemlerine aynısını koy. Set tutarlı olmalı.
  - düz renkli vektör çizim
  - kalın, eşit kalınlıkta koyu dış çizgi (`#17132B`)
  - palet: `#5B3DF5 #FFD43B #FF8FC4 #5EE0C0 #72B7FF #FFA552 #B9A0FF #C6F04D`
  - degrade yok, en fazla tek yumuşak gölge tonu
  - ortalanmış, saydam zemin
  - görselde yazı ya da harf yok
  - 36 px'te bile okunabilen basit biçimler
  - sevimli ve biraz muzip
- **Özgünlük:** marka, bilinen karakter ya da belli bir sanatçının tarzını taklit eden görsel yok.
- **Bütçe:** bütün yeni görseller WebP'ye çevrildikten sonra toplam yaklaşık 500 KB (uygulama bugün 1,2 MB).
  - Çıkartma setini değiştireceksen 24'ünün hepsini ver; yarısı emoji, yarısı çizim olan bir albüm olmaz.
  - En fazla 30 görsel.
- **Gemini anahtarı:** sohbete ya da dosyalara yazma. Ortamın gizli anahtar düzenini kullan.

### 3. Mock-up (isteğe bağlı, en fazla üç)

Bir resim sözden daha iyi anlatacaksa:

1. `uygulama/Basamak.html` dosyasının bir kopyasını düzenle.
2. Önce/sonra ekranlarını yan yana PNG olarak kaydet.
3. Yaptığın değişikliği (CSS ve küçük işaretleme yamaları) bir dosyada bırak; geliştirme oturumu oradan uygular.

## Kurallar

- Uygulamanın kaynağını değiştirme. Yalnızca kendi çıktı klasörüne yaz.
- Görsel tarafta kal: kod kalitesi, öğretim içeriği ve sesler kapsam dışı.
- Koyu tema ve "hareketi azalt" ayarı her öneride çalışmaya devam etmeli.
- Ekran 320 px genişliğe kadar yatay kaydırma olmadan sığmalı.

## Ön çalışma (`on-calisma/`)

Bu değerlendirme önce geliştirme oturumunda başladı ve kullanım sınırı yüzünden rapor yazılmadan durdu. Geriye üç mock-up ve yaması kaldı:

1. **Sürpriz adımı için "oyun odası":** kutu, oyun ve ödül ekranları noktalı mor bir zemin üzerinde; kutunun ve çıkartmanın arkasında dönen ışın deseni; çıkartma kalıp kesim kenarlı.
2. **Çıkartma albümü:** kalıp kesim çıkartmalar, kazanılmamışlar için silüet, adın altında Türkçesi.
3. **Koyu tema:** zemin ve yüzey renkleri biraz açılıyor, böylece kalın çizgi ve sert gölge koyuda yeniden görünüyor.

`oneri-yamasi.py` bu üç önerinin CSS'ini taşır. **Kendi değerlendirmeni bitirmeden bunlara bakma.** Amaç bağımsız ikinci bir göz; sonra katıldığın ya da katılmadığın yerleri yaz.

## Teslim

Bütün çıktıyı tek klasörde ya da zipte ver: `sanat-degerlendirme/`. İçinde şunlar olsun:

- `DEGERLENDIRME.md`
- varsa `mock/`
- varsa `gorseller/` ve `gorseller/liste.json`

Bu klasör geliştirme oturumuna verilecek ve oradan uygulanacak.
