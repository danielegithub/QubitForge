# Projektaufbau und Übersetzungen

[README](../../README.de.md) · [English](../en/contributing.md) · [Italiano](../it/contributing.md) · [Français](../fr/contributing.md) · [Deutsch](../de/contributing.md) · [Español](../es/contributing.md) · [Português](../pt/contributing.md)

## Wo die Dateien liegen

| Datei oder Ordner | Was du dort findest |
| --- | --- |
| [`qubitforge/core/`](../../qubitforge/core/) | Simulator und Gatterdefinitionen |
| [`qubitforge/lang/`](../../qubitforge/lang/) | Befehlsnamen und Argumente |
| [`qubitforge/terminal/`](../../qubitforge/terminal/) | Ausgabe im Terminal |
| [`qubitforge/i18n/locales/`](../../qubitforge/i18n/locales/) | Texte der Oberfläche |
| [`qubitforge/learn/lessons/`](../../qubitforge/learn/lessons/) | Lektionen für lesson |
| [`qubitforge/learn/examples/`](../../qubitforge/learn/examples/) | Schaltungen für example |

## Eine Sprache hinzufügen

Kopiere `en.json` in eine neue Datei, etwa `de.json`. Übersetze die Meldungen und trage den Namen der Sprache unter `meta.name` ein. Behalte die Schlüssel und Platzhalter wie `{n}` bei. Unter `aliases` kannst du Wörter der neuen Sprache mit vorhandenen Befehlen verknüpfen.

Kopiere für die Lektionen alle Dateien aus `qubitforge/learn/lessons/en/` in einen Ordner mit deinem Sprachcode. Behalte die Dateinamen und den Titel in der ersten Zeile bei. Übersetze den Text und lass die Befehle unverändert. Gibt es für die Sprache keine Lektionen, öffnet QubitForge die englischen Lektionen.

Starte QubitForge mit `--lang` und deinem Sprachcode. Prüfe mit `lang`, `help` und `lesson` die neuen Meldungen und die Liste der Lektionen. Probiere `example bell` und `probs`. Es sollten zwei Ergebnisse mit je 50 % erscheinen.

Lege für die Dokumentation ein README und Anleitungen unter `docs/<code>/` an. Verlinke sie aus den anderen Sprachen.
