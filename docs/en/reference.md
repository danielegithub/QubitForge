# Commands with examples

[README](../../README.md) · [English](../en/reference.md) · [Italiano](../it/reference.md) · [Français](../fr/reference.md) · [Deutsch](../de/reference.md) · [Español](../es/reference.md) · [Português](../pt/reference.md)

[First circuit, step by step](getting-started.md)

## Start, stop and get help

- `help`. Show all commands.
- `help cx`. Show how to enter one command. Try it when you forget which qubit goes first.
- `lesson` · `lesson 3`. List the lessons or open lesson 3 on why two qubits can give matching results.
- `example` · `example bell`. List the ready-made circuits or start the Bell circuit. Opening an example starts a fresh register.
- `explain on` · `explain off`. Show a short explanation after each operation. Use off to hide the explanations.
- `lang`. List interface languages. Use lang it for Italian or lang en for English.
- `clear`. Clear the screen in a terminal with colors enabled. The circuit is still there.
- `quit`. Close QubitForge.

## Build a circuit

- `qreg` · `qreg 3`. Show how many qubits you have. With 3, start over with three qubits at 0. You can choose from 1 to 14.
- `reset`. Put all qubits back at 0 and clear the circuit. Use this to start over with the same number of qubits.
- `undo`. Revert one operation. For measure all, undo once for each measured qubit you want to restore.
- `id 0`. Leave qubit 0 as it is. Use it to mark a step in the drawing.
- `x 0`. Flip 0 to 1 or 1 to 0. Try it after qreg 1, then use probs to see 1 at 100%.
- `h 0`. From 0, get 0 and 1 at 50% each. From 0, two h operations in a row take you back to 0.
- `x 0` · `y 0`. Both flip 0 and 1. Y also changes a phase, which can change the result of later operations.
- `z 0`. Change the sign of the number attached to 1 in state. Try the phase exercise below.
- `s 0` · `sdg 0`. Add a quarter turn of phase with s or undo that turn with sdg. Use state to see the change in the number attached to 1.
- `t 0` · `tdg 0`. Add an eighth of a turn of phase with t or undo it with tdg. Try h 0 first, then compare state before and after.
- `rx pi 0` · `ry pi/2 0` · `rz pi/2 0`. Rotate a qubit. Try rx pi 0 after qreg 1 to turn 0 into 1. Try ry pi/2 0 from 0 to get 50% each. Try rz pi/2 0 after h 0 and compare state before and after.
- `p pi/4 0`. Give the 1 part a phase change of pi/4. Use it when you want to set the phase angle yourself.
- `cx 0 1` · `cy 0 1` · `cz 0 1` · `ch 0 1`. Perform X, Y, Z or H on qubit 1 when qubit 0 is 1. Try x 0 followed by cx 0 1 after qreg 2. You get 11.
- `cp pi/4 0 1`. Change the phase of the part where both qubits are 1. Try h all first and use state to see what changed.
- `ccx 0 1 2`. Flip qubit 2 when both qubits 0 and 1 are 1. After qreg 3 and x 0 1, it takes 011 to 111.
- `swap 0 1`. Exchange two qubits. After qreg 2 and x 0, it takes 01 to 10.

Enter angles in radians before the qubit numbers. Type them without spaces, like `pi/2`. A single-qubit operation can take several qubits, for example `x 0 1`, or all of them, as in `h all`.

## Try how a phase changes the result

First run `qreg 1`, `h 0`, `h 0`, `probs`. You get `|0>` at 100%. Then enter the lines below. The extra `z 0` changes the result to `|1>` at 100%.

```qf
qreg 1
h 0
z 0
h 0
probs
```

## See what the circuit does

- `probs`. See the possible results and their percentages before measuring.
- `state`. See the numbers behind the percentages. Use it to check changes such as a plus sign becoming a minus sign while the percentages stay the same.
- `bloch 0`. See the orientation of one qubit and a value called purity. Try it after example bell. With the pair linked, qubit 0 shows purity 0.5. Without a qubit number, bloch shows all qubits.
- `circuit`. Draw the steps in order so you can check which qubits each operation used.
- `measure 0` · `measure all`. Measure qubit 0 or measure all qubits. A measurement changes the live state. Use probs afterward to see which results are still possible.
- `run 20`. Draw 20 results and count how many times each one appears. You can repeat it on the same state. With no number you get 1,024 draws. You can ask for up to 200,000.

## Save and replay

- `save bell.qf`. Save the circuit steps to a file. Pick a new filename each time. The steps include measurements you made, and a replay can draw a different result.
- `load bell.qf`. Run a file of QubitForge commands again. Use one command per line and start with qreg to start fresh. Use a filename without spaces or #.
- `qasm`. Print OpenQASM 2.0 text. Copy it if you need the circuit as text for another tool. The export keeps QubitForge's gate names.

[Save it and try it again](getting-started.md)

## Before opening QubitForge

```bash
python3 -m qubitforge --lang en --seed 42 --fast --no-color
```

- `--lang en` · `--lang it`. Use the English or Italian interface.
- `--seed 42`. Get the same random results on two launches when you repeat the same commands in the same order.
- `--fast`. Skip the wait between startup messages.
- `--no-color`. Turn off terminal colors.
- `--help`. List the options you can enter before opening the simulator.
- `bell.qf`. Run bell.qf from the current folder before showing the prompt.

```bash
python3 -m qubitforge --lang en bell.qf
```
