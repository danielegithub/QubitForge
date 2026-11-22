# Il tuo primo circuito

[README](../../README.it.md) · [English](../en/getting-started.md) · [Italiano](../it/getting-started.md) · [Français](../fr/getting-started.md) · [Deutsch](../de/getting-started.md) · [Español](../es/getting-started.md) · [Português](../pt/getting-started.md)

Un circuito è una lista di operazioni che vuoi far eseguire al simulatore. In questo esercizio farai in modo che due qubit diano lo stesso valore quando li misuri.

Apri il terminale nella cartella di QubitForge. Con Python 3.10 o successivo, esegui questo comando. Per usare QubitForge non servono altri pacchetti Python.

```bash
python3 -m qubitforge --lang it
```

Aspetta che appaia `qf[2q]>`. Digita una riga alla volta e premi Invio dopo ciascuna.

Puoi usare il menu e le lezioni integrate in italiano o in inglese. I comandi funzionano in entrambe le lingue.

## Parti con due qubit

```qf
qreg 2
```

`qreg 2` ricomincia con due qubit a 0. Sono numerati 0 e 1. Sullo schermo `|01>` significa che il qubit 1 è a 0 e il qubit 0 è a 1. Leggi il qubit 0 a destra.

## Applica due operazioni

```qf
h 0
cx 0 1
probs
circuit
```

`h 0` dà al qubit 0 il 50% di probabilità di dare 0 e il 50% di dare 1. `cx 0 1` inverte il qubit 1 quando il qubit 0 vale 1. Dopo questi due passaggi, i qubit danno lo stesso valore quando li misuri. `probs` mostra `|00>` e `|11>` al 50% ciascuno. `circuit` disegna le due operazioni in ordine.

```text
q0 ──H──●──
        │
q1 ─────X──
```

## Prova dei risultati e fai una misura

```qf
run 10
measure all
probs
```

`run 10` estrae dieci risultati. Vedrai solo `00` e `11`. Con dieci prove i conteggi possono essere diversi. `measure all` misura i due qubit del simulatore e li lascia nel risultato ottenuto. Il successivo `probs` mostra quel risultato al 100%.

## Salva il circuito e riaprilo

```qf
qreg 2
h 0
cx 0 1
save bell.qf
reset
load bell.qf
probs
```

Le prime tre righe ricreano il circuito così puoi salvarlo prima della misura. `save bell.qf` scrive i passaggi in un file nella cartella da cui hai avviato QubitForge. `reset` cancella le operazioni e riporta entrambi i qubit a 0. `load bell.qf` ripete i passaggi salvati. Scegli un altro nome se `bell.qf` esiste già.

## Prova un esempio già pronto

```qf
example ghz
probs
lesson 3
help cx
```

`example ghz` prepara un nuovo circuito da tre qubit. Usa `probs` per vedere che può dare `000` o `111`. `lesson 3` spiega il circuito a due qubit che hai appena fatto. `help cx` mostra come scrivere l'operazione con controllo.

## Installazione facoltativa

Dalla cartella del progetto esegui `python3 -m pip install -e .` nel tuo ambiente Python. Poi puoi avviare il simulatore digitando `qubitforge`.

[Comandi con esempi](reference.md)
