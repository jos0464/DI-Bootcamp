# ===============================================
# Daily Challenge: Lists & Strings
# Pédagogique + Robuste - Windows Safe
# ===============================================

# ---------------- Challenge 1: Multiples of a Number ----------------
print("* Challenge 1: Multiples of a Number")

try:
    # Demander les entrées utilisateur
    number = int(input("Enter a number: "))
    length = int(input("Enter the length: "))

    # Générer la liste des multiples avec list comprehension
    multiples = [number * i for i in range(1, length + 1)]

    # Afficher la liste
    print("Multiples list:", multiples)

except ValueError:
    # Gestion des erreurs si l'utilisateur n'entre pas un entier
    print("Invalid input! Please enter integers only.")

print("\n" + "-"*50 + "\n")

# ---------------- Challenge 2: Remove Consecutive Duplicate Letters ----------------
print("* Challenge 2: Remove Consecutive Duplicate Letters")

# Demander à l'utilisateur de saisir une chaîne
user_string = input("Enter a string: ")

if user_string:  # Vérifie que la chaîne n'est pas vide
    # Initialiser la nouvelle chaîne avec le premier caractère
    result = [user_string[0]]

    # Boucler sur le reste des caractères
    for char in user_string[1:]:
        if char != result[-1]:  # Ajouter uniquement si différent du précédent
            result.append(char)

    # Reconvertir la liste en chaîne
    final_string = ''.join(result)

    # Afficher le résultat
    print("Modified string:", final_string)

else:
    print("Empty string entered!")

print("\nAll challenges completed!")
