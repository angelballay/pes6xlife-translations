# PES6 translations (pes6xlife-translations)

Translations of **Pro Evolution Soccer 6 (PC)** into languages the game does not ship. Each one is a seventh option of
the game's language menu: the six original languages, your commentary, the registry and `pes6.exe` stay as they were.

| Language | Code | Version | State |
|---|---|---|---|
| Русский (Russian) | `ru` | 1.0 | tested in the game |
| Ελληνικά (Greek) | `el` | 1.0 | tested in the game |
| Türkçe (Turkish) | `tr` | 1.0 | tested in the game |
| Srpski (Serbian, Latin script) | `sr` | 1.0 | beta (tested in the lab) |
| Hrvatski (Croatian) | `hr` | 1.0 | beta (tested in the lab) |
| Português (Brasil) (Brazilian Portuguese) | `pt-br` | 1.0 | beta (tested in the lab) |
| Bahasa Indonesia (Indonesian) | `id` | 1.0 | beta (tested in the lab) |

Spanish below / [Castellano más abajo](#castellano).

## Install a language

You need PES 6 PC with Kitserver 6, **PES6 HD Text 1.0.2 or later** and **PES6 Translations** (`translations.dll`).
There are two downloads, both on the website and in this repository's Releases:

- **PES6 Translations**, the DLL, once: `PES6_Translations_DLL_v<version>.zip` (tag `dll-v<version>`).
- **Each language**: `PES6_Translation_<code>_v<version>.zip` (tag `<code>-v<version>`). It has only
  `dat/<code>_text.afs`; it does **not** include the DLL, and it says which version of the DLL it needs.

Steps:

1. **The first time only:** open `hdtext.exe`, press **Translations: Install…** and pick the DLL's `.zip`. It installs
   `Kitserver\translations.dll` and adds it to `kload.cfg`, after HD Text.
2. In `hdtext.exe`, open the **Translations** tab, press **Install from file…** and pick the language's `.zip` (no need
   to unzip it). `hdtext.exe` checks the signed manifest inside and leaves the language chosen.
3. Start the game and pick the new language on the language screen. The game remembers it.

**By hand:** copy the `dat` and `Kitserver` folders of each `.zip` into your PES 6 folder (the one the game is
installed to: the game reads `dat\` from there), add `DLL.<N> = "kitserver\translations.dll"` to `kload.cfg` after HD
Text's line (and raise `DLL.num`), and pick the language in the Translations tab of `hdtext.exe`.

To change the language, use the game's Options. To turn the translation off, disable it in the Translations tab.

## Propose a change

Each language is a JSON in `languages/<code>/<code>.json` with only the translations (`id`, `translatedText`,
`status`), its glossary (`glossary.md`, the terms every text must use) and its changelog.

- **A wrong text:** open an issue with the screen, what it says and what it should say, or a pull request that
  changes that line of the JSON. Each text is one line, so the diff shows exactly what changed.
- **To build and test it in your game**, see [CONTRIBUTING.md](CONTRIBUTING.md): you export the game's texts from
  your own copy, merge them with the JSON, check and build the `.afs`.

The CI checks the shape of every JSON, the website data and that no binary is committed. The full check
(`pes6tr.py check`: control codes, button icons and `%` formats against the English text) needs your game's texts, so
it runs locally.

## What is in this repository

```
languages/<code>/     <code>.json (translations only), glossary.md, CHANGELOG.md
tools/                pes6tr.py (export, merge, check, build, strip), lotes.py, letras.py, check_repo.py
docs/DISENO.md        the JSON format and how the .afs is rebuilt (in Spanish)
web/                  what the website shows: translations/ (guide and one entry per language),
                      mods/pes6-translations/ (the DLL's page)
packages/             pes6pkg recipes for the release zips (provisional format) and their README/LEEME
```

No text, image or file of the game is in this repository: the `.afs` of each language exists only inside its release
zip.

## License

- The whole repository (translations, glossaries, web texts and tools): **MIT with an attribution condition**, the same
  license as PES6 HD Text and the PES6 physics mod. Credit: "Mod PES6 Translations Original creado por PityCharly."
- **Konami's content is not covered:** each `.afs` is built on top of Konami's `e_text.afs` and keeps its original
  images and data, which belong to Konami.

See [LICENSE](LICENSE).

---

## Castellano

Traducciones de **Pro Evolution Soccer 6 (PC)** a idiomas que el juego no trae. Cada una es una séptima opción del
menú de idiomas: los seis idiomas originales, tu relato, el registro y `pes6.exe` quedan como estaban.

Ruso, griego y turco están probados en el juego. Serbio (latinica), croata, portugués de Brasil e indonesio son
beta, ya probados en el lab.

### Instalar un idioma

Hace falta PES 6 PC con Kitserver 6, **PES6 HD Text 1.0.2 o más nueva** y **PES6 Translations** (`translations.dll`).
Son dos descargas, en la web y en los Releases de este repo:

- **PES6 Translations**, la DLL, una sola vez: `PES6_Translations_DLL_v<versión>.zip` (tag `dll-v<versión>`).
- **Cada idioma:** `PES6_Translation_<código>_v<versión>.zip` (tag `<código>-v<versión>`). Trae solo
  `dat/<código>_text.afs`; **no** trae la DLL, y dice qué versión de la DLL necesita.

Pasos:

1. **Solo la primera vez:** abrí `hdtext.exe`, tocá **Translations: Install…** y elegí el `.zip` de la DLL. Instala
   `Kitserver\translations.dll` y la suma en `kload.cfg`, después de HD Text.
2. En `hdtext.exe`, entrá a la pestaña **Traducciones**, tocá **Install from file…** y elegí el `.zip` del idioma (sin
   descomprimir). `hdtext.exe` comprueba el manifiesto firmado que trae y deja el idioma elegido.
3. Abrí el juego y elegí el idioma nuevo en la pantalla de idiomas. El juego lo recuerda.

**A mano:** copiá las carpetas `dat` y `Kitserver` de cada `.zip` en la carpeta de tu PES 6 (donde está instalado el
juego: el juego lee `dat\` de ahí), sumá `DLL.<N> = "kitserver\translations.dll"` en `kload.cfg` después de la línea
de HD Text (y subí `DLL.num`) y elegí el idioma en la pestaña Traducciones de `hdtext.exe`.

Para cambiar de idioma, usá las Opciones del juego. Para apagar la traducción, desactivala en la pestaña Traducciones.

### Proponer un cambio

Cada idioma es un JSON en `languages/<código>/<código>.json` con solo las traducciones (`id`, `translatedText`,
`status`), su glosario (`glossary.md`, los términos que tienen que usar todos los textos) y su changelog.

- **Un texto mal:** abrí un issue con la pantalla, lo que dice y lo que tendría que decir, o un pull request que
  cambie esa línea del JSON. Cada texto es una línea, así el diff muestra justo lo que cambió.
- **Para armarlo y probarlo en tu juego**, mirá [CONTRIBUTING.md](CONTRIBUTING.md): exportás los textos de tu propia
  copia del juego, los juntás con el JSON, lo comprobás y armás el `.afs`.

### Licencia

Todo el repo (traducciones, glosarios, textos de la web y herramientas): MIT con atribución, la misma licencia que PES6
HD Text y el mod de física: "Mod PES6 Translations Original creado por PityCharly.". El contenido de Konami no
está cubierto: cada `.afs` se arma sobre el `e_text.afs` de Konami y conserva sus imágenes y datos originales, que son
de Konami. Ver [LICENSE](LICENSE).
