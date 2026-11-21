PES6 translation (one language)
===============================

This zip adds one more language to the language menu of PES 6 PC, without
touching the six original ones. It has:

  dat/<code>_text.afs                          the game's texts in this language
  Kitserver/pes6pkg/installed/translation-<code>.json (+ .minisig)
                                               signed list of the files, for hdtext.exe

You need PES 6 PC with Kitserver 6 and PES6 HD Text 1.0.2 or later.

Install with hdtext.exe (recommended)
  1. Download the language's .zip (no need to unzip it).
  2. Open hdtext.exe → Languages → Load a language file… and pick that
     .zip (or drop it on the window).
  3. Start PES6 and choose the language on the language screen.

  To change the language: in Languages, pick another one and press Use. None
  turns it off and Remove deletes it.

Install by hand
  Copy the dat folder of this zip into your PES 6 folder, the one the game is
  installed to, and pick the language in hdtext.exe → Languages → Use.

The .afs is built on top of Konami's e_text.afs: its original images and data
belong to Konami. The translations: MIT with attribution
("Mod PES6 Translations Original creado por PityCharly.").
Source, glossary and changelog: https://github.com/angelballay/pes6xlife-translations
