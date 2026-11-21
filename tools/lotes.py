r"""Traducir por lotes con varios agentes: cortar la plantilla, verificar cada lote y unir.

Es el flujo con el que se hizo el ruso (2026-11-19). Solo biblioteca estándar.

  python lotes.py cortar <plantilla.json> <carpeta> [--lotes 8] [--desde <sr.json>]
      Escribe <carpeta>/chunk_NN.jsonl: una línea por texto a traducir, {"id","en","max","fr","es","de","it"}.
      Con --desde, cada línea trae además la traducción de ese JSON con su código ("sr"): para adaptar
      una traducción a una lengua cercana (el croata sale del serbio).
      Saltea los que son iguales en todos los idiomas (sameInAllLanguages: nombres, siglas, números).
      Corta por tabla (el "tag" del id), sin partir una tabla entre dos lotes si se puede.

  python lotes.py verificar <chunk_NN.jsonl> <out_NN_*.json ...>
      Lo que corre cada agente sobre su lote. ERROR: falta un id, sobra un id, texto vacío, fichas
      ({c:..} {i:..} …) o formatos % distintos, llave suelta, letras prohibidas (; griego, ·, politónico). AVISO: saltos de línea distintos, línea > max.

  python lotes.py unir <plantilla.json> <carpeta> <salida.json> --language el --label Ελληνικά [--title Γλώσσα]
      Junta todos los <carpeta>/out_*.json en la plantilla (status "draft") y unifica los repetidos: un mismo
      texto inglés con las mismas traducciones oficiales lleva una sola traducción (la que pasa la verificación,
      entra en max y es la más usada). Lista los que unificó para revisarlos.

Después: python pes6tr.py check <salida.json>, python pes6tr.py build … y, para guardarlo en git,
python pes6tr.py strip <salida.json> -o languages/<código>/<código>.json (ver CONTRIBUTING.md).
La plantilla y todo lo que escriben cortar y unir llevan textos del juego: trabajar en work/.
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import pathlib
import re
import sys

TOKEN = re.compile(r"\{\{|\}\}|\{([cwkljnpui]):([0-9A-Za-z]+)\}")
CTRL = re.compile(r"\{[cwkljnpui]:[0-9A-Za-z]+\}")
PRINTF = re.compile(r"%(?:%|[-+ 0#]*\d*(?:\.\d+)?[dsfuxXc])")
REFS = ("fr", "es", "de", "it")
# Letras que la fuente no tiene o que el glosario prohíbe: «;» griego, «·», keraia y griego politónico.
FORBIDDEN = re.compile(r"[\u037e\u0387\u00b7\u0374\u0375\u1f00-\u1fff]")


def tokens(t: str) -> list[str]:
    return sorted(m.group(0) for m in TOKEN.finditer(t) if m.group(1))


def loose_brace(t: str) -> bool:
    rest = re.sub(r"\{\{|\}\}|\{[cwkljnpui]:[0-9A-Za-z]+\}", "", t)
    return "{" in rest or "}" in rest


def visible_max(t: str) -> int:
    return max(len(line) for line in CTRL.sub("", t).replace("{{", "{").replace("}}", "}").split("\n"))


def problems(en: str, tr: str, limit: int) -> tuple[list[str], list[str]]:
    err, warn = [], []
    if not tr.strip() and en.strip():
        return ["vacío"], []
    if tokens(en) != tokens(tr):
        err.append(f"fichas {tokens(en)} -> {tokens(tr)}")
    a, b = sorted(PRINTF.findall(en)), sorted(PRINTF.findall(tr))
    if a != b:
        err.append(f"formatos % {a} -> {b} (un % literal va como %%)")
    if loose_brace(tr):
        err.append("llave suelta (una llave literal va como {{ o }})")
    bad = sorted(set(FORBIDDEN.findall(tr)) - set(FORBIDDEN.findall(en)))
    if bad:
        err.append(f"letras prohibidas {[f'U+{ord(c):04X}' for c in bad]} (la pregunta va con ';' ASCII, sin '·' ni politónico)")
    # inglés TODO en mayúsculas: la traducción también (en turco, i → İ; en griego, sin tonos).
    # Solo con una palabra de 4 letras o más: las siglas (BGM, CK(R)) se traducen con palabras normales.
    plain_en, plain_tr = (PRINTF.sub("", CTRL.sub("", s)) for s in (en, tr))
    letters_en = [c for c in plain_en if c.isalpha()]
    if (letters_en and all(c.isupper() for c in letters_en)
            and re.search(r"[A-Za-z]{4}", plain_en)):
        low = sorted({c for c in plain_tr if c.islower()})
        if low:
            err.append(f"el inglés está en mayúsculas y la traducción tiene minúsculas {low}")
    if en.count("\n") != tr.count("\n"):
        warn.append(f"saltos de línea {en.count(chr(10))} -> {tr.count(chr(10))}")
    if visible_max(tr) > limit:
        warn.append(f"línea de {visible_max(tr)} > max {limit}")
    return err, warn


def load_template(path: str) -> dict:
    return json.load(open(path, encoding="utf-8"))


def cmd_cortar(a):
    doc = load_template(a.plantilla)
    items = [t for t in doc["texts"] if not t.get("sameInAllLanguages")]
    by_tag = collections.OrderedDict()
    for t in items:
        by_tag.setdefault(t["id"].split(":")[0], []).append(t)
    target = -(-len(items) // a.lotes)
    chunks, cur = [], []
    for tag_items in by_tag.values():
        for t in tag_items:            # una tabla grande se parte; una chica no se separa del resto de su tabla
            cur.append(t)
            if len(cur) >= target and len(chunks) < a.lotes - 1 and t is tag_items[-1]:
                chunks.append(cur)
                cur = []
        if len(cur) >= target * 1.25 and len(chunks) < a.lotes - 1:
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    # --desde: una traducción ya hecha que la tanda adapta (el croata sale del serbio)
    base, base_code = {}, None
    if a.desde:
        base_doc = json.load(open(a.desde, encoding="utf-8"))
        base_code = base_doc["language"]
        base = {t["id"]: t["translatedText"] for t in base_doc["texts"] if t.get("translatedText")}
    out = pathlib.Path(a.carpeta)
    out.mkdir(parents=True, exist_ok=True)
    for n, chunk in enumerate(chunks, 1):
        with open(out / f"chunk_{n:02d}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for t in chunk:
                line = {"id": t["id"], "en": t["defaultText"], "max": t.get("maxLength", 0)}
                if base_code:
                    if t["id"] not in base:
                        sys.exit(f"{t['id']}: no está traducido en {a.desde}")
                    line[base_code] = base[t["id"]]
                for code in REFS:
                    if code in t.get("reference", {}):
                        line[code] = t["reference"][code]
                f.write(json.dumps(line, ensure_ascii=False) + "\n")
        print(f"chunk_{n:02d}.jsonl: {len(chunk)} textos")
    print(f"{len(items)} textos para traducir en {len(chunks)} lotes; {len(doc['texts']) - len(items)} iguales en todos los idiomas quedan afuera")


def cmd_verificar(a):
    src = [json.loads(line) for line in open(a.lote, encoding="utf-8")]
    out = {}
    for p in a.salidas:
        out.update(json.load(open(p, encoding="utf-8")))
    err, warn = [], []
    for s in src:
        tr = out.get(s["id"])
        if tr is None:
            err.append(f"{s['id']}: falta")
            continue
        e, w = problems(s["en"], tr, s["max"])
        err += [f"{s['id']}: {x}" for x in e]
        warn += [f"{s['id']}: {x}" for x in w]
    extra = set(out) - {s["id"] for s in src}
    if extra:
        err.append(f"ids que no son del lote: {sorted(extra)[:5]}")
    for x in err:
        print("ERROR", x)
    for x in warn:
        print("aviso", x)
    print(f"{len(src)} textos, {len(out)} traducidos, {len(err)} errores, {len(warn)} avisos")
    sys.exit(1 if err else 0)


def cmd_unir(a):
    doc = load_template(a.plantilla)
    tr = {}
    for p in sorted(glob.glob(str(pathlib.Path(a.carpeta) / "out_*.json"))):
        tr.update(json.load(open(p, encoding="utf-8")))
    texts = {t["id"]: t for t in doc["texts"]}
    groups = collections.defaultdict(list)
    for k, t in texts.items():
        if k in tr:
            key = (t["defaultText"], tuple(sorted(t.get("reference", {}).items())))
            groups[key].append(k)
    unified = 0
    for (en, _), ids in groups.items():
        options = collections.Counter(tr[k] for k in ids)
        if len(options) < 2:
            continue
        limit = min(texts[k].get("maxLength", 999) for k in ids)
        good = [o for o, _ in options.most_common() if not problems(en, o, limit)[0] and visible_max(o) <= limit]
        best = good[0] if good else options.most_common(1)[0][0]
        print(f"unificado ({len(ids)}): {en!r} -> {best!r}  (había: {', '.join(repr(o) for o in options)})")
        for k in ids:
            tr[k] = best
        unified += 1
    n = 0
    for k, t in texts.items():
        if k in tr:
            t["translatedText"] = tr[k]
            t["status"] = "draft"
            n += 1
    doc["language"] = a.language
    doc["language_label"] = a.label
    if a.title:
        doc["language_title"] = a.title
    pathlib.Path(a.salida).write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{n} traducciones de {len(texts)} textos; {unified} grupos repetidos unificados -> {a.salida}")


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("cortar")
    p.add_argument("plantilla")
    p.add_argument("carpeta")
    p.add_argument("--lotes", type=int, default=8)
    p.add_argument("--desde", help="traducción ya hecha (JSON de pes6tr) que se agrega a cada línea para adaptarla")
    p.set_defaults(func=cmd_cortar)
    p = sub.add_parser("verificar")
    p.add_argument("lote")
    p.add_argument("salidas", nargs="+")
    p.set_defaults(func=cmd_verificar)
    p = sub.add_parser("unir")
    p.add_argument("plantilla")
    p.add_argument("carpeta")
    p.add_argument("salida")
    p.add_argument("--language", required=True)
    p.add_argument("--label", required=True)
    p.add_argument("--title", default="")
    p.set_defaults(func=cmd_unir)
    a = ap.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
