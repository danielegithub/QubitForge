# QubitForge

[English](README.md) · [Italiano](README.it.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Português](README.pt.md)

**Circuitos quânticos no terminal**

Com o QubitForge, você pode testar operações quânticas no seu computador. Veja quais resultados são possíveis, faça uma medição e salve os passos para repetir depois.

## Comece aqui

Abra um terminal na pasta do QubitForge. Execute o comando a seguir com Python 3.10 ou mais recente. O QubitForge funciona sem pacotes adicionais do Python.

```bash
python3 -m qubitforge --lang en
```

Espere aparecer `qf[2q]>`. Digite uma linha de cada vez e pressione Enter depois de cada uma.

```qf
qreg 1
h 0
probs
```

`qreg 1` começa com um qubit em 0. `h 0` deixa 0 e 1 com a mesma chance. `probs` mostra 50% para cada resultado. Um qubit é a unidade do simulador que dá 0 ou 1 quando você a mede. Para sair, digite `quit`.

Os menus e as lições integradas estão em inglês e italiano. Os comandos funcionam nos dois idiomas.

## Guias

- [Primeiro circuito, passo a passo](docs/pt/getting-started.md)
- [Comandos com exemplos](docs/pt/reference.md)
- [Estrutura do projeto e traduções](docs/pt/contributing.md)

## Licença

[MIT](LICENSE)
