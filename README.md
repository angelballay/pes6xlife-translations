# PES6 translations (pes6xlife-translations)

Translations of **Pro Evolution Soccer 6 (PC)** into languages the game does not ship. Each one is a seventh option of
the game's language menu: the six original languages, your commentary, the registry and `pes6.exe` stay as they were.

| Language | Code | Version | State |
|---|---|---|---|
| Русский (Russian) | `ru` | 1.0 | tested in the game |
| Ελληνικά (Greek) | `el` | 1.0 | tested in the game |
| Türkçe (Turkish) | `tr` | 1.0 | tested in the game |
| Srpski (Serbian, Latin script) | `sr` | 1.0 | beta, tested in the game |
| Hrvatski (Croatian) | `hr` | 1.0 | beta, tested in the game |
| Português do Brasil (Brazilian Portuguese) | `pt-br` | 1.0 | beta, tested in the game |
| Bahasa Indonesia (Indonesian) | `id` | 1.0 | beta, tested in the game |

Spanish below / [Castellano más abajo](#castellano).

## Install a language

You need PES 6 PC with Kitserver 6 and **PES6 HD Text 1.0.2 or later**. Each language is one `.zip`, on its page of
the website and in this repository's Releases: `PES6_Translation_<code>_v<version>.zip` (tag `<code>-v<version>`).

1. Download the language's `.zip` (no need to unzip it).
2. Open `hdtext.exe` → Languages → Load a language file… and pick that `.zip` (or drop it on the window).
3. Start PES6 and choose the language on the language screen.

The first time, `hdtext.exe` also gets a small add-on by itself (it needs internet): PES6 Translations
(`translations.dll`, tag `dll-v<version>`), which puts the languages in the game's menu and is updated by itself. To
change the language: in Languages, pick another one and press Use. None turns it off and Remove deletes it.

**Without internet, or by hand:** see the PES6 Translations page of the website. Without internet, load
`PES6_Translations_DLL_v<version>.zip` in `hdtext.exe` together with the language's `.zip`. By hand, copy the `dat` and
`Kitserver` folders of each `.zip` into your PES 6 folder (the one the game is installed to: the game reads `dat\` from
there), add `DLL.<N> = "kitserver\translations.dll"` to `kload.cfg` after HD Text's line (and raise `DLL.num`), and
pick the language in `hdtext.exe` → Languages → Use.

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

Los siete idiomas están probados en el juego. Serbio (latinica), croata, portugués de Brasil e indonesio siguen en
beta.

### Instalar un idioma

Hace falta PES 6 PC con Kitserver 6 y **PES6 HD Text 1.0.2 o más nueva**. Cada idioma es un `.zip`, en su página de
la web y en los Releases de este repo: `PES6_Translation_<código>_v<versión>.zip` (tag `<código>-v<versión>`).

1. Descargá el `.zip` del idioma (no hace falta descomprimirlo).
2. Abrí `hdtext.exe` → Languages → Load a language file… y elegí ese `.zip` (o soltalo sobre la ventana).
3. Abrí PES6 y elegí el idioma en la pantalla de idiomas.

La primera vez, `hdtext.exe` también baja solo un complemento chico (hace falta internet): PES6 Translations
(`translations.dll`, tag `dll-v<versión>`), que pone los idiomas en el menú del juego y se actualiza solo. Para cambiar
de idioma: en Languages, elegí otro y tocá Use. None lo apaga y Remove lo borra.

**Sin internet, o a mano:** mirá la página de PES6 Translations en la web. Sin internet, cargá
`PES6_Translations_DLL_v<versión>.zip` en `hdtext.exe` junto con el `.zip` del idioma. A mano, copiá las carpetas `dat` y
`Kitserver` de cada `.zip` en la carpeta de tu PES 6 (donde está instalado el juego: el juego lee `dat\` de ahí), sumá
`DLL.<N> = "kitserver\translations.dll"` en `kload.cfg` después de la línea de HD Text (y subí `DLL.num`) y elegí el
idioma en `hdtext.exe` → Languages → Use.

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
