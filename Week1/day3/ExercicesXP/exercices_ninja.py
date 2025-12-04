# ==========================================
# Exercises XP Ninja
# Last Updated: October 7th, 2025
# ==========================================

# ================================================================
# Exercise 1: Cars
# ================================================================

print("\n--- Exercise 1: Cars ---")

# 1 - Copier la chaîne et la convertir en liste
cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = [car.strip() for car in cars_string.split(",")]

# Afficher le nombre de constructeurs
print(f"Number of manufacturers: {len(cars_list)}")

# Afficher la liste en ordre décroissant (Z-A)
cars_desc = sorted(cars_list, reverse=True)
print("Manufacturers in reverse order (Z-A):")
print(cars_desc)

# 2 - Nombre de noms contenant la lettre 'o'
count_o = sum(1 for car in cars_list if 'o' in car.lower())
print(f"Number of manufacturers with 'o' in their name: {count_o}")

# 3 - Nombre de noms ne contenant pas la lettre 'i'
count_no_i = sum(1 for car in cars_list if 'i' not in car.lower())
print(f"Number of manufacturers without 'i' in their name: {count_no_i}")

# ------------------------------------------------
# Bonus 1 - Supprimer les doublons
# ------------------------------------------------
cars_duplicates = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
cars_no_duplicates = list(dict.fromkeys(cars_duplicates))  # Retire les doublons en conservant l'ordre

print("\nCompanies without duplicates:")
print(", ".join(cars_no_duplicates))
print(f"Number of companies after removing duplicates: {len(cars_no_duplicates)}")

# ------------------------------------------------
# Bonus 2 - Ordre croissant A-Z avec lettres inversées
# ------------------------------------------------
cars_sorted_reverse_letters = [car[::-1] for car in sorted(cars_no_duplicates)]
print("\nManufacturers in ascending order with letters reversed:")
print(cars_sorted_reverse_letters)
