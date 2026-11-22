# QubitForge

[English](README.md) · [Italiano](README.it.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Português](README.pt.md)

**Circuitos cuánticos en la terminal**

QubitForge te permite probar operaciones cuánticas en tu ordenador. Puedes ver qué resultados son posibles, hacer una medición y guardar los pasos para repetirlos.

## Empieza aquí

Abre una terminal en la carpeta de QubitForge. Ejecuta este comando con Python 3.10 o posterior. QubitForge funciona sin paquetes adicionales de Python.

```bash
python3 -m qubitforge --lang en
```

Espera a que aparezca `qf[2q]>`. Escribe una línea cada vez y pulsa Intro después de cada una.

```qf
qreg 1
h 0
probs
```

`qreg 1` empieza con un cúbit en 0. `h 0` hace que 0 y 1 sean igual de probables. `probs` muestra un 50 % para cada uno. Un cúbit es el elemento del simulador que da 0 o 1 al medirlo. Para salir, escribe `quit`.

Los menús y las lecciones integradas están en inglés e italiano. Los comandos funcionan en ambos idiomas.

## Guías

- [Primer circuito, paso a paso](docs/es/getting-started.md)
- [Comandos con ejemplos](docs/es/reference.md)
- [Estructura del proyecto y traducciones](docs/es/contributing.md)

## Licencia

[MIT](LICENSE)
