# The qubit and superposition

A classical bit is 0 or 1. A qubit can be in a combination of |0> and |1>,
called a superposition. Until you measure it, both possibilities "exist"
with certain amplitudes.

  1. qreg 1        a register with 1 qubit (starts in |0>)
  2. state         100% |0>
  3. h 0           put the qubit in superposition
  4. state         now 50% |0> and 50% |1>
  5. bloch 0       on the Bloch sphere it points to the equator (|+>)
  6. run 1000      repeat the experiment: ~500 zeros, ~500 ones
  7. measure 0     measuring collapses the state to 0 or 1

Question: what does 'state' show after the measurement?
