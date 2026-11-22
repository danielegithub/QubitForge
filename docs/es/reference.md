# Comandos con ejemplos

[README](../../README.es.md) · [English](../en/reference.md) · [Italiano](../it/reference.md) · [Français](../fr/reference.md) · [Deutsch](../de/reference.md) · [Español](../es/reference.md) · [Português](../pt/reference.md)

[Primer circuito, paso a paso](getting-started.md)

## Inicia, sal y consulta la ayuda

- `help`. Muestra todos los comandos.
- `help cx`. Muestra cómo escribir un comando. Úsalo si no recuerdas qué cúbit va primero.
- `lesson` · `lesson 3`. Lista las lecciones o abre la tercera, sobre cómo dos cúbits pueden dar el mismo resultado.
- `example` · `example bell`. Lista los circuitos incluidos o abre el de Bell. Al abrir un ejemplo empiezas con un registro nuevo.
- `explain on` · `explain off`. Muestra una explicación breve tras cada operación. Usa off para ocultarla.
- `lang`. Lista los idiomas de la interfaz. Usa lang it para italiano o lang en para inglés.
- `clear`. Limpia la pantalla si los colores de la terminal están activos. El circuito sigue disponible.
- `quit`. Cierra QubitForge.

## Construye un circuito

- `qreg` · `qreg 3`. Muestra cuántos cúbits tienes. Con 3, empieza de nuevo con tres cúbits en 0. Puedes elegir de 1 a 14.
- `reset`. Devuelve todos los cúbits a 0 y borra el circuito. Sirve para empezar de nuevo con el mismo número de cúbits.
- `undo`. Deshace una operación. Tras measure all, úsalo una vez por cada medición que quieras deshacer.
- `id 0`. Deja el cúbit 0 como está. Puedes usarlo para marcar un paso en el dibujo.
- `x 0`. Invierte 0 y 1. Pruébalo después de qreg 1 y usa probs para ver 1 con un 100 %.
- `h 0`. Desde 0, da 0 y 1 con un 50 % cada uno. Dos h seguidas te devuelven a 0.
- `x 0` · `y 0`. Ambas invierten 0 y 1. Y cambia también una fase, lo que puede cambiar el resultado de pasos posteriores.
- `z 0`. Cambia el signo del número asociado al 1 en state. Prueba el ejercicio de abajo.
- `s 0` · `sdg 0`. Con s añades un cuarto de vuelta de fase y con sdg lo quitas. Usa state para ver cómo cambia el número asociado al 1.
- `t 0` · `tdg 0`. Con t añades un octavo de vuelta de fase y con tdg lo quitas. Prueba primero h 0 y compara state antes y después.
- `rx pi 0` · `ry pi/2 0` · `rz pi/2 0`. Giran un cúbit. Prueba rx pi 0 después de qreg 1 para pasar de 0 a 1. Prueba ry pi/2 0 desde 0 para obtener un 50 % para cada valor. Prueba rz pi/2 0 después de h 0 y compara state antes y después.
- `p pi/4 0`. Cambia la fase de la parte asociada al 1 en pi/4. Úsalo para elegir el ángulo.
- `cx 0 1` · `cy 0 1` · `cz 0 1` · `ch 0 1`. Aplica X, Y, Z o H al cúbit 1 cuando el cúbit 0 vale 1. Después de qreg 2, prueba x 0 y luego cx 0 1. Obtienes 11.
- `cp pi/4 0 1`. Cambia la fase de la parte donde ambos cúbits valen 1. Prueba primero h all y mira el cambio con state.
- `ccx 0 1 2`. Invierte el cúbit 2 cuando los cúbits 0 y 1 valen 1. Después de qreg 3 y x 0 1, pasas de 011 a 111.
- `swap 0 1`. Intercambia dos cúbits. Después de qreg 2 y x 0, pasas de 01 a 10.

Escribe los ángulos en radianes antes de los números de los cúbits. Escríbelos sin espacios, como `pi/2`. Usa `x 0 1` para aplicar una operación a varios cúbits o `h all` para aplicarla a todos.

## Prueba cómo una fase cambia el resultado

Prueba `qreg 1`, `h 0`, `h 0`, `probs`. Obtienes `|0>` con un 100 %. Luego prueba las líneas de abajo. El `z 0` adicional cambia el resultado a `|1>` con un 100 %.

```qf
qreg 1
h 0
z 0
h 0
probs
```

## Comprueba qué hace el circuito

- `probs`. Muestra los resultados posibles y sus porcentajes antes de medir.
- `state`. Muestra los números de los que se obtienen los porcentajes. Sirve para ver cuándo un signo positivo pasa a negativo aunque los porcentajes sigan iguales.
- `bloch 0`. Muestra la orientación del cúbit y un número llamado pureza. Pruébalo tras example bell. Con la pareja enlazada, el cúbit 0 tiene una pureza de 0,5. Sin número, bloch muestra todos los cúbits.
- `circuit`. Dibuja las operaciones en orden para comprobar qué cúbits usaste en cada paso.
- `measure 0` · `measure all`. Mide el cúbit 0 o todos los cúbits. La medición cambia el estado del simulador. Usa luego probs para ver qué resultados siguen siendo posibles.
- `run 20`. Extrae 20 resultados y cuenta cuántas veces aparece cada uno. Puedes repetirlo con el mismo estado. Sin número hace 1024 sorteos. Puedes pedir hasta 200 000.

## Guarda y repite

- `save bell.qf`. Guarda los pasos en un archivo. Elige un nombre nuevo cada vez. Incluye las mediciones, que pueden dar otro resultado al repetir el circuito.
- `load bell.qf`. Ejecuta un archivo de comandos de QubitForge. Escribe uno por línea y empieza con qreg para partir de cero. Usa un nombre sin espacios ni #.
- `qasm`. Imprime el circuito en texto OpenQASM 2.0. Cópialo si necesitas el circuito en otra herramienta. La exportación conserva los nombres de las puertas de QubitForge.

[Guarda el circuito y vuelve a abrirlo](getting-started.md)

## Antes de abrir QubitForge

```bash
python3 -m qubitforge --lang en --seed 42 --fast --no-color
```

- `--lang en` · `--lang it`. Usa la interfaz en inglés o italiano.
- `--seed 42`. Obtén los mismos resultados aleatorios en dos inicios al repetir los mismos comandos en el mismo orden.
- `--fast`. Salta la espera entre los mensajes de inicio.
- `--no-color`. Desactiva los colores de la terminal.
- `--help`. Lista las opciones que puedes usar al iniciar.
- `bell.qf`. Ejecuta bell.qf de la carpeta actual antes de mostrar el indicador de entrada.

```bash
python3 -m qubitforge --lang en bell.qf
```
