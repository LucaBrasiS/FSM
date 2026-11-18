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
- **Doğru:** yeşil hap artık tik simgesi ve değişen bir övgüyle geliyor (Harika!, Süpersin!, Bildin!, Tam isabet!…). Seri anlarının kendi sözü var: üçte "Üç üst üste!", beşte "Beşte beş!", onda "On numara!". Tik işaretinden parıltı çıkar; seri anında x3, x5, x10 rozetinden kalpler de fışkırır. Ses değişmedi.
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
- **Eşleşme mi? (yeni)** `S/akis-eslesme-oyunu.png`: kartta bir İngilizce kelime ve bir Türkçe anlam var. Eşleşiyorsa sağa kaydırılır ya da kalbe dokunulur, eşleşmiyorsa sola ya da çarpıya. Sürüklerken "EŞLEŞME" ya da "DEĞİL" damgası belirir. Doğru karar kartı uçurur; doğru bir "eşleşiyor"dan kalpler çıkar. Yanlışta kart sallanır ve doğrusu yazılır ("observe aslında «gözlemlemek» demek."), 1,8 saniye sonra kart doğru yöne gider. Altı kart, yaklaşık 30 saniye. Bu yaş grubunun her gün kullandığı bir hareket, kelime öğretimine bağlandı. Eşleşen kartlar bugünkü kelimelerden, eşleşmeyenler aynı türden ve anlamı çakışmayan kelimelerden gelir.

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
- toplam kelime eşiği aşıldıysa "Toplam 50 kelime oldu!" (10, 25, 50, 75, 100, 150, 200, 250 ve bütün liste),
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
- **Sesler** tek düğmeyle kapanmaya devam ediyor. Yeni sesler: Lokum'un kıkırdaması, eşleşme oyununda "eşleşiyor" zili ve "eşleşmiyor" kayması, tada içinde çıkartmanın "tap"ı. Doğru, yanlış ve Bilmiyorum sesleri değişmedi.

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
1. **Uygulama simgesi.** Bugünkü simge bir form satırı ve tik; mağazada ve ana ekranda bir karakter daha çok akılda kalır. Lokum'lu öneri hazır: `sanat/oneri-ikon-lokum.svg`, karşılaştırma `S/ikon/karsilastirma.png`. Onaylarsan `icon.svg`, `icon-*.png` ve `android/icons/*` bundan üretilmeli, sonra APK yeniden derlenmeli. Ben değiştirmedim; marka kararı senin.
2. **Gemini görselleri isteğe bağlı.** Mağaza öne çıkan görseli ve Lokum poz seti için istemler `sanat/gemini-gorseller.md` içinde. Uygulama bunlara muhtaç değil.
3. **Gerçek telefonda deneme.** SVG filtreli çıkartmaların ve parçacıkların düşük güçlü Android'de akıcılığı ölçülmeli. Sesler telefon hoparlöründen dinlenmeli (özellikle kıkırdama ve "tap").
4. **İleride:** temalı çıkartma setleri (set tamamlama anı), Lokum'a çalıştıkça açılan aksesuarlar (fiyonk, taç). İkisi de toplama döngüsünü uzatır ama şimdi gerekli değil.
5. Ön çalışmadaki üç öneri (oyun odası, kalıp kesim albüm, açılmış koyu tema) uygulandı. `data/art.json` içinde daha önceden kalan, kullanılmayan birkaç çizim (madalya, not defteri, çerçeve…) ayrıca temizlenebilir.
