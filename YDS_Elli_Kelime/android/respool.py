"""Minimal reader/writer for Android binary XML (AXML) and resources.arsc string pools."""
import struct

def read_pool(buf, off):
    typ, hsz, size = struct.unpack_from('<HHI', buf, off)
    assert typ == 0x0001, hex(typ)
    count, styles, flags, sstart, ystart = struct.unpack_from('<IIIII', buf, off + 8)
    utf8 = bool(flags & 0x100)
    offs = struct.unpack_from('<%dI' % count, buf, off + hsz)
    out = []
    base = off + sstart
    for o in offs:
        p = base + o
        if utf8:
            def ln(p):
                n = buf[p]
                if n & 0x80: return ((n & 0x7f) << 8) | buf[p + 1], p + 2
                return n, p + 1
            _, p = ln(p); bl, p = ln(p)
            out.append(buf[p:p + bl].decode('utf-8'))
        else:
            n = struct.unpack_from('<H', buf, p)[0]; p += 2
            if n & 0x8000: n = ((n & 0x7fff) << 16) | struct.unpack_from('<H', buf, p)[0]; p += 2
            out.append(buf[p:p + 2 * n].decode('utf-16-le'))
    assert styles == 0, 'styled strings not supported'
    return {'strings': out, 'utf8': utf8, 'flags': flags, 'size': size, 'hsz': hsz}

def build_pool(info):
    strs, utf8 = info['strings'], info['utf8']
    data, offs = bytearray(), []
    for s in strs:
        offs.append(len(data))
        if utf8:
            b = s.encode('utf-8')
            def enc(n): return bytes([n]) if n < 0x80 else bytes([0x80 | (n >> 8), n & 0xff])
            data += enc(len(s)) + enc(len(b)) + b + b'\x00'
        else:
            b = s.encode('utf-16-le'); n = len(b) // 2
            data += (struct.pack('<H', n) if n < 0x8000 else struct.pack('<HH', 0x8000 | (n >> 16), n & 0xffff)) + b + b'\x00\x00'
    while len(data) % 4: data += b'\x00'
    hsz = 28
    sstart = hsz + 4 * len(strs)
    size = sstart + len(data)
    head = struct.pack('<HHIIIIII', 0x0001, hsz, size, len(strs), 0, info['flags'], sstart, 0)
    return head + struct.pack('<%dI' % len(strs), *offs) + bytes(data)

def replace_pool(buf, off, mapping):
    info = read_pool(buf, off)
    info['strings'] = [mapping.get(s, s) for s in info['strings']]
    new = build_pool(info)
    return buf[:off] + new + buf[off + info['size']:], len(new) - info['size']
