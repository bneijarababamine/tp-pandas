import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=== TP PANDAS - TOUTES LES COMMANDES ===\n")

# ─────────────────────────────────────────────
# SECTION 1 : IMPORT / EXPORT
# ─────────────────────────────────────────────
print("── SECTION 1 : Import / Export ──")

data = {
    'produit':       ['Stylo','Cahier','Règle','Gomme','Crayon',
                      'Stylo','Cahier','Règle','Gomme','Crayon'],
    'categorie':     ['Ecriture','Papeterie','Mesure','Ecriture','Ecriture',
                      'Ecriture','Papeterie','Mesure','Ecriture','Ecriture'],
    'quantite':      [10, 25, 5, 30, 20, 15, 10, 8, 45, 12],
    'prix_unitaire': [1.5, 3.0, 2.5, 0.5, 0.8, 1.5, 3.0, 2.5, 0.5, 0.8],
    'ville':         ['Paris','Lyon','Paris','Marseille','Lyon',
                      'Paris','Paris','Lyon','Marseille','Paris'],
    'mois':          ['Jan','Jan','Jan','Jan','Jan',
                      'Fev','Fev','Fev','Fev','Fev']
}

df = pd.DataFrame(data)                          # Créer depuis un dict
df.to_csv('ventes.csv', index=False)             # Export CSV
df.to_excel('ventes.xlsx', index=False)          # Export Excel
df.to_json('ventes.json')                        # Export JSON
df2 = pd.read_csv('ventes.csv')                  # Lire CSV
df3 = pd.read_excel('ventes.xlsx')              # Lire Excel
df4 = pd.read_json('ventes.json')               # Lire JSON
print("Fichiers créés : ventes.csv, ventes.xlsx, ventes.json")
print(df2.head(2))
print()

# ─────────────────────────────────────────────
# SECTION 2 : INSPECTION
# ─────────────────────────────────────────────
print("── SECTION 2 : Inspection ──")
print("head()      :\n", df.head())              # 5 premières lignes
print("tail()      :\n", df.tail())              # 5 dernières lignes
print("sample()    :\n", df.sample(3))           # 3 lignes aléatoires
print("shape       :", df.shape)                 # Dimensions
print("info()      :"); df.info()                # Résumé
print("describe()  :\n", df.describe())          # Stats numériques
print("dtypes      :\n", df.dtypes)              # Types des colonnes
print("columns     :", df.columns.tolist())      # Noms des colonnes
print("index       :", df.index)                 # Index
print()

# ─────────────────────────────────────────────
# SECTION 3 : SELECTION & INDEXATION
# ─────────────────────────────────────────────
print("── SECTION 3 : Sélection & Indexation ──")
print("colonne unique        :\n", df['produit'])
print("plusieurs colonnes    :\n", df[['produit','quantite']])
print("iloc[0]               :\n", df.iloc[0])
print("loc[0]                :\n", df.loc[0])
print("iloc[0,0]             :", df.iloc[0, 0])
print("loc[0,'ville']        :", df.loc[0, 'ville'])
print("filtre quantite > 15  :\n", df[df['quantite'] > 15])
print("iloc slice            :\n", df.iloc[0:3, 0:3])
df_idx = df.set_index('produit')                 # Définir index
print("set_index             :\n", df_idx.head(3))
print()

# ─────────────────────────────────────────────
# SECTION 4 : NETTOYAGE
# ─────────────────────────────────────────────
print("── SECTION 4 : Nettoyage ──")
df_dirty = df.copy()
df_dirty.loc[2, 'quantite']      = None
df_dirty.loc[5, 'prix_unitaire'] = None
df_dirty.loc[8, 'ville']         = None
df_dirty = pd.concat([df_dirty, df_dirty.iloc[[0,1]]], ignore_index=True)

print("isnull()        :\n", df_dirty.isnull().sum())
print("notnull() count :\n", df_dirty.notnull().sum())
df_dirty['quantite']      = df_dirty['quantite'].fillna(df_dirty['quantite'].median())
df_dirty['prix_unitaire'] = df_dirty['prix_unitaire'].fillna(0)
df_dirty = df_dirty.dropna(subset=['ville'])
df_dirty = df_dirty.drop_duplicates()
df_dirty = df_dirty.replace('Paris', 'IDF')
df_dirty = df_dirty.rename(columns={'prix_unitaire': 'prix'})
df_dirty['quantite'] = df_dirty['quantite'].astype(int)
df_dirty = df_dirty.reset_index(drop=True)
print("Après nettoyage :\n", df_dirty)
print()

# ─────────────────────────────────────────────
# SECTION 5 : TRI & FILTRAGE
# ─────────────────────────────────────────────
print("── SECTION 5 : Tri & Filtrage ──")
df['total_vente'] = df['quantite'] * df['prix_unitaire']

print("sort ASC         :\n", df.sort_values('total_vente').head(3))
print("sort DESC        :\n", df.sort_values('total_vente', ascending=False).head(3))
print("sort multi-col   :\n", df.sort_values(['ville','total_vente'], ascending=[True,False]).head(4))
print("filtre cond.     :\n", df[df['quantite'] > 15])
print("query            :\n", df.query('prix_unitaire < 1.0'))
print("sample(4)        :\n", df.sample(4))
print("nlargest(3)      :\n", df.nlargest(3, 'total_vente'))
print("nsmallest(3)     :\n", df.nsmallest(3, 'total_vente'))
print("filter like='e'  :\n", df.filter(like='e').head(3))
print()

# ─────────────────────────────────────────────
# SECTION 6 : GROUPEMENT & AGREGATION
# ─────────────────────────────────────────────
print("── SECTION 6 : Groupement & Agrégation ──")
print("groupby sum      :\n", df.groupby('categorie')['quantite'].sum())
print("groupby mean     :\n", df.groupby('produit')['prix_unitaire'].mean())
print("groupby count    :\n", df.groupby('ville')['produit'].count())
print("groupby max      :\n", df.groupby('categorie')['total_vente'].max())
print("pivot_table      :\n",
    df.pivot_table(values='total_vente', index='ville', columns='mois', aggfunc='sum'))
print("agg multi        :\n",
    df.agg({'quantite': 'sum', 'prix_unitaire': 'mean'}))
print("apply np.mean    :\n", df[['quantite','prix_unitaire','total_vente']].apply(np.mean))
df['pct_total'] = df['total_vente'].transform(lambda x: round(x / x.sum() * 100, 2))
print("transform pct    :\n", df[['produit','total_vente','pct_total']])
print()

# ─────────────────────────────────────────────
# SECTION 7 : OPERATIONS STATISTIQUES
# ─────────────────────────────────────────────
print("── SECTION 7 : Opérations Statistiques ──")
print("mean()    :\n", df[['quantite','prix_unitaire','total_vente']].mean())
print("median()  :\n", df[['quantite','prix_unitaire','total_vente']].median())
print("std()     :\n", df[['quantite','prix_unitaire','total_vente']].std())
print("var()     :\n", df[['quantite','prix_unitaire','total_vente']].var())
print("sum()     :\n", df[['quantite','total_vente']].sum())
print("min()     :\n", df[['quantite','prix_unitaire','total_vente']].min())
print("max()     :\n", df[['quantite','prix_unitaire','total_vente']].max())
print("count()   :\n", df.count())
print("corr()    :\n", df[['quantite','prix_unitaire','total_vente']].corr())
print()

# ─────────────────────────────────────────────
# SECTION 8 : VISUALISATION
# ─────────────────────────────────────────────
print("── SECTION 8 : Visualisation ──")
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('TP Pandas — Visualisations', fontsize=16, fontweight='bold')

df.groupby('produit')['total_vente'].sum().plot(
    kind='bar', ax=axes[0,0], title='Ventes par produit', color='steelblue')

df.groupby('produit')['total_vente'].sum().plot(
    kind='barh', ax=axes[0,1], title='Barres horizontales', color='coral')

df['total_vente'].plot(
    kind='hist', ax=axes[0,2], title='Distribution total_vente', bins=6, color='green')

df[['quantite','total_vente']].plot(
    kind='box', ax=axes[1,0], title='Box plot')

df['quantite'].plot(
    kind='kde', ax=axes[1,1], title='KDE quantite')

df.groupby('ville')['total_vente'].sum().plot(
    kind='pie', ax=axes[1,2], title='Répartition par ville', autopct='%1.0f%%')

df.plot.scatter(
    x='quantite', y='total_vente', ax=axes[2,0],
    title='Scatter quantite vs total', color='purple')

df.groupby('mois')['total_vente'].sum().plot(
    kind='line', ax=axes[2,1], title='Évolution mensuelle', marker='o')

df.groupby('produit')['total_vente'].sum().plot(
    kind='area', ax=axes[2,2], title='Area plot ventes', alpha=0.5)

plt.tight_layout()
plt.savefig('visualisations.png', dpi=120, bbox_inches='tight')
plt.close()
print("Graphique sauvegardé : visualisations.png")
