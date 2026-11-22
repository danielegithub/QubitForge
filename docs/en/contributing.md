# Project structure and translations

[README](../../README.md) · [English](../en/contributing.md) · [Italiano](../it/contributing.md) · [Français](../fr/contributing.md) · [Deutsch](../de/contributing.md) · [Español](../es/contributing.md) · [Português](../pt/contributing.md)

## Where to find things

| File or folder | What you will find |
| --- | --- |
| [`qubitforge/core/`](../../qubitforge/core/) | Simulator and gate definitions |
| [`qubitforge/lang/`](../../qubitforge/lang/) | Command names and arguments |
| [`qubitforge/terminal/`](../../qubitforge/terminal/) | Terminal display |
| [`qubitforge/i18n/locales/`](../../qubitforge/i18n/locales/) | Interface messages |
| [`qubitforge/learn/lessons/`](../../qubitforge/learn/lessons/) | Lessons shown by lesson |
| [`qubitforge/learn/examples/`](../../qubitforge/learn/examples/) | Circuits opened by example |

## Add a language

Copy `en.json` to a new file such as `fr.json`. Translate the messages and set `meta.name` to the language name. Keep the keys and placeholders such as `{n}`. In `aliases` you can add local spellings that point to the existing commands.

To translate the lessons, copy all the files from `qubitforge/learn/lessons/en/` to a folder named with your language code. Keep the filenames and the first title line in each file. Translate the text and keep the commands runnable. With no translated lessons for a language, QubitForge opens the English lessons.

Start QubitForge with `--lang` followed by your code. Type `lang`, `help` and `lesson` to see the new menu text and lesson list. Use `example bell` and `probs` to check for two results at 50% each.

For project documentation, add a README and guides under `docs/<code>/`. Link them from the other languages.
