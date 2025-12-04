# ===============================================
# Daily Challenge: Dictionaries
# Last Updated: October 31st, 2025
# ===============================================

# ---------------- Challenge 1: Letter Index Dictionary ----------------
print("Challenge 1: Letter Index Dictionary")

# Demander à l'utilisateur de saisir un mot
word = input("Enter a word: ")

# Initialiser un dictionnaire vide pour stocker les indices
letter_indices = {}

# Parcourir chaque caractère du mot avec son index
for index, char in enumerate(word):
    if char in letter_indices:
        # Si la lettre existe déjà, ajouter l'index à la liste
        letter_indices[char].append(index)
    else:
        # Sinon, créer une nouvelle entrée avec une liste contenant l'index
        letter_indices[char] = [index]

# Afficher le résultat
print("Letter index dictionary:", letter_indices)

# Explications :
# - enumerate(word) permet d'obtenir l'index et la lettre
# - Les indices de chaque lettre sont stockés dans une liste
# - Si une lettre apparaît plusieurs fois, on ajoute l'index à sa liste existante

print("\n" + "-"*50 + "\n")

# ---------------- Challenge 2: Affordable Items ----------------
print("Challenge 2: Affordable Items")

# Exemple de données
items_purchase = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}
wallet = "$100"

# Nettoyer le montant du portefeuille et convertir en entier
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

# Initialiser la liste du panier
basket = []

# Parcourir les items dans l'ordre du dictionnaire
for item, price_str in items_purchase.items():
    # Nettoyer le prix et convertir en entier
    price = int(price_str.replace("$", "").replace(",", ""))
    # Vérifier si l'article est abordable
    if price <= wallet_amount:
        basket.append(item)
        wallet_amount -= price  # Mettre à jour le portefeuille

# Affichage final
if basket:
    # Trier le panier par ordre alphabétique avant d'afficher
    print("Basket:", sorted(basket))
else:
    print("Nothing")

# Explications :
# - replace() enlève le signe "$" et les virgules pour convertir en entier
# - On parcourt le dictionnaire dans l'ordre pour respecter la priorité des items
# - On met à jour le portefeuille après chaque achat
# - Si aucun item n’est abordable, on affiche "Nothing"
# - Sinon, on affiche le panier trié alphabétiquement
