# Fasi e rotazioni

H, X e Z sono casi speciali: puoi ruotare di un angolo qualsiasi.
Gli angoli accettano pi, per esempio pi/2 oppure 2*pi/3.

  1. qreg 1
  2. ry pi/3 0     ruota di 60° attorno a Y
  3. bloch 0       guarda come si sposta il vettore
  4. probs         P(1) = sin²(θ/2) = 25%
  5. rz pi/2 0     cambia solo la fase: le probabilità restano uguali
  6. h 0           ma ora la fase si vede dopo una H!
  7. probs

Idea chiave: la fase non si vede se misuri subito, ma influenza
tutto ciò che viene dopo.
