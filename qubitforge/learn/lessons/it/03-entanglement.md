# Entanglement (la CNOT)

Due qubit possono essere correlati in modo che nessuno dei due abbia
uno stato proprio. È l'entanglement.

  1. qreg 2
  2. h 0           q0 in sovrapposizione
  3. cx 0 1        CNOT: q1 si inverte se q0 è |1>
  4. state         (|00> + |11>)/√2: uno stato di Bell
  5. bloch 0       purezza 0.5: il singolo qubit non ha uno stato definito
  6. run 1000      solo 00 o 11, mai 01 o 10
  7. measure 0  →  measure 1   il secondo risultato era deciso dal primo

Prova anche: example ghz
