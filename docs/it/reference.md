# Comandi con esempi

[README](../../README.it.md) · [English](../en/reference.md) · [Italiano](../it/reference.md) · [Français](../fr/reference.md) · [Deutsch](../de/reference.md) · [Español](../es/reference.md) · [Português](../pt/reference.md)

[Il primo circuito, passo per passo](getting-started.md)

## Avvio, uscita e aiuto

- `help`. Mostra tutti i comandi.
- `help cx`. Mostra come scrivere un comando. Usalo se non ricordi quale qubit va scritto per primo.
- `lesson` · `lesson 3`. Elenca le lezioni o apri la terza, su come ottenere due valori uguali quando misuri due qubit.
- `example` · `example bell`. Elenca i circuiti già pronti o avvia quello di Bell. Aprire un esempio crea un nuovo registro.
- `explain on` · `explain off`. Mostra una breve spiegazione dopo ogni operazione. Usa off per toglierla.
- `lang`. Elenca le lingue del programma. Usa lang it per l'italiano o lang en per l'inglese.
- `clear`. Pulisce lo schermo se il terminale usa i colori. Il circuito resta disponibile.
- `quit`. Chiude QubitForge.

## Costruisci un circuito

- `qreg` · `qreg 3`. Mostra quanti qubit hai. Con 3 ricominci con tre qubit a 0. Puoi sceglierne da 1 a 14.
- `reset`. Riporta tutti i qubit a 0 e cancella il circuito. Usalo per ricominciare con lo stesso numero di qubit.
- `undo`. Annulla un'operazione. Dopo measure all, usalo una volta per ogni misura che vuoi annullare.
- `id 0`. Lascia il qubit 0 com'è. Puoi usarlo per segnare un passaggio nel disegno.
- `x 0`. Inverte 0 e 1. Provalo dopo qreg 1, poi usa probs per vedere 1 al 100%.
- `h 0`. Partendo da 0, dà il 50% a 0 e il 50% a 1. Due h di fila ti riportano a 0.
- `x 0` · `y 0`. Entrambi invertono 0 e 1. Y cambia anche una fase, che può influire sulle operazioni successive.
- `z 0`. Cambia il segno del numero associato a 1 in state. Prova l'esercizio qui sotto.
- `s 0` · `sdg 0`. Con s aggiungi un quarto di giro alla fase, con sdg lo annulli. Usa state per vedere come cambia il numero associato a 1.
- `t 0` · `tdg 0`. Con t aggiungi un ottavo di giro alla fase, con tdg lo annulli. Prova prima h 0 e confronta state prima e dopo.
- `rx pi 0` · `ry pi/2 0` · `rz pi/2 0`. Fanno ruotare un qubit. Prova rx pi 0 dopo qreg 1 per passare da 0 a 1. Prova ry pi/2 0 partendo da 0 per ottenere 50% e 50%. Prova rz pi/2 0 dopo h 0 e confronta state prima e dopo.
- `p pi/4 0`. Cambia la fase della parte associata a 1 di pi/4. Usalo per scegliere l'angolo della fase.
- `cx 0 1` · `cy 0 1` · `cz 0 1` · `ch 0 1`. Applica X, Y, Z o H al qubit 1 quando il qubit 0 vale 1. Dopo qreg 2, prova x 0 e poi cx 0 1. Ottieni 11.
- `cp pi/4 0 1`. Cambia la fase della parte in cui entrambi i qubit valgono 1. Prova prima h all e controlla cosa cambia con state.
- `ccx 0 1 2`. Inverte il qubit 2 quando sia il qubit 0 sia il qubit 1 valgono 1. Dopo qreg 3 e x 0 1, passi da 011 a 111.
- `swap 0 1`. Scambia due qubit. Dopo qreg 2 e x 0, passi da 01 a 10.

Scrivi gli angoli in radianti prima dei numeri dei qubit. Scrivi gli angoli senza spazi, come `pi/2`. Puoi applicare un'operazione a più qubit con `x 0 1` o a tutti con `h all`.

## Prova a cambiare il risultato con una fase

Prova `qreg 1`, `h 0`, `h 0`, `probs`. Ottieni `|0>` al 100%. Poi prova le righe qui sotto. Quel `z 0` in più cambia il risultato in `|1>` al 100%.

```qf
qreg 1
h 0
z 0
h 0
probs
```

## Controlla cosa fa il circuito

- `probs`. Mostra i risultati possibili e le loro percentuali prima di misurare.
- `state`. Mostra i numeri da cui vengono calcolate le percentuali. Usalo per vedere un più che diventa meno anche quando le percentuali restano uguali.
- `bloch 0`. Mostra l'orientamento del qubit e un numero chiamato purezza. Provalo dopo example bell. Nella coppia collegata il qubit 0 ha purezza 0,5. Senza numero, bloch mostra tutti i qubit.
- `circuit`. Disegna le operazioni in ordine per verificare quali qubit hai usato.
- `measure 0` · `measure all`. Misura il qubit 0 o tutti i qubit. La misura cambia lo stato del simulatore. Usa poi probs per vedere quali risultati sono ancora possibili.
- `run 20`. Estrae 20 risultati e conta quante volte esce ciascuno. Puoi ripeterlo sullo stesso stato. Senza numero fa 1.024 estrazioni. Puoi chiederne fino a 200.000.

## Salva e ripeti

- `save bell.qf`. Salva in un file i passaggi del circuito. Scegli ogni volta un nome nuovo. Il file include le misure eseguite, che possono dare un risultato diverso quando ripeti il circuito.
- `load bell.qf`. Esegue un file di comandi di QubitForge. Scrivi un comando per riga e inizia con qreg per ripartire da zero. Usa un nome senza spazi o #.
- `qasm`. Stampa il circuito come testo OpenQASM 2.0. Copialo se ti serve il circuito in un altro programma. L'esportazione conserva i nomi delle porte di QubitForge.

[Salva il circuito e riaprilo](getting-started.md)

## Prima di aprire QubitForge

```bash
python3 -m qubitforge --lang it --seed 42 --fast --no-color
```

- `--lang en` · `--lang it`. Usa l'interfaccia in inglese o in italiano.
- `--seed 42`. Ottieni gli stessi risultati casuali in due avvii se ripeti gli stessi comandi nello stesso ordine.
- `--fast`. Salta l'attesa tra i messaggi di avvio.
- `--no-color`. Disattiva i colori del terminale.
- `--help`. Elenca le opzioni che puoi usare all'avvio.
- `bell.qf`. Esegue bell.qf dalla cartella corrente prima di mostrare il prompt.

```bash
python3 -m qubitforge --lang it bell.qf
```
