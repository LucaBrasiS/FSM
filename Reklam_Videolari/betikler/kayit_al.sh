#!/usr/bin/env bash
# Android telefondan oyun kaydı alır ve dosyayı standart adla ham/ klasörüne koyar.
#
# Kullanım:
#   ./kayit_al.sh demo                      # durum çubuğunu temizle (demo modu aç)
#   ./kayit_al.sh demo-kapat                # demo modunu kapat
#   ./kayit_al.sh scrcpy OYUN SAHNE [DIL]   # scrcpy ile kayıt (Ctrl+C ile bitir)
#   ./kayit_al.sh adb    OYUN SAHNE [DIL]   # adb screenrecord ile kayıt (en fazla 180 sn)
#
# OYUN: IYE | RNB | PIPE | MERDIVEN     DIL: TR (varsayılan) | EN
# Örnek: ./kayit_al.sh scrcpy IYE kombo_seri TR
set -euo pipefail

HAM_DIR="${HAM_DIR:-ham}"
mod="${1:-}"

demo_ac() {
  adb shell settings put global sysui_demo_allowed 1
  adb shell am broadcast -a com.android.systemui.demo -e command enter
  adb shell am broadcast -a com.android.systemui.demo -e command clock -e hhmm 0941
  adb shell am broadcast -a com.android.systemui.demo -e command battery -e level 100 -e plugged false
  adb shell am broadcast -a com.android.systemui.demo -e command network -e wifi show -e level 4
  adb shell am broadcast -a com.android.systemui.demo -e command notifications -e visible false
  echo "Demo modu açık."
}

dosya_adi() {
  local oyun="$1" sahne="$2" dil="$3" tarih n
  tarih="$(date +%Y%m%d)"
  mkdir -p "$HAM_DIR"
  n=1
  while :; do
    f="$HAM_DIR/${oyun}_${sahne}_${dil}_${tarih}_$(printf %02d "$n").mp4"
    [[ -e "$f" ]] || break
    n=$((n + 1))
  done
  echo "$f"
}

case "$mod" in
  demo) demo_ac ;;
  demo-kapat)
    adb shell am broadcast -a com.android.systemui.demo -e command exit
    echo "Demo modu kapalı." ;;
  scrcpy|adb)
    oyun="${2:?OYUN gerekli (IYE|RNB|PIPE|MERDIVEN)}"
    sahne="${3:?SAHNE adı gerekli}"
    dil="${4:-TR}"
    case "$oyun" in IYE|RNB|PIPE|MERDIVEN) ;; *) echo "Bilinmeyen oyun: $oyun" >&2; exit 1 ;; esac
    out="$(dosya_adi "$oyun" "$sahne" "$dil")"
    echo "Kayıt: $out"
    if [[ "$mod" == scrcpy ]]; then
      # Dahili ses (Android 11+), 60 fps, yüksek bit hızı. Pencere açık kalır; Ctrl+C ile bitirin.
      scrcpy --record="$out" --max-fps=60 --video-bit-rate=16M \
             --audio-source=output --stay-awake --no-mouse-hover || true
    else
      # adb screenrecord ses kaydetmez; ses gerekiyorsa scrcpy kullanın.
      tmp="/sdcard/nefata_kayit.mp4"
      echo "Kayıt başladı (en fazla 180 sn). Bitirmek için Ctrl+C."
      trap 'sleep 1' INT
      adb shell screenrecord --bit-rate 16000000 --time-limit 180 "$tmp" || true
      trap - INT
      sleep 1
      adb pull "$tmp" "$out" && adb shell rm "$tmp"
    fi
    echo "Kaydedildi: $out" ;;
  *)
    sed -n '2,12p' "$0"; exit 1 ;;
esac
