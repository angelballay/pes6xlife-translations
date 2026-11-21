PES6 Translations (translations.dll)
====================================

The add-on that puts the languages in the language menu of PES 6 PC: a
seventh option for the language you pick in hdtext.exe. The six original
languages and your commentary stay as they were; it touches neither the
registry nor pes6.exe.

You don't need this zip: PES6 HD Text 1.0.2 or later (hdtext.exe) installs the
add-on by itself with the first language and keeps it updated. This zip is for
installing it without internet or by hand.

This zip has:
  Kitserver/translations.dll
  Kitserver/pes6pkg/installed/translations.json (+ .minisig)
                                  signed list of the files, for hdtext.exe

Without internet
  Open hdtext.exe → Languages → Load a language file… and pick this zip
  together with the language's .zip (or drop them on the window).

By hand, without hdtext.exe
  1. Copy the Kitserver folder of this zip into your PES 6 folder.
  2. Add the DLL to Kitserver\kload.cfg after the line of HD Text, for example
       DLL.6 = "kitserver\translations.dll"
     and raise DLL.num by one.

To uninstall: remove its line from kload.cfg. The game starts as before.
Code: MIT. https://github.com/angelballay/pes6xlife-translations
