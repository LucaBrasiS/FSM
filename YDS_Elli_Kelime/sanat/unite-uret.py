"""Gramer ünitesi simgeleri: arayüz simgeleriyle aynı kural (düz renk, 1,3 birimlik #17132B dış çizgi, yuvarlak hatlar,
yüzsüz). Anahtar, yerini aldığı hazır çizimin adıdır; o çizimi kullanan bütün üniteler yenisini alır.
Kullanım: python3 unite-uret.py <çıktı.json>"""
import json, math, sys, importlib.util, os
spec = importlib.util.spec_from_file_location('a', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arayuz-uret.py'))
src = open(spec.origin, encoding='utf-8').read().split('U = {}')[0]   # yalnız yardımcılar
g = {}; exec(src, g)
E, C, P, L, R, tube, sparkle, W, INK, SW = (g[k] for k in ('E', 'C', 'P', 'L', 'R', 'tube', 'sparkle', 'W', 'INK', 'SW'))

def poly(n, cx, cy, r, rot=0):
    return 'M' + 'L'.join('%.2f %.2f' % (cx + r * math.cos(math.radians(rot + k * 360 / n)), cy + r * math.sin(math.radians(rot + k * 360 / n))) for k in range(n)) + 'Z'

U = {}
U['alarm-clock'] = (L('M10 26.2L8.2 28.6M22 26.2L23.8 28.6', 1.6) + C(8.6, 8.2, 3.4, '#FFD43B') + C(23.4, 8.2, 3.4, '#FFD43B') +
    R(14.4, 4.2, 3.2, 3, 1, '#FFD43B', True, 1.0) + C(16, 17.6, 10, '#FF6B6B') + C(16, 17.6, 7.2, W, True, 1.0) +
    L('M16 17.6L16 12.4M16 17.6L19.6 19.4', 1.5) + C(16, 17.6, 1.1, INK, False))
U['hourglass-not-done'] = (P('M9.6 7.4L22.4 7.4Q22.4 13.2 16 16Q22.4 18.8 22.4 24.6L9.6 24.6Q9.6 18.8 16 16Q9.6 13.2 9.6 7.4Z', '#BDE8FF') +
    P('M12.2 10.6L19.8 10.6Q19 13.2 16 14.6Q13 13.2 12.2 10.6Z', '#FFD43B', False) + P('M11 24Q11.6 20.4 16 19.4Q20.4 20.4 21 24Z', '#FFD43B', False) +
    L('M16 15.6L16 19.6', 1.0, '#FFB524') + R(6.6, 3.8, 18.8, 3.6, 1.6, '#BCA5FF') + R(6.6, 24.6, 18.8, 3.6, 1.6, '#BCA5FF'))
U['clapper-board'] = (R(5, 13, 22, 14.6, 2.4, '#4B4F8F') + L('M8.6 18.4L19 18.4M8.6 22.4L15.4 22.4', 1.4, W) +
    '<g transform="rotate(-14 5.4 12.6)">' + R(5.4, 7.6, 21.6, 5, 1.2, W) +
    ''.join(P('M%s 7.9L%s 7.9L%s 12.3L%s 12.3Z' % (x, x + 2.6, x + 0.8, x - 1.8), '#4B4F8F', False) for x in (9.4, 15.2, 21)) + '</g>' +
    C(5.6, 12.8, 1.2, '#FFD43B', True, .8))
U['tear-off-calendar'] = (P('M6.4 8.4Q6.4 5.6 9.2 5.6L22.8 5.6Q25.6 5.6 25.6 8.4L25.6 22L20.4 27.4L9.2 27.4Q6.4 27.4 6.4 24.6Z', W) +
    P('M6.4 12L6.4 8.4Q6.4 5.6 9.2 5.6L22.8 5.6Q25.6 5.6 25.6 8.4L25.6 12Z', '#5DB7FF', True, 1.0) +
    P('M25.6 22L20.4 27.4L20.4 23.6Q20.4 22 22 22Z', '#E3D9FF', True, 1.0) + R(10.4, 15.4, 11.2, 2.2, 1.1, '#BCA5FF', False) + R(10.4, 19.6, 7, 2.2, 1.1, '#BCA5FF', False) +
    R(10.2, 3.2, 2.4, 5, 1.2, '#FF6B6B', True, .9) + R(19.4, 3.2, 2.4, 5, 1.2, '#FF6B6B', True, .9))
U['rabbit'] = (E(12.2, 9, 2.6, 6.4, W, True, -10) + E(19.8, 9, 2.6, 6.4, W, True, 10) + E(12.2, 9.4, 1.1, 4.4, '#FF9DCB', False, -10) + E(19.8, 9.4, 1.1, 4.4, '#FF9DCB', False, 10) +
    E(16, 20.6, 9.2, 7.8, W) + C(12.6, 19.4, 1.1, INK, False) + C(19.4, 19.4, 1.1, INK, False) +
    P('M14.8 22L17.2 22L16 23.4Z', '#FF9DCB', True, .7) + E(16, 27.6, 3.4, 1.2, '#E3D9FF', False))
U['racing-car'] = (P('M3.6 20.4Q3.6 16.6 7.4 16.2L12.4 15.6L15.6 11.6Q16.4 10.8 17.6 10.8L22.8 10.8Q24.4 10.8 25.4 12.4L27 15.4Q28.6 15.8 28.6 18L28.6 21.6L3.6 21.6Z', '#FF6B6B') +
    P('M16.8 15.4L18.4 12.8L22.6 12.8L24 15.4Z', '#BDE8FF', True, .9) + L('M6 18.4L12 18.4', 1.4, W) +
    C(9.4, 22, 3.4, INK, False) + C(9.4, 22, 1.4, '#C9D2FF', False) + C(23.2, 22, 3.4, INK, False) + C(23.2, 22, 1.4, '#C9D2FF', False) +
    L('M2.6 13L6.4 13M1.6 16L4.4 16', 1.2))
U['hot-pepper'] = (P('M20.6 9.4Q25 10.6 24.6 16Q24 23.6 15.4 27.6Q9.8 29.8 6.4 27.4Q12 26 15 21.6Q17.8 17 17.4 12.4Q17.6 9.8 20.6 9.4Z', '#FF6B6B') +
    P('M17.4 11.6Q18.4 9 21.2 9.2Q23.6 9.6 24.4 11.6Q21.6 10.8 17.4 11.6Z', '#7BD389', True, 1.0) + L('M21 9.2Q21.4 6 24.4 4.6', 1.6, '#3FB596') +
    E(20.6, 15.6, 1, 2.4, W, False, 25))
U['plus'] = P('M12.6 6.6Q12.6 4.6 14.6 4.6L17.4 4.6Q19.4 4.6 19.4 6.6L19.4 12.6L25.4 12.6Q27.4 12.6 27.4 14.6L27.4 17.4Q27.4 19.4 25.4 19.4L19.4 19.4L19.4 25.4Q19.4 27.4 17.4 27.4L14.6 27.4Q12.6 27.4 12.6 25.4L12.6 19.4L6.6 19.4Q4.6 19.4 4.6 17.4L4.6 14.6Q4.6 12.6 6.6 12.6L12.6 12.6Z', '#BCA5FF')
U['stop-sign'] = (L('M16 26L16 30.4', 2.2) + P(poly(8, 16, 14.8, 11.4, 22.5), '#FF6B6B') + P(poly(8, 16, 14.8, 8.8, 22.5), 'none', True, .9).replace('stroke="#17132B"', 'stroke="#FFFFFF"') +
    R(10, 13.2, 12, 3.4, 1.4, W, False))
U['stopwatch'] = (R(13.6, 3, 4.8, 3, 1, '#FFD43B', True, 1.0) + R(15, 5.6, 2, 2.4, .6, '#FFD43B', True, .9) + P('M23 8.6L25.2 6.4L26.8 8L24.6 10.2Z', '#FFD43B', True, .9) +
    C(16, 18, 10.2, '#6FE3C4') + C(16, 18, 7.4, W, True, 1.0) + P('M16 18L16 11.4A6.6 6.6 0 0 1 21.7 14.7Z', '#FFD43B', False) + L('M16 18L16 12.2', 1.5) + C(16, 18, 1.1, INK, False))
U['compass'] = (C(16, 16, 12, '#FFD43B') + C(16, 16, 8.8, W, True, 1.0) +
    ''.join(P(d, INK, False) for d in ('M16 3.6L17.6 6.8L14.4 6.8Z', 'M28.4 16L25.2 17.6L25.2 14.4Z', 'M16 28.4L14.4 25.2L17.6 25.2Z', 'M3.6 16L6.8 14.4L6.8 17.6Z')) +
    P('M16 7.4L19.2 16L12.8 16Z', '#FF6B6B', True, 1.0) + P('M16 24.6L12.8 16L19.2 16Z', '#5DB7FF', True, 1.0) + C(16, 16, 1.4, INK, False))
U['crystal-ball'] = (P('M8.4 24.4L23.6 24.4L25.6 29Q25.8 29.6 25.2 29.6L6.8 29.6Q6.2 29.6 6.4 29Z', '#FF9DCB') +
    C(16, 14.4, 10.6, '#BCA5FF') + E(11.4, 9.8, 2.2, 3.6, W, False, 35) + sparkle(19.6, 15.6, 3.4, W) + sparkle(13.6, 19.2, 1.8, '#FFD43B'))
def chain(c1, c2):
    ring = lambda cx, cy, col: tube('M%s %sL%s %sA3.6 3.6 0 0 1 %s %sL%s %sA3.6 3.6 0 0 1 %s %sZ' % (cx - 4, cy - 3.6, cx + 4, cy - 3.6, cx + 4, cy + 3.6, cx - 4, cy + 3.6, cx - 4, cy - 3.6), col, 2.4)
    return ('<g transform="rotate(-35 16 16)">' + ring(10.6, 16, c1) + ring(21.4, 16, c2) + L('M17.4 12.4L17.4 13.8', 2.4 + 2 * SW * .85) + L('M17.4 12.4L17.4 13.8', 2.4, c1) + '</g>')
U['link'] = chain('#BCA5FF', '#6FE3C4')   # bağlaç atölyesi ve bağlaç üniteleri: kelime görselindeki zincirle aynı
U['red-heart'] = (P('M16 27.6Q4 20 4.2 11.8Q4.6 5.6 10.4 5.4Q14 5.4 16 9Q18 5.4 21.6 5.4Q27.4 5.6 27.8 11.8Q28 20 16 27.6Z', '#FF5C9D') +
    E(10.2, 10.6, 1.8, 2.8, W, False, 35))

json.dump({'un-' + k: v for k, v in U.items()}, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print(len(U), 'ünite simgesi', sum(len(v) for v in U.values()), 'bayt')
