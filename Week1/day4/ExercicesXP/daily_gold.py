# ------------------ Daily Challenge Gold: Solve the Matrix ------------------

# La chaîne "Matrix" donnée
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''       

# ------------------ Step 1: Transformer la chaîne en liste 2D ------------------
# On commence par nettoyer la chaîne et la transformer en liste de lignes
# Chaque ligne devient une liste de caractères
matrix = []

# On parcourt chaque ligne de MATRIX_STR après avoir enlevé les lignes vides
for line in MATRIX_STR.strip().split("\n"):  # .strip() enlève les lignes vides au début et à la fin
    row = list(line)  # transforme chaque ligne en liste de caractères
    matrix.append(row)

# À ce stade, "matrix" est une liste de listes, où chaque sous-liste représente une ligne

# ------------------ Step 2: Lire la matrice par colonnes ------------------
# Neo lit la matrice colonne par colonne (de gauche à droite, de haut en bas)
# On va créer une chaîne temporaire "temp_str" pour stocker tous les caractères lus

temp_str = ""

# On suppose que toutes les lignes ont la même longueur
num_rows = len(matrix)
num_cols = len(matrix[0])

# Parcours des colonnes
for col in range(num_cols):
    for row in range(num_rows):
        temp_str += matrix[row][col]  # ajouter le caractère à la chaîne temporaire

# ------------------ Step 3: Filtrer les caractères alphabétiques ------------------
# On ne garde que les lettres, mais on veut garder les symboles pour remplacer plus tard par des espaces
# On va juste préparer la chaîne pour le traitement final

# ------------------ Step 4: Remplacer les symboles entre deux lettres par un espace ------------------
decoded_message = ""  # message final
prev_alpha = False  # pour savoir si le caractère précédent était une lettre

for char in temp_str:
    if char.isalpha():  # si c'est une lettre
        decoded_message += char  # on ajoute la lettre au message
        prev_alpha = True  # on note que la lettre précédente était alphabétique
    else:  # c'est un symbole ou espace
        # si la lettre précédente était alphabétique et le prochain caractère sera alphabétique,
        # on ajoute un espace
        if prev_alpha:
            decoded_message += " "
            prev_alpha = False  # on remet à False pour éviter plusieurs espaces consécutifs

# Nettoyage final: suppression des espaces au début et à la fin et des espaces multiples
decoded_message = ' '.join(decoded_message.split())

# ------------------ Step 5: Affichage du message décodé ------------------
print(decoded_message)
