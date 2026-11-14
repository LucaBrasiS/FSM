#!/usr/bin/env python3
"""Tek dosyalık uygulamayı üretir: src/app.src.html + data/ -> index.html

Kullanım:  python3 src/build.py [--kitap KLASÖR] [--eksik-olabilir]

Şablondaki /*@@ART@@*/ ve /*@@GRAM@@*/ yer tutucuları veriyle, /*@@ARTLICENSE@@*/ lisans notuyla değiştirilir.
Gramer verisi iki kaynaktan birleşir: data/kitap/kNN.json (kitabın içindekiler sırasındaki 34 ünite) ve
data/gramer.json (YDS düzeyi 18 konu).
"""
import argparse, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOOK_UNITS = 34


def js(obj):
    """JSON'u <script> içine güvenle gömülecek biçimde yazar."""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def check_rows(uid, rows, reading=False):
    assert len(rows) == 30, (uid, len(rows))
    for row in rows:
        q, opts, a, why, kind = row[:5]
        assert len(opts) == 5 and len(set(opts)) == 5 and 0 <= a < 5 and why.strip(), (uid, q)
        assert reading or "----" in q, (uid, q)


def load_grammar(kitap_dir, allow_missing):
    topics, qs, pas = [], {}, {}
    for no in range(1, BOOK_UNITS + 1):
        path = kitap_dir / f"k{no:02d}.json"
        if not path.exists():
            if allow_missing:
                continue
            sys.exit(f"eksik ünite dosyası: {path}")
        u = json.loads(path.read_text(encoding="utf-8"))
        assert u["no"] == no and u["id"] == f"k{no:02d}", path
        reading = "passages" in u
        levels = [q["lvl"] for q in u["qs"]]
        assert levels == sorted(levels), (path, "sorular zorluk sırasında olmalı")
        rows = [[q["q"], q["o"], q["a"], q["e"], q["tip"]] + ([q["p"]] if reading else []) for q in u["qs"]]
        check_rows(u["id"], rows, reading)
        topics.append({"id": u["id"], "grp": "k", "no": no, "en": u["en"], "ad": u["tr"], "kisa": u["kisa"], "not": u["not"]})
        qs[u["id"]] = rows
        if reading:
            assert all(0 <= r[5] < len(u["passages"]) for r in rows), path
            pas[u["id"]] = u["passages"]
    yds = json.loads((ROOT / "data" / "gramer.json").read_text(encoding="utf-8"))
    for t in yds["t"]:
        check_rows(t["id"], yds["q"][t["id"]])
        topics.append({"id": t["id"], "grp": "y", "ad": t["ad"], "kisa": t["kisa"], "not": t["not"]})
        qs[t["id"]] = yds["q"][t["id"]]
    return {"t": topics, "q": qs, "pas": pas}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kitap", default=str(ROOT / "data" / "kitap"))
    ap.add_argument("--eksik-olabilir", action="store_true", help="eksik ünite dosyalarını atla (geliştirme için)")
    args = ap.parse_args()

    src = (ROOT / "src" / "app.src.html").read_text(encoding="utf-8")
    art = json.loads((ROOT / "data" / "art.json").read_text(encoding="utf-8"))
    lic = (ROOT / "assets" / "FLUENT-EMOJI-LICENSE.txt").read_text(encoding="utf-8").strip()
    gram = load_grammar(pathlib.Path(args.kitap), args.eksik_olabilir)

    for group in ("ui", "words"):
        for key, name in art[group].items():
            assert name in art["icons"], (group, key, name)
    for t in gram["t"]:
        assert "u-" + t["id"] in art["ui"], ("ünite görseli yok", t["id"])

    assert "*/" not in lic
    notice = "/* Fluent Emoji çizimleri:\n" + "\n".join("   " + l.strip() for l in lic.splitlines()) + "\n*/"
    out = src
    for mark, value in (
        ("/*@@ARTLICENSE@@*/", notice),
        ("/*@@ART@@*/{icons:{},ui:{},words:{}}", js(art)),
        ("/*@@GRAM@@*/{t:[],q:{},pas:{}}", js(gram)),
    ):
        assert out.count(mark) == 1, mark
        out = out.replace(mark, value)
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    n_book = sum(1 for t in gram["t"] if t["grp"] == "k")
    print(f"index.html: {len(out.encode('utf-8')):,} bayt | {len(art['icons'])} çizim | "
          f"{n_book} kitap ünitesi + {len(gram['t']) - n_book} YDS konusu | {sum(len(v) for v in gram['q'].values())} gramer sorusu")


if __name__ == "__main__":
    sys.exit(main())
