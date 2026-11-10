# PIPE çekim listesi

**Oyunun tek cümlesi:** Çatlayan borulardan su fışkırmadan önce çatlakları kapat. (Tek dokunuşlu refleks oyunu.)
**Reklamın vaadi:** "Hızlı refleks + tatmin edici su ve çatlak efektleri."
**Malzeme:** `PIPE_0.1.0_12_2026-11-09.apk`, Drive `pipe/2026-11-09` klasöründeki `PIPE_catlak_v2.png` ve `PIPE_catlak_tempo.png`.

Görsel dörtlü (bakır dikey çatlak, PVC açılı çatlak, iki yandan fışkırma, şişkinlik) her biri ayrı reklam sahnesidir.

> Çatlağın nasıl kapatıldığı (dokunma, kaydırma) ve şişkinliğin nasıl çalıştığı çekimden önce son build'de doğrulanmalıdır.

## Sahneler

| # | Sahne adı (dosya) | Süre | Ne kaydedilecek | Kullanım |
|---|---|---|---|---|
| 1 | `kanca_fiskirma` | 3–5 sn | Su ekranın iki yanına fışkırırken son anda kapatma | Açılış kancası |
| 2 | `bakir_catlak` | 5–8 sn | Bakır boruda dikey çatlak oluşması ve kapatılması | Mekanik anlatımı |
| 3 | `pvc_catlak` | 5–8 sn | Tuğla duvar önünde PVC, açılı çatlak | Çeşitlilik |
| 4 | `iki_yandan` | 5–8 sn | Ortadan iki yana fışkırma | Zorluk artışı |
| 5 | `siskinlik` | 5–8 sn | Şişen boru ve patlamadan önce müdahale (renkli gradyan zemin) | Görsel olarak en çarpıcı sahne; kapak karesi buradan |
| 6 | `tempo_artisi` | 10–15 sn | Çatlakların hızlandığı, art arda kapatma serisi | Ana gövde |
| 7 | `kayip_sel` | 3–5 sn | Kaçırılan çatlak, oyunun kaybetme anı | "Fail" kancası |
| 8 | `skor` | 3 sn | Sonuç ve rekor ekranı | Meydan okuma |

## Kurgu önerileri

**V1 · "Refleks testi" (15 sn):** 1 → 6 → 8. Yazı: "Kaç tanesini yakalayabilirsin?" / EN: "How fast are your reflexes?"

**V2 · "4 boru tipi" (20 sn):** 2 → 3 → 4 → 5, her birinin üstünde etiket (Bakır, PVC, İki yandan, Şişkinlik).

**V3 · "Tesisatçı" mizahı (12 sn):** 7 → 1. Yazı: "Tesisatçı çağırmadan önce…"

## Kontrol
- [ ] Su parçacıkları 60 fps'te akıcı (düşük fps'te titrer)
- [ ] Çatlak ve fışkırma yakın planı için kurguda %115 yakınlaştırma denenebilir
- [ ] Kapak: `siskinlik` sahnesinden bir kare
