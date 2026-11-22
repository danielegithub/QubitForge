# Comandos com exemplos

[README](../../README.pt.md) · [English](../en/reference.md) · [Italiano](../it/reference.md) · [Français](../fr/reference.md) · [Deutsch](../de/reference.md) · [Español](../es/reference.md) · [Português](../pt/reference.md)

[Primeiro circuito, passo a passo](getting-started.md)

## Inicie, saia e peça ajuda

- `help`. Mostra todos os comandos.
- `help cx`. Mostra como digitar um comando. Use quando esquecer qual qubit deve vir primeiro.
- `lesson` · `lesson 3`. Lista as lições ou abre a terceira, sobre como dois qubits podem dar o mesmo resultado.
- `example` · `example bell`. Lista os circuitos prontos ou abre o circuito de Bell. Ao abrir um exemplo, você começa com um novo registro.
- `explain on` · `explain off`. Mostra uma explicação curta depois de cada operação. Use off para ocultá-la.
- `lang`. Lista os idiomas da interface. Use lang it para italiano ou lang en para inglês.
- `clear`. Limpa a tela se as cores do terminal estiverem ativadas. O circuito continua disponível.
- `quit`. Fecha o QubitForge.

## Monte um circuito

- `qreg` · `qreg 3`. Mostra quantos qubits você tem. Com 3, recomece com três qubits em 0. Você pode escolher de 1 a 14.
- `reset`. Volta todos os qubits a 0 e apaga o circuito. Use para recomeçar com a mesma quantidade de qubits.
- `undo`. Desfaz uma operação. Depois de measure all, use uma vez para cada medição que você quiser desfazer.
- `id 0`. Deixa o qubit 0 como está. Você pode usar para marcar um passo no desenho.
- `x 0`. Inverte 0 e 1. Experimente depois de qreg 1 e use probs para ver 1 com 100%.
- `h 0`. A partir de 0, dá 0 e 1 com 50% cada. Dois h seguidos levam você de volta a 0.
- `x 0` · `y 0`. As duas operações invertem 0 e 1. Y também muda uma fase, o que pode mudar o resultado de passos posteriores.
- `z 0`. Inverte o sinal do número associado a 1 em state. Faça o exercício abaixo.
- `s 0` · `sdg 0`. Acrescente um quarto de volta à fase com s ou desfaça essa volta com sdg. Use state para ver mudar o número associado a 1.
- `t 0` · `tdg 0`. Acrescente um oitavo de volta à fase com t ou desfaça essa volta com tdg. Experimente h 0 primeiro e compare state antes e depois.
- `rx pi 0` · `ry pi/2 0` · `rz pi/2 0`. Giram um qubit. Experimente rx pi 0 depois de qreg 1 para ir de 0 a 1. Experimente ry pi/2 0 a partir de 0 para obter 50% para cada valor. Experimente rz pi/2 0 depois de h 0 e compare state antes e depois.
- `p pi/4 0`. Muda em pi/4 a fase da parte associada a 1. Use para escolher o ângulo.
- `cx 0 1` · `cy 0 1` · `cz 0 1` · `ch 0 1`. Aplica X, Y, Z ou H ao qubit 1 quando o qubit 0 vale 1. Depois de qreg 2, experimente x 0 e depois cx 0 1. Você obtém 11.
- `cp pi/4 0 1`. Muda a fase da parte em que os dois qubits valem 1. Experimente h all primeiro e veja a mudança com state.
- `ccx 0 1 2`. Inverte o qubit 2 quando os qubits 0 e 1 valem 1. Depois de qreg 3 e x 0 1, 011 vira 111.
- `swap 0 1`. Troca dois qubits. Depois de qreg 2 e x 0, 01 vira 10.

Digite os ângulos em radianos antes dos números dos qubits. Escreva sem espaços, como `pi/2`. Use `x 0 1` para aplicar uma operação a vários qubits ou `h all` para aplicar a todos.

## Veja como a fase muda o resultado

Experimente `qreg 1`, `h 0`, `h 0`, `probs`. Você obtém `|0>` com 100%. Depois, digite as linhas abaixo. O `z 0` a mais muda o resultado para `|1>` com 100%.

```qf
qreg 1
h 0
z 0
h 0
probs
```

## Veja o que o circuito faz

- `probs`. Mostra os resultados possíveis e suas porcentagens antes da medição.
- `state`. Mostra os números usados para calcular as porcentagens. Use para ver quando um sinal positivo vira negativo e as porcentagens continuam iguais.
- `bloch 0`. Mostra a orientação do qubit e um número chamado pureza. Experimente depois de example bell. Com o par ligado, o qubit 0 tem pureza 0,5. Sem número, bloch mostra todos os qubits.
- `circuit`. Desenha as operações em ordem para você conferir quais qubits foram usados.
- `measure 0` · `measure all`. Mede o qubit 0 ou todos os qubits. A medição altera o estado do simulador. Use probs em seguida para ver quais resultados ainda são possíveis.
- `run 20`. Sorteia 20 resultados e conta quantas vezes cada um aparece. Você pode repetir com o mesmo estado. Sem número são 1.024 sorteios. Você pode pedir até 200.000.

## Salve e repita

- `save bell.qf`. Salva os passos em um arquivo. Escolha um nome novo a cada vez. O arquivo inclui as medições, que podem dar outro resultado quando você repete o circuito.
- `load bell.qf`. Executa um arquivo de comandos do QubitForge. Escreva um comando por linha e comece com qreg para partir do zero. Use um nome sem espaço ou #.
- `qasm`. Mostra o circuito como texto OpenQASM 2.0. Copie o texto para usar o circuito em outra ferramenta. A exportação mantém os nomes das portas do QubitForge.

[Salve e reabra o circuito](getting-started.md)

## Antes de abrir o QubitForge

```bash
python3 -m qubitforge --lang en --seed 42 --fast --no-color
```

- `--lang en` · `--lang it`. Usa a interface em inglês ou italiano.
- `--seed 42`. Gera os mesmos resultados aleatórios em duas execuções quando você repete os mesmos comandos na mesma ordem.
- `--fast`. Pula a espera entre as mensagens de início.
- `--no-color`. Desativa as cores do terminal.
- `--help`. Lista as opções que você pode usar ao iniciar.
- `bell.qf`. Executa bell.qf da pasta atual antes de mostrar a linha de entrada.

```bash
python3 -m qubitforge --lang en bell.qf
```
