# Ton premier circuit

[README](../../README.fr.md) · [English](../en/getting-started.md) · [Italiano](../it/getting-started.md) · [Français](../fr/getting-started.md) · [Deutsch](../de/getting-started.md) · [Español](../es/getting-started.md) · [Português](../pt/getting-started.md)

Un circuit est une suite d'opérations que le simulateur exécute. Dans cet exercice, tu vas faire en sorte que deux qubits donnent le même résultat à la mesure.

Ouvre un terminal dans le dossier QubitForge. Avec Python 3.10 ou une version plus récente, lance cette commande. QubitForge fonctionne sans paquet Python supplémentaire.

```bash
python3 -m qubitforge --lang en
```

Attends de voir `qf[2q]>`. Saisis une ligne à la fois et appuie sur Entrée après chacune.

Les menus et les leçons intégrées sont en anglais ou en italien. Les commandes fonctionnent dans les deux langues.

## Commence avec deux qubits

```qf
qreg 2
```

`qreg 2` repart avec deux qubits à 0. Ils portent les numéros 0 et 1. À l'écran, `|01>` signifie que le qubit 1 vaut 0 et que le qubit 0 vaut 1. Le qubit 0 se lit à droite.

## Applique deux opérations

```qf
h 0
cx 0 1
probs
circuit
```

`h 0` donne au qubit 0 une chance sur deux de donner 0 et une chance sur deux de donner 1. `cx 0 1` inverse le qubit 1 quand le qubit 0 vaut 1. Après ces étapes, les deux qubits donnent le même résultat à la mesure. `probs` affiche `|00>` et `|11>` à 50 % chacun. `circuit` dessine les deux opérations dans l'ordre.

```text
q0 ──H──●──
        │
q1 ─────X──
```

## Fais des tirages puis une mesure

```qf
run 10
measure all
probs
```

`run 10` tire dix résultats. Tu verras uniquement `00` et `11`, avec parfois des nombres différents. `measure all` mesure les deux qubits et les laisse dans l'état obtenu. Ensuite, `probs` affiche ce résultat à 100 %.

## Enregistre le circuit et rouvre-le

```qf
qreg 2
h 0
cx 0 1
save bell.qf
reset
load bell.qf
probs
```

Les trois premières lignes recréent le circuit pour l'enregistrer avant de mesurer. `save bell.qf` écrit les étapes dans le dossier où tu as lancé QubitForge. `reset` efface les étapes et remet les deux qubits à 0. `load bell.qf` rejoue les étapes enregistrées. Choisis un autre nom si `bell.qf` existe déjà.

## Essaie un exemple intégré

```qf
example ghz
probs
lesson 3
help cx
```

`example ghz` démarre un nouveau circuit à trois qubits. Avec `probs`, tu verras qu'il peut donner `000` ou `111`. `lesson 3` explique le circuit à deux qubits que tu viens de faire. `help cx` montre comment saisir l'opération contrôlée.

## Installation facultative

Dans le dossier du projet, lance `python3 -m pip install -e .` dans ton environnement Python. Tu pourras ensuite lancer le simulateur avec `qubitforge`.

[Commandes et exemples](reference.md)
