# Gemini görselleri (isteğe bağlı)

Bu turda Gemini'ye erişim yoktu, bu yüzden hiçbir görsel üretilmedi. **Uygulama bunlara muhtaç değil:** maskot Lokum ve sürpriz kutusu bu proje için kodla çizildi (SVG, `src/app.src.html` içinde `lok()` ve `giftArt()`), çıkartmalar Fluent Emoji'den kalıp kesim olarak türetiliyor. Aşağıdaki görseller yalnızca uygulamanın dışında (mağaza, tanıtım) ya da ileride bütün çıkartma setini değiştirmek istersen işe yarar.

## Stil kilidi (her istemin sonuna aynen ekle)

> flat vector illustration, thick even dark outline (#17132B) around every shape, palette limited to #5B3DF5 #FFD43B #FF8FC4 #5EE0C0 #72B7FF #FFA552 #B9A0FF #C6F04D plus white, no gradients, at most one soft shadow tone, centered on a transparent background, no text, no letters, simple shapes that stay readable at 36 px, cute and a little mischievous. Original character design; do not imitate any brand, known character or artist.

## Lokum'un tarifi (karakter tutarlılığı için her Lokum isteminde)

> Lokum is a soft Turkish-delight cube character: a rounded square body (corner radius about a third of its width) in rose pink #FF9DCB, a white powdered-sugar cap covering the top third with a wavy dripping lower edge, a few tiny white sugar dots on the body, two small oval black eyes with one white highlight, pink blush ovals #FF5C9D under the eyes, a small smile, short oval arms on the sides and two small oval feet peeking out at the bottom. Front view.

## Liste

| Dosya | Boyut | Ne | Nerede kullanılır | Not |
|---|---|---|---|---|
| `magaza-one-cikan.png` | 1024×500 | Lokum, açılmış kurdeleli mor kutu ve etrafına saçılmış 4–5 çıkartma; mor puantiyeli zemin | Google Play "öne çıkan görsel" | Uygulamaya girmez. Zemin saydam değil: `#5B3DF5`, `#6A4FFF` puantiyeli. |
| `lokum-poz-1…6.png` | 512×512 | Lokum'un altı pozu: el sallayan, gülümseyen (gözler kapalı yay), iki kolu havada sevinen, şaşkın (yuvarlak ağız), uyuyan, kalp gözlü | Mağaza ekran görüntüleri, sosyal medya, açılış ekranı | Uygulamada SVG Lokum kalmalı: renk (tat) değiştirilebiliyor, göz kırpıyor, el sallıyor ve her boyutta keskin. |
| `stk-*.png` (24 adet) | 512×512 | Yalnızca bütün çıkartma setini değiştirmeye karar verirsen: aşağıdaki "Lokum'un dostları" seti | Ödül ekranı (150 px) ve albüm (62 px) | Yarısı emoji yarısı çizim olmaz; 24'ünü birden ver. Toplam WebP bütçesi yaklaşık 500 KB. |

### İstemler

**Mağaza görseli:**

> Wide 1024×500 banner. In the center, Lokum (see character description) jumping with both arms up, eyes closed in joy. Next to it an open gift box: violet #7B5CFF box with a yellow #FFD43B ribbon and bow, the lid flying off, yellow light rays bursting out. Around them five die-cut stickers with white borders (an otter, a unicorn, a penguin, a rainbow, a fox) floating at slight angles, four-pointed yellow and white sparkles. Background violet #5B3DF5 with a regular pattern of slightly lighter #6A4FFF polka dots. + stil kilidi (saydam zemin hariç)

**Lokum pozları (her biri ayrı istem):**

> Lokum (see character description), [POSE]. Single character, centered, transparent background. + stil kilidi

`[POSE]`: 1 "waving with its right arm raised", 2 "smiling with eyes closed as happy arcs, arms down", 3 "both arms raised in celebration, open smiling mouth, two small sparkles above", 4 "surprised, big round shiny eyes, small round open mouth, arms out to the sides", 5 "sleeping, eyes closed as downward arcs, two small white bubbles above its head", 6 "in love, eyes replaced by pink hearts, gentle smile".

**"Lokum'un dostları" çıkartma seti (yalnızca seti değiştireceksen):**

> A die-cut sticker of [ŞEY], with a thick white border around the whole silhouette and the dark outline outside the white border, slight tilt. + stil kilidi

Önerilen 24 öğe (İngilizcesi / Türkçesi; çıkartmalar kelime de öğretir): bunny / tavşan, kitten / yavru kedi, puppy / köpek yavrusu, hamster / hamster, panda / panda, koala / koala, otter / su samuru, penguin / penguen, hedgehog / kirpi, fox / tilki, owl / baykuş, sloth / tembel hayvan, cupcake / kek, strawberry / çilek, cherry / kiraz, doughnut / halka tatlı, bubble tea / balonlu çay, ice cream / dondurma, rainbow / gökkuşağı, cloud / bulut, star / yıldız, moon / ay, tulip / lale, butterfly / kelebek.

## Uygulamaya bağlamak (çıkartma seti için)

1. PNG'leri WebP'ye çevir (512 px, kalite 80; tanesi yaklaşık 15–20 KB).
2. `src/app.src.html` içindeki `STK` listesini yeni anahtarlarla güncelle ve `src/build.py`'ye WebP'leri `data:image/webp` olarak gömen küçük bir adım ekle; `art()` yerine `<img src="data:image/webp…">` döndüren bir `stkArt()` yaz. Kalıp kesim kenarı görselin içinde olacağı için `cut` filtresine gerek kalmaz.
3. Eski kayıtlardaki çıkartma anahtarlarını `sanitize()` içinde yeni anahtarlara eşle; yoksa albüm sayısı bozulur.
