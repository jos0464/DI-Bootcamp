# ==========================================
# Exercises XP Gold
# Last Updated: October 7th, 2025
# ==========================================

# ================================================================
# Exercise 1: Birthday Look-up
# ================================================================

print("\n--- Exercise 1: Birthday Look-up ---")

# Initialisation du dictionnaire des anniversaires
birthdays = {
    "Alice": "1995/05/12",
    "Bob": "1990/11/23",
    "Charlie": "1988/07/08",
    "Dana": "1992/01/30",
    "Eli": "1998/09/17"
}

print("Welcome! You can look up the birthdays of the people in the list!")

# Demander le nom de la personne à l'utilisateur
name = input("Enter a person's name: ")

# Récupérer et afficher l'anniversaire
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}")


# ================================================================
# Exercise 2: Birthdays Advanced
# ================================================================

print("\n--- Exercise 2: Birthdays Advanced ---")

# Afficher tous les noms disponibles
print("Available names:", ", ".join(birthdays.keys()))

# Demander le nom de la personne à l'utilisateur
name = input("Enter a person's name to look up: ")

# Vérifier si le nom existe
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}")


# ================================================================
# Exercise 3: Add Your Own Birthday
# ================================================================

print("\n--- Exercise 3: Add Your Own Birthday ---")

# Demander à l'utilisateur d'ajouter un nouvel anniversaire
new_name = input("Enter the name of a person to add: ")
new_birthday = input(f"Enter {new_name}'s birthday (YYYY/MM/DD): ")

# Ajouter les nouvelles informations au dictionnaire
birthdays[new_name] = new_birthday

# Afficher tous les noms disponibles après ajout
print("Updated names list:", ", ".join(birthdays.keys()))

# Permettre à l'utilisateur de rechercher un anniversaire
search_name = input("Enter a name to look up: ")
if search_name in birthdays:
    print(f"{search_name}'s birthday is {birthdays[search_name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {search_name}")


# ================================================================
# Exercise 4: Fruit Shop
# ================================================================

print("\n--- Exercise 4: Fruit Shop ---")

# Partie 1 : prix simples
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print("Item prices:")
for item, price in items.items():
    print(f"A {item} costs ${price}")

# Partie 2 : calcul du coût total des stocks
items_stock = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0
for item, info in items_stock.items():
    item_total = info["price"] * info["stock"]
    total_cost += item_total

print(f"\nThe total cost to buy everything in stock is: ${total_cost}")
