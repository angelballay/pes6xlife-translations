PES6 translation (one language)
===============================

This zip adds one more language to the language menu of PES 6 PC, without
touching the six original ones. It has:

  dat/<code>_text.afs                          the game's texts in this language
  Kitserver/pes6pkg/installed/translation-<code>.json (+ .minisig)
                                               signed list of the files, for hdtext.exe

You need:
  - PES 6 PC with Kitserver 6
  - PES6 HD Text 1.0.2 or later
  - PES6 Translations (translations.dll), downloaded once from its page.
    This zip does not include it.

Install with hdtext.exe (recommended)
  1. The first time only: install PES6 Translations with the
     "Translations: Install..." button of hdtext.exe.
  2. In hdtext.exe, open the Translations tab, press "Install from file..."
     and pick this zip (no need to unzip it). hdtext.exe checks the signature
     and leaves the language chosen.
  3. Start the game and pick the new language on the language screen.

Install by hand
  Copy the dat and Kitserver folders of this zip into your PES 6 folder (the
  one the game was installed to). Then pick the language in the Translations
  tab of hdtext.exe.

To change the language, use the game's Options. To turn the translation off,
disable it in the Translations tab of hdtext.exe.

The .afs is built on top of Konami's e_text.afs: its original images and data
belong to Konami. The translations: MIT with attribution
("Mod PES6 Translations Original creado por PityCharly.").
Source, glossary and changelog: https://github.com/angelballay/pes6xlife-translations
