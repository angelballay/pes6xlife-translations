r"""Letras de una traducción que no están en la fuente de PES6 HD Text.

  python letras.py <traduccion.json> <plantilla.json> <carpeta charset de font-creator>

<traduccion.json> puede ser el liviano de languages/<código>/ o el completo de merge.

La carpeta es font-creator/src/engine/charset del repo de HD Text. La fuente tiene los caracteres de
la fuente base (latin-table.ts, generada del HD_original_font.bin: 494 códigos no japoneses), las
letras nuevas de Pes6FontCreator (las constantes NEW_* de new-letters.ts) y la parte japonesa, que
latin-table.ts no lista: de esa parte se aceptan los signos que los textos del juego ya usan
(「」『』【】・∀, en la plantilla). Lista cada carácter que falta, con los textos que lo usan. Sale
con 1 si falta alguno.

Antes se tomaban como letras de la base las que usan los textos del juego (inglés y referencias):
eso daba por faltantes letras que la fuente sí tiene (Ç, Â, Ê, Ô, ã, õ…).
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
tr_path, plantilla_path, charset_dir = sys.argv[1:4]
TOKEN = re.compile(r"\{\{|\}\}|\{[cwkljnpui]:[0-9A-Za-z]+\}")

ts = open(os.path.join(charset_dir, "new-letters.ts"), encoding="utf-8").read()
new = set()
for m in re.finditer(r"export const NEW_\w+ = '([^']*)'", ts):
    new |= set(m.group(1))

table = open(os.path.join(charset_dir, "latin-table.ts"), encoding="utf-8").read()
base = {chr(int(h, 16)) for h in re.findall(r"cp: 0x([0-9A-Fa-f]+)", table)}

# lo que los textos originales ya muestran (inglés y referencias): el juego lo dibuja hoy
game = set()
for t in json.load(open(plantilla_path, encoding="utf-8"))["texts"]:
    for s in [t["defaultText"], *t.get("reference", {}).values()]:
        game |= set(TOKEN.sub("", s))

ok = base | new | game | {"\n"}
used = {}
for t in json.load(open(tr_path, encoding="utf-8"))["texts"]:
    for ch in TOKEN.sub("", t.get("translatedText", "")):
        used.setdefault(ch, []).append(t["id"])

missing = {c: ids for c, ids in used.items() if c not in ok}
print(f"{len(used)} caracteres distintos; fuente base {len(base)}; NEW_LETTERS {len(new)}")
for c, ids in sorted(missing.items()):
    print(f"FALTA U+{ord(c):04X} {c!r} en {len(ids)} textos: {ids[:8]}")
print("faltan", len(missing))
sys.exit(1 if missing else 0)
