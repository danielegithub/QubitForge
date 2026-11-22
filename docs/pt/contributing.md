# Estrutura do projeto e traduções

[README](../../README.pt.md) · [English](../en/contributing.md) · [Italiano](../it/contributing.md) · [Français](../fr/contributing.md) · [Deutsch](../de/contributing.md) · [Español](../es/contributing.md) · [Português](../pt/contributing.md)

## Onde encontrar os arquivos

| Arquivo ou pasta | O que você encontra |
| --- | --- |
| [`qubitforge/core/`](../../qubitforge/core/) | Simulador e definições das portas |
| [`qubitforge/lang/`](../../qubitforge/lang/) | Nomes dos comandos e argumentos |
| [`qubitforge/terminal/`](../../qubitforge/terminal/) | Texto exibido no terminal |
| [`qubitforge/i18n/locales/`](../../qubitforge/i18n/locales/) | Mensagens da interface |
| [`qubitforge/learn/lessons/`](../../qubitforge/learn/lessons/) | Lições abertas com lesson |
| [`qubitforge/learn/examples/`](../../qubitforge/learn/examples/) | Circuitos abertos com example |

## Adicione um idioma

Copie `en.json` para um novo arquivo, por exemplo `pt.json`. Traduza as mensagens e coloque o nome do idioma em `meta.name`. Mantenha as chaves e os marcadores como `{n}`. Em `aliases`, você pode associar palavras do idioma a comandos que já existem.

Para traduzir as lições, copie todos os arquivos de `qubitforge/learn/lessons/en/` para uma pasta com o código do idioma. Mantenha os nomes dos arquivos e o título na primeira linha. Traduza o texto e preserve os comandos. Quando o idioma não tem lições, o QubitForge abre as lições em inglês.

Inicie o QubitForge com `--lang` seguido do código. Digite `lang`, `help` e `lesson` para testar as novas mensagens e a lista de lições. Use `example bell` e `probs` para conferir se aparecem dois resultados com 50% cada.

Para traduzir a documentação, adicione um README e guias em `docs/<código>/`. Crie links nos outros idiomas.
