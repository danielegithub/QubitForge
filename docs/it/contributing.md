# Struttura del progetto e traduzioni

[README](../../README.it.md) · [English](../en/contributing.md) · [Italiano](../it/contributing.md) · [Français](../fr/contributing.md) · [Deutsch](../de/contributing.md) · [Español](../es/contributing.md) · [Português](../pt/contributing.md)

## Dove trovare i file

| File o cartella | Cosa trovi |
| --- | --- |
| [`qubitforge/core/`](../../qubitforge/core/) | Simulatore e definizioni delle porte |
| [`qubitforge/lang/`](../../qubitforge/lang/) | Nomi dei comandi e argomenti |
| [`qubitforge/terminal/`](../../qubitforge/terminal/) | Visualizzazione nel terminale |
| [`qubitforge/i18n/locales/`](../../qubitforge/i18n/locales/) | Messaggi dell'interfaccia |
| [`qubitforge/learn/lessons/`](../../qubitforge/learn/lessons/) | Lezioni aperte da lesson |
| [`qubitforge/learn/examples/`](../../qubitforge/learn/examples/) | Circuiti aperti da example |

## Aggiungi una lingua

Copia `en.json` in un nuovo file, per esempio `fr.json`. Traduci i messaggi e scrivi il nome della lingua in `meta.name`. Conserva chiavi e segnaposto come `{n}`. In `aliases` puoi associare parole della nuova lingua ai comandi già disponibili.

Per tradurre le lezioni, copia tutti i file da `qubitforge/learn/lessons/en/` in una cartella con il tuo codice lingua. Conserva i nomi dei file e il titolo sulla prima riga. Traduci il testo e mantieni i comandi eseguibili. Se non ci sono lezioni per una lingua, QubitForge apre quelle in inglese.

Avvia QubitForge con `--lang` seguito dal tuo codice. Digita `lang`, `help` e `lesson` per vedere i nuovi messaggi e l'elenco delle lezioni. Prova `example bell` e `probs` per controllare che escano due risultati al 50%.

Per tradurre la documentazione, aggiungi un README e le guide in `docs/<codice>/`. Aggiungi i link dalle altre lingue.
