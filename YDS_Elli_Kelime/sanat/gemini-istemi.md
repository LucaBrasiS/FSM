# Gemini Pro'ya verilecek istem (son sürüm değerlendirmesi)

## Nasıl kullanılır

1. Gemini'yi aç ve **Pro** modelini seç. En yüksek düşünme ayarı varsa (örneğin Deep Think) onu aç.
2. İki dosyayı ekle:
   - `Basamak-tanitim.mp4`
   - `Basamak-tanitim-dokum.txt`
3. Aşağıdaki çizgiler arasındaki metni olduğu gibi yapıştır.
4. Cevabın tamamını kopyalayıp `gemini-rapor.md` adıyla kaydet. Sonra `ilya-istemi.md` ile İlya'ya ver.

Bulut oturumunda Gemini anahtarı tanımlıysa `python3 gemini-gonder.py Basamak-tanitim.mp4 Basamak-tanitim-dokum.txt` aynı işi kendisi yapar.

---

Sen bağımsız bir değerlendiricisin: mobil uygulamaların hareketini, zamanlamasını, sesini ve öğretimini izleyip dinleyerek yargılayan, işin yapılmasında payı olmayan bir uzmansın. Bu, uygulamanın yayından önceki son değerlendirmesi; bulgularına göre son düzeltmeler yapılacak. Bu işi yüksek özenle yap:

- Videonun tamamını sesiyle en az iki kez izle.
- Aşağıdaki anlara kare kare bak.
- Her yargıyı videoda bir zamana bağla.

## Neyi değerlendiriyorsun

**Basamak**, YDS sınavına hazırlanan Türk öğrenciler için bir İngilizce öğrenme uygulaması. Telefonda çalışır, yalnızca dokunma ve sürükleme kullanılır, arayüz Türkçedir.

- **Hedef kitle:** 16–30 yaş, ağırlıklı olarak genç kadınlar.
- **Günlük kullanım:** yaklaşık 15 dakika.

İçerik:

- **Günlük kelime turu:** 20 yeni kelime. Tanıtım kartları, beş şıklı sorular, eşleştirme, cümle kurma, gün sonu kontrolü.
- **Yanlış cevap:** doğrusu gösterilir. Kullanıcının seçtiği şık başka bir kelimenin anlamıysa, "Neden yanlış?" kutusu o şıkkın hangi kelimeye ait olduğunu söyler. Karıştırılan kelime sonraki sorularda bilerek yeniden şık olarak gelir.
- **Sürpriz kutu:** günde bir kez, tur ortasında, puantiyeli mor bir "oyun odası" zemininde çıkar.
  - Kutu üç dokunuşla açılır.
  - İçinden sırayla üç kısa oyundan biri çıkar: balon patlat, hafıza kartları, "Eşleşme mi?".
  - "Eşleşme mi?" oyununda kart sağa kaydırılırsa "eşleşiyor", sola kaydırılırsa "eşleşmiyor" demektir.
  - Oyunun sonunda bir çıkartma kazanılır ve albüme yapışır.
- **Maskot:** Lokum adında, pudra şekerli bir lokum küpü. Bugün ekranında selam verir; dokununca kıkırdar ve kısa bir söz söyler. Kutlama kartlarında da görünür. Rengi ("tadı") Ayarlar'dan seçilir; yeni tatlar çalışma günleriyle açılır.
- **Gün özeti:** günün sonunda "bugün kazandıkların" çipleri çıkar: seri, çıkartma, öğrenilen kelime, toplam kelime eşiği, yeni tat.
- **Diğer:** günün grameri, fiil taraması (A1–B2 fiilleri) ve çıkartma albümü.

Uygulamanın sahibinin istekleri:

- Tatlı ve sevecen olsun; 16–30 yaş, çoğunlukla kadın kullanıcılara hitap etsin.
- Dopamin veren küçük ve sık ödüller olsun.
- Öğretim oyun havasında geçsin, ama oturum oyun gibi uzamasın.
- Sesler "tatlı, uyandırıcı, komik" olsun; kullanıcı sıkılmasın.
- Bugün ve Kelime ekranları sade kalsın. Bu ekranlara yeni öğe önerme.

Uygulamanın görsellerini, durağan ekran görüntülerinden yargılayan bir görsel yargıç ajan değerlendiriyor; adı **İlya**. İlya bu tasarımı yaptı ve 8/10 verdi, ama hareketi, zamanlamayı ve sesi göremiyor. Senin raporunun üç amacı var:

1. Bu kayıtta İlya'nın göremediğini görmek ve duymak.
2. Son düzeltmeler için öncelikli ve sayılarla yazılmış bir iş listesi vermek.
3. İlya'nın ölçütlerini hareket, zamanlama ve ses yönünde genişletmek.

## Kayıt hakkında bilmen gerekenler

- **Üst şerit uygulamanın parçası değil.** Videonun üstündeki koyu şerit kayda sonradan eklendi. Kaydın adını, bölümü, o anki adımı ve süre sayacını gösterir.
  - Zamanları bu sayaçtan **dakika:saniye.onda biri** olarak ver.
  - Sayaç, oynatıcının zamanıyla aynıdır.
- **Kayıt nasıl alındı.** Uygulama masaüstü tarayıcıda telefon boyunda (390×844) otomatik bir senaryoyla oynatıldı. Dokunuşlar bir insanınkinden daha düzenli ve biraz hızlı. Kullanıcının duraksamasını ya da kararsızlığını yargılama.
- **Sesler gerçek.** Efektlerin hepsi uygulamanın kendi ürettiği seslerdir, kod içinde sentezlenir. Hoparlörden değil, doğrudan sayısal olarak alındılar. Telefon hoparlöründe tizler daha baskın, baslar daha zayıf duyulur.
- **İngilizce okuyan ses kayda sonradan kondu.** Kayıttaki ses Piper'ın yapay sinir ağı sesidir (en_US-joe-medium); telefonda kelimeyi cihazın kendi sesi okur. Sesin tınısını yargılama; şunları yargıla:
  - **ne zaman** okuduğunu,
  - neyle çakıştığını,
  - ne sıklıkta okuduğunu.
- **Demo aracı.** İki kez kullanıldı. Bu araç gerçek uygulamada yok; onu yargılama.
  - **01:40–01:43:** "Eşleşme mi?" oyunu bir deneme düğmesiyle açıldı. Gerçek uygulamada bu oyun üçüncü gün kutudan çıkar. Bu yüzden oyunun sonunda "Deneme oyunu" yazıyor ve çıkartma albüme eklenmiyor.
  - **02:02–02:04:** Günün kalanı bir düğmeyle otomatik bitirildi.
- **Zaman dökümü.** Ekteki `Basamak-tanitim-dokum.txt`, hangi saniyede hangi adımın atıldığını, hangi sesin (iç adıyla) çaldığını ve neyin okunduğunu listeler.
  - Önce kendin izle ve dinle.
  - Dökümü yalnızca eşleştirmek için kullan, kanıt sayma.
  - Gördüğün ya da duyduğun döküme uymuyorsa bunu yaz.

## Kare kare bakılacak anlar

Her biri için görüntüyü ve sesi milisaniye düzeyinde eşleştir:

1. **Bugün ekranı:** Lokum'un selamı; iki dokunuşta kıkırdaması ve konuşma balonu.
2. **Tanıtım kartı:** kelimenin kendiliğinden okunması ve örnek cümledeki vurgunun nabız atması.
3. **Kart geçişi:** önceki ve sonraki tanıtım kartına geçiş, kart kayması ve "vup" sesi.
4. **Cevap anı:**
   - doğru: iki vuruş, tik işaretinden parıltı, her seferinde değişen övgü;
   - yanlış: "Bu sefer olmadı", "Neden yanlış?" kutusu;
   - Bilmiyorum: sakin lila hap.
5. **Devam:** cevaptan sonra eski kart sola kayar, yenisi sağdan gelir, "fşşt" sesi çalar. Günde yaklaşık 40 kez olur.
6. **Üç doğru üst üste:** x3 rozeti, "Üç üst üste!" övgüsü, kalpler ve "ding-ding".
7. **Bölüm geçişleri:** eşleştirmeye, cümleye ve kutuya geçerken "fiuv" ve ilk kartın zıplayarak gelmesi.
8. **Eşleştirme:** doğru çift ve kalpler, yanlış deneme, tur sonu.
9. **Cümle kurma:** parçaların yerleşme sesi, kontrol anı.
10. **Sürpriz kutu:** oyun odasına geçiş, üç dokunuşta artan sallanma ve uzayan trampet. Açılış: kapağın uçması, ışık, konfeti, zil ve tada, ardından oyuna geçiş.
11. **Balon patlatma:** doğru balonun patlaması, yanlış balonun sönmesi.
12. **Ödül anı:** çıkartmanın büyük ve eğik düşüp yapışması, "tap" sesi, damga kartı, çıkartmanın İngilizce adının okunması.
13. **"Eşleşme mi?" oyunu:** sürüklerken beliren damga, kartın uçması, yanlış kararda doğrusunun yazılması.
14. **Gün özeti:** Lokum, başlık, kazanılanlar çipleri. Ardından Bugün ve Kelime ekranında gün serisi hapının "alev" sesiyle zıplaması.
15. **Gramer:** zil tınılı doğru sesi, yanlış sesi, Devam kayması.
16. **Fiil taraması:** doğru cevapta kendiliğinden sıradaki fiile geçiş, tur boyunca tırmanan nota, x3 rozeti.
17. **Çıkartma albümü:** kazanılan çıkartmalar ve kazanılmayanların silüetleri.
18. **Koyu tema:** koyu temaya geçiş.

## Nasıl yargılarsın

- **Yeri göster.** Her yargı videoda bir zamanı ve ekranda bir yeri gösterir: hangi düğme, hangi kart, hangi köşe. Ardından kullanıcının ne kaybettiğini söyler.
- **Gözlemi yorumdan ayır.** Önce ne gördüğünü ve duyduğunu yaz, sonra hükmünü.
- **Her bulguyu etiketle:**
  - **KESİN:** videoda gördün ya da duydun.
  - **OLASI:** güçlü çıkarım.
  - **TAHMİN:** sınanması gerekir; hangi sınamanın çözeceğini yaz.
- **Ölçülebilir kusuru zevkten ayır.** Zevk olanı öyle etiketle.
  - Kusur örnekleri:
    - sesin hareketten 100 ms'den fazla önce ya da sonra gelmesi;
    - iki sesin çakışıp birbirini bastırması;
    - okunuşun bir efektle örtülmesi;
    - takılan ya da atlayan animasyon;
    - okunmayacak kadar hızlı geçen yazı;
    - dokunuşa 100 ms içinde karşılık gelmemesi;
    - bir yazının ya da düğmenin başka bir öğenin altında kalması.
  - Zevk örneği: "Ben daha tiz yapardım."
- **Sayı ver.**
  - süre: ms;
  - perde: yaklaşık Hz, ya da "yukarı/aşağı kayan";
  - yükseklik: öteki seslere göre daha yüksek, eşit ya da daha alçak.
- **Düzeltmeyi sayıyla öner.** Sesler kodla sentezlendiği için düzeltme parametre olarak yazılmalı. "Daha iyi ses" bir öneri değildir.
  - ses: süre (ms), başlangıç gecikmesi (ms), perde (Hz) ya da yön, göreli yükseklik (dB), sönüm süresi;
  - hareket: süre (ms), ölçek, açı, yön.
- **Övgüyle açma, kusur uydurma.** İyi olanı nedeniyle kısaca söyle.
- **Kaldırmayı eklemeye tercih et.** Sorunu çözmeyen yeni ses, hareket ya da süs önerme.
- **Tek kişinin yapabileceği öneriler ver.** Ses dosyası satın almak, besteci ya da illüstratör tutmak öneri değildir.
- **Hedef kitleyi gerçekçi tart.**
  - 16 yaşındaki bir lise öğrencisi ile 30 yaşında, iş arayan bir mezun aynı ekrana bakıyor. Tatlılık birine sevimli, ötekine çocuksu gelebilir; nerede sınırda olduğunu söyle.
  - "Kadınlar pembe sever" gibi kalıp yargılara dayanma. Duygusal tasarımın ölçülebilir işaretlerine bak:
    - ödülün sıklığı ve büyüklüğü,
    - hatanın nasıl karşılandığı,
    - kişiselleştirme,
    - karakterin ne kadar sık ve nerede çıktığı.
- **Puan ölçeğini sabit tut:**
  - 9–10: türünün en iyilerinin yanında durur
  - 7–8: iyi, küçük düzeltme ister
  - 5–6: çalışıyor ama yer yer amatör
  - 3–4: karışık ya da tutarsız
  - 1–2: işlemiyor

  Karşılaştırma için türün iyi örneklerini adıyla an: Duolingo, Memrise, Babbel, Drops, Quizlet, Finch gibi.

## Rapor

Türkçe yaz. Selam ya da hitap yazma, doğrudan KARAR ile başla. Aşağıdaki başlıkları bu sırayla ve bu adlarla kullan.

**KARAR:** Tek cümle. Ardından beş puan:

- Genel N/10
- Hareket N/10
- Ses N/10
- Tatlılık ve sevecenlik N/10
- Öğretim N/10

**ZAMAN ÇİZELGESİ:** Dikkat çeken 25–35 an, bir tabloda. "Uyum" sütununa ses ile hareket arasındaki farkı ms olarak yaz; ölçemiyorsan "ölçemedim" de.

| Zaman | Bölüm | Görüntü | Ses | Uyum | Not |
|---|---|---|---|---|---|

**ANLAR:** Yukarıdaki 18 anın her biri için kısa bir blok:

- Görüntü
- Ses
- Uyum
- Tekrar yükü: bir günlük oturumda kaç kez görülür ya da duyulur
- Hüküm: kusur ya da zevk
- Düzeltme: sayıyla

**HEDEF KİTLE:** Uygulamanın sahibinin isteğine göre değerlendir. Her maddeyi videodan bir zamana bağla.

- Tatlılık: tatlı ve sevecen mi? Nerede tam oturuyor, nerede çocuksu ya da fazla kaçıyor?
- Lokum: karakter işini görüyor mu, fazla mı az mı çıkıyor?
- Ödül döngüsü: küçük ve sık ödüller var mı? Ödüller birbirini bastırıyor mu, enflasyona uğruyor mu?
- Oturum süresi: oyun havası oturumu uzatıyor mu? Sürpriz adımının (kutu, oyun, ödül) toplam süresini ölç ve yargıla.
- Yarın geri gelmek: kullanıcıyı yarın geri getirecek şey ne? Eksik olan ne?

**ÖĞRETİM:**

- Yanlış cevabın karşılanması: "Bu sefer olmadı", "Neden yanlış?" kutusu ve "Eşleşme mi?" oyununda doğrusunun yazılması. Kullanıcı neden yanıldığını anlıyor mu, yazı okunacak kadar ekranda kalıyor mu?
- Oyunlar: sürpriz oyunlar öğretime bağlı mı, yoksa yalnızca süs mü?
- Okuma: İngilizce okumanın zamanlaması öğrenmeye yardım ediyor mu?

**SORUNLAR:** En çok beş, kullanıcıya verdiği zarar sırasıyla. Her biri için:

- etiket (KESİN, OLASI, TAHMİN)
- zaman
- ne ve nerede
- kullanıcı ne kaybeder
- düzeltme (sayıyla)
- aynı durumu iyi çözen bilinen bir uygulama

**DÜZELTME LİSTESİ:** Son düzeltmeler için öncelik sırasıyla en çok 10 madde. Her madde tek satır olsun ve şunları içersin:

- ne değişecek
- hangi ekranda ve hangi anda (zaman)
- hangi sayıyla
- beklenen etki

Bir geliştirici bu listeyi videoya bakmadan uygulayabilmeli. Yeni bir özellik, ekran ya da ikinci bir karakter önerme; var olanı düzelt.

**SIKILMA:** 15 dakikalık bir günlük oturumda ve bir haftalık kullanımda:

- hangi hareket ya da ses ilk bıktırır, neden ve ne zaman;
- hangisi bıktırmaz;
- hangisinin sayısı azaltılmalı ya da sesi kısılmalı.

**KORUNACAKLAR:** Düzeltirken bozulmaması gereken üç dört şey.

**İLYA İÇİN:** İlya yalnızca durağan ekran görüntülerine, kare dizilerine ve yazıya bakabilir. Her bulgunu onun kontrol edebileceği bir işarete çevir, tablo halinde.

| Bulgu | İlya'nın ölçütü | Durağan karede nerede | Durağan karede kontrol edilecek işaret |
|---|---|---|---|

- **İlya'nın ölçütü** şunlardan biri olmalı: okunabilirlik, odak ve sıra, durumun görünürlüğü, tutarlılık, kimlik, pazar ölçüsü, yapılabilirlik.
- **Durağan karede nerede:** zaman ya da ekran adı.

**İLYA'NIN TANIMINA EK:** İlya'nın değerlendirme ölçütlerine eklenebilecek, kendi kurallarıyla aynı üslupta, olduğu gibi yapıştırılabilir bir bölüm yaz. Başlığı şu olsun: `## Hareket, zamanlama ve ses (video, kare dizisi ya da döküm verildiğinde)`. İçeriği:

- **Neye bakılır:** önem sırasıyla numaralı maddeler. Her madde ölçülebilir bir denetim ve gerekçeli bir eşik içersin. Örnek konular:
  - dokunuştan karşılığa gecikme
  - ses ile hareketin eşleşmesi
  - geçiş süreleri
  - tekrar yükü: günde çok çalan bir sesin ne kadar kısa ve yumuşak olması gerektiği
  - kutlamaların seyrekliği
  - okunuşun efektlerle çakışmaması
  - "hareketi azalt" ayarında davranış
  - bir oturumun ritmi
- **Kanıt türleri:** bu ölçütleri video olmadan kare dizisinden, zaman dökümünden ve senin gibi bir gözlemcinin raporundan nasıl yargılayabileceği. Başka bir gözlemcinin bulgusunu nasıl etiketleyeceği; örneğin "gözlemciye göre (KESİN, 00:42.3)".
- **Görülmeyen kalır:** hiçbir kanıt yoksa yine "görmedim" diyeceği.
- **Puan:** aynı 1–10 ölçeğinin hareket ve ses için ne anlama geldiği.

Bu bölüm en fazla 350 kelime olsun ve yalnızca bu uygulamaya değil, mobil oyun ve uygulamalara genel olarak uysun.

**GÖREMEDİKLERİM:** Videodan yargılayamadığın şeyler (telefon hoparlörü, titreşim, cihazın gerçek okuma sesi, gerçek parmakla dokunma hissi) ve yaptığın varsayımlar.

---
