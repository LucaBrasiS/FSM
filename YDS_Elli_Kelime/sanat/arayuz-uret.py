"""Arayüz simgeleri: sekmeler, görev karoları, başlık simgeleri. Lokum ve çıkartmalarla aynı çizgi
(düz renk, eşit kalınlıkta #17132B dış çizgi, yuvarlak hatlar), ama yüzsüz: yüz Lokum'a ve çıkartmalara özel.
Hepsi 32x32 çizim alanında. Kullanım: python3 arayuz-uret.py <çıktı.json>"""
import json, sys
INK = '#17132B'; SW = 1.3; W = '#FFFFFF'

def st(w=SW):
    return 'stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"' % (INK, w)
def E(cx, cy, rx, ry, fill, line=True, rot=0, w=SW):
    t = ' transform="rotate(%s %s %s)"' % (rot, cx, cy) if rot else ''
    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s"%s%s/>' % (cx, cy, rx, ry, fill, (' ' + st(w)) if line else '', t)
def C(cx, cy, r, fill, line=True, w=SW):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"%s/>' % (cx, cy, r, fill, (' ' + st(w)) if line else '')
def P(d, fill, line=True, w=SW):
    return '<path d="%s" fill="%s"%s/>' % (d, fill, (' ' + st(w)) if line else '')
def L(d, w=1.0, col=INK):
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"/>' % (d, col, w)
def R(x, y, w_, h, rx, fill, line=True, w=SW, rot=None):
    t = ' transform="rotate(%s)"' % rot if rot else ''
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"%s%s/>' % (x, y, w_, h, rx, fill, (' ' + st(w)) if line else '', t)
def tube(d, col, w):
    """Koyu çizgili kalın şerit: önce koyu, sonra renk."""
    return L(d, w + 2 * SW * .85, INK) + L(d, w, col)
def sparkle(x, y, r, col):
    q = r * .32
    return P('M%s %sQ%s %s %s %sQ%s %s %s %sQ%s %s %s %sQ%s %s %s %sZ' % (
        x, y - r, x + q, y - q, x + r, y, x + q, y + q, x, y + r, x - q, y + q, x - r, y, x - q, y - q, x, y - r), col, True, .8)

U = {}
# Bugün: takvim, bugünün günü pembe kalp
U['tab-today'] = (R(4.5, 6.5, 23, 21.5, 4.5, W, False) +
    P('M4.5 13L4.5 11Q4.5 6.5 9 6.5L23 6.5Q27.5 6.5 27.5 11L27.5 13Z', '#FF6B6B', False) + L('M4.5 13L27.5 13', SW) +
    ''.join(R(x, y, 3.6, 3.2, 1, '#E3D9FF', False) for y in (15.6, 21.2) for x in (8, 14.2, 20.4) if not (x == 20.4 and y == 21.2)) +
    P('M22.2 25.2Q19.8 23.6 20.3 22.2Q20.8 21 22.2 21.9Q23.6 21 24.1 22.2Q24.6 23.6 22.2 25.2Z', '#FF5C9D', True, .7) +
    R(4.5, 6.5, 23, 21.5, 4.5, 'none') + R(9.6, 3.4, 2.6, 6, 1.3, '#BCA5FF', True, 1.0) + R(19.8, 3.4, 2.6, 6, 1.3, '#BCA5FF', True, 1.0))
# Kelime: abc karosu
U['tab-words'] = (R(3.5, 5.5, 25, 21, 5, '#5DB7FF') + L('M7 21.4L25 21.4', .9, '#3E95E0') +
    L('M12.1 15.2L12.1 20.4M12.1 17.8A2.5 2.5 0 1 0 12.1 17.9', 1.9, W) +
    L('M15.2 11.2L15.2 20.4M15.2 17.8A2.5 2.5 0 1 1 15.2 17.9', 1.9, W) +
    L('M25.1 16.1A2.6 2.6 0 1 0 25.1 19.6', 1.9, W))
# Gramer: üç kitap, biri yaslanmış
U['tab-units'] = (R(4.6, 8.4, 6.2, 18.8, 1.4, '#FF9DCB') + R(5.8, 12, 3.8, 1.6, .6, W, False) + R(5.8, 21.4, 3.8, 1.6, .6, W, False) +
    R(11.2, 5.4, 6.6, 21.8, 1.4, '#6FE3C4') + R(12.4, 9.4, 4.2, 4.2, 1, W, False) +
    '<g transform="rotate(16 21.4 27.2)">' + R(19.6, 8.6, 5.8, 18.6, 1.4, '#FFD43B') + R(20.6, 12.4, 3.8, 1.6, .6, W, False) + '</g>' +
    L('M3 27.4L29 27.4', SW))
# Fiil taraması: büyüteç
U['scan'] = ('<g transform="rotate(-45 20.8 21)">' + R(18.6, 18.6, 4.4, 11.6, 2.2, '#BCA5FF') + '</g>' +
    C(13.4, 13.4, 9.2, '#FFD43B') + C(13.4, 13.4, 6.4, '#BDE8FF', True, 1.0) + L('M9.6 11.4Q10.6 9.4 12.8 9', 1.5, W))
# Eşleştir: sarı yapboz parçası (yeşil bantta da seçilsin diye sarı)
U['t-match'] = P('M5.5 9L12 9Q10.8 5.8 13.6 5.3Q16.4 5 16.2 8Q16.1 8.6 15.6 9L22.5 9L22.5 15.4Q23.3 14.6 24.8 14.8Q27.4 15.4 27.1 18Q26.8 20.6 24.4 20.4Q23.4 20.3 22.5 19.6L22.5 26.5L5.5 26.5L5.5 20.2Q6.8 21.2 8.4 20.8Q10.6 20.1 10.3 17.8Q10 15.6 7.9 15.6Q6.6 15.6 5.5 16.4Z', '#FFD43B')
# Cümle: dizilmiş kelime kutucukları
U['t-sent'] = (R(9.4, 7.6, 13.2, 8.4, 2.4, '#FFD43B') + L('M12.8 11.8L19.2 11.8', 1.5, W) +
    R(3.4, 18.4, 12.4, 8.4, 2.4, '#FF9DCB') + L('M6.6 22.6L12.6 22.6', 1.5, W) +
    R(16.8, 18.4, 11.8, 8.4, 2.4, '#BCA5FF') + L('M19.8 22.6L25.6 22.6', 1.5, W))
# Balon patlat
U['balloon'] = (L('M16 23.4Q13.8 25.8 16.2 27.8Q18.2 29.6 15.8 31', 1.1) + P('M14.6 24L16 21.8L17.4 24Z', '#FF6B6B', True, .9) +
    E(16, 12.8, 8.2, 9.6, '#FF6B6B') + E(12.6, 9, 1.5, 2.6, W, False, 25))
# Kutlama: konfeti
U['party'] = (P('M4.6 27.6L10 12.6L19.6 22.2Z', '#BCA5FF') + L('M7.6 19.6L12.6 24.4M9 15.8L16.2 22.8', 1.2, '#FFD43B') +
    tube('M18.6 12.2Q21.6 10.4 21 6.4', '#FF6B6B', 1.2) + tube('M21.4 15.6Q24.6 14.2 27.2 16.4', '#6FE3C4', 1.2) +
    C(15.6, 6.4, 1.3, '#FFD43B', True, .8) + C(25.8, 9.4, 1.3, '#FF9DCB', True, .8) + C(13.6, 10.4, 1.0, '#6FE3C4', True, .8) +
    R(23.4, 4, 2.4, 2.4, .5, '#5DB7FF', True, .8))
# Seri: alev
U['fire'] = (P('M16 3.4Q18.2 8.4 21.6 11.4Q26.2 15.4 25.4 21Q24.2 28.6 16 28.6Q7.8 28.6 6.6 21.2Q5.8 16 9.6 12.2Q10 15.2 12.1 16Q11.6 9.8 16 3.4Z', '#FF9A4D') +
    P('M16 13.6Q17.8 16.8 19.6 18.6Q21.2 20.4 20.6 23Q19.8 26 16 26Q12.2 26 11.6 23.2Q11.2 20.8 13.4 18.8Q15.6 16.8 16 13.6Z', '#FFD43B', True, .9))
# Rekor: kupa
U['trophy'] = (tube('M9.4 8.4Q4.8 8.4 5.2 12Q5.6 15.2 9.8 15.4', '#FFD43B', 1.4) + tube('M22.6 8.4Q27.2 8.4 26.8 12Q26.4 15.2 22.2 15.4', '#FFD43B', 1.4) +
    R(14.2, 18.4, 3.6, 4.6, .8, '#FFB524') + P('M9 5.4L23 5.4L23 10.8Q23 18.6 16 19.2Q9 18.6 9 10.8Z', '#FFD43B') +
    sparkle(16, 11.6, 3.2, W) + R(9.6, 22.6, 12.8, 4.6, 1.8, '#BCA5FF'))
# Tekrar: pano ve tik
U['rev'] = (R(6, 5, 20, 23.6, 3.6, '#BCA5FF') + R(9, 8.6, 14, 17.4, 2, W, True, .9) + R(12, 3, 8, 4.6, 1.6, '#FFD43B', True, 1.0) +
    L('M11.6 13.2L20.4 13.2M11.6 16.6L18 16.6', 1.1, '#BCA5FF') + L('M11.8 21L13.8 22.9L17.6 19', 1.6, '#3FB596'))
# Karışık: çapraz oklar
U['mix'] = (R(3.5, 5.5, 25, 21, 5, '#6FE3C4') +
    L('M8 11.6L11.4 11.6Q13.6 11.6 15 14L17.4 18Q18.8 20.4 21 20.4L23.6 20.4', 1.9, W) + L('M8 20.4L11.4 20.4Q13.2 20.4 14.2 18.9M17.8 13.1Q18.8 11.6 21 11.6L23.6 11.6', 1.9, W) +
    L('M21.4 9L24.2 11.6L21.4 14.2M21.4 17.8L24.2 20.4L21.4 23', 1.7, W))

json.dump({'ui-' + k: v for k, v in U.items()}, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print(len(U), 'simge', sum(len(v) for v in U.values()), 'bayt')
