"""Tanıtım videosu için doğal İngilizce okuma sesi (Piper, en_US-joe-medium, CC0).
Model npm'de `vowel-lab-voices-float` paketinde yalnız .onnx olarak duruyor; bu betik yanına Piper'ın beklediği
.onnx.json ayarını yazar (Piper'ın standart espeak fonem eşlemesi, 22 050 Hz).

  mkdir ses && cd ses && npm pack vowel-lab-voices-float@0.1.0 && tar -xzf vowel-lab-voices-float-0.1.0.tgz
  python3 ../sanat/piper-ses-hazirla.py package/float.onnx
  PIPER_MODEL=$PWD/package/float.onnx node ../sanat/tanitim-birlestir.js <kayıt klasörü> ../index.html <çıktı.mp4>

Gerekenler: piper (pip: piper-tts). Uygulamanın kendisinde bu ses yok: telefonda kelimeyi cihazın kendi sesi okur."""
import json, sys
from piper.phoneme_ids import DEFAULT_PHONEME_ID_MAP
model = sys.argv[1]
json.dump({"audio": {"sample_rate": 22050}, "espeak": {"voice": "en-us"},
           "inference": {"noise_scale": 0.667, "length_scale": 1, "noise_w": 0.8},
           "phoneme_type": "espeak", "phoneme_id_map": DEFAULT_PHONEME_ID_MAP,
           "num_symbols": 256, "num_speakers": 1, "speaker_id_map": {}},
          open(model + ".json", "w"), ensure_ascii=False)
print("yazıldı:", model + ".json")
