# Tu primer circuito

[README](../../README.es.md) · [English](../en/getting-started.md) · [Italiano](../it/getting-started.md) · [Français](../fr/getting-started.md) · [Deutsch](../de/getting-started.md) · [Español](../es/getting-started.md) · [Português](../pt/getting-started.md)

Un circuito es una lista de pasos que ejecuta el simulador. En este ejercicio harás que dos cúbits den el mismo valor al medirlos.

Abre una terminal en la carpeta de QubitForge. Ejecuta este comando con Python 3.10 o posterior. QubitForge funciona sin paquetes adicionales de Python.

```bash
python3 -m qubitforge --lang en
```

Espera a que aparezca `qf[2q]>`. Escribe una línea cada vez y pulsa Intro después de cada una.

Los menús y las lecciones integradas están en inglés e italiano. Los comandos funcionan en ambos idiomas.

## Empieza con dos cúbits

```qf
qreg 2
```

`qreg 2` empieza de nuevo con dos cúbits en 0. Sus números son 0 y 1. En pantalla, `|01>` significa que el cúbit 1 vale 0 y el cúbit 0 vale 1. El cúbit 0 está a la derecha.

## Aplica dos operaciones

```qf
h 0
cx 0 1
probs
circuit
```

`h 0` hace que el cúbit 0 tenga un 50 % de probabilidad de dar 0 y otro 50 % de dar 1. `cx 0 1` invierte el cúbit 1 cuando el cúbit 0 vale 1. Tras ambos pasos, los cúbits dan el mismo valor cuando los mides. `probs` muestra `|00>` y `|11>` con un 50 % cada uno. `circuit` dibuja las dos operaciones en orden.

```text
q0 ──H──●──
        │
q1 ─────X──
```

## Haz varias pruebas y luego mide

```qf
run 10
measure all
probs
```

`run 10` extrae diez resultados. Solo verás `00` y `11`. Es posible que aparezcan en cantidades distintas. `measure all` mide los dos cúbits y los deja en el resultado obtenido. Después, `probs` muestra ese resultado con un 100 %.

## Guarda el circuito y vuelve a abrirlo

```qf
qreg 2
h 0
cx 0 1
save bell.qf
reset
load bell.qf
probs
```

Las tres primeras líneas vuelven a crear el circuito para guardarlo antes de medir. `save bell.qf` escribe los pasos en la carpeta desde la que abriste QubitForge. `reset` borra los pasos y pone los dos cúbits en 0. `load bell.qf` repite los pasos guardados. Elige otro nombre si `bell.qf` ya existe.

## Prueba un ejemplo incluido

```qf
example ghz
probs
lesson 3
help cx
```

`example ghz` inicia un circuito nuevo de tres cúbits. Con `probs` puedes ver que da `000` o `111`. `lesson 3` explica el circuito de dos cúbits que acabas de construir. `help cx` muestra cómo escribir la operación controlada.

## Instalación opcional

Dentro de la carpeta del proyecto, ejecuta `python3 -m pip install -e .` en tu entorno de Python. Luego puedes iniciar el simulador escribiendo `qubitforge`.

[Comandos con ejemplos](reference.md)
