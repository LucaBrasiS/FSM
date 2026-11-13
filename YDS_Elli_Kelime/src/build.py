#!/usr/bin/env python3
"""Tek dosyalık uygulamayı üretir: src/app.src.html + data/*.json -> index.html

Kullanım:  python3 src/build.py
Şablondaki /*@@ART@@*/ ve /*@@GRAM@@*/ yer tutucuları veriyle, /*@@ARTLICENSE@@*/ lisans notuyla değiştirilir.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def js(obj):
    """JSON'u <script> içine güvenle gömülecek biçimde yazar."""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def main():
    src = (ROOT / "src" / "app.src.html").read_text(encoding="utf-8")
    art = json.loads((ROOT / "data" / "art.json").read_text(encoding="utf-8"))
    gram = json.loads((ROOT / "data" / "gramer.json").read_text(encoding="utf-8"))
    lic = (ROOT / "assets" / "FLUENT-EMOJI-LICENSE.txt").read_text(encoding="utf-8").strip()

    for topic in gram["t"]:
        rows = gram["q"].get(topic["id"], [])
        assert len(rows) == 30, (topic["id"], len(rows))
        for q, opts, a, why, kind in rows:
            assert "----" in q and len(opts) == 5 and len(set(opts)) == 5 and 0 <= a < 5 and why.strip(), q
    for group in ("ui", "words"):
        for key, name in art[group].items():
            assert name in art["icons"], (group, key, name)

    notice = "/* Fluent Emoji çizimleri:\n" + "\n".join("   " + l.strip() for l in lic.splitlines()) + "\n*/"
    assert "*/" not in lic
    out = src
    for mark, value in (
        ("/*@@ARTLICENSE@@*/", notice),
        ("/*@@ART@@*/{icons:{},ui:{},words:{}}", js(art)),
        ("/*@@GRAM@@*/{t:[],q:{}}", js(gram)),
    ):
        assert out.count(mark) == 1, mark
        out = out.replace(mark, value)
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print(f"index.html: {len(out.encode('utf-8')):,} bayt | {len(art['icons'])} çizim | {sum(len(v) for v in gram['q'].values())} gramer sorusu")


if __name__ == "__main__":
    sys.exit(main())
