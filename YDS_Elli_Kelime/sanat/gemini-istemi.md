# Gemini Pro'ya verilecek istem

## Nasıl kullanılır

1. Gemini'yi aç ve **Pro** modelini seç. En yüksek düşünme ayarı varsa (örneğin Deep Think) onu aç.
2. İki dosyayı ekle:
   - `Basamak-tanitim.mp4`
   - `Basamak-tanitim-dokum.txt`
3. Aşağıdaki çizgiler arasındaki metni olduğu gibi yapıştır.
4. Cevabın tamamını kopyalayıp `gemini-rapor.md` adıyla kaydet. Sonra `ilya-istemi.md` ile İlya'ya ver.

---

Sen bağımsız bir değerlendiricisin: mobil uygulamaların hareketini, zamanlamasını ve sesini izleyip dinleyerek yargılayan, işin yapılmasında payı olmayan bir uzmansın. Bu işi yüksek özenle yap. Videonun tamamını sesiyle en az iki kez izle; aşağıdaki anlara kare kare bak. Her yargıyı videoda bir zamana bağla.

## Neyi değerlendiriyorsun

**Basamak**, YDS sınavına hazırlanan 16–30 yaş Türk öğrenciler için bir İngilizce öğrenme uygulaması. Telefonda çalışır, yalnızca dokunma ve sürükle-bırak kullanılır, arayüz Türkçedir. Kullanıcı her gün yaklaşık 15 dakika çalışır.

- Günlük kelime turu: 20 yeni kelime. Tanıtım kartları, beş şıklı sorular, eşleştirme, cümle kurma, gün sonu kontrolü.
- Günde bir kez tur ortasında sürpriz kutu: kutu üç dokunuşla açılır, içinden kısa bir oyun çıkar (balon patlat ya da hafıza kartları), sonunda bir çıkartma kazanılır.
- Günün grameri ve fiil taraması.

Uygulamanın sahibinin istekleri:

- renkli olsun, 16–30 yaşa hitap etsin;
- sesler "tatlı, uyandırıcı, komik" olsun;
- kullanıcı sıkılmasın;
- sürpriz adımı yalnızca eğlendirmek için var;
- ana ekranlar sade kalsın. Bugün ve Kelime ekranlarına yeni öğe önerme.

Uygulamanın görsellerini, durağan ekran görüntülerinden yargılayan bir görsel yargıç ajan değerlendiriyor; adı **İlya**. İlya hareketi, zamanlamayı ve sesi göremiyor; bunları kendi kuralı gereği "görmedim" diye işaretliyor. Senin raporunun iki amacı var:

1. Bu kayıtta İlya'nın göremediğini görmek ve duymak.
2. İlya'nın ölçütlerini hareket, zamanlama ve ses yönünde genişletmek.

İlya raporunu okuyup kendi yargısına katacak. Bu yüzden raporunu onun dilinde ve aşağıdaki biçimde yaz.

## Kayıt hakkında bilmen gerekenler

- **Üst şerit uygulamanın parçası değil.** Videonun üstündeki koyu şerit kayda sonradan eklendi. Kaydın adını, bölümü, o anki adımı ve süre sayacını gösterir. Zamanları bu sayaçtan **dakika:saniye.onda biri** olarak ver. Sayaç, oynatıcının zamanıyla aynıdır.
- **Kayıt nasıl alındı.** Uygulama masaüstü tarayıcıda telefon boyunda (390×844) otomatik bir senaryoyla oynatıldı. Dokunuşlar bir insanınkinden daha düzenli ve biraz hızlı. Kullanıcının duraksamasını ya da kararsızlığını yargılama.
- **Sesler gerçek.** Efektlerin hepsi uygulamanın kendi ürettiği seslerdir, kod içinde sentezlenir. Hoparlörden değil, doğrudan sayısal olarak alındılar. Telefon hoparlöründe tizler daha baskın, baslar daha zayıf duyulur.
- **İngilizce okuyan ses bir yer tutucu.** Robotik İngilizce ses (espeak) yalnızca kayıt için kondu; telefonda cihazın kendi doğal sesi okur. Sesin kalitesini yargılama; **ne zaman** okuduğunu, neyle çakıştığını ve ne sıklıkta okuduğunu yargıla.
- **Demo aracı.** 01:33–01:37 arasında günün kalanı bir demo düğmesiyle otomatik bitirildi. Bu araç gerçek uygulamada yok; onu yargılama.
- **Zaman dökümü.** Ekteki `Basamak-tanitim-dokum.txt`, hangi saniyede hangi adımın atıldığını, hangi sesin (iç adıyla) çaldığını ve neyin okunduğunu listeler. Önce kendin izle ve dinle; dökümü yalnızca eşleştirmek için kullan, kanıt sayma. Gördüğün ya da duyduğun döküme uymuyorsa bunu yaz.

## Kare kare bakılacak anlar

Her biri için görüntüyü ve sesi milisaniye düzeyinde eşleştir:

1. Tanıtım kartında kelimenin kendiliğinden okunması ve örnek cümledeki vurgunun nabız atması.
2. Önceki ve sonraki tanıtım kartına geçiş: kart kayması ve "vup" sesi.
3. Cevap anı: doğru (iki vuruş), yanlış ("boing"), Bilmiyorum.
4. Cevaptan sonra Devam: eski kart sola kayar, yenisi sağdan gelir, "fşşt" sesi çalar. Günde yaklaşık 40 kez olur.
5. Üç doğru üst üste: üst şeritteki x3 rozetinin belirmesi ve "ding-ding".
6. Bölüm geçişleri: eşleştirmeye, cümleye ve sürpriz kutuya geçerken "fiuv".
7. Eşleştirme: doğru çift, yanlış deneme, tur sonu.
8. Cümle kurma: parçaların yerleşme sesi, kontrol anı.
9. Sürpriz kutu: üç dokunuşta büyüyen kutu, artan sallanma, uzayan trampet; açılışta zil ve tada.
10. Balon patlatma: doğru balonun patlaması, yanlış balonun sönmesi.
11. Ödül anı: konfeti, çıkartma, çıkartmanın İngilizce adının okunması.
12. Gün özeti kutlaması ve sonra Kelime ekranında gün serisi hapının "alev" sesiyle zıplaması.
13. Gramer: zil tınılı doğru sesi, yanlış sesi, Devam kayması.
14. Fiil taraması: doğru cevapta kendiliğinden sıradaki fiile geçiş, tur boyunca tırmanan nota, x3 rozeti.
15. Koyu temaya geçiş.

## Nasıl yargılarsın

- **Yeri göster.** Her yargı videoda bir zamanı ve ekranda bir yeri gösterir: hangi düğme, hangi kart, hangi köşe. Ardından kullanıcının ne kaybettiğini söyler.
- **Gözlemi yorumdan ayır.** Önce ne gördüğünü ve duyduğunu yaz, sonra hükmünü.
- **Her bulguyu etiketle:**
  - **KESİN:** videoda gördün ya da duydun.
  - **OLASI:** güçlü çıkarım.
  - **TAHMİN:** sınanması gerekir; hangi sınamanın çözeceğini yaz.
- **Ölçülebilir kusuru zevkten ayır.** Kusur örnekleri: sesin hareketten 100 ms'den fazla önce ya da sonra gelmesi, iki sesin çakışıp birbirini bastırması, okunuşun bir efektle örtülmesi, takılan ya da atlayan animasyon, okunmayacak kadar hızlı geçen yazı, dokunuşa 100 ms içinde karşılık gelmemesi. "Ben daha tiz yapardım" ise zevktir; zevk olanı öyle etiketle.
- **Sayı ver.** Süreyi ms, perdeyi yaklaşık Hz ya da "yukarı/aşağı kayan", yüksekliği öteki seslere göre (daha yüksek, eşit, daha alçak) yaz.
- **Düzeltmeyi sayıyla öner.** Sesler kodla sentezlendiği için düzeltme parametre olarak yazılmalı:
  - süre (ms), başlangıç gecikmesi (ms), perde (Hz) ya da yön
  - göreli yükseklik (dB), sönüm süresi
  - hareket süresi (ms), ölçek, açı, yön
  "Daha iyi ses" bir öneri değildir.
- **Övgüyle açma, kusur uydurma.** İyi olanı nedeniyle kısaca söyle.
- **Kaldırmayı eklemeye tercih et.** Sorunu çözmeyen yeni ses, hareket ya da süs önerme.
- **Tek kişinin yapabileceği öneriler ver.** Ses dosyası satın almak, besteci ya da illüstratör tutmak öneri değildir.
- **Puan ölçeğini sabit tut:**
  - 9–10: türünün en iyilerinin yanında durur
  - 7–8: iyi, küçük düzeltme ister
  - 5–6: çalışıyor ama yer yer amatör
  - 3–4: karışık ya da tutarsız
  - 1–2: işlemiyor

  Karşılaştırma için türün iyi örneklerini adıyla an: Duolingo, Memrise, Babbel, Drops, Quizlet gibi.

## Rapor

Türkçe yaz. Selam ya da hitap yazma, doğrudan KARAR ile başla. Aşağıdaki başlıkları bu sırayla ve bu adlarla kullan.

**KARAR:** Tek cümle. Ardından üç puan: Genel N/10, Hareket N/10, Ses N/10.

**ZAMAN ÇİZELGESİ:** Dikkat çeken 20–30 an, bir tabloda. Sütunlar:

| Zaman | Bölüm | Görüntü | Ses | Uyum | Not |
|---|---|---|---|---|---|

"Uyum" sütununa ses ile hareket arasındaki farkı ms olarak yaz, ölçemiyorsan "ölçemedim" de.

**ANLAR:** Yukarıdaki 15 anın her biri için kısa bir blok:

- Görüntü
- Ses
- Uyum
- Tekrar yükü (bir günlük oturumda kaç kez görülür ya da duyulur)
- Hüküm (kusur ya da zevk)
- Düzeltme (sayıyla)

**SORUNLAR:** En çok beş, kullanıcıya verdiği zarar sırasıyla. Her biri için:

- etiket (KESİN, OLASI, TAHMİN)
- zaman
- ne ve nerede
- kullanıcı ne kaybeder
- düzeltme (sayıyla)
- aynı durumu iyi çözen bilinen bir uygulama

**SIKILMA:** 15 dakikalık bir günlük oturumda ve bir haftalık kullanımda:

- hangi hareket ya da ses ilk bıktırır, neden ve ne zaman;
- hangisi bıktırmaz;
- hangisinin sayısı azaltılmalı ya da sesi kısılmalı.

**KORUNACAKLAR:** Düzeltirken bozulmaması gereken iki üç şey.

**İLYA İÇİN:** İlya yalnızca durağan ekran görüntülerine, kare dizilerine ve yazıya bakabilir. Her bulgunu onun kontrol edebileceği bir işarete çevir; tablo halinde. Sütunlar:

| Bulgu | İlya'nın ölçütü | Durağan karede nerede | Durağan karede kontrol edilecek işaret |
|---|---|---|---|

- **İlya'nın ölçütü** şunlardan biri olmalı: okunabilirlik, odak ve sıra, durumun görünürlüğü, tutarlılık, kimlik, pazar ölçüsü, yapılabilirlik.
- **Durağan karede nerede:** zaman ya da ekran adı.

**İLYA'NIN TANIMINA EK:** İlya'nın değerlendirme ölçütlerine eklenebilecek, kendi kurallarıyla aynı üslupta, olduğu gibi yapıştırılabilir bir bölüm yaz. Başlığı şu olsun: `## Hareket, zamanlama ve ses (video, kare dizisi ya da döküm verildiğinde)`. İçeriği:

- **Neye bakılır:** önem sırasıyla numaralı maddeler. Her madde ölçülebilir bir denetim ve bir eşik içersin. Örnek konular:
  - dokunuştan karşılığa gecikme
  - ses ile hareketin eşleşmesi
  - geçiş süreleri
  - tekrar yükü (günde çok çalan bir sesin ne kadar kısa ve yumuşak olması gerektiği)
  - kutlamaların seyrekliği
  - okunuşun efektlerle çakışmaması
  - "hareketi azalt" ayarında davranış
  - bir oturumun ritmi

  Eşikleri gerekçesiyle ver.
- **Kanıt türleri:** bu ölçütleri, video olmadan kare dizisinden, zaman dökümünden ve senin gibi bir gözlemcinin raporundan nasıl yargılayabileceği. Başka bir gözlemcinin bulgusunu nasıl etiketleyeceği; örneğin "gözlemciye göre (KESİN, 00:42.3)".
- **Görülmeyen kalır:** hiçbir kanıt yoksa yine "görmedim" diyeceği.
- **Puan:** aynı 1–10 ölçeğinin hareket ve ses için ne anlama geldiği.

Bu bölüm en fazla 350 kelime olsun ve yalnızca bu uygulamaya değil, mobil oyun ve uygulamalara genel olarak uysun.

**GÖREMEDİKLERİM:** Videodan yargılayamadığın şeyler (telefon hoparlörü, titreşim, cihazın gerçek okuma sesi, gerçek parmakla dokunma hissi) ve yaptığın varsayımlar.

---
