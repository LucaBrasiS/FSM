#!/usr/bin/env bash
# Ham oyun kaydını TikTok / YouTube Shorts için 1080x1920 yayın dosyasına çevirir.
#
# Kullanım:
#   ./dikey_kurgu.sh GIRIS CIKIS [seçenekler]
#
# Seçenekler:
#   --bas SN          başlangıç saniyesi (varsayılan 0)
#   --son SN          bitiş saniyesi (varsayılan: videonun sonu)
#   --hiz X           oynatma hızı, örn. 1.25 (varsayılan 1)
#   --kanca "YAZI"    ilk 2.5 sn üstte gösterilecek kanca yazısı
#   --kapanis "YAZI"  sona eklenecek 2 sn kapanış kartı yazısı
#   --logo DOSYA      kapanış kartında gösterilecek simge (png)
#   --fps N           çıktı kare hızı (varsayılan 60)
#   --font DOSYA      yazı tipi (varsayılan: sistemdeki DejaVuSans-Bold)
#
# GIRIS bir görsel (png/jpg) ise 8 sn'lik yavaş yakınlaşan video üretilir (ör. Merdiven teaser).
set -euo pipefail

in="${1:?GIRIS dosyası gerekli}"; out="${2:?CIKIS dosyası gerekli}"; shift 2
bas=0; son=""; hiz=1; kanca=""; kapanis=""; logo=""; fps=60
font="${FONT:-}"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --bas) bas="$2"; shift 2 ;;
    --son) son="$2"; shift 2 ;;
    --hiz) hiz="$2"; shift 2 ;;
    --kanca) kanca="$2"; shift 2 ;;
    --kapanis) kapanis="$2"; shift 2 ;;
    --logo) logo="$2"; shift 2 ;;
    --fps) fps="$2"; shift 2 ;;
    --font) font="$2"; shift 2 ;;
    *) echo "Bilinmeyen seçenek: $1" >&2; exit 1 ;;
  esac
done

if [[ -z "$font" ]]; then
  font="$(fc-match -f '%{file}' 'DejaVu Sans:bold' 2>/dev/null || true)"
fi
[[ -f "$font" ]] || { echo "Yazı tipi bulunamadı; --font ile verin." >&2; exit 1; }

tmpd="$(mktemp -d)"; trap 'rm -rf "$tmpd"' EXIT
mkdir -p "$(dirname "$out")"

# drawtext için yazıyı dosyaya koy: tırnak/iki nokta kaçış sorunlarını önler.
# Uzun yazıları ekran genişliğine sığacak şekilde satırlara böl (UTF-8 karakter sayısına göre).
sar() { awk -v w="$2" 'BEGIN{RS=" "; ORS=""} {gsub(/\n/,""); if(len && len+1+length($0)>w){print "\n"; len=0} else if(len){print " "; len++} print; len+=length($0)}' <<<"$1"; }
sar "$kanca" 20 > "$tmpd/kanca.txt"
sar "$kapanis" 20 > "$tmpd/kapanis.txt"

W=1080; H=1920
fit="scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1"
# Kanca: üst güvenli alanın hemen altında (y=260), yarı saydam kutu içinde.
kanca_f=""
if [[ -n "$kanca" ]]; then
  kanca_f=",drawtext=fontfile='${font}':textfile='${tmpd}/kanca.txt':fontsize=64:line_spacing=14:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=28:x=(w-text_w)/2:y=260:enable='lt(t,2.5)'"
fi

case "${in,,}" in
  *.png|*.jpg|*.jpeg|*.webp)
    # Görsel girişi: 8 sn yavaş zoom, sessiz ses izi.
    ffmpeg -hide_banner -loglevel error -y -loop 1 -framerate "$fps" -t 8 -i "$in" \
      -f lavfi -t 8 -i anullsrc=r=48000:cl=stereo \
      -filter_complex "[0:v]${fit},scale=$((W*2)):$((H*2)),zoompan=z='min(zoom+0.0008,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=${W}x${H}:fps=${fps}${kanca_f},format=yuv420p[v]" \
      -map "[v]" -map 1:a -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k -shortest "$tmpd/govde.mp4"
    ;;
  *)
    trim=(-ss "$bas"); [[ -n "$son" ]] && trim+=(-to "$son")
    has_audio="$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$in" | head -n1)"
    vf="setpts=PTS/${hiz},fps=${fps},${fit}${kanca_f},format=yuv420p"
    if [[ -n "$has_audio" ]]; then
      ffmpeg -hide_banner -loglevel error -y "${trim[@]}" -i "$in" \
        -filter_complex "[0:v]${vf}[v];[0:a]atempo=${hiz},aresample=48000,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
        -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k "$tmpd/govde.mp4"
    else
      ffmpeg -hide_banner -loglevel error -y "${trim[@]}" -i "$in" -f lavfi -i anullsrc=r=48000:cl=stereo \
        -filter_complex "[0:v]${vf}[v]" -map "[v]" -map 1:a -shortest \
        -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k "$tmpd/govde.mp4"
    fi
    ;;
esac

if [[ -z "$kapanis" && -z "$logo" ]]; then
  mv "$tmpd/govde.mp4" "$out"; echo "Hazır: $out"; exit 0
fi

# Kapanış kartı: 2 sn, koyu zemin, ortada simge, altında yazı.
kart_in=(-f lavfi -t 2 -i "color=c=0x0E131F:s=${W}x${H}:r=${fps}")
kart_f="[0:v]null[bg]"; ses_idx=1
if [[ -n "$logo" ]]; then
  kart_in+=(-loop 1 -t 2 -i "$logo")
  kart_f="[1:v]scale=420:-1[lg];[0:v][lg]overlay=(W-w)/2:(H-h)/2-160[bg]"; ses_idx=2
fi
txt=""
[[ -n "$kapanis" ]] && txt=",drawtext=fontfile='${font}':textfile='${tmpd}/kapanis.txt':fontsize=72:line_spacing=14:fontcolor=white:x=(w-text_w)/2:y=h/2+160"
ffmpeg -hide_banner -loglevel error -y "${kart_in[@]}" -f lavfi -t 2 -i anullsrc=r=48000:cl=stereo \
  -filter_complex "${kart_f};[bg]fade=t=in:st=0:d=0.3${txt},format=yuv420p[v]" \
  -map "[v]" -map "${ses_idx}:a" -t 2 -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k "$tmpd/kart.mp4"

ffmpeg -hide_banner -loglevel error -y -i "$tmpd/govde.mp4" -i "$tmpd/kart.mp4" \
  -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k -movflags +faststart "$out"
echo "Hazır: $out"
