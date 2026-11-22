# QubitForge

[English](README.md) · [Italiano](README.it.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Português](README.pt.md)

**Des circuits quantiques dans le terminal**

QubitForge permet d'essayer des opérations quantiques sur ton ordinateur. Tu peux voir les résultats possibles, faire une mesure et enregistrer les étapes pour les rejouer.

## Pour commencer

Ouvre un terminal dans le dossier QubitForge. Avec Python 3.10 ou une version plus récente, lance cette commande. QubitForge fonctionne sans paquet Python supplémentaire.

```bash
python3 -m qubitforge --lang en
```

Attends de voir `qf[2q]>`. Saisis une ligne à la fois et appuie sur Entrée après chacune.

```qf
qreg 1
h 0
probs
```

`qreg 1` repart avec un qubit à 0. `h 0` donne autant de chances d'obtenir 0 que 1. `probs` affiche 50 % pour chacun. Un qubit est l'élément du simulateur qui donne un 0 ou un 1 quand tu le mesures. Pour quitter, tape `quit`.

Les menus et les leçons intégrées sont en anglais ou en italien. Les commandes fonctionnent dans les deux langues.

## Guides

- [Premier circuit, pas à pas](docs/fr/getting-started.md)
- [Commandes et exemples](docs/fr/reference.md)
- [Structure du projet et traductions](docs/fr/contributing.md)

## Licence

[MIT](LICENSE)
