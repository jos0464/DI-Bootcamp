import pandas as pd

# -----------------------------
# Chemin du fichier CSV
# -----------------------------
chemin_csv = r"C:\Users\josep\PycharmProjects\GenerativeAI\media\cleaned_datasets\dataset_1\cleaned_maisons_100.csv"

# -----------------------------
# Lecture du CSV
# -----------------------------
df = pd.read_csv(chemin_csv)

# -----------------------------
# Colonnes numériques à analyser
# -----------------------------
colonnes_numeriques = ['surface', 'nb_pieces', 'annee_construction', 'prix']

# Convertir en numérique (valeurs invalides deviennent NaN)
for col in colonnes_numeriques:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# -----------------------------
# Affichage des statistiques descriptives
# -----------------------------
stats = df[colonnes_numeriques].describe()
print("Statistiques descriptives :\n")
print(stats)

# -----------------------------
# Optionnel : vérifier les valeurs manquantes
# -----------------------------
print("\nValeurs manquantes par colonne :")
print(df[colonnes_numeriques].isna().sum())
