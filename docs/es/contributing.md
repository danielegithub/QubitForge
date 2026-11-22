# Estructura del proyecto y traducciones

[README](../../README.es.md) · [English](../en/contributing.md) · [Italiano](../it/contributing.md) · [Français](../fr/contributing.md) · [Deutsch](../de/contributing.md) · [Español](../es/contributing.md) · [Português](../pt/contributing.md)

## Dónde encontrar los archivos

| Archivo o carpeta | Qué encontrarás |
| --- | --- |
| [`qubitforge/core/`](../../qubitforge/core/) | Simulador y definición de las puertas |
| [`qubitforge/lang/`](../../qubitforge/lang/) | Nombres de los comandos y argumentos |
| [`qubitforge/terminal/`](../../qubitforge/terminal/) | Texto que se muestra en la terminal |
| [`qubitforge/i18n/locales/`](../../qubitforge/i18n/locales/) | Mensajes de la interfaz |
| [`qubitforge/learn/lessons/`](../../qubitforge/learn/lessons/) | Lecciones que abre lesson |
| [`qubitforge/learn/examples/`](../../qubitforge/learn/examples/) | Circuitos que abre example |

## Añade un idioma

Copia `en.json` en un archivo nuevo, por ejemplo `es.json`. Traduce los mensajes y escribe el nombre del idioma en `meta.name`. Conserva las claves y los marcadores como `{n}`. En `aliases` puedes asociar palabras del nuevo idioma a comandos existentes.

Para traducir las lecciones, copia todos los archivos de `qubitforge/learn/lessons/en/` en una carpeta con tu código de idioma. Conserva los nombres de archivo y el título de la primera línea. Traduce el texto y conserva los comandos. Si no hay lecciones para un idioma, QubitForge abre las lecciones en inglés.

Inicia QubitForge con `--lang` seguido de tu código. Escribe `lang`, `help` y `lesson` para comprobar los nuevos mensajes y la lista de lecciones. Prueba `example bell` y `probs` para ver si aparecen dos resultados con un 50 % cada uno.

Para traducir la documentación, añade un README y guías en `docs/<código>/`. Enlázalos desde los demás idiomas.
