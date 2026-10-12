# FSM Tasarımları ve Etkileşimli Simülasyonlar

Bu klasörde beş sonlu durum makinesi (FSM) tasarımı bulunur. Her tasarımın Verilog ve SystemVerilog kaynak kodu ile tarayıcıda çalışan etkileşimli bir simülasyonu vardır.

## Klasör yapısı

```
FSM/
├── VERİLOG/          Verilog kaynak kodları ve testbench dosyaları
├── System Verilog/   SystemVerilog kaynak kodları ve testbench dosyaları
└── Simulations/      Tarayıcıda açılan etkileşimli simülasyonlar (.html)
```

Kaynak kodlar `.txt` uzantılıdır. Vivado'da kullanmak için Verilog dosyalarını `.v`, SystemVerilog dosyalarını `.sv` uzantısıyla kaydedin.

## Tasarımlar

| Tasarım | Ne yapar? | Simülasyon |
|---|---|---|
| **Lock_Door** | Seri girilen 3 bitlik şifreyi kontrol eden kilit | `lock_door_fsm.html` |
| **Array2_Detector** | Giriş akışında `1101` ve `1011` dizilerini yakalar; 1–8 bitlik özel dizi desteği | `array2_detector.html` |
| **Elevator_FSM** | 4 katlı asansör denetleyicisi (9 durumlu Moore makinesi) | `elevator-fsm-explorer.html` |
| **FIFO** | 8 derinlikli, 8 bit senkron FIFO | `sync_fifo_explorer.html` |
| **Toggle_LED** | Sayaçla saat bölme; LED belirli aralıkla yanıp söner | `toggle_led_explorer.html` |

## Simülasyonları kullanma

Kurulum gerekmez. `Simulations` klasöründeki `.html` dosyasını bir tarayıcıda açmanız yeterlidir.

- **Girişler:** Düğmelerle FSM'e giriş verin ya da saat darbesini adım adım ilerletin.
- **Durum diyagramı:** Aktif durum ve son geçiş vurgulanır.
- **Dalga formu:** Son çevrimlerin sinyalleri RTL dalga formu olarak gösterilir.
- **💡 FSM Açıklamaları:** Sağ alttaki düğme, FSM mantığını anlatan paneli açar. Her başlıktaki başarılı ve başarısız senaryolar tek tıkla adım adım oynatılır.
- **Dil:** Sayfalar Türkçe açılır; sağ üstteki **EN** düğmesiyle İngilizceye geçilir.

## Araçlar

- Xilinx Vivado 2025.2 (sentez ve simülasyon)
- Herhangi bir güncel tarayıcı (etkileşimli simülasyonlar)
