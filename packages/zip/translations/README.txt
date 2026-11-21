PES6 Translations (translations.dll)
====================================

The add-on that puts the languages in the language menu of PES 6 PC: a
seventh option for the language you pick in hdtext.exe. The six original
languages and your commentary stay as they were; it touches neither the
registry nor pes6.exe.

It needs PES6 HD Text. Every language's zip already includes it: loading a
language with "Load a language file…" installs it, and hdtext.exe doesn't
overwrite a newer one and keeps it updated. This zip is for installing it by
hand or for getting a newer one.

This zip has:
  Kitserver/translations.dll
  Kitserver/pes6pkg/installed/translations.json (+ .minisig)
                                  signed list of the files, for hdtext.exe

Install with hdtext.exe
  Open hdtext.exe → Languages → Load a language file… and pick this zip (or
  drop it on the window). No need to unzip it.

Install by hand
  1. Copy the Kitserver folder of this zip into your PES 6 folder.
  2. If Kitserver\kload.cfg doesn't load the DLL yet, add it after the line of
     PES6 HD Text, for example
       DLL.6 = "kitserver\translations.dll"
     and raise DLL.num by one.

Each language
  Load its .zip in hdtext.exe → Languages → Load a language file… (or, by
  hand, copy its dat and Kitserver folders into your PES 6 folder and press
  Use in Languages), then choose it on the game's language screen.

To uninstall: remove its line from kload.cfg. The game starts as before.
Code: MIT. https://github.com/angelballay/pes6xlife-translations
