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
  - PES6 Translations (translations.dll), installed only once. This zip does
    not include it: download it together with the languages.

Install with hdtext.exe (recommended)
  1. Open hdtext.exe. If it is the first time, press "Translations: Install...";
     if you already see the Translations tab, go there and press
     "Install from file...".
  2. Either way, pick this zip together with the others you downloaded
     (PES6 Translations and other languages), without unzipping them.
     hdtext.exe checks their signatures and installs PES6 Translations first
     and then the languages.
  3. Start the game and pick the new language on the language screen.
     If you installed several languages, pick which one to use in the
     Translations tab of hdtext.exe.

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
