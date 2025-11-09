import random

# 1️⃣ Demander une entrée utilisateur
user_string = input("Entrez une chaîne de 10 caractères : ")

# 2️⃣ Vérifier la longueur de la chaîne
if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string!")

    # 3️⃣ Afficher le premier et le dernier caractère
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])

    # 4️⃣ Construire la chaîne caractère par caractère
    print("\nBuilding the string step by step:")
    for i in range(1, len(user_string) + 1):
        print(user_string[:i])

    # 5️⃣ BONUS : Mélanger la chaîne
    chars = list(user_string)
    random.shuffle(chars)
    jumbled_string = ''.join(chars)
    print("\nJumbled string:", jumbled_string)
