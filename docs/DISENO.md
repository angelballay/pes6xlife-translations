# Traducciones de PES6: diseño del JSON

Objetivo: sacar todos los textos del juego de un `X_text.afs` a un JSON, traducirlo de a poco a otros idiomas y, con otra herramienta, volver a armar el AFS con los textos traducidos.

## Uso

```powershell
python tools\pes6tr.py export "<juego>\dat" -o work\plantilla_tr.json --language tr --label "Türkçe"
```

- **Qué toma:** usa `e_text.afs` como base (`--base` cambia el idioma) y los otros `X_text.afs` de la carpeta como referencia.
- **Requisitos:** solo la biblioteca estándar de Python 3.
- **Tiempo:** alrededor de 1 s con los 6 idiomas.

Este documento explica cómo es el formato y por qué. Los datos salen de los seis `X_text.afs` oficiales (e, f, g, i, p, s), medidos el 2026-11-19. Lo que se sabe del formato del juego está documentado en `pes6xlife` (vault, `SRC-s-text-afs`).

## 1. Qué hay en un `X_text.afs`

- **421 entradas** en cada idioma:
  - **29 tablas de texto** comprimidas con zlib (cabecera `00 06 01 00`), en UTF-8;
  - **392 entradas más** (cabecera `00 02 00 00`), que son imágenes. Algunas tienen palabras dibujadas y cambian según el idioma.
- **Cada tabla de texto tiene bloques.** Cada bloque tiene una etiqueta (`tag`) y una lista de registros `{id, x, bytes, chars, off}` con su cadena terminada en `\0`. En total son 224 bloques y 14 991 registros.
- **El juego pide cada texto con `text_id = tag << 16 | id`.** Su obtenedor busca la tabla por `tag`, no por el número de entrada.

## 2. La clave: `tag:id`, no la posición

Medido en los seis idiomas:

| Dato | Valor |
|---|---|
| Registros | 14 991 |
| Claves `(tag, id)` distintas | **9 299**, el mismo conjunto en los 6 idiomas |
| Claves con más de un texto distinto | **0** |
| Claves repetidas (la misma tabla en varias entradas) | 3 579, hasta 5 copias cada una |
| Claves con texto en inglés | 9 093; las otras 206 están vacías |

Por qué la clave es `tag:id`:
- **El número de entrada no sirve.** En inglés, francés, alemán e italiano las tablas están en otras entradas que en español y polaco. Por ejemplo, la última está en la 416 en inglés, en la 417 en francés y en la 418 en español. También cambia la distribución en bloques: los textos del editor ocupan 27 bloques en inglés y 2 en español.
- **`tag:id` es lo que pide el juego,** y es igual en los 6 idiomas. Así, el mismo JSON sirve para armar el AFS de cualquier lugar (inglés, francés, español…).
- **Cada texto aparece una sola vez en el JSON.** Se pasa de 14 991 registros a 9 093 textos, y el armador escribe la traducción en todas las copias.

## 3. Códigos de control: fichas legibles

Los textos traen códigos que hay que conservar. Gramática medida en los 6 idiomas (7 603 apariciones, todas encajan salvo una de español que viene cortada):

| Código en el juego | Qué es | Ficha en el JSON |
|---|---|---|
| `\x11c` + 8 hex | color RGBA (`ffffffff` blanco, `ffdc28ff` amarillo…) | `{c:ffdc28ff}` |
| `\x11w` + 2 hex | sin confirmar (`ff`, `fe`, `00`, `fd`) | `{w:ff}` |
| `\x11k`, `\x11l`, `\x11j`, `\x11n`, `\x11p` + una letra | íconos (botones del mando, etc.), sin confirmar | `{k:a}`, `{l:b}`… |
| caracteres de uso privado U+E000…F8FF (665 veces, 66 distintos) | íconos de botones del mando que dibuja la fuente | `{i:e087}` |
| salto de línea `\x0A` | salto de línea | `\n` (el normal de JSON) |
| `{` y `}` literales (aparecen en 3 textos en alemán) | texto | `{{` y `}}` |
| cualquier otro carácter de control | | `{u:0011}` (su código) |

Por qué fichas y no el carácter `\u0011` crudo:
- Quien traduce (una persona o un modelo) ve `{c:ffdc28ff}Pase{c:ffffffff}` en lugar de caracteres invisibles. Es difícil borrar una por error.
- La conversión es exacta en las dos direcciones. El exportador la verifica en cada texto y no escribe el JSON si alguno no vuelve idéntico.

**Formatos de `printf`** (`%d` 2 259 veces, `%s` 2 209, `%3d`, `%03d`, `%f`, `%%`): quedan como están, porque son legibles y el juego los necesita así.
- Una traducción puede cambiar el orden de las fichas y de los `%`, pero no su cantidad.
- Ojo: en francés aparece `% d` como texto ("100 % des…"), y `printf` lo lee como un formato. El validador avisa de esos casos.

## 4. El archivo

```json
{
  "schema": "pes6-text-translation/1",
  "format": "afs",
  "file_name_output": "e_text.afs",
  "language": "tr",
  "language_label": "Türkçe",
  "install": "afs2fs",
  "base": { "file": "e_text.afs", "lang": "e", "sha256": "d90c9d8a…", "records": 14991, "texts": 9093 },
  "texts": [
    {
      "id": "52:0",
      "defaultText": "{c:ffdc28ff}Match{c:ffffffff}",
      "translatedText": "",
      "status": "todo",
      "maxLength": 13,
      "reference": { "fr": "…", "de": "…", "it": "…", "es": "…", "pl": "…" }
    }
  ]
}
```

| Campo | Qué es |
|---|---|
| `schema` | versión del formato, para poder cambiarlo sin romper traducciones viejas |
| `format` | siempre `afs` |
| `file_name_output` | el archivo que se arma, o sea, el lugar de idioma que ocupa (`e_text.afs`, `f_text.afs`…) |
| `language`, `language_label` | código (`tr`, `el`, `ru`…) y nombre en su idioma |
| `language_title` | opcional: la palabra "Language" en ese idioma, para el menú de idiomas (ver 5) |
| `install` | `afs2fs` (carpeta `Kitserver\dat\<archivo>\`, sin tocar el original) o `afs` (el archivo completo) |
| `base` | de qué AFS salió, con su SHA-256, para saber si el JSON corresponde al archivo que se usa |
| `id` | `tag:id` en decimal, la clave del juego |
| `defaultText` | el inglés, con fichas |
| `translatedText` | la traducción, con las mismas fichas; vacío mientras no esté hecha |
| `status` | `todo`, `draft` o `done` |
| `maxLength` | **solo una guía:** la línea visible más larga entre los 6 idiomas oficiales (sin contar fichas). Si la traducción lo supera mucho, puede no entrar en pantalla |
| `sameInAllLanguages` | aparece solo si el texto es igual en los 6 idiomas (1 135 casos: nombres, números, siglas). Puede que no haga falta traducirlo |
| `reference` | el mismo texto en los otros idiomas oficiales, como contexto. Sirve para desambiguar: hay 1 138 textos ingleses que el español traduce de dos o más formas según la pantalla |

**Orden:** el del archivo base, por primera aparición. Así, los textos de una misma pantalla quedan juntos.

**Qué queda fuera:**
- los registros vacíos en el idioma base (el armador los deja vacíos). Con base inglés son 206. Siete de ellos (`100:2`, `100:6`, `100:8`, `100:19`…) solo tienen texto en polaco: son nombres de conectores de PS2;
- los campos internos (`x`, `bytes`, `chars`, cabeceras): el armador los toma del AFS base y recalcula `bytes` y `chars`.

## 5. El armador (`build`) y el validador (`check`)

```powershell
python tools\pes6tr.py check work\tr.json
python tools\pes6tr.py build work\tr.json --dat "<juego>\dat" -o work\tr
```

### Qué AFS toma de partida

- **Con `--dat`:** usa el archivo de `file_name_output` si está en esa carpeta. Si no está, usa el de la base.
  - Partir del archivo del mismo lugar conserva sus imágenes y su orden.
  - Si se parte de otro, el AFS queda con el orden de ese otro. Según el estudio estático, el orden no importa (el mismo exe funciona con los dos órdenes y busca por `tag`), pero eso no se confirmó en el juego.
- **Con `--source`:** usa el AFS que se le indique.

### Qué texto va en cada registro

Cada registro se busca por `tag:id`:
- `translatedText`, si no está vacío y es válido;
- si no, el respaldo:
  - `--fallback default` (por defecto): el inglés del JSON;
  - `--fallback source`: el del AFS de partida.

Los registros vacíos quedan vacíos.

### Validación

**Errores**, que frenan el armado salvo con `--skip-invalid` (en ese caso esos textos usan el respaldo):
- una llave suelta;
- fichas distintas a las del inglés: el orden puede cambiar, la cantidad no;
- formatos `%` distintos. Un `%` mal puesto puede colgar el juego; un `%` suelto se escribe `%%`.

**Avisos:**
- cambia la cantidad de saltos de línea;
- una línea supera en más del 30 % al `maxLength`.

### Cómo se rearma cada tabla

Es el formato medido en los 174 originales (29 × 6). Con un JSON sin traducir, las 174 vuelven **idénticas byte a byte** (descomprimidas).
- **Cuerpo:** `{nblk, 8, offs[nblk], 8}`, alineado a 16.
- **Cada bloque, alineado a 16:**
  - cabecera de 32 bytes `{0x400, L, L, 0…}`, con `L` = tabla + cadenas;
  - la tabla `{cnt, tag, {id, x, bytes, chars, off}…}`;
  - las cadenas seguidas, en el orden de los registros, terminadas en `\0`;
  - relleno con ceros.
- **`bytes` y `chars`:** `bytes` = largo UTF-8 + 1. `chars` = cantidad de caracteres; solo se recalcula si el texto cambió, porque hay un registro español con un `chars` que no coincide y así se conserva.
- **La entrada:** cabecera `{0x00010600, comprimido, descomprimido, 0…}` (32 bytes) + zlib.
  - El zlib comprimido no es idéntico al de Konami: es otra implementación.
  - El juego descomprime cualquier zlib estándar.

### Salida

- **`afs2fs` (por defecto):** `<salida>\kitserver\dat\<archivo>\unnamed_<N>.bin`, una por tabla de texto.
  - afs2fs toma cualquier archivo con `_<N>` en el nombre como la entrada `N`, tal cual (cabecera incluida).
  - Se instala copiando `<salida>\kitserver` encima del `kitserver` del juego, y no toca el AFS original.
  - Hace falta el AFS del mismo lugar como partida, porque los números de entrada cambian según el idioma.
- **`afs`:** `<salida>\dat\<archivo>`.
  - La misma cabecera hasta `0x1000` (incluye un puntero viejo a la tabla de nombres, que ya apuntaba a datos).
  - Cada entrada empieza en el siguiente múltiplo de `0x800`, como en los originales.
  - Las 392 entradas que no son texto van byte a byte.

### Verificado sin el juego (2026-11-19)

Con una traducción de prueba (todos los textos con prefijo griego) armada en los lugares inglés, francés y español:
- al volver a exportar, los 14 991 registros dan el texto esperado;
- las entradas que no son texto son idénticas;
- los `.bin` de afs2fs son iguales a las entradas del AFS completo.

**No se probó en el juego.**

### Menú de idiomas

El juego tiene un menú con los seis lugares. Sus textos están en la tabla 52:
- el nombre de cada lugar: `52:64` English, `52:65` Français, `52:66` Deutsch, `52:67` Italiano y `52:68` Español;
- la palabra "Language" en el idioma de cada lugar, de `52:71` a `52:75`.

Al armar un lugar, el armador pone en esos dos textos `language_label` y `language_title` (campo opcional del JSON; en ruso, «Язык»). El polaco no tiene par en esa tabla, así que en ese lugar no se cambia nada.

Cada lugar lee estos nombres de su propio AFS. Mientras el jugador usa otro idioma, el lugar sigue con su nombre de siempre ("Deutsch"); cuando lo elige, el menú muestra «Русский».

## 6. Instalación a la antigua (reemplazada)

Primero se probó publicar la traducción ocupando el lugar alemán (`r_text.afs` copiado como `g_text.afs`, con un instalador que tocaba `lang_g`). La decisión del usuario del 2026-11-20 la reemplazó por el idioma extra de `translations.dll` (`MODULO_IDIOMA.md` de `pes6xlife_mods`), que no pisa ningún idioma ni toca el registro, y el instalador se sacó del repo. Lo que se aprendió en esa prueba sigue valiendo:

**Se parte del archivo inglés, no del alemán.** Hay imágenes con palabras dibujadas, y el primer armado sobre `g_text.afs` mostró el menú principal en alemán (prueba del usuario, 2026-11-20).
- Hay 392 imágenes por idioma. Las que no son iguales en los 6 idiomas son 39, en inglés estas: 0, 15, 128, 151, 157, 158, 173, 192, 197, 284, 286, 288–298, 300, 301, 303–310, 349, **356** (el menú principal), 359, 364, 369, 415 y 420.
- Partiendo de `e_text.afs` esas imágenes quedan en inglés.
- Lo completo, como en los parches que traducen el menú, es redibujar esas 39 imágenes en el idioma nuevo.

**Qué idioma se guarda.** El juego guarda solo el idioma del relato, en el byte +5 de la configuración del sistema (`0x008612E0`, archivo de opciones); `0x00B19320` lo lee al cargar. El del texto no se guarda: en cada arranque `0x00870EF0` lo elige por el idioma de Windows si hay uno solo instalado, o muestra la pantalla de idioma si hay más de uno.

### Lo que falta

- **Las letras.** Los caracteres nuevos (griego, cirílico, latín extendido) tienen que estar en la fuente. Eso lo resuelve PES6 HD Text / Pes6FontCreator, no este armador.

## 7. Contenido del juego

El JSON incluye los textos del juego (el inglés y las referencias), así que la salida del exportador no se versiona en este repo. `.gitignore` excluye `work/`, donde se trabaja con los JSON completos.

## 8. El JSON liviano (lo que va en git)

En `languages/<código>/<código>.json` está solo lo que es de la traducción, con `schema` `pes6-text-translation-light/1`:

- **Cabecera:** `file_name_output`, `language`, `language_label`, `language_title` (opcional), `install` y `base` (`file`, `lang`, `sha256`, `records`, `texts`). La `base` ata la traducción al `e_text.afs` original: `merge` no arma nada con una plantilla de otro archivo.
- **Cada texto:** `id`, `translatedText` y `status`. Solo los traducidos. No van `defaultText`, `reference`, `maxLength` ni `sameInAllLanguages`: son textos o datos del juego, y salen de la plantilla de cada uno.
- **Un texto por línea**, para que cada cambio de traducción sea una línea del diff.

```powershell
python tools\pes6tr.py export "<juego>\dat" -o work\plantilla.json
python tools\pes6tr.py merge work\plantilla.json languages\tr\tr.json -o work\tr.json
python tools\pes6tr.py check work\tr.json
python tools\pes6tr.py build work\tr.json --source "<juego>\dat\e_text.afs" --install afs -o work\tr_text.afs
python tools\pes6tr.py strip work\tr.json -o languages\tr\tr.json
```

- `merge` falla si el SHA-256 de la base no coincide o si un `id` de la traducción no está en la plantilla.
- `strip` de lo que dio `merge` devuelve el mismo archivo, byte a byte.

