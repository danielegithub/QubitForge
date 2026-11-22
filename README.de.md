# QubitForge

[English](README.md) · [Italiano](README.it.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Português](README.pt.md)

**Quantenschaltungen im Terminal**

Mit QubitForge kannst du Quantenoperationen auf deinem Computer ausprobieren. Sieh dir die möglichen Ergebnisse an, führe eine Messung durch und speichere die Schritte für später.

## Loslegen

Öffne ein Terminal im QubitForge-Ordner. Führe den folgenden Befehl mit Python 3.10 oder neuer aus. QubitForge braucht zum Starten keine zusätzlichen Python-Pakete.

```bash
python3 -m qubitforge --lang en
```

Warte, bis `qf[2q]>` erscheint. Gib die folgenden Zeilen einzeln ein und drücke nach jeder Zeile die Eingabetaste.

```qf
qreg 1
h 0
probs
```

`qreg 1` startet mit einem Qubit bei 0. `h 0` macht 0 und 1 gleich wahrscheinlich. `probs` zeigt für beide 50 % an. Ein Qubit ist die Einheit im Simulator, die bei einer Messung 0 oder 1 liefert. Mit `quit` beendest du das Programm.

Menüs und eingebaute Lektionen gibt es auf Englisch und Italienisch. Die Befehle funktionieren in beiden Sprachen.

## Anleitungen

- [Erste Schaltung, Schritt für Schritt](docs/de/getting-started.md)
- [Befehle mit Beispielen](docs/de/reference.md)
- [Projektaufbau und Übersetzungen](docs/de/contributing.md)

## Lizenz

[MIT](LICENSE)
