#!/usr/bin/env python3
"""Tek dosyalık uygulamayı üretir: src/app.src.html + data/ -> index.html

Kullanım:  python3 src/build.py [--kitap KLASÖR] [--eksik-olabilir]

Şablondaki /*@@ART@@*/, /*@@GRAM@@*/, /*@@BAG@@*/, /*@@WORDS@@*/ ve /*@@VERBS@@*/ yer tutucuları veriyle, /*@@ARTLICENSE@@*/ lisans notuyla değiştirilir.
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


def load_words(path):
    """data/kelimeler.txt: kelime|tür|Türkçe|eş anlamlılar|cümle (/ parçalar, [kelime])|çeviri|görseller -> ilk altı alan."""
    out, seen = [], set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        p = line.split("|")
        assert len(p) == 7 and p[0] not in seen, line
        assert len(p[4].split(" / ")) == 4 and "[" + p[0] + "]" in p[4].lower(), line
        seen.add(p[0])
        out.append("|".join(p[:6]))
    return "\n".join(out)


def load_verbs(path):
    """data/fiiller.txt: fiil|düzey (A1, A2, B1, B2)|Türkçe|aynı soruda şık olmaması gereken fiiller (isteğe bağlı)."""
    rows, seen = [], {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        p = line.split("|")
        assert len(p) in (3, 4) and p[1] in ("A1", "A2", "B1", "B2") and p[2].strip(), line
        assert p[0] == p[0].strip().lower() and p[0] not in seen, line
        avoid = [x.strip() for x in p[3].split(",")] if len(p) == 4 else []
        seen[p[0]] = {"w": p[0], "lv": p[1], "tok": {t.strip() for t in p[2].split(",")}, "av": avoid}
        rows.append("|".join(p))
    for v in seen.values():
        assert all(a in seen for a in v["av"]), ("bilinmeyen fiil", v["w"], v["av"])
        free = [x for x in seen.values() if x["lv"] == v["lv"] and x is not v
                and not (x["tok"] & v["tok"]) and x["w"] not in v["av"] and v["w"] not in x["av"]]
        assert len(free) >= 12, ("yanlış şık için yeterli fiil yok", v["w"], len(free))
    return "\n".join(rows), len(rows)


def load_bag(d, allow_missing):
    """Bağlaç atölyesi: list.json (gruplar, yapılar) + kartlar.json + sec/iliski/anlam.json -> {groups, yapi, qs}."""
    if not (d / "list.json").exists():
        if allow_missing:
            return {"groups": [], "yapi": {}, "qs": {}}
        sys.exit(f"eksik: {d / 'list.json'}")
    lst = json.loads((d / "list.json").read_text(encoding="utf-8"))
    need = ["kartlar.json", "sec.json", "iliski.json", "anlam.json"]
    if not all((d / n).exists() for n in need):
        if allow_missing:
            return {"groups": [], "yapi": {}, "qs": {}}
        sys.exit(f"eksik bağlaç dosyası: {[n for n in need if not (d / n).exists()]}")
    cards = {c["w"]: c for c in json.loads((d / "kartlar.json").read_text(encoding="utf-8"))}
    groups = []
    for g in lst["groups"]:
        items = []
        for w, y in g["items"]:
            c = cards[w]
            items.append({"w": w, "y": y, "tr": c["tr"], "ex": c["ex"], "ext": c["ext"], "not": c["not"]})
        groups.append({"id": g["id"], "ad": g["ad"], "items": items})
    qs = {}
    for k in ("sec", "iliski", "anlam"):
        rows = json.loads((d / f"{k}.json").read_text(encoding="utf-8"))
        assert len(rows) == 30 and [q["lvl"] for q in rows] == sorted(q["lvl"] for q in rows), k
        qs[k] = [[q["q"], q["o"], q["a"], q["e"], k, q.get("g") or q.get("w")] for q in rows]
        for r in qs[k]:
            assert len(r[1]) == 5 and len(set(r[1])) == 5 and 0 <= r[2] < 5, (k, r[0])
    return {"groups": groups, "yapi": lst["yapi"], "qs": qs}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kitap", default=str(ROOT / "data" / "kitap"))
    ap.add_argument("--eksik-olabilir", action="store_true", help="eksik ünite dosyalarını atla (geliştirme için)")
    args = ap.parse_args()

    src = (ROOT / "src" / "app.src.html").read_text(encoding="utf-8")
    art = json.loads((ROOT / "data" / "art.json").read_text(encoding="utf-8"))
    lic = (ROOT / "assets" / "FLUENT-EMOJI-LICENSE.txt").read_text(encoding="utf-8").strip()
    gram = load_grammar(pathlib.Path(args.kitap), args.eksik_olabilir)
    bag = load_bag(ROOT / "data" / "baglac", args.eksik_olabilir)
    words = load_words(ROOT / "data" / "kelimeler.txt")
    verbs, n_verbs = load_verbs(ROOT / "data" / "fiiller.txt")

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
        ("/*@@BAG@@*/{groups:[],yapi:{},qs:{}}", js(bag)),
        ("/*@@WORDS@@*/''", js(words)),
        ("/*@@VERBS@@*/''", js(verbs)),
    ):
        assert out.count(mark) == 1, mark
        out = out.replace(mark, value)
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    n_book = sum(1 for t in gram["t"] if t["grp"] == "k")
    print(f"index.html: {len(out.encode('utf-8')):,} bayt | {len(art['icons'])} çizim | "
          f"{n_book} kitap ünitesi + {len(gram['t']) - n_book} YDS konusu | {sum(len(v) for v in gram['q'].values())} gramer sorusu | "
          f"{n_verbs} fiil")


if __name__ == "__main__":
    sys.exit(main())
