# Grover's algorithm

Grover searches an unsorted list in about √N steps instead of N.

  1. example grover    loads the circuit for 2 qubits
  2. circuit           look at it: H, oracle (CZ), diffusion
  3. state             |11> with probability 100%

With 2 qubits there are 4 items and a single round is enough. The oracle
marks |11> with a negative phase; the diffusion turns that phase into
probability. To search for another item, wrap the CZ with X gates on the
qubits that should be 0.
