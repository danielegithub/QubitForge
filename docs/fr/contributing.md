# Structure du projet et traductions

[README](../../README.fr.md) · [English](../en/contributing.md) · [Italiano](../it/contributing.md) · [Français](../fr/contributing.md) · [Deutsch](../de/contributing.md) · [Español](../es/contributing.md) · [Português](../pt/contributing.md)

## Où trouver les fichiers

| Fichier ou dossier | Ce que tu y trouveras |
| --- | --- |
| [`qubitforge/core/`](../../qubitforge/core/) | Simulateur et définition des portes |
| [`qubitforge/lang/`](../../qubitforge/lang/) | Noms des commandes et arguments |
| [`qubitforge/terminal/`](../../qubitforge/terminal/) | Affichage dans le terminal |
| [`qubitforge/i18n/locales/`](../../qubitforge/i18n/locales/) | Messages de l'interface |
| [`qubitforge/learn/lessons/`](../../qubitforge/learn/lessons/) | Leçons ouvertes avec lesson |
| [`qubitforge/learn/examples/`](../../qubitforge/learn/examples/) | Circuits ouverts avec example |

## Ajouter une langue

Copie `en.json` dans un nouveau fichier, par exemple `fr.json`. Traduis les messages et indique le nom de la langue dans `meta.name`. Garde les clés et les marqueurs comme `{n}`. Dans `aliases`, tu peux associer des mots de la langue aux commandes existantes.

Pour traduire les leçons, copie tous les fichiers de `qubitforge/learn/lessons/en/` dans un dossier portant le code de ta langue. Garde le nom des fichiers et le titre en première ligne. Traduis le texte et conserve les commandes. Si la langue ne contient aucune leçon, QubitForge ouvre les leçons en anglais.

Lance QubitForge avec `--lang` suivi du code. Tape `lang`, `help` et `lesson` pour vérifier les nouveaux messages et la liste des leçons. Essaie `example bell` puis `probs` pour vérifier que deux résultats sont à 50 %.

Pour traduire la documentation, ajoute un README et des guides sous `docs/<code>/`. Ajoute des liens depuis les autres langues.
