# Your first circuit

[README](../../README.md) · [English](../en/getting-started.md) · [Italiano](../it/getting-started.md) · [Français](../fr/getting-started.md) · [Deutsch](../de/getting-started.md) · [Español](../es/getting-started.md) · [Português](../pt/getting-started.md)

A circuit is a list of steps you want the simulator to perform. In this exercise you will make two qubits give the same result when measured.

Open a terminal in the QubitForge folder. With Python 3.10 or later, run this command. QubitForge needs no extra Python packages to run.

```bash
python3 -m qubitforge --lang en
```

Wait for `qf[2q]>`. Then type these lines one at a time and press Enter after each line.

QubitForge displays its menus and built-in lessons in English or Italian. The commands below work with either language.

## Start with two qubits

```qf
qreg 2
```

`qreg 2` starts over with two qubits at 0. Those qubits are numbered 0 and 1. On screen the label `|01>` means qubit 1 is 0 and qubit 0 is 1. Read qubit 0 on the right.

## Apply two operations

```qf
h 0
cx 0 1
probs
circuit
```

`h 0` gives qubit 0 a 50% chance of 0 and a 50% chance of 1. `cx 0 1` flips qubit 1 when qubit 0 is 1. Together they make the two qubits agree when measured. `probs` shows `|00>` and `|11>` at 50% each. `circuit` draws those two operations in order.

```text
q0 ──H──●──
        │
q1 ─────X──
```

## Compare a sample with a measurement

```qf
run 10
measure all
probs
```

`run 10` draws ten results. Expect only `00` and `11`. Ten tries may give an uneven split. `measure all` measures the two qubits in the simulator and leaves them at the result it picked. The following `probs` shows that result at 100%.

## Save it and try it again

```qf
qreg 2
h 0
cx 0 1
save bell.qf
reset
load bell.qf
probs
```

The first three lines rebuild the circuit so you can save it before measuring. `save bell.qf` writes the steps to a file in the folder where you started QubitForge. `reset` clears the steps and returns both qubits to 0. `load bell.qf` repeats the saved steps. Choose a fresh filename if `bell.qf` already exists.

## Try a built-in example

```qf
example ghz
probs
lesson 3
help cx
```

`example ghz` starts a fresh three-qubit circuit. Use `probs` to check that it can give `000` or `111`. `lesson 3` explains the two-qubit circuit you just made. `help cx` shows how to enter the controlled operation.

## Optional installation

From the project folder, run `python3 -m pip install -e .` in your Python environment. Then you can start the simulator by typing `qubitforge`.

[Commands with examples](reference.md)
