# QubitForge

[English](README.md) · [Italiano](README.it.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Português](README.pt.md)

**Circuiti quantistici nel terminale**

Con QubitForge puoi provare operazioni quantistiche sul tuo computer. Puoi vedere quali risultati sono possibili, fare una misura e salvare i passaggi per ripeterli.

## Da dove cominciare

Apri il terminale nella cartella di QubitForge. Con Python 3.10 o successivo, esegui questo comando. Per usare QubitForge non servono altri pacchetti Python.

```bash
python3 -m qubitforge --lang it
```

Aspetta che appaia `qf[2q]>`. Digita una riga alla volta e premi Invio dopo ciascuna.

```qf
qreg 1
h 0
probs
```

`qreg 1` riparte con un qubit a 0. `h 0` rende 0 e 1 ugualmente probabili. `probs` mostra entrambi al 50%. Un qubit è l'elemento del simulatore che ti dà 0 oppure 1 quando lo misuri. Per uscire, usa `quit`.

Puoi usare il menu e le lezioni integrate in italiano o in inglese. I comandi funzionano in entrambe le lingue.

## Guide

- [Il primo circuito, passo per passo](docs/it/getting-started.md)
- [Comandi con esempi](docs/it/reference.md)
- [Struttura del progetto e traduzioni](docs/it/contributing.md)

## Licenza

[MIT](LICENSE)
