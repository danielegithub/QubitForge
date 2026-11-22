# Deine erste Schaltung

[README](../../README.de.md) · [English](../en/getting-started.md) · [Italiano](../it/getting-started.md) · [Français](../fr/getting-started.md) · [Deutsch](../de/getting-started.md) · [Español](../es/getting-started.md) · [Português](../pt/getting-started.md)

Eine Schaltung ist eine Reihe von Schritten, die der Simulator ausführt. Hier baust du eine Schaltung, bei der zwei Qubits bei der Messung denselben Wert liefern.

Öffne ein Terminal im QubitForge-Ordner. Führe den folgenden Befehl mit Python 3.10 oder neuer aus. QubitForge braucht zum Starten keine zusätzlichen Python-Pakete.

```bash
python3 -m qubitforge --lang en
```

Warte, bis `qf[2q]>` erscheint. Gib die folgenden Zeilen einzeln ein und drücke nach jeder Zeile die Eingabetaste.

Menüs und eingebaute Lektionen gibt es auf Englisch und Italienisch. Die Befehle funktionieren in beiden Sprachen.

## Starte mit zwei Qubits

```qf
qreg 2
```

`qreg 2` startet neu mit zwei Qubits bei 0. Sie tragen die Nummern 0 und 1. `|01>` auf dem Bildschirm bedeutet, dass Qubit 1 den Wert 0 und Qubit 0 den Wert 1 hat. Qubit 0 steht rechts.

## Führe zwei Operationen aus

```qf
h 0
cx 0 1
probs
circuit
```

Nach `h 0` liefert Qubit 0 bei einer Messung mit je 50 % Wahrscheinlichkeit 0 oder 1. `cx 0 1` kehrt Qubit 1 um, wenn Qubit 0 den Wert 1 hat. Nach beiden Schritten stimmen die Messwerte überein. `probs` zeigt `|00>` und `|11>` mit je 50 %. `circuit` zeichnet die beiden Operationen in ihrer Reihenfolge.

```text
q0 ──H──●──
        │
q1 ─────X──
```

## Ziehe Stichproben und miss dann

```qf
run 10
measure all
probs
```

`run 10` zieht zehn Ergebnisse. Es erscheinen nur `00` und `11`. Die Anzahl kann unterschiedlich sein. `measure all` misst die zwei Qubits und lässt sie im Zustand des gezogenen Ergebnisses. Danach zeigt `probs` dieses Ergebnis mit 100 % an.

## Speichere und lade die Schaltung

```qf
qreg 2
h 0
cx 0 1
save bell.qf
reset
load bell.qf
probs
```

Die ersten drei Zeilen bauen die Schaltung wieder auf, damit du sie vor der Messung speichern kannst. `save bell.qf` schreibt die Schritte in den Ordner, in dem du QubitForge gestartet hast. `reset` löscht die Schritte und setzt beide Qubits auf 0. `load bell.qf` führt die gespeicherten Schritte erneut aus. Wähle einen anderen Namen, wenn `bell.qf` schon existiert.

## Probiere ein eingebautes Beispiel

```qf
example ghz
probs
lesson 3
help cx
```

`example ghz` startet eine neue Schaltung mit drei Qubits. Mit `probs` siehst du, dass `000` oder `111` herauskommen kann. `lesson 3` erklärt die Schaltung mit zwei Qubits, die du gerade gebaut hast. `help cx` zeigt die Eingabe für die gesteuerte Operation.

## Optionale Installation

Führe im Projektordner `python3 -m pip install -e .` in deiner Python-Umgebung aus. Danach kannst du den Simulator mit `qubitforge` starten.

[Befehle mit Beispielen](reference.md)
