import numpy as np
import pandas as pd

# Exemple : array de notes
movie_ratings = np.array([
    [5, 1, 4],
    [4, 4, 2],
    [4, 3, 5],
    [1, 1, 5],
    [3, 2, 1]
])

# Transformer en DataFrame (optionnel : ajouter des noms de colonnes)
df = pd.DataFrame(movie_ratings, columns=["Film1", "Film2", "Film3"])

# Exporter en CSV
df.to_csv("movie_ratings.csv", index=False)  # index=False pour ne pas inclure l'index
