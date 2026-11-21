PES6 Translations (translations.dll)
====================================

The DLL that adds a seventh option to the language menu of PES 6 PC for the
translation you pick. The six original languages and your commentary stay as
they were; it touches neither the registry nor pes6.exe. You install it once;
each language is a separate download.

This zip has:
  Kitserver/translations.dll
  Kitserver/pes6pkg/installed/translations.json (+ .minisig)
                                  signed list of the files, for hdtext.exe

You need PES 6 PC with Kitserver 6 and PES6 HD Text 1.0.2 or later.

Install with hdtext.exe (recommended)
  Open hdtext.exe, press "Translations: Install..." and pick this zip (no need
  to unzip it). It installs translations.dll and adds it to kload.cfg, after
  HD Text, keeping a copy of the old kload.cfg. From then on hdtext.exe has the
  Translations tab, where you install each language with "Install from file...".

Install by hand
  1. Copy the Kitserver folder of this zip into your PES 6 folder.
  2. Add the DLL to Kitserver\kload.cfg after the line of HD Text, for example
       DLL.6 = "kitserver\translations.dll"
     and raise DLL.num by one.

To uninstall: remove its line from kload.cfg. The game starts as before.
Code: MIT. https://github.com/angelballay/pes6xlife-translations
