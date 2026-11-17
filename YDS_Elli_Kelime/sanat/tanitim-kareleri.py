"""Basamak tanıtım kaydı, 3. adım: önemli anların kare dizileri.

Her an için olayın (sesin ya da okumanın başladığı anın) öncesinden ve sonrasından birkaç kare yan yana dizilir, altına
olaya göre ms yazılır. Durağan karelere bakan bir değerlendirici (İlya), videoyu izleyen birinin hareket ve zamanlama
iddialarını bu dizilerle denetler.

Kullanım: python3 tanitim-kareleri.py [kayıt klasörü] [çıktı klasörü]
"""
import bisect, json, os, re, sys
from PIL import Image, ImageDraw, ImageFont

DIR = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else 'tanitim')
OUT = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else os.path.join(DIR, 'video-kareleri'))
os.makedirs(OUT, exist_ok=True)
R = json.load(open(os.path.join(DIR, 'kayit.json'), encoding='utf-8'))
T0 = R['frames'][0][1] * 1000
times = [ts * 1000 - T0 for _, ts in R['frames']]
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 22)
FONTB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26)


def frame(ms):
    i = max(0, bisect.bisect_right(times, ms) - 1)
    return os.path.join(DIR, 'kareler', R['frames'][i][0])


def mm(ms):
    s = ms / 1000
    return '%02d:%04.1f' % (int(s // 60), s - 60 * int(s // 60))


def nth(name, k=0, pred=None):
    hits = [t - T0 for n, a, t in R['sfx'] if n == name and (pred is None or pred(a))]
    return hits[k] if len(hits) > k else None


def speak(k=0, pred=None):
    hits = [e['t'] - T0 for e in R['tts'] if e['k'] == 'speak' and (pred is None or pred(e['s']))]
    return hits[k] if len(hits) > k else None


def act(text):
    for a in R['acts']:
        if a.get('bolum') == text and 'adim' not in a:
            return a['t'] - T0
    return None


def strip(no, title, at, offs, crop=None):
    if at is None:
        print('atlandı:', title)
        return
    w = 260
    ims = []
    for o in offs:
        im = Image.open(frame(at + o)).convert('RGB')
        if crop:
            im = im.crop(crop)
        im = im.resize((w, round(im.height * w / im.width)))
        ims.append((o, im))
    h = ims[0][1].height
    sheet = Image.new('RGB', (len(ims) * (w + 10) + 10, h + 110), (23, 19, 43))
    d = ImageDraw.Draw(sheet)
    d.text((12, 10), '%02d · %s · olay %s' % (no, title, mm(at)), font=FONTB, fill=(255, 255, 255))
    for i, (o, im) in enumerate(ims):
        x = 10 + i * (w + 10)
        sheet.paste(im, (x, 50))
        d.text((x + 4, 58 + h), ('%+d ms' % o) if o else '0 ms (olay)', font=FONT, fill=(255, 212, 59) if o == 0 else (171, 164, 212))
    slug = title.lower().translate(str.maketrans('ıişğüöçâ', 'iisguoca'))
    name = '%02d-%s.jpg' % (no, re.sub(r'[^a-z0-9]+', '-', slug).strip('-'))
    sheet.save(os.path.join(OUT, name), quality=86)
    print(name)


TOP = (0, 0, 780, 700)     # ekranın üst yarısı: başlık, kart
FULL = None
strip(1, 'tanıtım kartı okunuşu', speak(0), [-300, 0, 150, 300, 500, 800, 1100], TOP)
strip(2, 'tanıtım kartı geçişi', nth('flip', 0), [-60, 0, 40, 80, 120, 180, 260])
strip(3, 'doğru cevap', nth('ok', 0), [-80, 0, 80, 160, 300, 600])
strip(4, 'Devam kayması', nth('slide', 1), [-60, 0, 40, 80, 120, 160, 220])
strip(5, 'x3 rozeti', nth('combo', 0), [-80, 0, 100, 200, 300, 450], (0, 0, 780, 420))
strip(6, 'yanlış cevap', nth('no', 0), [-80, 0, 80, 160, 300, 600])
strip(7, 'bölüm geçişi', nth('swish', 0), [-60, 0, 60, 120, 200, 400])
strip(8, 'eşleştirme yanlış ve doğru', nth('miss', 0), [-100, 0, 150, 300, 450, 700])
strip(9, 'cümle parça yerleşmesi', nth('place', 0), [-60, 0, 60, 120, 200])
strip(10, 'kutu 1. dokunuş', nth('roll', 0), [0, 100, 200, 300, 450])
strip(11, 'kutu 2. dokunuş', nth('roll', 1), [0, 100, 200, 300, 450])
strip(12, 'kutu 3. dokunuş ve açılış', nth('roll', 2), [0, 100, 200, 300, 450, 600, 900])
strip(13, 'balon patlaması', nth('pop', 0), [-60, 0, 80, 160, 240, 400])
strip(14, 'yanlış balon sönmesi', nth('fizz', 0), [0, 150, 300, 450, 650])
strip(15, 'ödül anı', nth('tada', 1), [0, 200, 400, 800, 1200, 1800])
strip(16, 'gün özeti kutlaması', nth('win', 0), [0, 300, 600, 900, 1300])
strip(17, 'gün serisi alevi', nth('fire', 0), [-80, 0, 100, 200, 300, 450], (0, 0, 780, 300))
strip(18, 'gramer doğru (zil)', nth('ok', 0, lambda a: isinstance(a, dict) and a.get('t') == 'bell'), [-80, 0, 100, 250, 500])
strip(19, 'fiil taraması kendiliğinden geçiş', nth('okStep', 0), [-80, 0, 200, 450, 650, 700, 760, 850])
strip(20, 'koyu tema', act('Koyu tema'), [0, 300, 700, 1500])
