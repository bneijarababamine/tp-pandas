# TP Pandas — Manipulation et Visualisation de Données

Travaux pratiques sur la bibliothèque **pandas** appliqués à un jeu de données de ventes commerciales.

## Contenu

| Fichier | Description |
|---|---|
| `tp_pandas.ipynb` | Notebook Jupyter — 8 sections interactives |
| `tp_pandas.py` | Script Python équivalent |
| `ventes.csv / .json / .xlsx` | Jeu de données de ventes |
| `visualisations.png` | Graphiques générés |

## Sections couvertes

1. **Import / Export** — CSV, JSON, Excel avec pandas
2. **Inspection** — `head()`, `info()`, `describe()`, types de données
3. **Sélection** — `loc`, `iloc`, filtrage booléen, colonnes
4. **Nettoyage** — valeurs manquantes, doublons, types
5. **Tri** — `sort_values()`, `sort_index()`
6. **Groupement** — `groupby()`, `agg()`, `pivot_table()`
7. **Statistiques** — corrélation, variance, describe complet
8. **Visualisation** — `plot()`, barres, histogrammes, scatter, heatmap

## Lancer le notebook

```bash
# Créer l'environnement
python -m venv env
source env/bin/activate

# Installer les dépendances
pip install pandas matplotlib seaborn openpyxl scipy jupyter

# Lancer Jupyter
jupyter notebook tp_pandas.ipynb
```

## Dépendances

- Python ≥ 3.10
- pandas
- matplotlib
- seaborn
- openpyxl
- scipy
