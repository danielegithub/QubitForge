# QubitForge

[English](README.md) · [Italiano](README.it.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Português](README.pt.md)

**Learn quantum circuits in your terminal**

QubitForge lets you try quantum operations on your computer. You can see which results are possible, try a measurement and save the steps to repeat later.

## Start here

Open a terminal in the QubitForge folder. With Python 3.10 or later, run this command. QubitForge needs no extra Python packages to run.

```bash
python3 -m qubitforge --lang en
```

Wait for `qf[2q]>`. Then type these lines one at a time and press Enter after each line.

```qf
qreg 1
h 0
probs
```

`qreg 1` starts with one qubit at 0. `h 0` makes 0 and 1 equally likely. `probs` shows both at 50%. A qubit is the part of the simulator that gives you a 0 or a 1 when you measure it. Use `quit` to leave.

QubitForge displays its menus and built-in lessons in English or Italian. The commands below work with either language.

## Guides

- [First circuit, step by step](docs/en/getting-started.md)
- [Commands with examples](docs/en/reference.md)
- [Project structure and translations](docs/en/contributing.md)

## License

[MIT](LICENSE)
