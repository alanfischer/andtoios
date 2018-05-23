# andtoios
andtoios.py is a simple python script to share your android localized strings with your ios storyboards/localized strings.

## Recomended workflow
Translate your android strings.xml file, resulting in a directory structure like:
- res/values/strings.xml
- res/values-de/strings.xml

Use xcode's storyboard internationalization, resulting in a directory structure like:
- Base.lproj/
- de.lproj/

Then, add another unused 'reference' language to xcode.  For this example it is called 'reference'.
- reference.lproj/

Then edit the reference.lproj/ strings files, and change the translated text to be the android string key name, such as:
- "B3f-ze-f2m.text" = "android_string_hello"

Finally, run andtoios.py as follows:
andtoios.py android/src/main/res/values-de.strings.xml ios/src/reference.lproj ios/src/de.lproj

And it will copy the correct android string entry to the de.lproj string text, including converting %s to %@.
