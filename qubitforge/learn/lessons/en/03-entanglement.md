# Entanglement (the CNOT)

Two qubits can be correlated so that neither has a state of its own.
This is entanglement.

  1. qreg 2
  2. h 0           q0 in superposition
  3. cx 0 1        CNOT: q1 flips if q0 is |1>
  4. state         (|00> + |11>)/√2: a Bell state
  5. bloch 0       purity 0.5: a single qubit has no definite state
  6. run 1000      only 00 or 11, never 01 or 10
  7. measure 0  →  measure 1   the second result was decided by the first

Also try: example ghz
