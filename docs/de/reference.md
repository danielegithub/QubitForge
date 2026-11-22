# Befehle mit Beispielen

[README](../../README.de.md) · [English](../en/reference.md) · [Italiano](../it/reference.md) · [Français](../fr/reference.md) · [Deutsch](../de/reference.md) · [Español](../es/reference.md) · [Português](../pt/reference.md)

[Erste Schaltung, Schritt für Schritt](getting-started.md)

## Starten, beenden und Hilfe finden

- `help`. Zeigt alle Befehle.
- `help cx`. Zeigt, wie du einen Befehl eingibst. Hilft, wenn du die Reihenfolge der Qubits vergessen hast.
- `lesson` · `lesson 3`. Listet die Lektionen auf oder öffnet Lektion 3 über zwei Qubits mit gleichen Messwerten.
- `example` · `example bell`. Listet die fertigen Schaltungen auf oder startet die Bell-Schaltung. Ein Beispiel beginnt mit einem neuen Register.
- `explain on` · `explain off`. Zeigt nach jeder Operation eine kurze Erklärung. Mit off blendest du sie aus.
- `lang`. Listet die Sprachen auf. Mit lang it wählst du Italienisch, mit lang en Englisch.
- `clear`. Leert den Bildschirm, wenn Terminalfarben aktiv sind. Die Schaltung bleibt erhalten.
- `quit`. Beendet QubitForge.

## Eine Schaltung bauen

- `qreg` · `qreg 3`. Zeigt die Anzahl deiner Qubits. Mit 3 startest du neu mit drei Qubits bei 0. Du kannst 1 bis 14 wählen.
- `reset`. Setzt alle Qubits auf 0 und löscht die Schaltung. Starte damit bei gleicher Qubit-Anzahl neu.
- `undo`. Macht eine Operation rückgängig. Nach measure all brauchst du den Befehl einmal pro Messung, die du zurücknehmen willst.
- `id 0`. Lässt Qubit 0 unverändert. Damit kannst du einen Schritt in der Zeichnung markieren.
- `x 0`. Vertauscht 0 und 1. Probiere es nach qreg 1 und zeige mit probs die 1 bei 100 % an.
- `h 0`. Aus 0 werden 0 und 1 mit je 50 %. Zweimal h hintereinander bringt dich wieder zu 0.
- `x 0` · `y 0`. Beide kehren 0 und 1 um. Y ändert auch eine Phase. Das kann das Ergebnis späterer Schritte ändern.
- `z 0`. Kehrt das Vorzeichen der Zahl für 1 in state um. Probiere die Übung unten.
- `s 0` · `sdg 0`. Fügt mit s eine Vierteldrehung zur Phase hinzu. sdg nimmt sie zurück. Mit state siehst du, wie sich die Zahl für 1 ändert.
- `t 0` · `tdg 0`. Fügt mit t eine Achteldrehung zur Phase hinzu. tdg nimmt sie zurück. Probiere zuerst h 0 und vergleiche state davor und danach.
- `rx pi 0` · `ry pi/2 0` · `rz pi/2 0`. Drehen ein Qubit. Mit rx pi 0 wird nach qreg 1 aus 0 eine 1. Mit ry pi/2 0 aus 0 erhältst du je 50 %. Probiere rz pi/2 0 nach h 0 und vergleiche state davor und danach.
- `p pi/4 0`. Ändert die Phase des Anteils für 1 um pi/4. Damit kannst du den Winkel selbst wählen.
- `cx 0 1` · `cy 0 1` · `cz 0 1` · `ch 0 1`. Wendet X, Y, Z oder H auf Qubit 1 an, wenn Qubit 0 den Wert 1 hat. Probiere nach qreg 2 zuerst x 0 und dann cx 0 1. Du erhältst 11.
- `cp pi/4 0 1`. Ändert die Phase des Anteils, in dem beide Qubits den Wert 1 haben. Probiere zuerst h all und prüfe die Änderung mit state.
- `ccx 0 1 2`. Kehrt Qubit 2 um, wenn Qubits 0 und 1 beide 1 sind. Nach qreg 3 und x 0 1 wird aus 011 dann 111.
- `swap 0 1`. Tauscht zwei Qubits. Nach qreg 2 und x 0 wird aus 01 dann 10.

Gib Winkel im Bogenmaß vor den Qubit-Nummern ein, ohne Leerzeichen wie in `pi/2`. Mit `x 0 1` wendest du eine Operation auf mehrere Qubits an, mit `h all` auf alle.

## So verändert eine Phase das Ergebnis

Probiere `qreg 1`, `h 0`, `h 0`, `probs`. Du erhältst `|0>` mit 100 %. Gib dann die Zeilen unten ein. Mit dem zusätzlichen `z 0` erhältst du `|1>` mit 100 %.

```qf
qreg 1
h 0
z 0
h 0
probs
```

## Die Schaltung prüfen

- `probs`. Zeigt vor der Messung die möglichen Ergebnisse und ihre Prozentwerte.
- `state`. Zeigt die Zahlen, aus denen die Prozentwerte berechnet werden. Damit siehst du zum Beispiel einen Wechsel von Plus zu Minus bei gleichen Prozentwerten.
- `bloch 0`. Zeigt die Ausrichtung eines Qubits und einen Wert namens Reinheit. Probiere es nach example bell. Beim verbundenen Paar hat Qubit 0 eine Reinheit von 0,5. Ohne Nummer zeigt bloch alle Qubits.
- `circuit`. Zeichnet die Operationen in ihrer Reihenfolge. So prüfst du, welche Qubits du verwendet hast.
- `measure 0` · `measure all`. Misst Qubit 0 oder alle Qubits. Eine Messung ändert den Zustand im Simulator. Zeige mit probs an, welche Ergebnisse danach möglich sind.
- `run 20`. Zieht 20 Ergebnisse und zählt sie. Du kannst denselben Zustand erneut verwenden. Ohne Zahl zieht der Befehl 1.024 Ergebnisse. Bis zu 200.000 sind möglich.

## Speichern und wiederholen

- `save bell.qf`. Speichert die Schritte in einer Datei. Wähle jedes Mal einen neuen Namen. Die Datei enthält auch Messungen, die beim erneuten Ausführen andere Ergebnisse liefern können.
- `load bell.qf`. Führt Befehle aus einer QubitForge-Datei aus. Schreibe einen Befehl pro Zeile und beginne mit qreg für einen Neustart. Verwende einen Namen ohne Leerzeichen oder #.
- `qasm`. Gibt die Schaltung als OpenQASM-2.0-Text aus. Kopiere den Text für ein anderes Werkzeug. Der Export übernimmt die Namen der QubitForge-Gatter.

[Speichere und lade die Schaltung](getting-started.md)

## Vor dem Start von QubitForge

```bash
python3 -m qubitforge --lang en --seed 42 --fast --no-color
```

- `--lang en` · `--lang it`. Verwendet die englische oder italienische Oberfläche.
- `--seed 42`. Erzeugt dieselben Zufallsergebnisse bei zwei Starts, wenn du dieselben Befehle in derselben Reihenfolge ausführst.
- `--fast`. Überspringt die Wartezeit zwischen Startmeldungen.
- `--no-color`. Schaltet die Terminalfarben aus.
- `--help`. Zeigt die Optionen für den Programmstart.
- `bell.qf`. Führt bell.qf aus dem aktuellen Ordner aus, bevor die Eingabe erscheint.

```bash
python3 -m qubitforge --lang en bell.qf
```
