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
# 1. Créer un environnement virtuel isolé
python -m venv env
source env/bin/activate        # macOS / Linux
# env\Scripts\activate         # Windows

# 2. Installer les dépendances exactes
pip install -r requirements.txt

# 3. Lancer Jupyter
jupyter notebook tp_pandas.ipynb
```

> L'environnement virtuel est isolé — il n'utilise pas les packages installés sur le système.

## Dépendances (requirements.txt)

| Package | Version |
|---|---|
| pandas | 3.0.3 |
| numpy | 2.5.0 |
| matplotlib | 3.11.0 |
| seaborn | 0.13.2 |
| openpyxl | 3.1.5 |
| scipy | 1.18.0 |
| notebook | 7.6.0 |

Python ≥ 3.10 requis.
