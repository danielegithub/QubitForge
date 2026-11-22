# Commandes et exemples

[README](../../README.fr.md) · [English](../en/reference.md) · [Italiano](../it/reference.md) · [Français](../fr/reference.md) · [Deutsch](../de/reference.md) · [Español](../es/reference.md) · [Português](../pt/reference.md)

[Premier circuit, pas à pas](getting-started.md)

## Démarrer, quitter et obtenir de l'aide

- `help`. Affiche toutes les commandes.
- `help cx`. Montre comment saisir une commande. Utile si tu as oublié l'ordre des qubits.
- `lesson` · `lesson 3`. Liste les leçons ou ouvre la troisième, sur deux qubits qui donnent le même résultat.
- `example` · `example bell`. Liste les circuits prêts à l'emploi ou lance le circuit de Bell. Un exemple repart avec un nouveau registre.
- `explain on` · `explain off`. Affiche une courte explication après chaque opération. Utilise off pour la masquer.
- `lang`. Liste les langues des menus. Tape lang it pour l'italien ou lang en pour l'anglais.
- `clear`. Efface l'écran si les couleurs du terminal sont actives. Le circuit reste disponible.
- `quit`. Ferme QubitForge.

## Construire un circuit

- `qreg` · `qreg 3`. Affiche le nombre de qubits. Avec 3, repars avec trois qubits à 0. Tu peux en choisir de 1 à 14.
- `reset`. Remet tous les qubits à 0 et efface le circuit. Utilise-le pour recommencer avec le même nombre de qubits.
- `undo`. Annule une opération. Après measure all, utilise-le une fois par mesure à annuler.
- `id 0`. Laisse le qubit 0 tel quel. Tu peux l'utiliser pour marquer une étape sur le dessin.
- `x 0`. Inverse 0 et 1. Essaie après qreg 1, puis tape probs pour voir 1 à 100 %.
- `h 0`. À partir de 0, donne 0 et 1 à 50 % chacun. Deux h de suite ramènent à 0.
- `x 0` · `y 0`. Les deux inversent 0 et 1. Y change aussi une phase, ce qui peut modifier le résultat des opérations suivantes.
- `z 0`. Inverse le signe du nombre associé à 1 dans state. Essaie l'exercice ci-dessous.
- `s 0` · `sdg 0`. Ajoute un quart de tour de phase avec s, ou retire-le avec sdg. Utilise state pour voir le nombre associé à 1 changer.
- `t 0` · `tdg 0`. Ajoute un huitième de tour de phase avec t, ou retire-le avec tdg. Essaie d'abord h 0, puis compare state avant et après.
- `rx pi 0` · `ry pi/2 0` · `rz pi/2 0`. Font tourner un qubit. Essaie rx pi 0 après qreg 1 pour passer de 0 à 1. Essaie ry pi/2 0 à partir de 0 pour avoir 50 % chacun. Essaie rz pi/2 0 après h 0 et compare state avant et après.
- `p pi/4 0`. Change de pi/4 la phase de la partie associée à 1. Utilise cette commande pour choisir l'angle.
- `cx 0 1` · `cy 0 1` · `cz 0 1` · `ch 0 1`. Applique X, Y, Z ou H au qubit 1 quand le qubit 0 vaut 1. Après qreg 2, essaie x 0 puis cx 0 1. Tu obtiens 11.
- `cp pi/4 0 1`. Change la phase de la partie où les deux qubits valent 1. Essaie d'abord h all, puis regarde le changement avec state.
- `ccx 0 1 2`. Inverse le qubit 2 quand les qubits 0 et 1 valent tous deux 1. Après qreg 3 et x 0 1, tu passes de 011 à 111.
- `swap 0 1`. Échange deux qubits. Après qreg 2 et x 0, tu passes de 01 à 10.

Écris les angles en radians avant les numéros de qubits, sans espace, comme `pi/2`. Applique une opération à plusieurs qubits avec `x 0 1` ou à tous avec `h all`.

## Voir comment une phase change le résultat

Essaie `qreg 1`, `h 0`, `h 0`, `probs`. Tu obtiens `|0>` à 100 %. Essaie ensuite les lignes ci-dessous. Le `z 0` en plus donne `|1>` à 100 %.

```qf
qreg 1
h 0
z 0
h 0
probs
```

## Voir ce que fait le circuit

- `probs`. Affiche les résultats possibles et leurs pourcentages avant la mesure.
- `state`. Affiche les nombres qui servent à calculer les pourcentages. Utile pour voir un signe plus devenir un moins alors que les pourcentages restent les mêmes.
- `bloch 0`. Affiche l'orientation du qubit et un nombre appelé pureté. Essaie après example bell. Avec cette paire liée, le qubit 0 a une pureté de 0,5. Sans numéro, bloch affiche tous les qubits.
- `circuit`. Dessine les opérations dans l'ordre pour vérifier quels qubits tu as utilisés.
- `measure 0` · `measure all`. Mesure le qubit 0 ou tous les qubits. La mesure change l'état du simulateur. Ensuite, tape probs pour voir les résultats encore possibles.
- `run 20`. Tire 20 résultats et compte le nombre d'apparitions de chacun. Tu peux recommencer sur le même état. Sans nombre, tu obtiens 1 024 tirages. Tu peux en demander jusqu'à 200 000.

## Enregistrer et rejouer

- `save bell.qf`. Enregistre les étapes dans un fichier. Choisis un nouveau nom à chaque fois. Le fichier inclut les mesures effectuées, qui peuvent donner un autre résultat lors d'une nouvelle exécution.
- `load bell.qf`. Exécute un fichier de commandes QubitForge. Écris une commande par ligne et commence par qreg pour repartir de zéro. Utilise un nom sans espace ni #.
- `qasm`. Affiche le circuit sous forme de texte OpenQASM 2.0. Copie-le si tu veux utiliser le circuit dans un autre outil. L'export conserve les noms des portes de QubitForge.

[Enregistre le circuit et rouvre-le](getting-started.md)

## Avant d'ouvrir QubitForge

```bash
python3 -m qubitforge --lang en --seed 42 --fast --no-color
```

- `--lang en` · `--lang it`. Utilise les menus en anglais ou en italien.
- `--seed 42`. Retrouve les mêmes résultats aléatoires après deux lancements en rejouant les mêmes commandes dans le même ordre.
- `--fast`. Supprime l'attente entre les messages du démarrage.
- `--no-color`. Désactive les couleurs dans le terminal.
- `--help`. Liste les options à saisir au démarrage.
- `bell.qf`. Exécute bell.qf depuis le dossier courant avant d'afficher l'invite.

```bash
python3 -m qubitforge --lang en bell.qf
```
