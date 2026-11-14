#!/usr/bin/env python3
"""Builds Basamak.apk from the earlier KELIME WebView wrapper and the current index.html.
Usage: python3 -I build_apk.py <old_extract_dir> <index.html> <icons_dir> <out_unsigned.apk>"""
import os, struct, sys, zipfile, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import respool
src, index, icons, out = sys.argv[1:5]

def rd(p): return open(os.path.join(src, p), 'rb').read()

# manifest: new package and label; the activity name becomes fully qualified because its class keeps the old package
m = rd('AndroidManifest.xml')
m, delta = respool.replace_pool(m, 8, {
    'com.nefata.kelime': 'com.nefata.basamak',
    '.MainActivity': 'com.nefata.kelime.MainActivity',
    'KELİME': 'Basamak',
    '0.4.0': '1.0.0',
})
m = m[:4] + struct.pack('<I', len(m)) + m[8:]
assert respool.read_pool(m, 8)['strings'].count('com.nefata.basamak') == 1

# resources: package name field and theme / icon colours
a = bytearray(rd('resources.arsc'))
pool = respool.read_pool(bytes(a), 12)
off = 12 + pool['size']
assert struct.unpack_from('<H', a, off)[0] == 0x0200
name = 'com.nefata.basamak'.encode('utf-16-le').ljust(256, b'\x00')
a[off + 12: off + 12 + 256] = name
for old, new in ((0xff2f6fed, 0xff5b3df5), (0xfff5f6fa, 0xfff1eeff), (0xff171e29, 0xff1f1a3d), (0xff0e131b, 0xff120f24)):
    ob, nb = struct.pack('<I', old), struct.pack('<I', new)
    assert a.count(ob) == 1, hex(old)
    i = a.index(ob); a[i:i + 4] = nb

files = {
    'AndroidManifest.xml': m,
    'resources.arsc': bytes(a),
    'classes.dex': rd('classes.dex'),
    'res/mipmap-anydpi-v26/ic_launcher.xml': rd('res/mipmap-anydpi-v26/ic_launcher.xml'),
    'assets/www/index.html': open(index, 'rb').read(),
}
for d in ('mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi'):
    for kind in ('ic_launcher', 'ic_launcher_fg'):
        files[f'res/mipmap-{d}-v4/{kind}.png'] = open(os.path.join(icons, f'{kind}-{d}.png'), 'rb').read()

# resources.arsc and PNGs stored uncompressed, 4-byte aligned (required for targetSdk 30+)
order = ['AndroidManifest.xml', 'classes.dex', 'resources.arsc'] + sorted(k for k in files if k.startswith('res/')) + ['assets/www/index.html']
with open(out, 'wb') as fh:
    z = zipfile.ZipFile(fh, 'w')
    for n in order:
        data = files[n]
        stored = n == 'resources.arsc' or n.endswith('.png')
        zi = zipfile.ZipInfo(n, date_time=(1981, 1, 1, 0, 0, 0))
        zi.compress_type = zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED
        if stored:
            pad = (-(fh.tell() + 30 + len(n.encode()))) % 4
            if pad:
                pad += 4 if pad < 4 else 0
                zi.extra = struct.pack('<HH', 0xD935, pad - 4) + b'\x00' * (pad - 4)
        z.writestr(zi, data)
    z.close()
z = zipfile.ZipFile(out)
for zi in z.infolist():
    if zi.compress_type == zipfile.ZIP_STORED:
        start = zi.header_offset + 30 + len(zi.filename.encode()) + len(zi.extra)
        assert start % 4 == 0, (zi.filename, start)
print('unsigned apk written:', out, os.path.getsize(out), 'bytes,', len(order), 'entries')
