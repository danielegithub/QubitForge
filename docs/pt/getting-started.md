# Seu primeiro circuito

[README](../../README.pt.md) · [English](../en/getting-started.md) · [Italiano](../it/getting-started.md) · [Français](../fr/getting-started.md) · [Deutsch](../de/getting-started.md) · [Español](../es/getting-started.md) · [Português](../pt/getting-started.md)

Um circuito é uma lista de passos que o simulador executa. Neste exercício, você vai fazer com que dois qubits deem o mesmo valor quando forem medidos.

Abra um terminal na pasta do QubitForge. Execute o comando a seguir com Python 3.10 ou mais recente. O QubitForge funciona sem pacotes adicionais do Python.

```bash
python3 -m qubitforge --lang en
```

Espere aparecer `qf[2q]>`. Digite uma linha de cada vez e pressione Enter depois de cada uma.

Os menus e as lições integradas estão em inglês e italiano. Os comandos funcionam nos dois idiomas.

## Comece com dois qubits

```qf
qreg 2
```

`qreg 2` recomeça com dois qubits em 0. Eles têm os números 0 e 1. Na tela, `|01>` significa que o qubit 1 vale 0 e o qubit 0 vale 1. O qubit 0 fica à direita.

## Aplique duas operações

```qf
h 0
cx 0 1
probs
circuit
```

`h 0` dá ao qubit 0 uma chance de 50% de dar 0 e 50% de dar 1. `cx 0 1` inverte o qubit 1 quando o qubit 0 vale 1. Depois dos dois passos, os qubits dão o mesmo valor quando medidos. `probs` mostra `|00>` e `|11>` com 50% cada. `circuit` desenha as duas operações em ordem.

```text
q0 ──H──●──
        │
q1 ─────X──
```

## Experimente alguns resultados e faça uma medição

```qf
run 10
measure all
probs
```

`run 10` sorteia dez resultados. Só aparecem `00` e `11`, e as quantidades podem ser diferentes. `measure all` mede os dois qubits e os deixa no estado obtido. Depois, `probs` mostra esse resultado com 100%.

## Salve e reabra o circuito

```qf
qreg 2
h 0
cx 0 1
save bell.qf
reset
load bell.qf
probs
```

As três primeiras linhas refazem o circuito para você salvar antes da medição. `save bell.qf` grava os passos em um arquivo na pasta onde você iniciou o QubitForge. `reset` apaga os passos e coloca os dois qubits em 0. `load bell.qf` repete os passos salvos. Escolha outro nome se `bell.qf` já existir.

## Experimente um exemplo pronto

```qf
example ghz
probs
lesson 3
help cx
```

`example ghz` abre um novo circuito com três qubits. Use `probs` para ver que ele pode dar `000` ou `111`. `lesson 3` explica o circuito de dois qubits que você acabou de montar. `help cx` mostra como digitar a operação controlada.

## Instalação opcional

Na pasta do projeto, execute `python3 -m pip install -e .` no ambiente Python. Depois, você pode iniciar o simulador digitando `qubitforge`.

[Comandos com exemplos](reference.md)
