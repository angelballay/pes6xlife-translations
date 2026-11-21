r"""Herramienta de traducciones de PES6: X_text.afs -> JSON -> X_text.afs.

Uso:
  python pes6tr.py export <dat | X_text.afs> -o work/plantilla.json
         [--base e] [--language tr] [--label Türkçe] [--output-file e_text.afs]
         [--install afs2fs|afs] [--no-references]

  - <dat>: carpeta con los X_text.afs del juego. Se usa como base el de --base
    (inglés por defecto) y los demás que haya como referencia.
  - <X_text.afs>: un archivo suelto. Las referencias se buscan en su misma carpeta.

  python pes6tr.py merge work/plantilla.json languages/tr/tr.json -o work/tr.json
  python pes6tr.py check work/tr.json
  python pes6tr.py build work/tr.json --source <dat>/e_text.afs --install afs -o work/tr_text.afs
         [--output-file f_text.afs] [--fallback default|source] [--skip-invalid]
  python pes6tr.py strip work/tr.json -o languages/tr/tr.json

Dos formas del JSON:
  - completo (pes6-text-translation/1): lo que escribe export, con los textos del juego
    (el inglés y las referencias). Es el que usan check, build, lotes.py y letras.py.
    Lleva textos de Konami: nunca va en git (se trabaja en work/, que está ignorada).
  - liviano (pes6-text-translation-light/1): solo las traducciones (id, translatedText,
    status) y la cabecera del idioma. Es el que está en git, en languages/<código>/.
  merge arma el completo desde la plantilla de tu propio juego y el liviano; strip hace lo
  contrario.

El formato del JSON y el porqué de cada campo están en docs/DISENO.md; el flujo, en
CONTRIBUTING.md. Solo biblioteca estándar. Los AFS se abren solo para leer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import struct
import sys
import zlib

SCHEMA = "pes6-text-translation/1"
SCHEMA_LIGHT = "pes6-text-translation-light/1"   # solo traducciones: lo que va en git
# Cabecera del liviano: lo que es del idioma (no del juego) y la base que lo ata a un e_text.afs.
LIGHT_HEADER = ("file_name_output", "language", "language_label", "language_title", "install")
LIGHT_BASE = ("file", "lang", "sha256", "records", "texts")
LIGHT_TEXT = ("id", "translatedText", "status")
STATUSES = ("todo", "draft", "done")
LANGS = "efgisp"                      # los seis lugares de idioma del juego
# Menú de idiomas (tabla 52): nombre del lugar y "Language" en su idioma. El polaco no tiene par.
SLOT_TEXTS = {"e_text.afs": ("52:64", "52:71"), "f_text.afs": ("52:65", "52:72"),
              "g_text.afs": ("52:66", "52:73"), "i_text.afs": ("52:67", "52:74"),
              "s_text.afs": ("52:68", "52:75")}
LANG_CODE = {"e": "en", "f": "fr", "g": "de", "i": "it", "s": "es", "p": "pl"}

# ---------------------------------------------------------------- AFS y tablas

ENTRY_HDR = 0x20
FLAGS_ZLIB = 0x00010600
BLOCK_HDR = 0x20
REC = struct.Struct("<HHHHI")         # id, x, bytes (con el \0), chars, off (desde la tabla)


class FormatError(Exception):
    pass


def read_afs(path):
    data = pathlib.Path(path).read_bytes()
    if data[:4] != b"AFS\0":
        raise FormatError(f"{path}: no es un AFS")
    (count,) = struct.unpack_from("<I", data, 4)
    items = [struct.unpack_from("<II", data, 8 + 8 * i) for i in range(count)]
    return data, items


def parse_text_entry(body):
    """Bloques de una entrada de texto descomprimida, o None si no tiene esa forma."""
    n = len(body)
    if n < 16:
        return None
    nblk, tbl_off = struct.unpack_from("<II", body, 0)
    if tbl_off != 8 or not 0 < nblk < 4096 or 8 + 4 * nblk > n:
        return None
    offs = list(struct.unpack_from(f"<{nblk}I", body, 8))
    blocks = []
    for start, end in zip(offs, offs[1:] + [n]):
        if not (8 + 4 * nblk <= start and start + BLOCK_HDR + 8 <= end <= n):
            return None
        tbl = start + BLOCK_HDR
        cnt, tag = struct.unpack_from("<II", body, tbl)
        if cnt * REC.size + 8 > end - tbl:
            return None
        recs = []
        for k in range(cnt):
            rid, _x, nbytes, _chars, off = REC.unpack_from(body, tbl + 8 + k * REC.size)
            s, e = tbl + off, tbl + off + nbytes
            if nbytes == 0 or e > end or body[e - 1] != 0 or b"\0" in body[s:e - 1]:
                return None
            try:
                recs.append((rid, body[s:e - 1].decode("utf-8")))
            except UnicodeDecodeError:
                return None
        blocks.append((tag, recs))
    return blocks


def read_texts(path):
    """Lee un X_text.afs. Devuelve (sha256, cantidad de registros, {"tag:id": texto})
    en el orden del archivo. Falla si una misma clave tiene dos textos distintos."""
    data, items = read_afs(path)
    texts, records = {}, 0
    for off, size in items:
        raw = data[off:off + size]
        if len(raw) < ENTRY_HDR:
            continue
        flags, a, b = struct.unpack_from("<III", raw, 0)
        if flags != FLAGS_ZLIB:
            continue
        try:
            body = zlib.decompress(raw[ENTRY_HDR:ENTRY_HDR + a])
        except zlib.error:
            continue
        if len(body) != b:
            continue
        blocks = parse_text_entry(body)
        if blocks is None:
            continue
        for tag, recs in blocks:
            for rid, text in recs:
                records += 1
                key = f"{tag}:{rid}"
                if texts.setdefault(key, text) != text:
                    raise FormatError(f"{path}: la clave {key} tiene dos textos distintos")
    return hashlib.sha256(data).hexdigest(), records, texts


# ---------------------------------------------------------------- fichas

# \x11 + letra + argumento -> {letra:argumento}. Gramática medida en los 6 idiomas.
CONTROL = re.compile(r"\x11(?:(c)([0-9A-Fa-f]{8})|(w)([0-9A-Fa-f]{2})|([kljnp])([a-z]))")
TOKEN = re.compile(r"\{\{|\}\}|\{([cwkljnpui]):([0-9A-Za-z]+)\}")


def is_icon(ch):
    """Íconos de botones: caracteres de uso privado que dibuja la fuente del juego."""
    return 0xE000 <= ord(ch) <= 0xF8FF


def encode(text):
    """Texto del juego -> texto con fichas legibles (ver DISENO.md, sección 3)."""
    out, i = [], 0
    while i < len(text):
        m = CONTROL.match(text, i)
        if m:
            letter = m.group(1) or m.group(3) or m.group(5)
            arg = m.group(2) or m.group(4) or m.group(6)
            out.append(f"{{{letter}:{arg}}}")
            i = m.end()
            continue
        ch = text[i]
        if ch == "{":
            out.append("{{")
        elif ch == "}":
            out.append("}}")
        elif is_icon(ch):
            out.append(f"{{i:{ord(ch):04x}}}")
        elif ch != "\n" and (ord(ch) < 0x20 or 0x7F <= ord(ch) < 0xA0):
            out.append(f"{{u:{ord(ch):04x}}}")
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def decode(text):
    """Inversa de encode. Una llave que no forma ficha es un error."""
    out, i = [], 0
    while i < len(text):
        ch = text[i]
        if ch in "{}":
            m = TOKEN.match(text, i)
            if not m:
                raise FormatError(f"llave suelta en la posición {i}: {text!r}")
            tok = m.group(0)
            if tok == "{{":
                out.append("{")
            elif tok == "}}":
                out.append("}")
            elif m.group(1) in "ui":
                out.append(chr(int(m.group(2), 16)))
            else:
                out.append("\x11" + m.group(1) + m.group(2))
            i = m.end()
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def visible_max_line(text):
    """Largo de la línea visible más larga (sin códigos de control)."""
    plain = CONTROL.sub("", text)
    return max(len(line) for line in plain.split("\n"))


# ---------------------------------------------------------------- export

def find_afs(folder, lang):
    p = pathlib.Path(folder) / f"{lang}_text.afs"
    return p if p.is_file() else None


def cmd_export(args):
    src = pathlib.Path(args.source)
    if src.is_dir():
        base_path = find_afs(src, args.base)
        if base_path is None:
            sys.exit(f"no está {args.base}_text.afs en {src}")
        folder = src
    else:
        base_path, folder = src, src.parent
    base_lang = base_path.name[0] if base_path.name[1:] == "_text.afs" else args.base

    sha, records, base = read_texts(base_path)

    refs = {}
    if not args.no_references:
        for lang in LANGS:
            p = find_afs(folder, lang)
            if lang == base_lang or p is None:
                continue
            _, _, texts = read_texts(p)
            if set(texts) != set(base):
                sys.exit(f"{p.name}: sus claves no coinciden con las de {base_path.name}")
            refs[LANG_CODE[lang]] = texts

    entries = []
    for key, text in base.items():
        if not text:
            continue                          # los vacíos quedan vacíos al armar
        enc = encode(text)
        if decode(enc) != text:               # la conversión tiene que ser exacta
            sys.exit(f"{key}: la ficha no vuelve idéntica: {text!r}")
        item = {"id": key, "defaultText": enc, "translatedText": "", "status": "todo"}
        all_versions = [text] + [r[key] for r in refs.values()]
        item["maxLength"] = max(visible_max_line(t) for t in all_versions)
        if refs and all(t == text for t in all_versions):
            item["sameInAllLanguages"] = True
        elif refs:
            ref = {}
            for code, texts in refs.items():
                e = encode(texts[key])
                if decode(e) != texts[key]:
                    sys.exit(f"{key} ({code}): la ficha no vuelve idéntica")
                ref[code] = e
            item["reference"] = ref
        entries.append(item)

    doc = {
        "schema": SCHEMA,
        "format": "afs",
        "file_name_output": args.output_file or base_path.name,
        "language": args.language,
        "language_label": args.label,
        "install": args.install,
        "base": {"file": base_path.name, "lang": base_lang, "sha256": sha,
                 "records": records, "texts": len(entries)},
        "texts": entries,
    }
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    same = sum(1 for e in entries if e.get("sameInAllLanguages"))
    print(f"{base_path.name}: {records} registros, {len(base)} claves, {len(entries)} textos "
          f"({same} iguales en todos los idiomas), referencias: {', '.join(refs) or 'ninguna'}")
    print(f"-> {out}")


# ---------------------------------------------------------------- armado

AFS_ALIGN = 0x800
FIRST_ENTRY = 0x1000                  # el AFS reserva hasta acá para la tabla de entradas
PRINTF = re.compile(r"%(?:%|[-+ 0#]*\d*(?:\.\d+)?[dsfuxXc])")


def align(n, a):
    return (n + a - 1) & ~(a - 1)


def load_text_entries(data, items):
    """{índice: (bloques, cuerpo)} de las entradas de texto. Cada bloque es
    (tag, [(id, x, chars, texto)]): todo lo necesario para volver a armarlo."""
    found = {}
    for idx, (off, size) in enumerate(items):
        raw = data[off:off + size]
        if len(raw) < ENTRY_HDR:
            continue
        flags, a, b = struct.unpack_from("<III", raw, 0)
        if flags != FLAGS_ZLIB:
            continue
        try:
            body = zlib.decompress(raw[ENTRY_HDR:ENTRY_HDR + a])
        except zlib.error:
            continue
        if len(body) != b or parse_text_entry(body) is None:
            continue
        nblk = struct.unpack_from("<I", body, 0)[0]
        offs = struct.unpack_from(f"<{nblk}I", body, 8)
        blocks = []
        for start in offs:
            tbl = start + BLOCK_HDR
            cnt, tag = struct.unpack_from("<II", body, tbl)
            recs = []
            for k in range(cnt):
                rid, x, nbytes, chars, roff = REC.unpack_from(body, tbl + 8 + k * REC.size)
                text = body[tbl + roff:tbl + roff + nbytes - 1].decode("utf-8")
                recs.append((rid, x, chars, text))
            blocks.append((tag, recs))
        found[idx] = (blocks, body)
    return found


def serialize_entry(blocks):
    """Cuerpo descomprimido de una entrada de texto, con el formato medido en los
    6 idiomas (DISENO.md): bloques alineados a 16, cabecera {0x400, L, L}, tabla,
    cadenas seguidas en el orden de los registros y relleno con ceros."""
    nblk = len(blocks)
    # {nblk, 8, offs[nblk], 8}, alineado a 16 (el 8 final está en los 174 originales)
    out = bytearray(align(8 + 4 * nblk + 4, 16))
    struct.pack_into("<II", out, 0, nblk, 8)
    struct.pack_into("<I", out, 8 + 4 * nblk, 8)
    for k, (tag, recs) in enumerate(blocks):
        start = len(out)
        struct.pack_into("<I", out, 8 + 4 * k, start)
        table = bytearray(struct.pack("<II", len(recs), tag))
        strings = bytearray()
        pos = 8 + REC.size * len(recs)
        for rid, x, chars, text in recs:
            enc = text.encode("utf-8") + b"\0"
            table += REC.pack(rid, x, len(enc), chars, pos + len(strings))
            strings += enc
        used = len(table) + len(strings)
        out += struct.pack("<IIII", 0x400, used, used, 0) + bytes(BLOCK_HDR - 16)
        out += table + strings
        out += bytes(align(len(out), 16) - len(out))
    return bytes(out)


def pack_entry(body):
    comp = zlib.compress(body, 9)
    return struct.pack("<III", FLAGS_ZLIB, len(comp), len(body)) + bytes(ENTRY_HDR - 12) + comp


def check_translation(default, translated):
    """Errores (no se puede armar) y avisos de una traducción frente al inglés."""
    errors, warnings = [], []
    try:
        decode(translated)
    except FormatError as e:
        return [str(e)], []
    tok = lambda t: sorted(m.group(0) for m in TOKEN.finditer(t) if m.group(1) and m.group(1) != "i")
    if tok(default) != tok(translated):
        errors.append(f"fichas distintas: {tok(default)} -> {tok(translated)}")
    # Íconos de botones: caracteres de uso privado (U+E000…F8FF) que dibuja la fuente.
    # Se comparan ya decodificados: da igual si vienen como {i:e087} o como el carácter.
    icons = lambda t: sorted(f"{{i:{ord(c):04x}}}" for c in decode(t) if is_icon(c))
    if icons(default) != icons(translated):
        errors.append(f"íconos de botones distintos: {icons(default)} -> {icons(translated)}")
    if sorted(PRINTF.findall(default)) != sorted(PRINTF.findall(translated)):
        errors.append(f"formatos % distintos: {sorted(PRINTF.findall(default))} -> "
                      f"{sorted(PRINTF.findall(translated))} (un % suelto se escribe %%)")
    if default.count("\n") != translated.count("\n"):
        warnings.append(f"saltos de línea: {default.count(chr(10))} -> {translated.count(chr(10))}")
    return errors, warnings


def load_translation(path):
    doc = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    if doc.get("schema") == SCHEMA_LIGHT:
        sys.exit(f"{path}: es un JSON liviano (solo traducciones). Primero armá el completo con la "
                 f"plantilla de tu juego: pes6tr.py merge <plantilla.json> {path} -o work/<código>.json")
    if doc.get("schema") != SCHEMA or doc.get("format") != "afs":
        sys.exit(f"{path}: no es un JSON de traducción ({SCHEMA}, format afs)")
    ids = [t["id"] for t in doc["texts"]]
    if len(ids) != len(set(ids)):
        sys.exit(f"{path}: hay ids repetidos")
    return doc


def review(doc):
    """Valida todas las traducciones. Devuelve ({id: texto del juego}, errores, avisos)."""
    chosen, errors, warnings = {}, [], []
    for t in doc["texts"]:
        tr = t.get("translatedText") or ""
        if not tr:
            continue
        err, warn = check_translation(t["defaultText"], tr)
        errors += [f'{t["id"]}: {e}' for e in err]
        warnings += [f'{t["id"]}: {w}' for w in warn]
        limit = t.get("maxLength")
        if not err and limit and visible_max_line(decode(tr)) > limit * 1.3:
            warnings.append(f'{t["id"]}: línea de {visible_max_line(decode(tr))} caracteres '
                            f'(los idiomas oficiales llegan a {limit}); puede cortarse en pantalla')
        if not err:
            chosen[t["id"]] = decode(tr)
    return chosen, errors, warnings


def cmd_check(args):
    doc = load_translation(args.json)
    chosen, errors, warnings = review(doc)
    total = len(doc["texts"])
    for line in errors:
        print("ERROR", line)
    for line in warnings:
        print("aviso", line)
    print(f"{len(chosen)} de {total} textos traducidos y válidos, {len(errors)} errores, {len(warnings)} avisos")
    sys.exit(1 if errors else 0)


def cmd_build(args):
    doc = load_translation(args.json)
    target = args.output_file or doc["file_name_output"]
    install = args.install or doc.get("install", "afs2fs")

    # AFS de partida: el del mismo lugar si está en dat, si no el de la base.
    if args.source:
        src = pathlib.Path(args.source)
    else:
        dat = pathlib.Path(args.dat)
        src = dat / target if (dat / target).is_file() else dat / doc["base"]["file"]
    if not src.is_file():
        sys.exit(f"no encuentro el AFS de partida: {src}")
    if install == "afs2fs" and src.name != target:
        sys.exit(f"afs2fs reemplaza entradas de {target}, así que hace falta ese archivo como partida "
                 f"(está {src.name}); usá --install afs o pasá --source")

    chosen, errors, warnings = review(doc)
    if errors and not args.skip_invalid:
        for line in errors:
            print("ERROR", line)
        sys.exit(f"{len(errors)} errores: no se arma (con --skip-invalid esos textos quedan en el texto de respaldo)")
    for line in warnings:
        print("aviso", line)

    # Menú de idiomas: cada lugar tiene su nombre (52:64 "English"…) y la palabra "Language"
    # en su idioma (52:71…). Se reemplazan por los de la traducción en el lugar que ocupa.
    # 52:136 y 52:138 son el nombre y la palabra "Language" del id 8 (inglés de Asia, sin uso en
    # PC). El módulo de idioma extra de HD Text usa el id 8 y lee de 52:136 el nombre del idioma.
    pairs = [("52:136", "52:138")]
    if target.lower() in SLOT_TEXTS:
        pairs.insert(0, SLOT_TEXTS[target.lower()])
    for name_key, title_key in pairs:
        for key, value in ((name_key, doc.get("language_label")), (title_key, doc.get("language_title"))):
            if value:
                chosen[key] = decode(value)
                print(f"menú de idiomas: {key} -> {value}")

    fallback = {t["id"]: decode(t["defaultText"]) for t in doc["texts"]} if args.fallback == "default" else {}

    data, items = read_afs(src)
    entries = load_text_entries(data, items)
    if len(entries) != 29:
        print(f"aviso: {src.name} tiene {len(entries)} tablas de texto (los oficiales tienen 29)")

    new_raw, changed, used = {}, 0, set()
    for idx, (blocks, body) in entries.items():
        new_blocks = []
        for tag, recs in blocks:
            new_recs = []
            for rid, x, chars, text in recs:
                key = f"{tag}:{rid}"
                new = chosen.get(key, fallback.get(key, text)) if text or key in chosen else text
                if key in chosen:
                    used.add(key)
                if new != text:
                    chars = len(new)
                    changed += 1
                new_recs.append((rid, x, chars, new))
            new_blocks.append((tag, new_recs))
        new_body = serialize_entry(new_blocks)
        if new_body != body or args.repack:
            new_raw[idx] = pack_entry(new_body)

    missing = set(chosen) - used
    if missing:
        print(f"aviso: {len(missing)} ids del JSON no están en {src.name}: {sorted(missing)[:5]}")

    out = pathlib.Path(args.out)
    if install == "afs2fs":
        # La salida copia la estructura del juego: se copia <out>\kitserver encima de la
        # carpeta kitserver del juego. afs2fs lee <kitserver>\dat\<archivo>\<algo>_<N>.<ext>
        # y usa el archivo tal cual como la entrada N (cabecera de 32 bytes incluida).
        folder = out / "kitserver" / "dat" / target
        folder.mkdir(parents=True, exist_ok=True)
        for old in folder.glob("unnamed_*.bin"):
            old.unlink()                      # que no quede una entrada de un armado anterior
        for idx, raw in sorted(new_raw.items()):
            (folder / f"unnamed_{idx}.bin").write_bytes(raw)
        print(f"{changed} registros cambiados, {len(new_raw)} entradas -> {folder}")
        print(f"instalar: copiar {out / 'kitserver'} encima de la carpeta kitserver del juego")
        return

    # AFS completo: misma cabecera, cada entrada en el siguiente múltiplo de 0x800.
    first = items[0][0] if items else FIRST_ENTRY
    blob = bytearray(data[:first])
    toc = []
    for idx, (off, size) in enumerate(items):
        raw = new_raw.get(idx, data[off:off + size])
        pos = align(len(blob), AFS_ALIGN)
        blob += bytes(pos - len(blob)) + raw
        toc.append((pos, len(raw)))
    blob += bytes(align(len(blob), AFS_ALIGN) - len(blob))
    for idx, (pos, size) in enumerate(toc):
        struct.pack_into("<II", blob, 8 + 8 * idx, pos, size)
    path = out if out.suffix.lower() == ".afs" else out / "dat" / target
    if path.resolve() == src.resolve():
        sys.exit("la salida no puede ser el mismo AFS de partida")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(blob)
    print(f"{changed} registros cambiados, {len(new_raw)} entradas rearmadas -> {path} ({len(blob)} bytes)")


# ---------------------------------------------------------------- liviano (strip / merge)

def light_problems(doc):
    """Problemas de forma de un JSON liviano (sin la plantilla: no compara contra el inglés).
    Lo usan merge y la CI (tools/check_repo.py)."""
    out = []
    if not isinstance(doc, dict):
        return ["no es un objeto JSON"]
    if doc.get("schema") != SCHEMA_LIGHT:
        out.append(f"schema tiene que ser {SCHEMA_LIGHT!r}")
    allowed = {"schema", "base", "texts", *LIGHT_HEADER}
    out += [f"campo desconocido en la cabecera: {k!r}" for k in doc if k not in allowed]
    for k in ("file_name_output", "language", "language_label", "install"):
        if not isinstance(doc.get(k), str) or not doc.get(k):
            out.append(f"falta {k!r} (texto)")
    if "language_title" in doc and not isinstance(doc["language_title"], str):
        out.append("language_title tiene que ser un texto")
    if doc.get("install") not in ("afs", "afs2fs", None):
        out.append("install tiene que ser afs o afs2fs")
    base = doc.get("base")
    if not isinstance(base, dict):
        out.append("falta base (objeto)")
    else:
        out += [f"campo desconocido en base: {k!r}" for k in base if k not in LIGHT_BASE]
        if not isinstance(base.get("file"), str) or not re.fullmatch(r"[efgisp]_text\.afs", base.get("file", "")):
            out.append("base.file tiene que ser un X_text.afs oficial")
        if not isinstance(base.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", base.get("sha256", "")):
            out.append("base.sha256 tiene que ser un SHA-256 en hexadecimal minúsculo")
        for k in ("records", "texts"):
            if not isinstance(base.get(k), int) or base.get(k) <= 0:
                out.append(f"base.{k} tiene que ser un entero positivo")
    texts = doc.get("texts")
    if not isinstance(texts, list):
        return out + ["falta texts (lista)"]
    seen = set()
    for i, t in enumerate(texts):
        at = f"texts[{i}]"
        if not isinstance(t, dict):
            out.append(f"{at}: no es un objeto")
            continue
        at = f"{at} ({t.get('id')})"
        extra = [k for k in t if k not in LIGHT_TEXT]
        if extra:
            # defaultText, reference, maxLength… son textos o datos del juego: no van en el liviano
            out.append(f"{at}: campos que no van en el liviano: {extra}")
        if not isinstance(t.get("id"), str) or not re.fullmatch(r"\d+:\d+", t.get("id", "")):
            out.append(f"{at}: id tiene que ser tag:id")
        elif t["id"] in seen:
            out.append(f"{at}: id repetido")
        else:
            seen.add(t["id"])
        tr = t.get("translatedText")
        if not isinstance(tr, str) or not tr:
            out.append(f"{at}: translatedText vacío (en el liviano van solo los traducidos)")
        else:
            try:
                decode(tr)
            except FormatError as e:
                out.append(f"{at}: {e}")
        if t.get("status") not in STATUSES:
            out.append(f"{at}: status tiene que ser uno de {STATUSES}")
    return out


def write_light(doc, path):
    """Cabecera indentada y un texto por línea: diffs de una línea por cambio de traducción."""
    head = {k: v for k, v in doc.items() if k != "texts"}
    lines = json.dumps(head, ensure_ascii=False, indent=2)[:-2]   # sin el "\n}" final
    body = ",\n".join("    " + json.dumps(t, ensure_ascii=False) for t in doc["texts"])
    text = f'{lines},\n  "texts": [\n{body}\n  ]\n}}\n'
    json.loads(text)                                              # que siga siendo JSON válido
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def cmd_strip(args):
    doc = load_translation(args.json)
    light = {"schema": SCHEMA_LIGHT}
    for k in LIGHT_HEADER:
        if k in doc:
            light[k] = doc[k]
    if args.output_file:
        light["file_name_output"] = args.output_file
    light["base"] = {k: doc["base"][k] for k in LIGHT_BASE if k in doc["base"]}
    texts, same = [], []
    for t in doc["texts"]:
        tr = t.get("translatedText") or ""
        if not tr:
            continue
        texts.append({"id": t["id"], "translatedText": tr, "status": t.get("status") or "draft"})
        if tr == t["defaultText"] and len(tr) >= 20:
            same.append(t["id"])
    light["texts"] = texts
    problems = light_problems(light)
    if problems:
        sys.exit("\n".join(problems))
    write_light(light, args.out)
    print(f"{len(texts)} traducciones de {len(doc['texts'])} textos -> {args.out}")
    if same:
        # una "traducción" igual al inglés es texto de Konami en el repo: revisarla
        print(f"aviso: {len(same)} traducciones largas iguales al inglés: {same[:10]}")


def load_light(path):
    doc = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    problems = light_problems(doc)
    if problems:
        sys.exit(f"{path}: no es un JSON liviano válido:\n  " + "\n  ".join(problems[:20]))
    return doc


def cmd_merge(args):
    tpl = load_translation(args.template)
    light = load_light(args.light)
    lb, tb = light["base"], tpl["base"]
    if lb["sha256"] != tb["sha256"] or lb["file"] != tb["file"]:
        sys.exit(f"la plantilla sale de otro {tb['file']} (sha256 {tb['sha256']}) que la traducción "
                 f"({lb['file']}, sha256 {lb['sha256']}): exportá la plantilla del {lb['file']} original")
    by_id = {t["id"]: t for t in tpl["texts"]}
    missing = [t["id"] for t in light["texts"] if t["id"] not in by_id]
    if missing:
        sys.exit(f"{len(missing)} ids de la traducción no están en la plantilla: {missing[:10]}")
    tr = {t["id"]: t for t in light["texts"]}
    doc = {"schema": SCHEMA, "format": "afs"}
    for k in LIGHT_HEADER:
        if k in light:
            doc[k] = light[k]
    doc["base"] = tb
    texts = []
    for t in tpl["texts"]:
        t = dict(t)
        if t["id"] in tr:
            t["translatedText"] = tr[t["id"]]["translatedText"]
            t["status"] = tr[t["id"]]["status"]
        else:
            t["translatedText"], t["status"] = "", "todo"
        texts.append(t)
    doc["texts"] = texts
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(tr)} traducciones en {len(texts)} textos de la plantilla -> {out}")


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):    # la consola de Windows no es UTF-8 por defecto
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("export", help="X_text.afs -> JSON para traducir")
    p.add_argument("source", help="carpeta dat o un X_text.afs")
    p.add_argument("-o", "--out", required=True)
    p.add_argument("--base", default="e", choices=list(LANGS), help="idioma base si source es una carpeta")
    p.add_argument("--language", default="", help="código del idioma de la traducción (tr, el, ru…)")
    p.add_argument("--label", default="", help="nombre del idioma en su idioma (Türkçe, Ελληνικά…)")
    p.add_argument("--output-file", default="", help="AFS que se va a armar (por defecto, el de la base)")
    p.add_argument("--install", default="afs2fs", choices=["afs2fs", "afs"])
    p.add_argument("--no-references", action="store_true", help="no agregar los otros idiomas oficiales")
    p.set_defaults(func=cmd_export)

    p = sub.add_parser("check", help="valida las traducciones de un JSON")
    p.add_argument("json")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("build", help="JSON -> AFS (o carpeta afs2fs)")
    p.add_argument("json")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--dat", help="carpeta dat del juego: parte del AFS del lugar o, si no está, del de la base")
    src.add_argument("--source", help="AFS de partida explícito")
    p.add_argument("-o", "--out", required=True, help="carpeta de salida (o un .afs con --install afs)")
    p.add_argument("--output-file", default="", help="pisa file_name_output del JSON")
    p.add_argument("--install", choices=["afs2fs", "afs"], help="pisa install del JSON")
    p.add_argument("--fallback", choices=["default", "source"], default="default",
                   help="texto sin traducir: el inglés del JSON (default) o el del AFS de partida (source)")
    p.add_argument("--skip-invalid", action="store_true", help="arma igual; las traducciones con errores usan el respaldo")
    p.add_argument("--repack", action="store_true", help="recomprime también las tablas que no cambian")
    p.set_defaults(func=cmd_build)

    p = sub.add_parser("strip", help="JSON completo -> liviano (solo traducciones, lo que va en git)")
    p.add_argument("json")
    p.add_argument("-o", "--out", required=True)
    p.add_argument("--output-file", default="", help="pisa file_name_output (por ejemplo ru_text.afs)")
    p.set_defaults(func=cmd_strip)

    p = sub.add_parser("merge", help="plantilla de tu juego + liviano -> JSON completo para check y build")
    p.add_argument("template", help="la plantilla de export, sacada de tu propio juego")
    p.add_argument("light", help="languages/<código>/<código>.json")
    p.add_argument("-o", "--out", required=True)
    p.set_defaults(func=cmd_merge)
    args = ap.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
