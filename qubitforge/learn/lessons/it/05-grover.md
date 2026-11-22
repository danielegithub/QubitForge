# Algoritmo di Grover

Grover cerca in una lista non ordinata in circa √N passi invece di N.

  1. example grover    carica il circuito per 2 qubit
  2. circuit           guardalo: H, oracolo (CZ), diffusione
  3. state             |11> con probabilità 100%

Con 2 qubit gli elementi sono 4 e basta un solo giro. L'oracolo marca
|11> con una fase negativa; la diffusione trasforma quella fase in
probabilità. Per cercare un altro elemento, metti delle X attorno al CZ
sui qubit che devono valere 0.
