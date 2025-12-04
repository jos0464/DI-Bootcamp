# ---------------- Timed Challenge #1: Count Occurrences ----------------

# Étape 1: Demander à l'utilisateur une chaîne de caractères
user_string = input("Enter a string: ")

# Étape 2: Demander à l'utilisateur le caractère à chercher
char_to_count = input("Enter a character: ")

# Étape 3: Vérifier que l'utilisateur a entré exactement un caractère
if len(char_to_count) != 1:
    print("Please enter exactly one character!")
else:
    # Étape 4: Compter les occurrences du caractère dans la chaîne
    count = 0
    for ch in user_string:
        if ch == char_to_count:
            count += 1
    
    # Étape 5: Afficher le résultat
    print(f"The character '{char_to_count}' occurs {count} times in the string.")
