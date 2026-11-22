# QubitForge

A quantum computer in your terminal, made for learning. Pure Python, no dependencies.

```
╭─────────────────────────────────╮
│  ⟨0|  Q U B I T F O R G E  |1⟩  │
╰─────────────────────────────────╯
qf[2q]> h 0
qf[2q]> cx 0 1
qf[2q]> circuit
q0 ──H──●──
        │
q1 ─────X──
```

## Run

```bash
python3 -m qubitforge            # or: pip install -e . && qubitforge
python3 -m qubitforge --lang it  # interface language (en, it)
python3 -m qubitforge my.qf      # run a script first, then open the prompt
```

Options: `--lang`, `--seed` (reproducible measurements), `--fast` (skip boot animation), `--no-color`.

## What you can do

| Area | Commands |
|---|---|
| Register | `qreg n`, `reset`, `undo` |
| Gates | `h x y z s t id rx ry rz p cx cy cz ch cp ccx swap sdg tdg` |
| Inspect | `state`, `probs`, `bloch [q]`, `circuit`, `qasm` |
| Measure | `measure [q\|all]`, `run [shots]` |
| Files | `save f.qf`, `load f.qf` |
| Learn | `lesson [n]`, `example [name]`, `explain on`, `help [cmd]` |

Gates take parameters first, then qubits: `rx pi/2 0`, `cx 0 1`, `ccx 0 1 2`. Single-qubit gates broadcast: `h all`, `x 0 2`.
Convention: `q0` is the rightmost bit of a state label, `|q2 q1 q0>`.

## Layout

```
qubitforge/
├── core/       the "chip": gates, state vector, machine, analysis (knows nothing about the terminal)
├── lang/       the command language: registry, dispatcher, angle expressions
├── terminal/   boot animation, prompt loop, rendering, colors
├── i18n/       translations: locales/<code>.json
└── learn/      lessons/<code>/*.md and examples/*.qf
tests/
```

## Add a language

1. Copy `qubitforge/i18n/locales/en.json` to `<code>.json` and translate it (add command `aliases` if you like).
2. Optionally add lessons in `qubitforge/learn/lessons/<code>/` (missing ones fall back to English).

The test suite fails if a language is missing any key.

## Tests

```bash
python3 -m unittest discover -s tests -t .
```

## License

MIT. See [LICENSE](LICENSE).
