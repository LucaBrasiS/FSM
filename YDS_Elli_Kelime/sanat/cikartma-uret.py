"""Lokum'un arkadaşları: albümün 24 çıkartması, Lokum'un çizgisinde (düz renk, eşit kalınlıkta koyu dış çizgi,
yuvarlak hatlar, Lokum'un yüzü: parıltılı göz, pembe yanak, küçük gülüş). Hepsi 32x32 çizim alanında.
Kullanım: python3 uret.py <çıktı.json>"""
import json, math, sys
INK = '#17132B'; SW = 1.15; BL = '#FF7FAE'; W = '#FFFFFF'

def a(**k):
    return ' '.join('%s="%s"' % (x.replace('_', '-'), v) for x, v in k.items())
def st(w=SW):
    return 'stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"' % (INK, w)
def E(cx, cy, rx, ry, fill, line=True, rot=0, w=SW, op=None):
    t = ' transform="rotate(%s %s %s)"' % (rot, cx, cy) if rot else ''
    o = ' opacity="%s"' % op if op is not None else ''
    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s"%s%s%s/>' % (cx, cy, rx, ry, fill, (' ' + st(w)) if line else '', t, o)
def C(cx, cy, r, fill, line=True, w=SW, op=None):
    o = ' opacity="%s"' % op if op is not None else ''
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"%s%s/>' % (cx, cy, r, fill, (' ' + st(w)) if line else '', o)
def P(d, fill, line=True, w=SW, op=None):
    o = ' opacity="%s"' % op if op is not None else ''
    return '<path d="%s" fill="%s"%s%s/>' % (d, fill, (' ' + st(w)) if line else '', o)
def L(d, w=0.9, col=INK):
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"/>' % (d, col, w)
def R(x, y, w_, h, rx, fill, line=True, w=SW):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"%s/>' % (x, y, w_, h, rx, fill, (' ' + st(w)) if line else '')

def face(cx, cy, s=1.0, dx=2.7, blush=True, bdx=None, bdy=1.35, mouth='smile', big=1.0):
    """Lokum'un yüzü: koyu oval göz ve beyaz parıltı, pembe yanak, küçük gülüş."""
    o = ''
    for sx in (-1, 1):
        x = cx + sx * dx * s
        o += E(round(x, 2), cy, round(0.86 * s * big, 2), round(1.08 * s * big, 2), INK, False)
        o += C(round(x + 0.32 * s * big, 2), round(cy - 0.42 * s * big, 2), round(0.34 * s * big, 2), W, False)
    if blush:
        b = bdx if bdx is not None else dx + 1.75
        for sx in (-1, 1):
            o += E(round(cx + sx * b * s, 2), round(cy + bdy * s, 2), round(1.15 * s, 2), round(0.68 * s, 2), BL, False, op=.9)
    if mouth == 'smile':
        o += L('M%s %sQ%s %s %s %s' % (round(cx - 0.95 * s, 2), round(cy + 1.15 * s, 2), cx, round(cy + 2.15 * s, 2), round(cx + 0.95 * s, 2), round(cy + 1.15 * s, 2)), round(0.85 * s, 2))
    elif mouth == 'open':
        o += P('M%s %sQ%s %s %s %sZ' % (round(cx - 1.25 * s, 2), round(cy + 1.1 * s, 2), cx, round(cy + 3.0 * s, 2), round(cx + 1.25 * s, 2), round(cy + 1.1 * s, 2)), INK, True, round(0.7 * s, 2))
        o += E(cx, round(cy + 2.1 * s, 2), round(0.62 * s, 2), round(0.4 * s, 2), '#FF7FA8', False)
    return o

def cloud(pts, fill=W):
    """Bulut: dairelerin birleşimi; önce kalın koyu çizgi, sonra dolgu: içteki çizgiler görünmez."""
    return ''.join(C(x, y, r, INK, False) for x, y, r in [(x, y, r + SW) for x, y, r in pts]) + ''.join(C(x, y, r, fill, False) for x, y, r in pts)

def sparkle(x, y, r, col='#FFD43B'):
    q = r * .32
    return P('M%s %sQ%s %s %s %sQ%s %s %s %sQ%s %s %s %sQ%s %s %s %sZ' % (
        x, y - r, x + q, y - q, x + r, y, x + q, y + q, x, y + r, x - q, y + q, x - r, y, x - q, y - q, x, y - r), col, True, .7)

S = {}
# 1 tembel hayvan
S['sloth'] = (E(11.5, 27.3, 2.7, 1.8, '#A9805C') + E(20.5, 27.3, 2.7, 1.8, '#A9805C') +
    C(16, 16.6, 11, '#C8A07A') + E(16, 18.2, 8.2, 6.6, '#F2DEC4', False) +
    E(12.4, 17.3, 2.7, 1.8, '#7A5640', False, -22) + E(19.6, 17.3, 2.7, 1.8, '#7A5640', False, 22) +
    face(16, 17.2, 1, 3.1, True, 4.7, 2.2, None) + E(16, 19.5, 1.1, .75, INK, False) + L('M14.9 20.8Q16 21.8 17.1 20.8', .85) +
    E(21.6, 6.6, 1.7, 3.0, '#7BD389', True, 40, .9) + L('M20.6 5.4L22.4 7.8', .6) +
    E(11.5, 26.6, 2.7, 1.8, '#A9805C') + E(20.5, 26.6, 2.7, 1.8, '#A9805C'))
# 2 su samuru
S['otter'] = (C(8.4, 9.8, 2.5, '#B47A55') + C(23.6, 9.8, 2.5, '#B47A55') + C(8.4, 9.8, 1.15, '#E9B994', False) + C(23.6, 9.8, 1.15, '#E9B994', False) +
    E(16, 17, 11, 10.6, '#B47A55') + E(16, 20.2, 5.4, 3.9, '#F3DCC4', False) +
    face(16, 15.7, 1, 4.1, True, 6.0, 2.4, None) + E(16, 18.9, 1.35, .95, INK, False) +
    L('M14.2 20.6Q15.1 21.6 16 20.6Q16.9 21.6 17.8 20.6', .8) + L('M11.4 19.6L8.6 19.1M11.4 20.8L8.8 21.3M20.6 19.6L23.4 19.1M20.6 20.8L23.2 21.3', .55) +
    E(12.2, 26.4, 2.4, 1.8, '#9C6644', True, -20) + E(19.8, 26.4, 2.4, 1.8, '#9C6644', True, 20) +
    P('M13.9 27.6Q16 23.2 18.1 27.6Q16 28.8 13.9 27.6Z', '#FF9DCB', True, .8) + L('M16 24.9L16 27.9M15 25.5L14.8 27.8M17 25.5L17.2 27.8', .5))
# 3 penguen
S['penguin'] = (E(5.9, 19.2, 2.2, 4.7, '#4B4F8F', True, 22) + E(26.1, 19.2, 2.2, 4.7, '#4B4F8F', True, -22) +
    E(12.3, 28.7, 2.7, 1.3, '#FFA24C') + E(19.7, 28.7, 2.7, 1.3, '#FFA24C') +
    E(16, 17.5, 10.6, 11.4, '#4B4F8F') + E(16, 20, 7.6, 8.3, W, False) + C(12.8, 14.6, 4.3, W, False) + C(19.2, 14.6, 4.3, W, False) +
    face(16, 15.2, 1, 3.1, True, 5.0, 2.4, None) + P('M14.5 17.2Q16 16.4 17.5 17.2Q16.6 19.3 16 19.3Q15.4 19.3 14.5 17.2Z', '#FFA24C', True, .75))
# 4 baykuş
S['owl'] = (P('M7 10.5L8.6 4.6L13 8.2Q16 7.4 19 8.2L23.4 4.6L25 10.5Q27.6 14.2 27.1 19.4Q26.4 28.6 16 28.6Q5.6 28.6 4.9 19.4Q4.4 14.2 7 10.5Z', '#9B7BFF') +
    E(16, 23, 6.3, 5, '#E3D9FF', False) + L('M13.4 21.6L14.4 22.6L15.4 21.6M16.6 21.6L17.6 22.6L18.6 21.6M15 24.2L16 25.2L17 24.2', .6, '#9B7BFF') +
    C(11.8, 15, 3.7, W, True, .9) + C(20.2, 15, 3.7, W, True, .9) + face(16, 15, 1, 4.2, True, 6.5, 3.4, None, 1.3) +
    P('M14.8 17.6L16 16.6L17.2 17.6L16 19.4Z', '#FFC94D', True, .7) + E(16, 28.6, 3.6, 1.1, '#FFC94D', True, 0, .8))
# 5 tilki
S['fox'] = (P('M5 7.6L10 5.2Q12.3 8.9 16 8.9Q19.7 8.9 22 5.2L27 7.6Q28.2 13 27.1 18Q25.2 26.6 16 27.2Q6.8 26.6 4.9 18Q3.8 13 5 7.6Z', '#FF9A4D') +
    P('M6.4 8.6L9.4 6.8Q10.3 8.6 11 9.6Q8.6 9.6 7 11.6Z', '#FFE3CC', False) + P('M25.6 8.6L22.6 6.8Q21.7 8.6 21 9.6Q23.4 9.6 25 11.6Z', '#FFE3CC', False) +
    P('M6.2 16.6Q10 21.4 16 21Q22 21.4 25.8 16.6Q24.8 25.8 16 26.6Q7.2 25.8 6.2 16.6Z', '#FFF4E8', False) +
    face(16, 16.1, 1, 4.3, True, 6.5, 2.6, None) + E(16, 20.9, 1.45, 1.0, INK, False) + L('M14.7 22.3Q16 23.3 17.3 22.3', .85))
# 6 tek boynuzlu at
S['unicorn'] = (P('M10.6 11L9.6 5.6L13.6 8.6Z', W, True, .9) + P('M21.4 11L22.4 5.6L18.4 8.6Z', W, True, .9) +
    E(16, 18.2, 10.1, 9.6, W) + E(16, 23, 6.1, 4, '#FFE4F1', False) +
    C(7.6, 12.6, 3.1, '#FF9DCB') + C(9.6, 8.9, 2.8, '#BCA5FF') + C(22.6, 9.2, 2.8, '#6FE3C4') + C(24.6, 12.9, 3.0, '#FF9DCB') + C(6.4, 16.6, 2.4, '#6FE3C4') +
    P('M14.2 10.2L16 2.4L17.8 10.2Q16 11 14.2 10.2Z', '#FFD43B') + L('M14.9 7.6L17.2 6.6M14.6 9.2L17.5 8.2', .6) +
    face(16, 17.6, 1, 3.8, True, 5.6, 2.3, None) + C(14.5, 23.1, .45, INK, False) + C(17.5, 23.1, .45, INK, False) + L('M14.9 24.5Q16 25.4 17.1 24.5', .8))
# 7 dinozor
S['t-rex'] = (P('M11.2 9.4L12.8 5.4L15 8.2L17.2 4.6L19.2 8.2L22 5.8L22.6 10Z', '#FFD43B', True, .9) +
    E(11.4, 28.1, 2.8, 1.6, '#5DBB72') + E(20.6, 28.1, 2.8, 1.6, '#5DBB72') +
    E(16, 17.6, 10.6, 10.1, '#7BD389') + E(16, 23.2, 6.1, 4.4, '#DFF6C8', False) + C(23.6, 12.4, .8, '#5DBB72', False) + C(9, 21.4, .7, '#5DBB72', False) +
    E(9.7, 22.6, 1.4, 2.1, '#7BD389', True, 30, .9) + E(22.3, 22.6, 1.4, 2.1, '#7BD389', True, -30, .9) +
    face(16, 15.6, 1, 3.9, True, 5.9, 2.4, 'open'))
# 8 ahtapot: yüksek yuvarlak baş, iki yana açılan sekiz kıvrık kol, vantuz noktaları (denizanasından silüetle ayrılsın)
def arm(d):
    return L(d, 3.4 + 2 * SW * .8, INK) + L(d, 3.4, '#FF8FA8')
ARMS = ['M11 20Q5 21 3.6 25.6Q3 28.6 5.8 28.4', 'M12.6 21.6Q9.4 25.4 9.6 28.6Q9.8 30.4 11.8 29.6', 'M14.8 22.4Q14 26.6 15.6 29.4',
        'M17.2 22.4Q18 26.6 16.4 29.4', 'M19.4 21.6Q22.6 25.4 22.4 28.6Q22.2 30.4 20.2 29.6', 'M21 20Q27 21 28.4 25.6Q29 28.6 26.2 28.4',
        'M10.2 18Q4.6 16.6 2.6 19.6Q1.8 21.2 3.2 22', 'M21.8 18Q27.4 16.6 29.4 19.6Q30.2 21.2 28.8 22']
S['octopus'] = (''.join(arm(d) for d in ARMS) +
    ''.join(C(x, y, .55, '#FFD6E0', False) for x, y in ((5.2, 24.6), (10.4, 26.2), (21.6, 26.2), (26.8, 24.6), (15, 26.4), (17, 26.4))) +
    E(16, 13.4, 9.6, 10.2, '#FF8FA8') + C(11, 7.8, 1.1, '#FFC2D1', False) + C(21.2, 9, .8, '#FFC2D1', False) + C(19.4, 6.4, .6, '#FFC2D1', False) +
    face(16, 14.4, 1, 3.5, True, 5.4, 2.2))
# 9 papağan
S['parrot'] = (E(6.8, 20.6, 2.8, 5.4, '#5DB7FF', True, 16) + E(25.2, 20.6, 2.8, 5.4, '#5DB7FF', True, -16) +
    E(13.6, 6.6, 1.2, 2.7, '#FFD43B', True, -24, .85) + E(16.2, 5.6, 1.2, 2.9, '#FFD43B', True, 0, .85) + E(18.8, 6.6, 1.2, 2.7, '#FFD43B', True, 24, .85) +
    E(16, 18.2, 9.6, 10.6, '#FF6B6B') + E(16, 24.4, 5, 3.6, '#FF9A9A', False) +
    face(16, 14.3, 1, 3.9, True, 5.8, 2.6, None) +
    P('M14.2 16Q16 15 17.8 16Q17.8 19.8 16 20.6Q14.2 19.8 14.2 16Z', '#FFE7A3', True, .8) + L('M14.6 17.6Q16 18.3 17.4 17.6', .55))
# 10 kirpi
S['hedgehog'] = (P(''.join(('M' if i == 0 else 'L') + '%.2f %.2f' % (16 + (13.2 if i % 2 == 0 else 10.2) * math.cos(math.radians(a_)), 18 - (13.2 if i % 2 == 0 else 10.2) * math.sin(math.radians(a_)))
        for i, a_ in enumerate([-12 + k * 12.8 for k in range(17)])) + 'Z', '#9C6B4E') +
    E(16, 20, 8.7, 7.6, '#F6DCC0') + C(9.4, 14.6, 1.6, '#F6DCC0', True, .9) + C(22.6, 14.6, 1.6, '#F6DCC0', True, .9) +
    face(16, 18.6, 1, 3.4, True, 5.3, 2.3, None) + C(16, 21.2, 1.15, INK, False) + L('M14.9 22.6Q16 23.5 17.1 22.6', .8) +
    C(24.2, 7.6, 2.3, '#FF6B6B') + E(25.4, 4.8, 1.2, .6, '#7BD389', True, -30, .7))
# 11 lama
S['llama'] = (R(10.4, 20, 11.2, 9.6, 3.2, '#FFF1DC') +
    P('M10.5 24.6L21.5 24.6L21.5 28.2Q21.5 29.4 20.3 29.4L11.7 29.4Q10.5 29.4 10.5 28.2Z', '#FF9DCB', True, .9) + L('M11 26.6L21 26.6', 1.0, '#6FE3C4') + L('M12.6 25.1L12.6 28.8M15 25.1L15 28.8M17.4 25.1L17.4 28.8M19.8 25.1L19.8 28.8', .5, '#FFD43B') +
    E(10.2, 6.4, 1.8, 3.4, '#FFF1DC', True, -20) + E(21.8, 6.4, 1.8, 3.4, '#FFF1DC', True, 20) +
    E(10.2, 6.7, .75, 2.1, '#FFC2D1', False, -20) + E(21.8, 6.7, .75, 2.1, '#FFC2D1', False, 20) +
    P('M7.6 13.2Q7.6 7.8 16 7.8Q24.4 7.8 24.4 13.2L24.4 19.2Q24.4 23 16 23Q7.6 23 7.6 19.2Z', '#FFF1DC') +
    cloud([(13.2, 8.4, 2.4), (16, 7.0, 2.7), (18.8, 8.4, 2.4)]) +
    E(16, 18.6, 5.3, 3.5, '#FFE0C2', False) + face(16, 14.2, 1, 3.6, True, 5.7, 2.0, None) +
    C(14.6, 18.2, .45, INK, False) + C(17.4, 18.2, .45, INK, False) + L('M14.9 19.7Q16 20.6 17.1 19.7', .8))
# 12 flamingo
S['flamingo'] = (L('M14.2 27.6L14.2 31', 1.0) + L('M17.8 27.6L17.8 29.6L19.6 29.6', 1.0) +
    E(16, 18.8, 10.1, 9.6, '#FF9DCB') + P('M19.6 21.6Q24.2 20.4 25 23.8Q23.6 27 20.2 26Q18.8 23.8 19.6 21.6Z', '#FFC2DD', True, .85) +
    E(13.4, 8.8, 1.1, 2.4, '#FF9DCB', True, -30, .8) + E(15.6, 8.1, 1.1, 2.5, '#FF9DCB', True, 5, .8) +
    face(16, 14.6, 1, 3.4, True, 5.3, 2.3, None) +
    P('M14.4 16.7Q16 15.9 17.6 16.7Q17.6 18.4 16.9 19.4Q16.2 20.6 15.3 20.2Q14.6 18.6 14.4 16.7Z', W, True, .8) + P('M15.1 19.2Q16.1 19.8 16.95 19.3Q16.4 20.7 15.4 20.3Z', INK, False))
# 13 robot
S['robot'] = (L('M16 9.2L16 5.4', 1.1) + C(16, 4.3, 1.9, '#FF5C9D') +
    R(3.4, 14, 2.6, 6.2, 1.1, '#9DAAF0', True, .9) + R(26, 14, 2.6, 6.2, 1.1, '#9DAAF0', True, .9) +
    R(10.4, 25.4, 11.2, 4, 1.6, '#9DAAF0') + P('M16 28.6Q14.2 27.2 14.8 26.5Q15.4 25.9 16 26.7Q16.6 25.9 17.2 26.5Q17.8 27.2 16 28.6Z', '#FF5C9D', False) +
    R(5.6, 9, 20.8, 17, 5.2, '#C9D2FF') + R(8.6, 12, 14.8, 10.6, 3.6, W, True, .9) + C(7.3, 10.7, .55, '#9DAAF0', False) + C(24.7, 10.7, .55, '#9DAAF0', False) +
    face(16, 16.4, .95, 2.9, True, 4.5, 2.3))
# 14 uzaylı
S['alien'] = (L('M11.2 6.6L8.2 2.6', 1.0) + L('M20.8 6.6L23.8 2.6', 1.0) + C(8, 2.4, 1.6, '#FFD43B') + C(24, 2.4, 1.6, '#FFD43B') +
    P('M16 5Q27.6 5 27.1 15.6Q26.6 25 16 28Q5.4 25 4.9 15.6Q4.4 5 16 5Z', '#8BE8A0') +
    C(9.8, 9.6, 1.1, '#C6F5D0', False) + C(23, 22, .9, '#C6F5D0', False) + C(21.4, 8.4, .7, '#C6F5D0', False) +
    face(16, 15.8, 1, 4.4, True, 6.6, 3.2, None, 1.55) + L('M14.6 21.2Q16 22.4 17.4 21.2', .85))
# 15 hayalet
S['ghost'] = (E(5.6, 18.2, 1.7, 2.9, W, True, 30) + E(26.4, 18.2, 1.7, 2.9, W, True, -30) +
    P('M6 16Q6 5 16 5Q26 5 26 16L26 26.4Q24.4 28.6 22.8 26.4Q21.2 28.6 19.4 26.4Q17.7 28.6 16 26.4Q14.3 28.6 12.6 26.4Q10.8 28.6 9.2 26.4Q7.6 28.6 6 26.4Z', W) +
    E(22.4, 9.6, 1.4, .8, '#E9E4FF', False, -30) + face(16, 14.6, 1, 3.6, True, 5.6, 2.4, 'open'))
# 16 roket
S['rocket'] = (P('M10.6 14.6L6.2 21.2Q5.8 23.8 8.4 23.2L10.6 21.4Z', '#FF6B6B') + P('M21.4 14.6L25.8 21.2Q26.2 23.8 23.6 23.2L21.4 21.4Z', '#FF6B6B') +
    P('M12.6 23.4Q16 32 19.4 23.4Z', '#FFD43B', True, .9) + P('M14.4 23.4Q16 28.2 17.6 23.4Z', '#FF9A4D', False) +
    R(12.2, 20.8, 7.6, 2.8, 1, '#9DAAF0', True, .9) +
    P('M16 3.4Q23.2 9 22 21.2L10 21.2Q8.8 9 16 3.4Z', W) + P('M16 3.4Q20.4 6.6 21.4 10.4Q16 11.6 10.6 10.4Q11.6 6.6 16 3.4Z', '#FF6B6B', True, .9) +
    face(16, 14.8, .85, 2.5, True, 4.0, 2.2) + sparkle(26.4, 6.4, 2.2) + sparkle(5.4, 9.4, 1.5, W))
# 17 gökkuşağı
def arc(r, col, w):
    d = 'M%s 22A%s %s 0 0 1 %s 22' % (16 - r, r, r, 16 + r)
    return L(d, w + 2 * SW * .8, INK) + L(d, w, col)
S['rainbow'] = (arc(11.6, '#FF9DCB', 2.4) + arc(9.2, '#FFD43B', 2.4) + arc(6.8, '#6FE3C4', 2.4) + arc(4.4, '#8FD3FF', 2.4) +
    cloud([(3.6, 23.6, 2.6), (6.4, 21.8, 3.2), (9.4, 23.8, 2.6), (6.6, 25.4, 2.4)]) + cloud([(22.6, 23.8, 2.6), (25.6, 21.8, 3.2), (28.4, 23.6, 2.6), (25.4, 25.4, 2.4)]) +
    face(6.5, 23, .62, 2.6, True, 4.3, 2.0) + face(25.5, 23, .62, 2.6, True, 4.3, 2.0))
# 18 taç
S['crown'] = (P('M5 11.6L10.2 17.2L16 8L21.8 17.2L27 11.6L25.4 25.4L6.6 25.4Z', '#FFD43B') +
    P('M6.2 21.4L25.8 21.4L25.4 25.4L6.6 25.4Z', '#FFB524', True, .9) +
    C(5, 11.2, 1.7, '#FF9DCB') + C(16, 7.4, 1.9, '#6FE3C4') + C(27, 11.2, 1.7, '#BCA5FF') +
    P('M16 22.2L17.2 23.4L16 24.6L14.8 23.4Z', '#FF5C9D', True, .6) + C(10.6, 23.4, .8, '#8FD3FF', True, .6) + C(21.4, 23.4, .8, '#8FD3FF', True, .6) +
    face(16, 16.4, .9, 2.8, True, 4.6, 2.0) + sparkle(27.6, 4.6, 1.8, W))
# 19 kaktüs
S['cactus'] = (P('M10.8 16L8.2 16Q6.2 16 6.2 14L6.2 10.6Q6.2 9 7.7 9Q9.2 9 9.2 10.6L9.2 13L10.8 13Z', '#6FD38F', True, .95) +
    P('M21.2 14.4L23.6 14.4Q25.6 14.4 25.6 12.4L25.6 9.6Q25.6 8 24.1 8Q22.6 8 22.6 9.6L22.6 11.6L21.2 11.6Z', '#6FD38F', True, .95) +
    R(10.4, 5.8, 11.2, 17.4, 5.6, '#6FD38F') + L('M13.4 9.4L13.4 10.4M18.8 8.8L18.8 9.8M12.6 19.4L12.6 20.4M19.6 18.6L19.6 19.6', .55, '#3E9E5E') +
    P('M9 22.6L23 22.6L21.4 29.6L10.6 29.6Z', '#FF9A6B') + R(8, 20.6, 16, 3.2, 1.3, '#FFB48F') +
    ''.join(C(round(17.6 + 1.45 * math.cos(math.radians(90 + k * 72)), 2), round(4.6 - 1.45 * math.sin(math.radians(90 + k * 72)), 2), 1.15, '#FF9DCB', True, .6) for k in range(5)) + C(17.6, 4.6, .8, '#FFD43B', False) +
    face(16, 13.6, .85, 2.6, True, 4.2, 2.2))
# 20 avokado
S['avocado'] = (P('M16 3.4Q22 3.4 23.6 11Q28.2 16 27.1 22.2Q25.6 29.6 16 29.6Q6.4 29.6 4.9 22.2Q3.8 16 8.4 11Q10 3.4 16 3.4Z', '#5BAE5B') +
    P('M16 5.9Q20.6 5.9 21.7 12Q25.6 16.6 24.7 21.6Q23.5 27.2 16 27.2Q8.5 27.2 7.3 21.6Q6.4 16.6 10.3 12Q11.4 5.9 16 5.9Z', '#DDF3A3', False) +
    C(16, 21.2, 4.6, '#B9805A') + E(14.6, 19.6, 1.3, .8, '#D9A57E', False, -30) +
    face(16, 13.2, .9, 2.8, True, 4.6, 2.0))
# 21 disko topu
S['mirror-ball'] = (L('M16 1.4L16 5.6', .9) + R(14, 5, 4, 2.3, .8, '#9DAAF0', True, .9) +
    C(16, 18, 11, '#DDE3FF') +
    ''.join(L('M%.2f %.2fL%.2f %.2f' % (16 - math.sqrt(max(0, 10.4 ** 2 - (y - 18) ** 2)), y, 16 + math.sqrt(max(0, 10.4 ** 2 - (y - 18) ** 2)), y), .55, '#AEB9F2') for y in (11.2, 14.6, 21.4, 24.8)) +
    E(16, 18, 4.4, 10.4, 'none', False) + L('M16 7.6L16 28.4', .55, '#AEB9F2') +
    '<ellipse cx="16" cy="18" rx="4.4" ry="10.4" fill="none" stroke="#AEB9F2" stroke-width=".55"/><ellipse cx="16" cy="18" rx="8.2" ry="10.4" fill="none" stroke="#AEB9F2" stroke-width=".55"/>' +
    R(10.2, 9.6, 2.4, 2.2, .4, W, False) + R(19.6, 22.6, 2.4, 2.2, .4, '#FFC2DD', False) + R(21.6, 12.4, 2.2, 2, .4, '#C9F3E6', False) + R(8.6, 21.8, 2, 2, .4, '#FFE58A', False) +
    C(16, 18, 11, 'none') + face(16, 17.6, 1, 3.2, True, 5.0, 2.4) + sparkle(26.2, 6.8, 2.4, W) + sparkle(5.2, 9.2, 1.5))
# 22 uçan daire
S['flying-saucer'] = (P('M11.8 21.4L20.2 21.4L23.6 29.4L8.4 29.4Z', '#FFF3B0', True, .8, .9) +
    P('M9.6 15.4Q9.6 5.8 16 5.8Q22.4 5.8 22.4 15.4Z', '#BDE8FF') + E(13.4, 9.6, 1.1, .7, W, False, -30) +
    face(16, 11.4, .78, 2.6, True, 4.3, 2.0) +
    E(16, 17.6, 13, 4.6, '#BCA5FF') + L('M5.6 16.2Q16 19.6 26.4 16.2', .7, '#9B7BFF') +
    ''.join(C(x, y, 1.0, '#FFD43B', True, .6) for x, y in ((8.6, 18.6), (12.4, 19.7), (16, 20.0), (19.6, 19.7), (23.4, 18.6))))
# 23 ejderha
S['dragon'] = (P('M7.6 13.6L2.6 10.4Q2.2 15.6 4.6 18.2L3.4 21.2Q6.8 21.6 8.6 19.6Z', '#FF9DCB', True, .95) + P('M24.4 13.6L29.4 10.4Q29.8 15.6 27.4 18.2L28.6 21.2Q25.2 21.6 23.4 19.6Z', '#FF9DCB', True, .95) +
    P('M10.2 10.4Q8.6 6.4 10.2 3.8Q11.4 7 13.2 8.6Z', '#FFD43B', True, .9) + P('M21.8 10.4Q23.4 6.4 21.8 3.8Q20.6 7 18.8 8.6Z', '#FFD43B', True, .9) +
    P('M14.4 8.4L16 5.6L17.6 8.4Z', '#FF9DCB', True, .8) +
    E(16, 17.6, 10.4, 9.6, '#5FD3B5') + E(16, 21.8, 5.8, 3.8, '#B5F2E2', False) + C(22.6, 12.6, .8, '#3FB596', False) + C(9.6, 13.8, .6, '#3FB596', False) +
    face(16, 16.2, 1, 3.8, True, 5.8, 2.4, None) + C(14.7, 21.2, .45, INK, False) + C(17.3, 21.2, .45, INK, False) +
    L('M14.7 23Q16 24.1 17.3 23', .8) + P('M16.7 23.4L17.2 24.6L17.6 23.3Z', W, True, .45))
# 24 denizanası
S['jellyfish'] = (''.join(L(d, 3.0, INK) + L(d, 1.7, '#BCA5FF') for d in (
        'M9.2 18.4Q7.6 21 9.2 23.4Q10.8 25.8 9.2 28.4', 'M12.8 18.8Q11.6 21.6 13 24.2Q14.2 26.6 13 29.4', 'M16 19Q17.4 21.8 16 24.6Q14.6 27.4 16 30',
        'M19.2 18.8Q20.4 21.6 19 24.2Q17.8 26.6 19 29.4', 'M22.8 18.4Q24.4 21 22.8 23.4Q21.2 25.8 22.8 28.4')) +
    P('M5.4 17Q5.4 5.8 16 5.8Q26.6 5.8 26.6 17Q24.8 19.1 23 17.3Q21.2 19.1 19.5 17.3Q17.7 19.1 16 17.3Q14.3 19.1 12.5 17.3Q10.8 19.1 9 17.3Q7.2 19.1 5.4 17Z', '#BCA5FF') +
    E(10.8, 9.8, 1.6, .9, '#E3D9FF', False, -35) + C(21.6, 8.8, .7, '#E3D9FF', False) +
    face(16, 12.6, 1, 3.4, True, 5.4, 2.2))

ORDER = ['sloth', 'otter', 'penguin', 'owl', 'fox', 'unicorn', 't-rex', 'octopus', 'parrot', 'hedgehog', 'llama', 'flamingo', 'robot', 'alien', 'ghost', 'rocket',
         'rainbow', 'crown', 'cactus', 'avocado', 'mirror-ball', 'flying-saucer', 'dragon', 'jellyfish']
assert sorted(ORDER) == sorted(S), set(ORDER) ^ set(S)
json.dump({'lk-' + k: S[k] for k in ORDER}, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print(len(S), 'çıkartma', sum(len(v) for v in S.values()), 'bayt')
