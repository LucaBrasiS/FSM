# İlya'nın tasarımı: tatlı ve sevecen Basamak

Necip'in isteği: 16–30 yaş, ağırlıklı kadın kullanıcılar için daha tatlı ve sevecen bir uygulama. Dopamin veren küçük ve sık ödüller olsun, öğretim oyun havasında geçsin ama oyun gibi uzamasın. Bu belge neyin neden değiştiğini ekran ekran anlatır.

Görseller (hepsi scratchpad'de, `S = /tmp/claude-0/-home-user-FSM/5cd3a96b-661d-5662-80d5-279398c449c4/scratchpad/ilya5`):

- Önce ve sonra yan yana: `S/once-sonra/*.png` (17 ekran)
- Bütün ekranlar, önce: `S/once/`, sonra: `S/sonra/` (`sanat/ekran-cek.js` ile çekilen 34 ekran)
- Akışlar: `S/akis-kutu-acilisi.png`, `S/akis-eslesme-oyunu.png`, `S/akis-lokum-ozet-album.png`, `S/akis-koyu.png`, `S/akis-320.png`
- Lokum'un pozları ve tatları: `S/lokum-pozlar.png`. Simge önerisi: `S/ikon/karsilastirma.png`
- Yavaşlatılmış hareket kareleri (ödül, Lokum): `S/yavas/`

## Tek dil: Lokum'un şeker kutusu

Dağınık süs eklemedim. Bütün değişiklikler beş kurala bağlı.

1. **Bir karakter.** Lokum, pudra şekerli bir lokum küpü. Bu proje için kodla çizildi (`lok()`): düz renk, eşit kalınlıkta koyu dış çizgi, yazısız, 30 px'te de okunuyor. Altı pozu var: el sallar, gülümser, sevinir, şaşırır, uyur, kalp gözlü. Yeni bir süs olarak eklenmedi: kahraman ve kutlama kartlarındaki rastgele emojilerin (hedef tahtası, kupa, konfeti, şemsiye) yerine geçti. Türkçede "tatlı" hem lezzetli hem sevimli demek; Lokum bu sözün kendisi ve uygulamayı başka bir kelime uygulamasından ayıran imza.
2. **Bir renk dili.** Var olan tokenlar korundu: lavanta zemin, mor kahraman, sarı birincil düğme, kelime türü renkleri. Sevecenlik pembe vurguyla geldi: Lokum, kalpler, sürpriz kartı ve hafıza kartlarının arkası. Yeni tokenlar `--candy`, `--room`, `--room-dot`, `--ray` ve `--ray-sun`.
3. **Bir süs motifi, yalnızca ödül anlarında.** Kalp, dört köşeli parıltı ve konfeti. Doğru cevapta tik işaretinden, eşleşen çiftte kalpler, kutu açılınca hepsi birden fışkırır. İş ekranlarında (tanıtım kartı, soru, gramer, fiil taraması) kalıcı süs yok. Bu parçalar sayfanın üstünde 0,7–1 saniye yaşar ve kendini siler. "Hareketi azalt" açıkken hiç çizilmez.
4. **İki ayrı yer.** İş ekranları sakin kaldı. Sürpriz adımı (kutu, oyun, ödül) puantiyeli mor bir **oyun odasında** geçer: kullanıcı mola verdiğini zeminden anlar.
5. **Sıcak ve yargılamayan dil.** Kullanıcıya "sen" diye seslenir, kısa ve içtendir. Hatada utandırmaz ama dürüst kalır. Doğru cevapta övgü her seferinde değişir.

## Ekran ekran

### Bugün (ana ekran)
`S/once-sonra/01-bugun.png`. Necip'in "sade kalsın" isteği korundu: kahraman kartı, son 7 gün ve ipucu; yeni öğe yok (test de bunu denetliyor).
- Hedef tahtası emojisinin yerinde 76 px Lokum var. Gelişte iki kez el sallar, sonra yalnızca göz kırpar; sürekli hareket görevlerden dikkat çalardı.
- Başlık günün saatine göre selamlıyor: Günaydın!, Merhaba!, İyi akşamlar!, İyi geceler!. İki görev bitince "Bugün tamam!", iki gün ve daha uzun aradan sonra "Tekrar hoş geldin!".
- Lokum'a dokununca zıplar, kıkırdar, kalpler saçar ve kısa bir söz söyler ("Küçük adımlar, büyük basamaklar."). Yeni kullanıcıya ilk dokunuşta kendini tanıtır. Görevler bitince sözleri de değişir ("Gurur duyuyorum!"). Ekranda yer kaplamayan, bedava bir küçük sevinç.
- Son 7 gün: çalışılan gün yeşil tik yerine pembe daire içinde kalple işaretlenir. Biçim farkı (kalp ya da boş daire) renkten bağımsız da okunur. Çalışılan bir günde Bugün ekranı ilk açıldığında bugünün kalbi bir kez zıplar (seri arttıysa "alev" sesi de çalar). Yedi günün hepsi doluysa: "Tam yedi gün, harikasın!".

### Kelime
`S/once-sonra/02-kelime.png`. Yapı aynı. Kahraman kartındaki emoji yerine duruma göre Lokum var: el sallar, iş bitmişse sevinir, kelime kalmamışsa uyur. Çıkartma albümü satırında son üç çıkartma küçük birer kesik çıkartma olarak görünür; koleksiyon kapalı satırdan da sezilir. Ayarlar'a **"Lokum'un tadı"** satırı eklendi (ayrıntı aşağıda). Yolculuk çubuğu çizgili "şeker çubuğu" dolgusu aldı.

### Tanıtım kartı ve sorular
`S/once-sonra/04-soru.png`, `05-dogru.png`, `06-yanlis.png`. Öğretim ekranları bilerek sakin kaldı.
- **Doğru:** yeşil hap artık tik simgesi ve değişen bir övgüyle geliyor (Harika!, Süpersin!, Bildin!, Tam isabet!…). Seri anlarının kendi sözü var: üçte "Üç üst üste!", beşte "Beşte beş!", onda "On numara!". Tik işaretinden parıltı çıkar; seri anında x3, x5, x10 rozetinden kalpler de fışkırır. Ses değişmedi. *(Sonra değişti: kalpler ve zil x5'ten başlıyor, doğru sesi 4 dB alçaldı; bkz. Son düzeltmeler, 2 ve 3.)*
- **Yanlış:** "Yanlış" yerine "Bu sefer olmadı", altında "Sorun değil, yarın yeniden karşına çıkacak." Kırmızı renk, çarpı simgesi ve sallanma durduğu için durum açıkça okunuyor. Dürüstlük korunuyor, utandırma yok. "Neden yanlış?" kutusu aynen duruyor.
- **Bilmiyorum:** artık yanlışın kırmızı hapı değil. Ampul simgeli sakin lila hap, sallanmadan. Bilmemek hata değil.
- Gramer, bağlaç ve fiil taramasında da aynı hap ve aynı övgü dili var.

### Eşleştir ve cümle
`S/once-sonra/07-eslestirme.png`. Bulunan her çiftin tikinden kalpler çıkar. Tur sonunda yanlış yoksa "Kusursuz!", varsa "Tamam!" ve "N yanlış deneme, ama hepsini buldun." Bölüm değişince (eşleştirme, cümle, kutu, tanıtım, gün sonu) ilk kart hafifçe zıplayarak gelir; "fiuv" sesine görüntü de eşlik eder.

### Sürpriz kutu (oyun odası)
`S/once-sonra/09-surpriz-kutu.png`, `S/akis-kutu-acilisi.png`. Önceki raporun 1. sorunu buydu: sarı diskte sarı kutu, açılış anı yok.
- Zemin puantiyeli mor oyun odası. Pembe kartın ortasında kenarlara doğru solan, yavaş dönen ışınlar var.
- Kutu artık kendi çizimimiz: mor kutu, sarı kurdele ve fiyonk. Pembe kart üzerinde açık ve net okunuyor. Kapak ayrı bir parça olarak çizildi.
- Üç dokunuşta sallanma ve trampet eskisi gibi büyüyor. Üçüncüde son nokta da dolar ve yazı "Açılıyor!" olur. Sonra kapak fiyonguyla birlikte uçar, kutudan sarı ışık fışkırır, konfeti, kalp ve parıltı saçılır; yaklaşık 0,6 saniye sonra oyun gelir. Hareketi azalt açıkken doğrudan oyuna geçer.
- Kart ekranın ortasına alındı; önceki ekrandaki 250 px'lik boşluk kapandı.

### Üç mini oyun
Kutudan sırayla üç oyundan biri çıkar: balon, hafıza, eşleşme. Sürprizin gerçekten sürpriz olması için artık iki değil üç oyun var.
- **Balon patlat** (`10-balon-patlat.png`): doğru balon kendi renginde parçalara ayrılır.
- **Hafıza kartları** (`13-hafiza-kartlari.png`): kartların arkası pembe puantiyeli, ortasında kalp. Seçilmeyen 20 px başlık simgesi kaldırıldı. Eşleşen iki karttan kalpler çıkar.
- **Eşleşme mi? (yeni)** `S/akis-eslesme-oyunu.png`: kartta bir İngilizce kelime ve bir Türkçe anlam var. Eşleşiyorsa sağa kaydırılır ya da kalbe dokunulur, eşleşmiyorsa sola ya da çarpıya. Sürüklerken "EŞLEŞME" ya da "DEĞİL" damgası belirir. Doğru karar kartı uçurur; doğru bir "eşleşiyor"dan kalpler çıkar. Yanlışta kart sallanır ve doğrusu yazılır ("observe aslında «gözlemlemek» demek."), 1,8 saniye sonra kart doğru yöne gider. *(Sonra değişti: yazı karakter sayısına göre 2,4–4,2 s kalıyor ve kapalı düğmelerin yerinde çıkıyor; bkz. Son düzeltmeler, 2.)* Altı kart, yaklaşık 30 saniye. Bu yaş grubunun her gün kullandığı bir hareket, kelime öğretimine bağlandı. Eşleşen kartlar bugünkü kelimelerden, eşleşmeyenler aynı türden ve anlamı çakışmayan kelimelerden gelir.

### Ödül
`S/once-sonra/11-cikartma-odulu.png`, yavaş kareler `S/yavas/y1.png`. Önceki raporun 2. sorunu buydu: küçük ve boş.
- Çıkartma 150 px, **kalıp kesim**: beyaz kenar, koyu çizgi, gölge. Bu görünüm SVG filtresiyle görselin içinde çiziliyor, her yerde aynı duruyor.
- Çıkartma büyük ve eğik düşer, ezilir, yapışır; düşüş tada sesinin içine eklenen yumuşak "tap" ile aynı anda biter (~340 ms). Arkasında sarı ışınlar döner, yanında parıltılar göz kırpar, yapıştığı anda parıltı saçılır.
- **Damga kartı:** 24 yuva (iki sıra, on iki sütun). Bugünkü yuva dolarken zıplar; koleksiyonun ilerlemesi bir bakışta görülür.
- İngilizce adı eskisi gibi kendiliğinden okunur.

### Albüm
`S/once-sonra/16-cikartma-albumu.png`, koyu: `S/ek/e21-koyu-album.png`. Kazanılan çıkartmalar kalıp kesim, hafif eğik ve altlarında İngilizcesiyle Türkçesi yazıyor. Kazanılmayanların silüeti görünüyor; ne kaldığı merak ediliyor. Kazanılan çıkartmaya dokununca zıplar ve İngilizce adı okunur: koleksiyon da kelime öğretiyor. Bugün kazanılan çıkartma albüm açılınca yeniden yapışır. Sayfa noktalı bir çıkartma defteri gibi duruyor.

### Gün özeti
`S/once-sonra/15-gun-ozeti.png`. Konfeti emojisinin yerinde kalp gözlü ya da sevinen Lokum var. Başlık günün başarısına göre: "Muhteşem bir gün!" (%80 ve üstü), "Güzel bir gün!", "Bugün de buradaydın!". Sonuncusu çabayı ödüllendiriyor, sonucu değil. Altında **bugün kazandıkların** çipleri:
- seri ("3 gün üst üste"),
- bugünkü çıkartma,
- "+N kelime öğrendin" (yalnız yeni öğrenilenler; pekiştirmeler sayılmaz),
- toplam kelime eşiği aşıldıysa "Toplam 50 kelime oldu!" (10, 25, 50, 75, 100, 150, 200, 250 ve bütün liste), *(sonra: "50 kelimeye ulaştın!")*
- yeni Lokum tadı açıldıysa "Yeni tat: Lavanta · dene" (dokununca Lokum o tada boyanır).

Gün sonu kontrolü, en uzun seri ve eşleştirme notları sıkı tek bir blokta toplandı; eşik günlerinde de "Yarın" kartı ilk ekranda kalıyor.

### Gramer, fiil taraması, bağlaç
`S/once-sonra/21-gramer-sonuc.png`. Sonuç kartında kupa ve konfeti yerine puana göre Lokum var. Boş yıldızlar sarı kartta görünmüyordu; artık içi boş, düz çizgili yıldızlar (☆ ile ★ ayrımı). Önceki en iyi sonuç geçildiyse "Kendi rekorunu geçtin: 6 → 8" çipi çıkar. Düşük puanda dil yumuşadı: "Olsun, önce konu özetini birlikte okuyalım, sonra yeniden dene." Bağlaç Ayır oyununda doğru bırakılan her kartta parıltı var.

### Lokum'un tadı (kişiselleştirme)
Ayarlar'da "Lokum'un tadı" satırı. Her dokunuşta açık tatlar arasında döner (Gül, Limon, Nane). Lavanta 3., Fıstık 7., Portakal 14. çalışma gününde açılır. Tat cihaz tercihi olarak `PREF.lok` içinde saklanır. Kilitli ya da bozuk bir değer Gül'e döner. Klavye yok, yalnızca dokunma.

### Koyu tema, 320 px, hareketi azalt, sesler
- **Koyu tema** (`S/akis-koyu.png`, `29…34` çiftleri): zemin `#211A42`, yüzey `#30285F`. Kalın çizgi ve sert gölge koyu zeminde artık görünüyor (ön çalışmadaki 3. öneri, biraz daha sıcak tonla). Silüetler koyuda açık renkli.
- **320 px:** bütün yeni ekranlar yatay kaydırma olmadan sığıyor (testte ölçülüyor).
- **Hareketi azalt:** parçacıklar hiç çizilmez, kutu doğrudan açılır, eşleşme kartı uçmadan gelir.
- **Sesler** tek düğmeyle kapanmaya devam ediyor. Yeni sesler: Lokum'un kıkırdaması, eşleşme oyununda "eşleşiyor" zili ve "eşleşmiyor" kayması, tada içinde çıkartmanın "tap"ı. Doğru, yanlış ve Bilmiyorum sesleri değişmedi. *(Sonra değişti; önce ve sonra ölçümleri Son düzeltmeler, 3'te.)*

## Kaldırılanlar
- Kahraman ve kutlama kartlarındaki rastgele emojiler (hedef tahtası, kupa, konfeti, plaj şemsiyesi): yerlerinde Lokum var.
- Sürpriz kutusunun arkasındaki sarı disk ve emoji kutu: yerine okunaklı çizim geldi.
- Hafıza kartları başlığındaki seçilmeyen joker simgesi.
- Yıldız emojisi ve gri "kapalı yıldız" filtresi.
- Kullanılmayan üç çizim `data/art.json`'dan çıktı (238 çizim).

## Oturum uzadı mı?
Hayır. Günlük akışa hiçbir adım eklenmedi. Kutu açılışı yaklaşık 0,6 saniye ekliyor. Eşleşme oyunu öteki iki oyundan kısa (yaklaşık 30 saniye). Bütün kutlamalar dokunuş beklemiyor. 20 kelimelik gün yine yaklaşık 12 dakika.

## Kod notları
- Yeni kalıcı alan `S.ses.stk`: o gün kazanılan çıkartma (gün özeti için). İsteğe bağlı; yoksa çip çıkmaz. Eski kayıtlar etkilenmez. `fresh()`/`sanitize()` değişmedi, çünkü `S.ses` her gün yeniden kurulur.
- Yeni cihaz tercihi `PREF.lok`: yükleme sırasında doğrulanır.
- Öğrenme verilerine (`kelimeler.txt`, `fiiller.txt`, `karisanlar.txt`, `kitap/`, `gramer.json`, `baglac/`) dokunulmadı.
- `index.html` 1,28 MB (sınır 2 MB).

## Testler
`scratchpad/test/run13.js` eklendi (55 denetim): Lokum, tat seçimi ve kilitli tat, övgü, yanlış ve Bilmiyorum hapları, parçacıkların kendini silmesi, oyun odası, kutu açılışı, eşleşme oyunu (düğme, sürükleme, yanlış), damga kartı, kalıp kesim albüm, gün özeti çipleri, bugünün kalbi, rekor, sessiz kip, hareketi azalt, koyu tema, 320 px. `hepsi.sh` bu paketi de çalıştırıyor (8 paket, 316 denetim; son çalıştırma: HEPSİ GEÇTİ). run6–run12 dosyalarına dokunulmadı; bilerek değiştirdiğim hiçbir davranış onları bozmadı.

## Kalan işler (Necip'in kararı)
1. **Uygulama simgesi.** Bugünkü simge bir form satırı ve tik; mağazada ve ana ekranda bir karakter daha çok akılda kalır. Lokum'lu öneri hazır: `sanat/oneri-ikon-lokum.svg`, karşılaştırma `S/ikon/karsilastirma.png`. Onaylarsan `icon.svg`, `icon-*.png` ve `android/icons/*` bundan üretilmeli, sonra APK yeniden derlenmeli. Ben değiştirmedim; marka kararı senin. *(Güncelleme: Necip'in "yolu varsa yap" sözüyle yapıldı; bkz. Son düzeltmeler, 4. APK yeniden derlenmeli.)*
2. **Gemini görselleri isteğe bağlı.** Mağaza öne çıkan görseli ve Lokum poz seti için istemler `sanat/gemini-gorseller.md` içinde. Uygulama bunlara muhtaç değil.
3. **Gerçek telefonda deneme.** SVG filtreli çıkartmaların ve parçacıkların düşük güçlü Android'de akıcılığı ölçülmeli. Sesler telefon hoparlöründen dinlenmeli (özellikle kıkırdama ve "tap").
4. **İleride:** temalı çıkartma setleri (set tamamlama anı), Lokum'a çalıştıkça açılan aksesuarlar (fiyonk, taç). İkisi de toplama döngüsünü uzatır ama şimdi gerekli değil.
5. Ön çalışmadaki üç öneri (oyun odası, kalıp kesim albüm, açılmış koyu tema) uygulandı. `data/art.json` içinde daha önceden kalan, kullanılmayan birkaç çizim (madalya, not defteri, çerçeve…) ayrıca temizlenebilir.

## Son düzeltmeler (gözlemci raporundan sonra)

Gemini'ye ulaşılamadığı için tanıtım videosunu, tasarımda payı olmayan bir Claude gözlemcisi Gemini istemiyle (`sanat/gemini-istemi.md`) değerlendirdi. Sesi duyamadığı için ölçtü. Raporu ve ölçüm betikleri `scratchpad/gozlemci/` altında. Bu bölüm o rapordan sonra neyi neden değiştirdiğimi anlatır. Necip bilgisayar başında değildi ve "yolu varsa yap, sorma" dedi; simge kararını da bu yüzden ben verdim.

Görseller `S6 = /tmp/claude-0/-home-user-FSM/5cd3a96b-661d-5662-80d5-279398c449c4/scratchpad/ilya6` altında:
- 34 ekran: `S6/sonra/`
- Yeni durumlar: `S6/ek/pafta-eslesme.png`, `S6/ek/pafta-fiil-seri.png`, `S6/ek/pafta-azalt-koyu.png`
- Simge: `S6/ikon/kontrol-kucuk.png`, `S6/ikon/kontrol-buyuk.png`

### 1. Dokunuş tuzağı (zorunlu, öğrenme verisi)
**Hata.** Devam'a hızlı ya da geç ikinci bir dokunuş, sonraki soruyu "Bilmiyorum" diye kaydediyordu. Gözlemcinin betiğiyle yeniden üretildi: kelime turunda 120 ve 250 ms, fiil taramasında doğru cevaptan 700, 800 ve 1000 ms sonra.

**Önce nerede ne durduğunu ölçtüm** (390, 360 ve 320 px; `S6/konum.js`, `S6/konum2.js`):
- Devam'ın yerinde her soru ekranında Bilmiyorum çıkıyor. Bu kelime turu, gün sonu kontrolü, gramer, fiil taraması ve son tanıtım kartının "Soruları başlat" düğmesi için geçerli.
- Bilmiyorum'un yerinde sonuç ekranında Sabitle ve Devam çıkıyor. Çift dokunuş kelimeyi sabitleyebiliyordu; bu da öğrenme verisi.
- Gövdedeki başlat satırları ilk sorunun şıklarıyla üst üste biniyor. Bunlar ünite sayfasındaki test satırları ve fiil merkezindeki düzey satırları. Yani bu satırlara çift dokunuş ilk soruya rastgele bir şık yazabiliyordu.
- Altbilgi ayrı bir bölge, gövde kaydırılıyor. Bu yüzden şıklar hiçbir zaman Devam'ın altına girmiyor.

**Çözüm: konuma bağlı kapı.** Yeni bir soru ya da sonuç çizildikten sonraki 500 ms içinde, az önce dokunulan düğmenin dikdörtgenine (±8 px) düşen cevap ya da Sabitle dokunuşu yok sayılır. Kendiliğinden geçişte bu yer altbilgidir. Başka yere yapılan dokunuş hiç beklemez: Devam'dan hemen sonra bir şıkka dokunmak anında sayılır.
- Gözlemci bütün cevap dokunuşlarını 400 ms yok saymayı önermişti. Benim kapım daha dar (yalnız tuzağın yeri), Sabitle'yi de kapsıyor ve 500 ms sürüyor (ölçülen en geç çift dokunuş 450 ms).
- Kod: `GUARD`, `scrNow()`, `nearTap()`, tıklama dinleyicisi ve `render()` içindeki iki satır.

**Fiil taraması.** Doğru cevapta Devam artık çizilmiyor; ekran 650 ms sonra kendiliğinden geçiyor (Quizlet Öğren gibi). Yanlış ve Bilmiyorum cevaplarında Devam durur ve bekler.

**Kanıt.**
- `test/run14.js` (37 denetim): çift ve geç dokunuş her yüzeyde; başlat satırları; Sabitle; kasıtlı dokunuşun yarım saniye sonra sayıldığı; şıkka hemen dokunmanın beklemediği.
- Gözlemcinin betikleri, eski ve yeni sürümde aynı ölçüyle: eski sürümde "SAYILDI", yeni sürümde her denemede "etkilenmedi / sorun yok".

### 2. Düzeltme listesi: kararlar
| # | Karar | Neden |
|---|---|---|
| 3 | değiştirilerek | ok ve match önerildiği gibi −4 dB. Fiil taramasının okStep'i de aynı oranda, çünkü o turda da en sık ses oydu ve tur sonundaki kutlamadan yüksekti. |
| 4 | değiştirilerek | Kutu açılışından tada kalktı, ama zil 0,5'te kaldı. 0,35'te telefonda x3 serideki bir doğru cevabın yalnız 1 dB üstündeydi. Açılışın bütün düzeyi neredeyse değişmedi; tada günde 2'den 1'e indi. |
| 5 | değiştirilerek | Kıkırdama önerildiği gibi. Alev için önerilen değerler düz dBFS'te kutlama düzeyine çıkıyordu (−16,8) ama telefonda bir doğru cevap kadar kalıyordu (−22,3). Enerjiyi telefonun verdiği banda taşıdım (süzgeç 900→3200 Hz, ton 0,7). |
| 6 | değiştirilerek | "Boing" ve çıkartmanın "tap"ı yukarı taşındı; "boing"in titreşim derinliği perdeyle birlikte ölçeklendi ki karakteri aynı kalsın. Trampet değişmedi: önerilen 260→180 Hz'in enerjisi yine %100 300 Hz altındaydı, telefonda −42 dB, ve zil 30 ms sonra başlıyor. |
| 7 | değiştirilerek | x3 küçük ödül olarak kaldı: rozet belirip zıplar, "Üç üst üste!" der. Zil ve kalpler x5'ten başlar. Büyük kutlama günde 9,2'den 4,75'e iniyor (benzetim); Necip'in sık küçük ödül isteği korunuyor. |
| 8 | değiştirilerek | Süre önerildiği gibi en az 2 s, 500 ms + karakter başına 60 ms. Boş 70 px'lik yuva yerine doğru anlam, karar sırasında zaten kapalı olan iki düğmenin yerinde yazar. 320×568'de yuva düğmeleri altbilginin arkasına iterdi. |
| 9 | değiştirilerek | "N kelime eşiğini geçtin!" yerine "N kelimeye ulaştın!": toplam tam N olduğunda da doğru, "eşik" teknik bir söz. |
| 10 | uygulandı | Son iki övgü yeniden çıkmaz; 30 doğruda tekrar yok, 8 övgünün hepsi görüldü. |

### 3. Sesler: önce ve sonra
Her ses tek başına, uygulamanın kendi koduyla, kayıt dışı çizildi (`S6/ses/uret.js`, `S6/ses/olc.py`; gözlemcinin yöntemi). Değerler 50 ms'lik en yüksek düzeydir, dB cinsinden: düz / A ağırlıklı / telefon modeli. Telefon modeli A ağırlığı ile 500 Hz yüksek geçiren süzgecin birlikte uygulanmasıdır; kaba bir taklittir.

| Ses (günde) | Önce | Sonra |
|---|---|---|
| ok, seri 1 (~36) | −15,5 / −17,1 / −18,3 | −19,6 / −21,2 / −22,4 |
| ok, seri 7+ | −15,5 / −14,6 / −14,6 | −19,6 / −18,7 / −18,7 |
| gramer zili (≤10) | −14,9 / −16,6 / −17,8 | −19,0 / −20,7 / −22,0 |
| match (~12) | −16,9 / −17,3 / −17,7 | −20,7 / −21,1 / −21,6 |
| okStep, fiil turu (≤20) | −16,1 / −19,2 / −21,0 | −20,2 / −23,3 / −25,1 |
| kutu açılışı (1) | zil+tada −12,6 / −16,2 / −16,5 | yalnız zil −13,3 / −16,5 / −16,6 |
| tada, çıkartma (1) | −16,3 / −17,7 / −18,5 | −16,3 / −17,6 / −18,4 |
| "tap" (tada içinde, tek başına) | telefon −36,3, merkez 245 Hz | telefon −29,4, merkez 581 Hz |
| win, gün sonu (1) | −16,7 / −16,8 / −17,0 | değişmedi |
| fire, seri alevi (1) | −25,1 / −26,2 / −26,2 | −13,8 / −16,7 / −18,9 |
| giggle, Lokum (0–3) | −32,3 / −31,7 / −31,8 | −27,7 / −27,1 / −27,1 |
| no, yanlış (~5) | −16,6 / −23,7 / −31,4 | −20,8 / −23,6 / −25,9 |
| no 290, gramer | −16,6 / −24,9 / −33,5 | −20,8 / −24,3 / −27,6 |

- "Boing"in ilk 250 ms'sindeki 300 Hz altı enerji %72'den %0'a indi. Perdesi ~340→220 Hz yerine ~640→430 Hz.
- **Asıl bulgu.** Gözlemcinin değerleri düz dBFS'te istenen sırayı kuruyordu, ama A ağırlıklı ölçümde ve telefon modelinde kurmuyordu. Zil ve alev telefonda sıradan bir doğru cevaptan büyük duyulmuyordu. Kararları bu yüzden A ağırlıklı ve telefon modeli değerlerine göre verdim.
- run14 bu sırayı da denetliyor: günde 20'den çok çalan ses her günlük kutlamanın en az 3 dB altında; yanlış ve Bilmiyorum doğru cevaptan alçak; kıkırdama duyulur ama doğru cevaptan alçak; "boing" 300 Hz'in üstünde.
- Kimse dinlemedi. Her değişiklik tek satırdır, eski değeri bu tabloda ve `git diff` içinde durur.

### 4. Uygulama simgesi: Lokum
Kararı ben verdim, çünkü Necip "yolu varsa yap" dedi. Eski simge (üç satırlık form ve tik) 48 px'te üç ince çubuğa dönüşüyordu ve herhangi bir anket uygulaması gibiydi. Lokum aynı boyda bir yüz olarak okunuyor ve uygulamanın karakteri.

Ana çizim `sanat/oneri-ikon-lokum.svg`. Tek değişiklik: parıltı başa yaklaştırıldı ve %15 küçüldü. Böylece maskelenebilir simgenin %80'lik güvenli dairesine giriyor; en uzak nokta 201 px, sınır 205 px.

Üretilen dosyalar:
- `icon.svg`
- `icon-180.png`, `icon-192.png`, `icon-512.png`: RGB, tam dolu kare.
- `android/icons/ic_launcher-*.png`: 48–192 px, bugünkü yuvarlak kare maskesiyle.
- `android/icons/ic_launcher_fg-*.png`: 108–432 px, saydam ön plan. Arka plan uygulamanın morunu (#5B3DF5) veren renk kaynağı. En uzak nokta 128 px, 66 dp güvenli dairesi 132 px. Lokum tuvalin %57'si; eski çizim %46'ydı.

Çizim Chromium ile yapıldı, maske ve renk tipi PIL ile; betik `S6/ikon/uret.js` ve `son.py`. Daire, yumuşak kare, damla ve yuvarlak kare maskelerinde 48, 72 ve 110 px'te açık ve koyu duvar kağıdında denetlendi. İmzasız deneme APK'sı yeni simgelerle üretildi. Hizmet çalışanı simgeleri "önce önbellek, arkada güncelle" düzeniyle verdiği için yeni simge web'de ikinci açılışta görünür.

### 5. Çıkartma seti
Değişmedi. Tek temalı bir set Gemini görseli istiyor, Gemini'ye buradan ulaşılamıyor.

### 6. Gözlemcinin İLYA İÇİN tablosu
On dört satırı kare dizileri, döküm ve yeni çekimlerle tek tek denetledim.
- On iki satırı kendi gözümle doğruladım (kare dizileri ve döküm).
- Ses düzeyi satırı karede denetlenemez; ölçümü kendim yeniden ürettim, gözlemcinin sayılarıyla birebir.
- Hareketi azalt videoda yok; kendi çekimlerimle ve animasyon sayımıyla (0 animasyon, 0 parçacık) denetledim.
- Bir satırda neden farklı çıktı: x3 rozetinin kendisi sayaca hiç binmiyor (iki sürümde de 0 kare). Sayacı örten, rozetten uçan kalplerdi: eski sürümde 154–604 ms arasında 28 kare, yeni sürümde x3'te 0 kare.
- Bir satır yalnız kısmen doğru: seri hapının zıplaması 17. dizide +200–300 ms'de seçiliyor, ama çok küçük.

### 7. Testler
`test/run14.js` eklendi (37 denetim) ve `hepsi.sh` artık 9 paket, 353 denetim çalıştırıyor: HEPSİ GEÇTİ.

Eski testlerde değişenler:
- **Yalnız zamanlama.** run6 ve run7: setin ilk sorusundan önce 520 ms. run9 ve run13: Devam'ın yerindeki Bilmiyorum'dan önce 520 ms; run13 ayrıca test satırından sonraki ilk şıktan önce. run11: fiil düzey satırından sonra 520 ms. run10: sayfa saati kuruldu; doğru cevapta artık olmayan Devam'a basmak yerine 650 ms'lik geçiş ve 500 ms'lik kapı ileri sarılıyor. Hepsi insanın yapamayacağı kadar hızlı dokunuşlardı.
- **Bilerek değiştirdiğim davranış, aynı sıkılıkta.** run11: x3'te ses kaydı "ok" (önce "ok,combo"), fiil x3'te "okStep,okStep", kutu açılışında "crash" (önce "crash,tada"). run13: "10 kelimeye ulaştın!".
- Hiçbir denetim zayıflatılmadı; paketlerin denetim sayıları aynı.
- run12 bu turdan önce de paralel yük altında arada bir kırılıyordu; tek başına art arda üç kez geçti.

### 8. Kalanlar
1. Cevap anında seçilen şık 300 px yukarı sıçrıyor (her cevapta; 03. kare dizisi). Sonuç ekranında şıklar yerinde kalıp renklenmeli, açıklama altta gelmeli. Bir sonraki tasarım turu.
2. Çıkartmalar hazır Fluent Emoji ve tek bir temaları yok. Gemini ile Lokum'un çizgisinde 24'lük bir set.
3. Sesler gerçek telefonda dinlenmeli. Orta sınıf bir Android'de %50 seste şu sırayla: ok (seri 1 ve 7), no, idk, giggle, fire, kutu açılışı, tada. Kötü olanın tek satırı geri alınır.
4. Küçükler, dokunulmadı: Lokum'un balonu 2,4 s tarih satırını örtüyor (isteğe bağlı dokunuşta); kart geçişinde 100 ms çift pozlama (zevk); 320×568'de Eşleşme mi?'nin yardım yazısı altbilginin altında kalıyor (önceden de böyleydi).


## 9/10 turu (İlya'nın 8/10 raporundan sonra)

Necip: "sen dene baklaım 9 için neler yapacaksın." Yapılanlar:

1. **Şıklar cevapta yerinde.** Sonuç ekranında beş şık soru ekranındaki yerinde kalır; doğru yeşil ve tikli, seçilen yanlış kırmızı ve çarpılı, ötekiler soluk. Hap ve "Neden yanlış?" şıkların altında, kelime kartı en altta. Kelime turu, cümle tamamlama, gramer ve fiil taramasında 320–390 px'te 0 px kayma (`test/run15.js`).
2. **Yumuşak kaydırma kartı kesmez.** Açıklama görünmüyorsa gövde ya hiç kaymaz ya soru kartının (ve soru cümlesinin) tamamını geçer.
3. **Çıkartmalar ve arayüz simgeleri bizim çizgimizde.** 24 çıkartma Lokum'un yüzüyle (`sanat/cikartma-uret.py`), 12 arayüz simgesi yüzsüz (`sanat/arayuz-uret.py`). Gramer ünitesi simgeleri ve 238 kelime görseli 1,05 birimlik #17132B dış çizgiyle gösterilir; ince kalanlar `sanat/ince-kelime-gorselleri.md` içinde.
4. **Sesler.** Necip telefonda dinledi ve cevap seslerinin (doğru, "boing", fiil adımı, eşleşme, x3 zili) öncekini istedi; geri alındı. Kutu açılışı, seri alevi ve Lokum'un kıkırdaması son düzeltmelerdeki değerlerde.
5. **Yazılar.** "Yapay zekâ kokmasın": ipuçları, Lokum'un sözleri, Nasıl işliyor, kutu ve albüm notları sadeleşti; çeviri kokan sözler gitti ("Durdurulamazsın!" → "Seni tutan yok!"). Gramer ve bağlaç açıklamalarında 783 noktalı virgül noktaya çevrildi.
6. **Küçükler.** Lokum konuşurken balon tarih satırının yerine geçer. Kısa ekranda eşleşme oyununun yardım yazısı gizlenir. Fiil taramasında altbilgi Devam olmasa da aynı boyda kalır. Gramer sonucunda İngilizce ünite adı Türkçe büyük harfe çevrilmez. Balon ipi 10 px, satır arası 36 px: ip alttaki balona girmez.

İlya'nın sonucu: **9/10.** Sonra:
- **Balonlar** gerçek balon biçiminde çizildi (Necip: "balonların şekillerini hiç beğenmedim"); boyları ekrandaki boşluğa göre hesaplanır, patlama anlam kartının altında kalır.
- **İlk 13 gramer ünitesinin simgeleri** düz renkle yeniden çizildi (`sanat/unite-uret.py`; aynı çizimi kullanan 14 ünite).
- **İnce kelime görselleri** (16 kelime) kalın biçimlerle yeniden çizildi (`sanat/kelime-gorsel-uret.py`).
- **Tanıtım videosunda** İngilizce kelimeleri Piper'ın doğal sesi okur (`sanat/piper-ses-hazirla.py`).
- **İlya'nın silüet turu** (balon ekranı 8/10, genel 9/10): ahtapot sekiz kıvrık kollu yeniden çizildi (denizanasından ayrılsın); kelime görseli kutunun %80'ini doldurur ve beyaz yuvarlak tabana oturur; teleskop mor (fiil mavisine karışmasın); ataş gerçek ataş; bağlaç atölyesi ve bağlaç üniteleri yeni zinciri kullanır; pusulaya dört yön çentiği; balon çizgisi kart çizgisine yakın, grup dikeyde ortalı; koyu temada test halkaları seçilir.
- Kalan: öteki 29 ünite simgesi (çizgili hazır çizim).
