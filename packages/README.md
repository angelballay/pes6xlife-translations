# Recetas de `pes6pkg`

> Formato oficial `"recipe": "pes6pkg-recipe/1"` (P-2 de `pes6-package-pc`, HEAD 4081d3b). Se arma con
> `pes6pkg build <package> <version> --recipes <pes6xlife-translations>\packages`. `"pe_version": true` en
> `Kitserver/translations.dll`: pes6pkg comprueba que el FileVersion de la DLL sea la versión del paquete (PUB-4).

Dos paquetes independientes (cambio 1 del spec):

| Receta | Paquete | Tag | Zip | Instala |
|---|---|---|---|---|
| `translations.json` | `translations` (la DLL) | `dll-v<versión>` | `PES6_Translations_DLL_v<versión>.zip` | `Kitserver/translations.dll` |
| `translation-<código>.json` | `translation-<código>` | `<código>-v<versión>` | `PES6_Translation_<código>_v<versión>.zip` | `dat/<código>_text.afs` |

El zip de un idioma **no** trae la DLL: dice en `requires` la versión mínima de `translations` (y de `hdtext`, la que
trae la pestaña Languages). `hdtext.exe` baja la DLL del índice con el primer idioma y la actualiza sola, así que la DLL
y los siete idiomas tienen que estar en el índice antes o junto con HD Text 1.0.2. Una DLL nueva que lee los mismos
`.afs` no obliga a publicar de nuevo los idiomas.

## Campos

| Campo | Qué es |
|---|---|
| `recipe` | versión de este formato provisional |
| `package`, `name` | id del paquete (FMT-7) y nombre para mostrar; pasan tal cual al manifiesto |
| `release.repo`, `release.tag`, `release.archive` | dónde se publica y cómo se llaman el tag y el zip; `{version}` es la versión que se pasa a `pes6pkg build` |
| `requires` | pasa tal cual al manifiesto: `{package, min}` |
| `bundles` | solo en los idiomas: `["translations"]`. `pes6pkg build --bundle` mete adentro del zip del idioma el paquete `translations` tal cual (sus archivos y su manifiesto firmado, sin modificar) |
| `files[].path` | ruta dentro del zip y, con `install: true`, ruta donde se instala (relativa a la carpeta del juego, FMT-8). `--from` es una carpeta con esos archivos en esas mismas rutas |
| `files[].install` | como en el manifiesto: `false` para lo que es solo para quien instala a mano (README, LEEME). Esos documentos van en `Docs/<id del paquete>/` (`Docs/translations/README.txt`, `Docs/translation-ru/LEEME.txt`…): un solo nivel, y cada paquete escribe solo en su carpeta, así el README de la DLL y el del idioma no chocan dentro de un mismo zip |
| `files[].from` | de dónde sale cada archivo, para quien arma la carpeta de `--from` (no va al manifiesto) |

`pes6pkg` agrega solo el manifiesto firmado en `Kitserver/pes6pkg/installed/<package>.json` (+ `.json.minisig`); no se
lista en `files`.

## De dónde sale cada archivo

- **`translations.dll`:** se compila en `pes6xlife_mods` con `build.ps1` (sale en `build\Release\translations.dll`).
  Su `FileVersion` tiene que ser la versión del paquete llevada a 4 números (PUB-4: `1.0` → `1.0.0.0`; la 1.0.0 ya lo
  tiene).
- **`<código>_text.afs`:** se arma con tu propio juego (no se distribuye nada de Konami fuera del zip):

  ```powershell
  python tools\pes6tr.py export "<juego>\dat" -o work\plantilla.json
  python tools\pes6tr.py merge work\plantilla.json languages\ru\ru.json -o work\ru.json
  python tools\pes6tr.py check work\ru.json
  python tools\pes6tr.py build work\ru.json --source "<juego>\dat\e_text.afs" --install afs -o work\pkg\translation-ru\dat\ru_text.afs
  ```

  La `base.sha256` de `languages/<código>/<código>.json` es la del `e_text.afs` original
  (`d90c9d8a…be7b`); con otro, `merge` no arma.
- **README.txt y LEEME.txt:** salen de `zip/translations/` (los de la DLL) y de `zip/translation/` (los de cada idioma;
  el mismo texto para todos, con `<código>` genérico). En la carpeta de `--from` y en el zip van en `Docs/<id del
  paquete>/`: `work\pkg\translations\Docs\translations\README.txt`, `work\pkg\translation-ru\Docs\translation-ru\README.txt`…

## Versiones

Cada idioma tiene su versión y su `CHANGELOG.md` en `languages/<código>/`. La primera es `1.0` para todos
(`ru`, `el`, `tr`, `sr`, `hr`, `pt-br`, `id`), y `1.0` para la DLL.
