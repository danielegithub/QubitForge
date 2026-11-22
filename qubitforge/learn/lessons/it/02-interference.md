# Interferenza

Le ampiezze hanno un segno (una fase): possono sommarsi o annullarsi.
Questo è il vero motore del calcolo quantistico.

  1. qreg 1
  2. h 0           sovrapposizione 50/50
  3. h 0           di nuovo H: le ampiezze di |1> si annullano!
  4. state         sei tornato a |0> al 100%

Ora metti una fase nel mezzo:
  5. reset  →  h 0  →  z 0  →  h 0  →  state
     Z inverte il segno di |1>, e il secondo H ti porta a |1>.

Senza Z i due cammini verso |1> interferiscono in modo distruttivo.
Con Z interferiscono in modo costruttivo.
