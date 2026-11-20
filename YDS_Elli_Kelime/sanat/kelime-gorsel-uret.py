"""İnce kalan kelime görselleri, kalın biçimlerle yeniden: düz renk, 1,3 birimlik #17132B dış çizgi, yüzsüz.
Anahtar yerini aldığı hazır çizimin adıdır; o çizimi kullanan bütün kelimeler yenisini alır (sanat/ince-kelime-gorselleri.md).
Kullanım: python3 kelime-gorsel-uret.py <çıktı.json>"""
import json, sys, os
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arayuz-uret.py'), encoding='utf-8').read().split('U = {}')[0]
g = {}; exec(src, g)
E, C, P, L, R, tube, sparkle, W, INK, SW = (g[k] for k in ('E', 'C', 'P', 'L', 'R', 'tube', 'sparkle', 'W', 'INK', 'SW'))

def chain(c1, c2):
    ring = lambda cx, cy, col: tube('M%s %sL%s %sA3.6 3.6 0 0 1 %s %sL%s %sA3.6 3.6 0 0 1 %s %sZ' % (cx - 4, cy - 3.6, cx + 4, cy - 3.6, cx + 4, cy + 3.6, cx - 4, cy + 3.6, cx - 4, cy - 3.6), col, 2.4)
    return ('<g transform="rotate(-35 16 16)">' + ring(10.6, 16, c1) + ring(21.4, 16, c2) +
            L('M17.4 12.4L17.4 13.8', 2.4 + 2 * SW * .85) + L('M17.4 12.4L17.4 13.8', 2.4, c1) + '</g>')   # birinci halka ikincinin önünden geçer

U = {}
U['telescope'] = (tube('M15 17.6L9 28.4', '#FFD43B', 2) + tube('M15 17.6L21 28.4', '#FFD43B', 2) + tube('M15 17.6L15 28.6', '#FFD43B', 2) +
    '<g transform="rotate(-28 15 12)">' + R(4, 8.6, 21, 7, 3, '#BCA5FF') + R(22, 7.4, 5.6, 9.4, 2, '#FF9DCB') + R(1.6, 10, 3.6, 4.2, 1.2, '#FFD43B', True, 1.0) + '</g>' +
    C(15, 17.4, 2.4, '#FF9DCB'))
U['chart-increasing'] = (R(4.4, 20.4, 6, 7.6, 1.6, '#FF9DCB') + R(13, 15.4, 6, 12.6, 1.6, '#FFD43B') + R(21.6, 10, 6, 18, 1.6, '#6FE3C4') +
    tube('M4.8 15L11.2 9.6L15.6 12.2L23.4 5.2', '#FF6B6B', 2.2) + P('M20 4L25.8 3L24.8 8.8Z', '#FF6B6B', True, 1.0))
U['chart-decreasing'] = (R(4.4, 10, 6, 18, 1.6, '#6FE3C4') + R(13, 15.4, 6, 12.6, 1.6, '#FFD43B') + R(21.6, 20.4, 6, 7.6, 1.6, '#FF9DCB') +
    tube('M4.8 4.6L11.2 10L15.6 7.4L23.4 14.4', '#FF6B6B', 2.2) + P('M20 15.6L25.8 16.6L24.8 10.8Z', '#FF6B6B', True, 1.0))
U['link'] = chain('#BCA5FF', '#6FE3C4')
clip = 'M12 8L12 22Q12 26 16 26Q20 26 20 22L20 6Q20 3 17 3Q14 3 14 6L14 20Q14 22 16 22Q18 22 18 20L18 9'   # tek tel: dış ve iç ilmek
U['linked-paperclips'] = ('<g transform="rotate(-24 16 16)">' + tube(clip, '#BCA5FF', 2.2) + '</g>' +
    '<g transform="rotate(30 18 18) translate(4 3)">' + tube(clip, '#FFD43B', 2.2) + '</g>')
U['white-flag'] = (R(6.4, 4.4, 3, 25, 1.4, '#B9805A') + C(7.9, 4.2, 2.2, '#FFD43B', True, 1.0) +
    P('M9.4 6.4Q14.4 4 18.6 6.4Q22.8 8.8 26.6 6.6L26.6 17.6Q22.8 19.8 18.6 17.4Q14.4 15 9.4 17.4Z', W) + L('M13 11.6Q16 10.4 19 11.8', 1.0, '#E3D9FF'))
U['level-slider'] = (L('M9 5L9 27M16 5L16 27M23 5L23 27', 2.2) + R(5.4, 17, 7.2, 4.6, 1.8, '#FF9DCB') + R(12.4, 8.4, 7.2, 4.6, 1.8, '#FFD43B') + R(19.4, 20.6, 7.2, 4.6, 1.8, '#6FE3C4'))
puff = [(20.4, 15.4, 6.2), (14.4, 17.8, 4.6), (25.6, 18.6, 4), (19, 20.6, 4.4)]
U['dashing-away'] = (''.join(C(x, y, r + SW, INK, False) for x, y, r in puff) + ''.join(C(x, y, r, W, False) for x, y, r in puff) +
    L('M2.6 10.6L10.4 10.6M1.6 15.6L8 15.6M3.2 20.6L8.8 20.6', 1.8) + E(17.6, 13.6, 2, 1.2, '#E3D9FF', False, -20))

json.dump({'kg-' + k: v for k, v in U.items()}, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print(len(U), 'kelime görseli', sum(len(v) for v in U.values()), 'bayt')
