# R&B Birds çekim listesi

**Oyunun tek cümlesi:** Telin üstündeki kırmızı ve mavi kuşla ritme uyarak oyna. (Ritim oyunu.)
**Reklamın vaadi:** "Müzik + tek dokunuş + piksel sanat. Ses açık izlenmesi gereken video."
**Malzeme:** `RnB_Birds_2026-11-09_8.apk`, Drive `RnB_Play` klasöründeki simge, özellik grafiği ve 5 ekran görüntüsü, `RnB_kuslar` ve `RnB_sicak_palet` görselleri.

> Mekanik ayrıntısı (hangi kuşa ne zaman dokunulduğu, kaçırma cezası) çekimden önce oyunda doğrulanmalıdır. Aşağıdaki sahneler oyunda varsa çekilir.

## Hazırlık
- Ses mutlaka cihazdan **dahili ses** olarak kaydedilsin (scrcpy 2.0+ `--audio-source=output`). Mikrofonla kayıt yapmayın.
- Kulaklık takılıyken kayıt almayın; bazı cihazlar dahili sesi kesiyor.
- 60 fps kayıt şart: ritim ile görüntü senkronu kurguda bozulmasın.

## Sahneler

| # | Sahne adı (dosya) | Süre | Ne kaydedilecek | Kullanım |
|---|---|---|---|---|
| 1 | `kanca_kusursuz_seri` | 6–8 sn | Hiç kaçırmadan yoğun bir bölüm, "perfect" geri bildirimleri | Açılış kancası |
| 2 | `kirmizi_mavi` | 8 sn | Kırmızı ve mavi kuşun ayrı ayrı tepki verdiği bölüm (iki renk ayrımı açıkça görülsün) | Mekaniğin anlatımı |
| 3 | `hizlanan_tempo` | 10–15 sn | Temponun arttığı kısım | Gerilim |
| 4 | `kacirma_fail` | 3–5 sn | Bir notayı kaçırma ve oyunun buna tepkisi | "Ritmi tutturabilir misin?" kancası |
| 5 | `sonuc_ekrani` | 3 sn | Skor / yıldız ekranı | Meydan okuma |
| 6 | `menu_kuslar` | 4 sn | Ana menü, iki kuş telin üstünde | Kapanış kartının arkası |
| 7 | `el_kamerasi` (isteğe bağlı) | 10 sn | Telefonla oynayan elin üstten çekimi (ikinci telefonla) | TikTok'ta güçlü çalışır: "gerçek oyun" hissi |

## Kurgu önerileri

**V1 · "Ses aç" (15 sn):** 1 → 2 → 3, kesmeler vuruşlara denk gelsin.
Yazı: "Sesi aç 🔊 ve ritmi yakala" / EN: "Sound on. Catch the beat."

**V2 · "Fail" (12 sn):** 3 → 4 → 5. Yazı: "Bu kısımda herkes kaçırıyor."

**V3 · "El + ekran" (20 sn):** 7 ile 1 yan yana veya ardışık.

## Kontrol
- [ ] Dahili ses kaydedildi, gecikme yok
- [ ] Vuruşlar ile kesmeler senkron
- [ ] Müzik oyuna ait (telifli dış müzik kullanılmayacak; TikTok/YouTube reklam için telif sorunu çıkar)
