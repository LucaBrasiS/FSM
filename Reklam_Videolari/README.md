# NeFaTa Games: YouTube Shorts ve TikTok reklam videoları

Bu klasör dört oyunun reklam videoları için çekim planını, kayıt kurallarını ve kurgu betiklerini içerir.

| Oyun | Durum | Çekim listesi | Öncelik |
|---|---|---|---|
| İYE (Klasik mod) | Hazır (APK 1.1) | [cekim_listeleri/IYE_Klasik.md](cekim_listeleri/IYE_Klasik.md) | 1 |
| R&B Birds | Hazır (build 8) | [cekim_listeleri/RnB_Birds.md](cekim_listeleri/RnB_Birds.md) | 2 |
| PIPE | Hazır (0.1.0 build 12) | [cekim_listeleri/PIPE.md](cekim_listeleri/PIPE.md) | 3 |
| Merdiven | Hazır değil | [cekim_listeleri/Merdiven.md](cekim_listeleri/Merdiven.md) | Bekliyor |

Yayın sırası ve metinler: [YAYIN_TAKVIMI.md](YAYIN_TAKVIMI.md)

## 1. Teknik ölçüler (iki platform için ortak)

| Ayar | Değer | Not |
|---|---|---|
| Çözünürlük | 1080 × 1920 (9:16, dikey) | Oyunlar dikey oynandığı için kırpma gerekmez |
| Kare hızı | 60 fps kayıt, 30 veya 60 fps çıktı | Hızlı hareketlerde (PIPE, R&B) 60 fps |
| Süre | 15–30 sn (ana), 45–60 sn (uzun) | İlk 2 saniye kancadır |
| Kodek | H.264, yuv420p, AAC 48 kHz | `betikler/dikey_kurgu.sh` bunu otomatik yapar |
| Ses seviyesi | −14 LUFS | Betik normalize eder |
| Güvenli alan | Üstten 220 px, alttan 420 px, sağdan 140 px boş | TikTok/Shorts arayüzü bu bölgeleri kapatır; yazı ve skor buraya düşmesin |

## 2. Kayıt öncesi telefon hazırlığı (her çekimde)

1. Rahatsız Etme modu açık, bildirimler kapalı.
2. Geliştirici seçeneklerinde "Dokunuşları göster" **kapalı** (reklamda parmak noktası istenmiyorsa). Öğretici videolarda açılabilir.
3. Durum çubuğu temiz: saat 09:41 gibi sabit, şarj dolu. (`betikler/kayit_al.sh demo` komutu Android demo modunu açar.)
4. Parlaklık yüksek, oyun sesi açık, titreşim kapalı (kayıtta tıkırtı yapmasın).
5. DEV panelinden ilerleme sıfırlanmış veya çekime uygun seviyeye getirilmiş olmalı. Debug yazıları, FPS sayacı, DEV butonu görünmemeli.
6. Oyun dili: TR hesap için TR, global hesap için EN. Her ana çekimi iki dilde alın.

## 3. Kayıt yöntemi

Öncelik sırası:

1. **scrcpy ile bilgisayardan kayıt** (en temiz, kayıpsız): telefon USB ile bağlı, `betikler/kayit_al.sh scrcpy IYE klasik_kanca`.
2. **adb screenrecord** (scrcpy yoksa): `betikler/kayit_al.sh adb PIPE catlak_seri`. Tek parça en fazla 3 dakika.
3. **Telefonun kendi ekran kaydı**: bağlantı yoksa. Kayıt sonrası dosyayı `ham/` klasörüne aynı adlandırmayla koyun.
4. **Unity Recorder** (Editor'de, 1080×1920 Game view): tanıtım filmi ve kusursuz "mükemmel oyun" sahneleri için. Drive'daki `FFmpegPipe.cs` örneği bu iş için kullanılabilir.

Her sahneyi **en az 3 kez** kaydedin; kurguda en iyi alınan seçilir.

## 4. Dosya adlandırma ve klasörler

```
Drive/NeFaTa_Reklam/
  ham/        OYUN_sahne_dil_tarih_alinis.mp4   örn. IYE_kombo_TR_20261110_02.mp4
  kurgu/      OYUN_vNN_platform_dil.mp4         örn. PIPE_v01_tiktok_TR.mp4
  kapak/      OYUN_vNN_kapak.png                (1080×1920, Shorts için)
  muzik/      lisanslı müzikler ve oyun sesleri
```

Oyun kodları: `IYE`, `RNB`, `PIPE`, `MERDIVEN`.

## 5. Kurgu

`betikler/dikey_kurgu.sh` ham kaydı yayına hazır hale getirir:

```bash
# ham kayıttan 3.5–21 sn arası, üstte kanca yazısı, sonda 2 sn kapanış kartı
betikler/dikey_kurgu.sh ham/IYE_kombo_TR_20261110_02.mp4 kurgu/IYE_v01_TR.mp4 \
    --bas 3.5 --son 21 --kanca "Bu tahtayı temizleyebilir misin?" \
    --kapanis "İYE · Google Play'de" --logo kapak/IYE_Ikon_512_PlayStore.png
```

Betik görüntüyü 1080×1920'ye oturtur, sesi −14 LUFS'a çeker, kancayı ilk 2.5 saniyede gösterir ve kapanış kartını ekler. Aynı çıktı hem TikTok hem Shorts'a yüklenebilir.

Ek kurgu kuralları:
- İlk karede oyun zaten hareket halinde olsun; logo ile açmayın.
- Her 2–3 saniyede bir kesme veya olay (kombo, patlama, sayı artışı).
- Videonun sonu başına bağlansın (loop): son kare ilk kareye benzer bir tahta durumuyla bitsin.
- Yazılar büyük ve kısa: en fazla 6–7 kelime.
- TikTok'ta ses açık izlenir: ritim/oyun sesini öne çıkarın. Shorts'ta altyazı şart.

## 6. Bu depoda olmayanlar

Ham kayıtların kendisi telefonda oynanarak alınmalıdır; bu ortamda Android cihaz veya emülatör yoktur. Çekim listeleri, hangi sahnenin nasıl kaydedileceğini adım adım tarif eder.
