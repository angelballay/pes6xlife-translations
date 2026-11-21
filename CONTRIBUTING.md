# Contributing / Cómo contribuir

English first; [Castellano más abajo](#castellano).

## The two JSON files

| | Where | What it has | In git |
|---|---|---|---|
| **light** (`pes6-text-translation-light/1`) | `languages/<code>/<code>.json` | only the translations: `id`, `translatedText`, `status`, and the language header | yes |
| **full** (`pes6-text-translation/1`) | `work/` (ignored by git) | also the game's texts: the English (`defaultText`), the official French, German, Italian, Spanish and Polish (`reference`), `maxLength` | **never** |

The full JSON contains Konami's texts, so it is built on your machine from **your own copy of the game** and never
leaves it. `tools/pes6tr.py merge` builds it, `tools/pes6tr.py strip` turns it back into the light one.

## You need

- Python 3.11 or later (only the standard library).
- PES 6 PC with its original `dat\e_text.afs` (SHA-256 `d90c9d8a6712a5227b901bcf1e622da592539961e78b02222a40922ccf75be7b`).
  The other `X_text.afs` of the same folder (`f`, `g`, `i`, `s`, `p`) are optional: they become the `reference` texts.
- To test in the game: PES6 HD Text 1.0.2 or later with its languages add-on (`translations.dll`, it comes with the
  first language you install; see the README).

## Edit a language and build its `.afs`

```powershell
# 1. Template from your own game (the same for every language)
python tools\pes6tr.py export "<game>\dat" -o work\template.json

# 2. Full JSON = template + the translations of the language
python tools\pes6tr.py merge work\template.json languages\tr\tr.json -o work\tr.json

# 3. Edit: either languages\tr\tr.json (then merge again) or work\tr.json (then strip, step 6)

# 4. Check: 0 errors needed (warnings are for review)
python tools\pes6tr.py check work\tr.json

# 5. Build the .afs on top of e_text.afs and try it in the game
python tools\pes6tr.py build work\tr.json --source "<game>\dat\e_text.afs" --install afs -o work\tr_text.afs

# 6. If you edited work\tr.json: back to the light JSON
python tools\pes6tr.py strip work\tr.json -o languages\tr\tr.json

# 7. What the CI checks
python tools\check_repo.py
```

To try it: copy `work\tr_text.afs` to the `dat\` folder of the game's installation and pick it in `hdtext.exe` →
Languages → Use (it shows as changed, because it is not the signed file), or set `translation = tr_text.afs` in
`hdtext.cfg`.

`merge` stops if your `e_text.afs` is not the original one (another SHA-256) or if an `id` of the translation is not in
your template. Then export the template again from an original `e_text.afs`.

## Rules for a translation

- Keep every token exactly as in the English: colours `{c:ffdc28ff}`, codes `{w:ff}` `{k:a}`…, button icons
  `{i:e087}` and `printf` formats (`%d`, `%s`, `%3d`, `%%`). Their order may change, their number may not. A literal
  `{` or `}` is written `{{` or `}}`, a literal `%` is `%%`. `check` turns any of these into an error.
- Keep the line breaks (`\n`) where you can: a different number is a warning, the line may not fit.
- `maxLength` (in the full JSON) is the longest line among the official languages. Much longer than that may be cut
  on screen.
- Follow `glossary.md` of the language: the same term everywhere.
- `status`: `draft` (first pass) or `done` (reviewed in the game).
- Letters: `python tools\letras.py languages\tr\tr.json work\template.json <font-creator>\src\engine\charset`
  lists any character that the PES6 HD Text font does not have.
- Never commit `work/`, a full JSON, an `.afs` or any other binary: `.gitignore` and the CI stop them.

The JSON format and how the `.afs` is rebuilt are in [docs/DISENO.md](docs/DISENO.md) (in Spanish).

## A new language

1. `export` with its header: `--language <code> --label "<name in the language>" --output-file <code>_text.afs --install afs`.
2. Translate in batches with `tools\lotes.py` (`cortar`, `verificar`, `unir`; `unir --title` sets the word
   "Language" of the language menu). A close language can start from another one (`cortar --desde`).
3. `check`, `build`, test in the game, `strip` into `languages/<code>/<code>.json`.
4. Add `languages/<code>/glossary.md` and `CHANGELOG.md`, `web/translations/<code>/translation.json` and
   `packages/translation-<code>.json` (copy those of another language).

---

## Castellano

### Los dos JSON

| | Dónde | Qué tiene | En git |
|---|---|---|---|
| **liviano** (`pes6-text-translation-light/1`) | `languages/<código>/<código>.json` | solo las traducciones: `id`, `translatedText`, `status`, y la cabecera del idioma | sí |
| **completo** (`pes6-text-translation/1`) | `work/` (ignorada por git) | además los textos del juego: el inglés (`defaultText`), los oficiales en francés, alemán, italiano, español y polaco (`reference`), `maxLength` | **nunca** |

El completo lleva textos de Konami, así que se arma en tu máquina con **tu propia copia del juego** y no sale de ahí.
`tools/pes6tr.py merge` lo arma y `tools/pes6tr.py strip` lo vuelve liviano.

### Hace falta

- Python 3.11 o más nuevo (solo la biblioteca estándar).
- PES 6 PC con su `dat\e_text.afs` original (SHA-256 `d90c9d8a6712a5227b901bcf1e622da592539961e78b02222a40922ccf75be7b`).
  Los otros `X_text.afs` de la carpeta (`f`, `g`, `i`, `s`, `p`) son opcionales: son los textos de `reference`.
- Para probar en el juego: PES6 HD Text 1.0.2 o más nueva con su complemento de idiomas (`translations.dll`, viene con
  el primer idioma que instalás; ver el README).

### Editar un idioma y armar su `.afs`

```powershell
# 1. Plantilla de tu juego (la misma para todos los idiomas)
python tools\pes6tr.py export "<juego>\dat" -o work\plantilla.json

# 2. Completo = plantilla + las traducciones del idioma
python tools\pes6tr.py merge work\plantilla.json languages\tr\tr.json -o work\tr.json

# 3. Editar: languages\tr\tr.json (y volver a hacer merge) o work\tr.json (y después strip, paso 6)

# 4. Comprobar: tiene que dar 0 errores (los avisos son para revisar)
python tools\pes6tr.py check work\tr.json

# 5. Armar el .afs sobre e_text.afs y probarlo en el juego
python tools\pes6tr.py build work\tr.json --source "<juego>\dat\e_text.afs" --install afs -o work\tr_text.afs

# 6. Si editaste work\tr.json: de vuelta al liviano
python tools\pes6tr.py strip work\tr.json -o languages\tr\tr.json

# 7. Lo que comprueba la CI
python tools\check_repo.py
```

Para probarlo: copiá `work\tr_text.afs` a la carpeta `dat\` de la instalación del juego y elegilo en `hdtext.exe` →
Languages → Use (sale como cambiado, porque no es el archivo firmado), o poné `translation = tr_text.afs` en
`hdtext.cfg`.

`merge` se frena si tu `e_text.afs` no es el original (otro SHA-256) o si un `id` de la traducción no está en tu
plantilla. En ese caso, volvé a exportar la plantilla de un `e_text.afs` original.

### Reglas de una traducción

- Cada ficha queda igual que en el inglés: colores `{c:ffdc28ff}`, códigos `{w:ff}` `{k:a}`…, íconos de botones
  `{i:e087}` y formatos de `printf` (`%d`, `%s`, `%3d`, `%%`). Puede cambiar el orden, no la cantidad. Una llave
  literal se escribe `{{` o `}}` y un `%` literal, `%%`. `check` da error con cualquiera de estas.
- Los saltos de línea (`\n`), donde se pueda: otra cantidad es un aviso, la línea puede no entrar.
- `maxLength` (en el completo) es la línea más larga entre los idiomas oficiales. Mucho más larga puede cortarse en
  pantalla.
- Seguí el `glossary.md` del idioma: el mismo término en todos lados.
- `status`: `draft` (primera pasada) o `done` (revisado en el juego).
- Letras: `python tools\letras.py languages\tr\tr.json work\plantilla.json <font-creator>\src\engine\charset` lista
  los caracteres que la fuente de PES6 HD Text no tiene.
- Nunca se commitea `work/`, un JSON completo, un `.afs` ni ningún binario: `.gitignore` y la CI los frenan.

El formato del JSON y cómo se rearma el `.afs` están en [docs/DISENO.md](docs/DISENO.md).

### Un idioma nuevo

1. `export` con su cabecera: `--language <código> --label "<nombre en su idioma>" --output-file <código>_text.afs --install afs`.
2. Traducir por tandas con `tools\lotes.py` (`cortar`, `verificar`, `unir`; `unir --title` pone la palabra
   "Language" del menú de idiomas). Un idioma cercano puede salir de otro (`cortar --desde`).
3. `check`, `build`, probar en el juego y `strip` a `languages/<código>/<código>.json`.
4. Sumar `languages/<código>/glossary.md` y `CHANGELOG.md`, `web/translations/<código>/translation.json` y
   `packages/translation-<código>.json` (copiando los de otro idioma).
