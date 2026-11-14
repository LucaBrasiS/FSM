#!/usr/bin/env python3
"""APK Signature Scheme v2 signer (RSA PKCS#1 v1.5 + SHA-256). Usage: v2sign.py <key.p12> <password> <in.apk> <out.apk>"""
import hashlib, struct, sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import pkcs12

p12, pw, src, dst = sys.argv[1:5]
key, cert, _ = pkcs12.load_key_and_certificates(open(p12, 'rb').read(), pw.encode())
data = open(src, 'rb').read()

eocd = data.rfind(b'PK\x05\x06')
assert eocd >= 0 and len(data) - eocd == 22, 'EOCD with comment not supported'
cd_size, cd_off = struct.unpack_from('<II', data, eocd + 12)
assert cd_off + cd_size == eocd
entries, cdir, end = data[:cd_off], data[cd_off:eocd], data[eocd:]

def lp(b): return struct.pack('<I', len(b)) + b
def chunked_digest(parts):
    digests = []
    for part in parts:
        for i in range(0, len(part), 1 << 20):
            c = part[i:i + (1 << 20)]
            digests.append(hashlib.sha256(b'\xa5' + struct.pack('<I', len(c)) + c).digest())
    return hashlib.sha256(b'\x5a' + struct.pack('<I', len(digests)) + b''.join(digests)).digest()

ALG = 0x0103
digest = chunked_digest([entries, cdir, end])          # EOCD's CD offset already equals the signing block's offset
cert_der = cert.public_bytes(serialization.Encoding.DER)
signed = lp(lp(struct.pack('<I', ALG) + lp(digest))) + lp(lp(cert_der)) + lp(b'')
sig = key.sign(signed, padding.PKCS1v15(), hashes.SHA256())
pub = key.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
signer = lp(signed) + lp(lp(struct.pack('<I', ALG) + lp(sig))) + lp(pub)
v2 = lp(lp(signer))
pair = struct.pack('<QI', 4 + len(v2), 0x7109871a) + v2
size = len(pair) + 8 + 16
block = struct.pack('<Q', size) + pair + struct.pack('<Q', size) + b'APK Sig Block 42'
new_end = end[:16] + struct.pack('<I', cd_off + len(block)) + end[20:]
open(dst, 'wb').write(entries + block + cdir + new_end)
print('signed (v2):', dst, len(entries + block + cdir + new_end), 'bytes')
