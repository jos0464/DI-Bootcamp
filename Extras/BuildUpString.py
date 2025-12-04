import random

# 1. Demander à l'utilisateur d'entrer une chaîne
user_input = input("Entrez une chaîne de exactement 10 caractères : ")

# 2. Vérifier la longueur
if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string")

    # 3. Afficher le premier et dernier caractère
    print(f"First character: {user_input[0]}")
    print(f"Last character: {user_input[-1]}")

    # 4. Construire et afficher la chaîne caractère par caractère
    print("\nBuilding string step by step:")
    for i in range(1, len(user_input)+1):
        print(user_input[:i])

    # 5. Bonus : mélanger la chaîne
    jumbled = list(user_input)
    random.shuffle(jumbled)
    jumbled_string = ''.join(jumbled)
    print("\nJumbled string:", jumbled_string)
