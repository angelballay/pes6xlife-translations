r"""Comprobación del repo sin el juego (lo que corre la CI, .github/workflows/check.yml).

  python tools/check_repo.py

1. languages/<código>/<código>.json: forma del JSON liviano (pes6tr.light_problems), sin textos del juego
   (defaultText, reference…), y que cada idioma tenga su glossary.md y su CHANGELOG.md.
2. web/: guide.json, <id>/translation.json y mods/pes6-translations/mod.json con las reglas de la web
   (site/src/content/rules.ts y validate-*.ts de Pes6FontCreator, copiadas acá), imágenes .webp incluidas.
3. packages/: una receta por idioma y la de la DLL, con sus requires.
4. Ningún binario (*.afs *.zip *.dll *.exe *.bin) en el repo.

No puede correr `pes6tr.py check`: para eso hace falta la plantilla de tu juego (CONTRIBUTING.md).
Solo biblioteca estándar. Sale con 1 si hay algún problema.
"""
from __future__ import annotations

import json
import math
import pathlib
import re
import struct
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import pes6tr  # noqa: E402

BINARY = re.compile(r"\.(afs|zip|dll|exe|bin)$", re.I)
PENDING = "@pendiente"

# ---------------------------------------------------------------- reglas de la web (rules.ts)

BADGE_COLORS = ("yellow", "green", "teal", "orange", "red", "white", "grey")   # @pfc/shared
BADGE_MAX = 6
MAX_IMAGES = 12
MAX_IMAGE_KB, MAX_IMAGE_W, MAX_IMAGE_H = 300, 1920, 1080
FORMATS = {
    "id": re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$"),
    "url": re.compile(r"^(https://\S+|/(?!/)\S*)$"),
    "https": re.compile(r"^https://\S+$"),
    "date": re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"),
    "youtubeId": re.compile(r"^[\w-]{11}$"),
    "repo": re.compile(r"^[\w.-]+/[\w.-]+$"),
    "duration": re.compile(r"^\d{1,2}(:[0-5]\d){1,2}$"),
}
# Las categorías de site.json de la web (un mod de este repo tiene que caer en una de ellas).
SITE_CATEGORIES = ("mods", "tools")


def req(rule):
    return (rule, True)


def opt(rule):
    return (rule, False)


plain = lambda mx=None: ("plain", mx)
localized = lambda mx=None: ("localized", mx)
TEXT = ("text",)
LOCALIZED_LIST = ("localizedList",)
fmt = lambda f: ("format", f)
one_of = lambda vals: ("oneOf", tuple(vals))
NUMBER, BOOLEAN = ("number",), ("boolean",)
obj = lambda fields: ("object", fields)
lst = lambda of, mn=None, mx=None: ("list", of, mn, mx)

LINK = obj({"kind": req(one_of(("github", "youtube", "forum", "other"))), "url": req(fmt("url")),
            "label": opt(localized())})
IMAGES = lst(obj({"file": req(plain()), "alt": req(localized()), "caption": opt(localized())}), 1, MAX_IMAGES)
REQUIREMENTS = lst(obj({"label": req(localized()), "value": req(TEXT), "mod": opt(fmt("id"))}), 1)
GROUPS = lst(obj({"id": req(fmt("id")), "name": req(localized()), "color": req(one_of(BADGE_COLORS))}), 1)


def release(download):
    return obj({"version": req(plain()), "date": req(fmt("date")), "download": req(fmt(download)),
                "file": opt(plain()), "size": opt(plain()),
                "notes": opt(lst(obj({"kind": req(one_of(("new", "fix"))), "text": req(localized())}), 1))})


MOD_FIELDS = {
    "id": req(fmt("id")), "kind": req(one_of(("mod", "tool"))), "category": req(fmt("id")),
    "order": opt(NUMBER), "name": req(plain()), "author": req(plain()),
    "badge": req(localized(BADGE_MAX)), "badgeColor": req(one_of(BADGE_COLORS)),
    "summary": req(localized()), "description": req(LOCALIZED_LIST),
    "licenses": req(lst(obj({"scope": req(localized()), "name": req(TEXT), "url": opt(fmt("url"))}), 1)),
    "videos": opt(lst(obj({"youtubeId": req(fmt("youtubeId")), "title": req(localized()),
                           "duration": opt(fmt("duration"))}), 1)),
    "images": opt(IMAGES), "release": opt(release("url")),
    "github": opt(obj({"repo": req(fmt("repo")), "releases": opt(BOOLEAN)})),
    "requirements": opt(REQUIREMENTS), "install": opt(LOCALIZED_LIST), "links": opt(lst(LINK, 1)),
}
TRANSLATION_FIELDS = {
    "id": req(fmt("id")), "group": req(fmt("id")), "order": opt(NUMBER), "name": req(plain()),
    "language": req(localized()), "badge": req(plain(BADGE_MAX)), "badgeColor": req(one_of(BADGE_COLORS)),
    "author": req(plain()), "beta": opt(BOOLEAN), "summary": req(localized()),
    "description": req(LOCALIZED_LIST), "images": opt(IMAGES), "release": opt(release("https")),
    "requirements": opt(REQUIREMENTS), "install": opt(LOCALIZED_LIST),
    "credits": opt(lst(obj({"role": req(localized()), "name": req(plain())}), 1)),
}
GUIDE_FIELDS = {
    "intro": req(LOCALIZED_LIST), "groups": req(GROUPS), "requirements": req(REQUIREMENTS),
    "steps": req(LOCALIZED_LIST), "notes": opt(LOCALIZED_LIST),
}


def bare(s):
    return s[len(PENDING):].strip() if s.startswith(PENDING) else s


def js_len(s):
    """Largo como lo cuenta JavaScript (unidades UTF-16)."""
    return len(s.encode("utf-16-le")) // 2


def is_text(v):
    return isinstance(v, str) and bare(v).strip() != ""


def localized_problem(v, at, mx=None):
    if not isinstance(v, dict) or not is_text(v.get("es")) or not is_text(v.get("en")):
        return f'"{at}" tiene que tener "es" y "en" con texto'
    if mx is not None and (js_len(bare(v["es"])) > mx or js_len(bare(v["en"])) > mx):
        return f'"{at}" pasa de {mx} letras'
    return None


def check_value(v, rule, at, out):
    kind = rule[0]
    if kind == "object":
        if not isinstance(v, dict):
            out.append(f'"{at}" tiene que ser un objeto')
        else:
            check_fields(v, rule[1], at, out)
    elif kind == "list":
        _, of, mn, mx = rule
        if not isinstance(v, list):
            out.append(f'"{at}" tiene que ser una lista')
            return
        if mn is not None and len(v) < mn:
            out.append(f'"{at}" necesita al menos {mn}')
        if mx is not None and len(v) > mx:
            out.append(f'"{at}" tiene {len(v)} (máximo {mx})')
        for i, item in enumerate(v):
            check_value(item, of, f"{at}[{i}]", out)
    elif kind == "plain":
        if not is_text(v):
            out.append(f'"{at}" tiene que ser un texto')
        elif rule[1] is not None and js_len(bare(v)) > rule[1]:
            out.append(f'"{at}" pasa de {rule[1]} letras')
    elif kind == "localized":
        p = localized_problem(v, at, rule[1])
        if p:
            out.append(p)
    elif kind == "text":
        if not is_text(v):
            p = localized_problem(v, at)
            if p:
                out.append(p)
    elif kind == "localizedList":
        ok = lambda l: isinstance(l, list) and len(l) > 0 and all(is_text(x) for x in l)
        if not (isinstance(v, dict) and ok(v.get("es")) and ok(v.get("en"))):
            out.append(f'"{at}" tiene que tener "es" y "en", cada uno una lista de textos')
    elif kind == "format":
        if not (isinstance(v, str) and FORMATS[rule[1]].search(bare(v))):
            out.append(f'"{at}" no tiene el formato {rule[1]}')
    elif kind == "oneOf":
        if not (isinstance(v, str) and v in rule[1]):
            out.append(f'"{at}" tiene que ser uno de: {", ".join(rule[1])}')
    elif kind == "number":
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            out.append(f'"{at}" tiene que ser un número')
    elif kind == "boolean":
        if not isinstance(v, bool):
            out.append(f'"{at}" tiene que ser true o false')


def check_fields(v, fields, at, out):
    join = lambda k: f"{at}.{k}" if at else k
    for key, (rule, required) in fields.items():
        if key not in v:
            if required:
                out.append(f'falta "{join(key)}"')
        else:
            check_value(v[key], rule, join(key), out)
    for key in v:
        if key not in fields:
            out.append(f'"{join(key)}" no es un campo conocido')


def find_pending(v, path=""):
    if isinstance(v, str):
        return [path] if v.startswith(PENDING) else []
    if isinstance(v, list):
        return [p for i, x in enumerate(v) for p in find_pending(x, f"{path}[{i}]")]
    if isinstance(v, dict):
        return [p for k, x in v.items() for p in find_pending(x, f"{path}.{k}" if path else k)]
    return []


def webp_size(b):
    """(ancho, alto) de un WebP, o None (como webp-size.ts: VP8, VP8L y VP8X)."""
    if len(b) < 30 or b[:4] != b"RIFF" or b[8:12] != b"WEBP":
        return None
    chunk = b[12:16]
    if chunk == b"VP8 " and b[23:26] == b"\x9d\x01\x2a":
        w, h = struct.unpack_from("<HH", b, 26)
        return w & 0x3FFF, h & 0x3FFF
    if chunk == b"VP8L" and b[20] == 0x2F:
        bits = int.from_bytes(b[21:25], "little")
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    if chunk == b"VP8X":
        return int.from_bytes(b[24:27], "little") + 1, int.from_bytes(b[27:30], "little") + 1
    return None


def image_problems(doc, folder):
    out = []
    for i, img in enumerate(doc.get("images") or []):
        f = img.get("file") if isinstance(img, dict) else None
        if not isinstance(f, str):
            continue
        at = f"images[{i}]"
        if not f.lower().endswith(".webp"):
            out.append(f"{at} tiene que ser .webp")
            continue
        p = folder / f
        if not p.is_file():
            out.append(f"{at} no existe ({p.relative_to(ROOT).as_posix()})")
            continue
        b = p.read_bytes()
        if len(b) > MAX_IMAGE_KB * 1024:
            out.append(f"{at} pesa {math.ceil(len(b) / 1024)} KB (máximo {MAX_IMAGE_KB} KB)")
        size = webp_size(b)
        if not size:
            out.append(f"{at} no es un WebP que se pueda leer")
        elif size[0] > MAX_IMAGE_W or size[1] > MAX_IMAGE_H:
            out.append(f"{at} mide {size[0]} × {size[1]} (máximo {MAX_IMAGE_W} × {MAX_IMAGE_H})")
    return out


def load(path, out):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        out.append(f"{path.relative_to(ROOT).as_posix()}: no existe")
    except json.JSONDecodeError as e:
        out.append(f"{path.relative_to(ROOT).as_posix()}: no es JSON válido ({e})")
    return None


def entry_problems(doc, fields, folder, groups, group_field, group_ok):
    out = []
    if not isinstance(doc, dict):
        return ["tiene que ser un objeto"]
    check_fields(doc, fields, "", out)
    if isinstance(doc.get("id"), str) and doc["id"] != folder.name:
        out.append(f'la carpeta se llama "{folder.name}" y el id es "{doc["id"]}"')
    g = doc.get(group_field)
    if isinstance(g, str) and g not in groups:
        out.append(group_ok(g))
    out += image_problems(doc, folder)
    out += [f'"{p}" está @pendiente' for p in find_pending(doc)]
    return out


def requirement_mods(doc):
    return {r.get("mod") for r in doc.get("requirements") or [] if isinstance(r, dict)}


def check_web(problems):
    web = ROOT / "web"
    guide_path = web / "translations" / "guide.json"
    guide = load(guide_path, problems)
    groups = set()
    if guide is not None:
        out = []
        if isinstance(guide, dict):
            check_fields(guide, GUIDE_FIELDS, "", out)
            ids = [g.get("id") for g in guide.get("groups") or [] if isinstance(g, dict)]
            out += [f'el grupo "{i}" está repetido' for i in sorted({i for i in ids if ids.count(i) > 1})]
            groups = {i for i in ids if isinstance(i, str)}
            out += [f'"{p}" está @pendiente' for p in find_pending(guide)]
            for need in ("pes6-hd-text", "pes6-translations"):
                if need not in requirement_mods(guide):
                    out.append(f'requirements no tiene la fila con mod "{need}" (WEB-4)')
        else:
            out.append("tiene que ser un objeto")
        problems += [f"web/translations/guide.json: {p}" for p in out]
    folders = sorted(p for p in (web / "translations").iterdir() if p.is_dir())
    for folder in folders:
        f = folder / "translation.json"
        doc = load(f, problems)
        if doc is None:
            continue
        out = entry_problems(doc, TRANSLATION_FIELDS, folder, groups, "group",
                             lambda g: f'el grupo "{g}" no está en translations/guide.json')
        if isinstance(doc, dict) and "pes6-translations" not in requirement_mods(doc):
            out.append('requirements no tiene la fila PES6 Translations con mod "pes6-translations" (WEB-4)')
        problems += [f"{f.relative_to(ROOT).as_posix()}: {p}" for p in out]
    for folder in sorted(p for p in (web / "mods").iterdir() if p.is_dir()):
        f = folder / "mod.json"
        doc = load(f, problems)
        if doc is None:
            continue
        out = entry_problems(doc, MOD_FIELDS, folder, set(SITE_CATEGORIES), "category",
                             lambda c: f'la categoría "{c}" no está en site.json de la web')
        if isinstance(doc, dict) and (doc.get("github") or {}).get("releases"):
            out.append("sin github.releases: el último release del repo puede ser de un idioma (WEB-7)")
        problems += [f"{f.relative_to(ROOT).as_posix()}: {p}" for p in out]
    for p in web.rglob("*"):
        if re.search(r"\.(png|jpe?g)$", p.name, re.I):
            problems.append(f"{p.relative_to(ROOT).as_posix()}: las imágenes van en .webp (no .png ni .jpg)")
    return [f.name for f in folders]


# ---------------------------------------------------------------- idiomas, recetas y binarios

def check_languages(problems):
    codes = []
    for folder in sorted(p for p in (ROOT / "languages").iterdir() if p.is_dir()):
        code = folder.name
        codes.append(code)
        rel = f"languages/{code}"
        for name in ("glossary.md", "CHANGELOG.md"):
            if not (folder / name).is_file():
                problems.append(f"{rel}: falta {name}")
        doc = load(folder / f"{code}.json", problems)
        if doc is None:
            continue
        out = pes6tr.light_problems(doc)
        if isinstance(doc, dict):
            if doc.get("language") != code:
                out.append(f'language es "{doc.get("language")}" y la carpeta "{code}"')
            if doc.get("file_name_output") != f"{code}_text.afs":
                out.append(f'file_name_output tiene que ser "{code}_text.afs"')
        problems += [f"{rel}/{code}.json: {p}" for p in out[:50]]
        if len(out) > 50:
            problems.append(f"{rel}/{code}.json: … y {len(out) - 50} problemas más")
    others = [p for p in (ROOT / "languages").rglob("*")
              if p.is_file() and p.name not in ("glossary.md", "CHANGELOG.md", f"{p.parent.name}.json")]
    problems += [f"{p.relative_to(ROOT).as_posix()}: archivo inesperado en languages/" for p in others]
    return codes


def check_packages(problems, codes):
    pk = ROOT / "packages"
    dll = load(pk / "translations.json", problems)
    if isinstance(dll, dict) and dll.get("package") != "translations":
        problems.append('packages/translations.json: package tiene que ser "translations"')
    for code in codes:
        f = pk / f"translation-{code}.json"
        doc = load(f, problems)
        if not isinstance(doc, dict):
            continue
        rel = f.relative_to(ROOT).as_posix()
        if doc.get("package") != f"translation-{code}":
            problems.append(f'{rel}: package tiene que ser "translation-{code}"')
        reqs = {r.get("package"): r.get("min") for r in doc.get("requires") or [] if isinstance(r, dict)}
        for need in ("hdtext", "translations"):
            if need not in reqs:
                problems.append(f"{rel}: requires no tiene {need} (TRA-9)")
        installs = [x.get("path") for x in doc.get("files") or [] if isinstance(x, dict) and x.get("install")]
        if installs != [f"dat/{code}_text.afs"]:
            problems.append(f"{rel}: instala {installs}; un idioma instala solo dat/{code}_text.afs (VER-9)")


def check_binaries(problems):
    found = set()
    try:
        tracked = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True, check=True)
        found |= {f for f in tracked.stdout.decode("utf-8").split("\0") if f and BINARY.search(f)}
    except (OSError, subprocess.CalledProcessError):
        pass
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT)
        if p.is_file() and rel.parts[0] not in (".git", "work") and BINARY.search(p.name):
            found.add(rel.as_posix())
    problems += [f"{f}: binario en el repo (el .afs y la DLL van solo en el zip del release)" for f in sorted(found)]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    problems = []
    codes = check_languages(problems)
    web_codes = check_web(problems)
    if sorted(codes) != sorted(web_codes):
        problems.append(f"languages/ tiene {codes} y web/translations/ tiene {web_codes}")
    check_packages(problems, codes)
    check_binaries(problems)
    for p in problems:
        print("ERROR", p)
    print(f"{len(codes)} idiomas ({', '.join(codes)}), {len(problems)} problemas")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
