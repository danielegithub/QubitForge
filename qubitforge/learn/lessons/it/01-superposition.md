# Il qubit e la sovrapposizione

Un bit classico vale 0 oppure 1. Un qubit può stare in una combinazione
di |0> e |1>, detta sovrapposizione. Finché non lo misuri, entrambe le
possibilità "esistono" con certe ampiezze.

  1. qreg 1        un registro con 1 qubit (parte in |0>)
  2. state         100% |0>
  3. h 0           porta il qubit in sovrapposizione
  4. state         ora 50% |0> e 50% |1>
  5. bloch 0       sulla sfera di Bloch punta sull'equatore (|+>)
  6. run 1000      ripeti l'esperimento: ~500 zeri, ~500 uni
  7. measure 0     la misura fa collassare lo stato su 0 o su 1

Domanda: cosa mostra 'state' dopo la misura?
(I comandi funzionano anche in italiano: stato, esegui, misura...)
