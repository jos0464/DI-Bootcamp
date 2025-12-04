# =========================
# Challenge 1: Sorting
# =========================

# Étape 1: Obtenir une chaîne de mots séparés par des virgules
user_input = input("Entrez des mots séparés par des virgules: ")  # ex: "without,hello,bag,world"

# Étape 2: Séparer la chaîne en une liste de mots
words_list = user_input.split(",")  # ['without', 'hello', 'bag', 'world']

# Étape 3: Trier la liste par ordre alphabétique
words_list.sort()  # ['bag', 'hello', 'without', 'world']

# Étape 4: Rejoindre la liste triée en une seule chaîne, séparée par des virgules
sorted_string = ",".join(words_list)

# Étape 5: Afficher le résultat
print("Mots triés:", sorted_string)


# =========================
# Challenge 2: Longest Word
# =========================

# Étape 1: Définir la fonction qui prend une phrase en paramètre
def longest_word(sentence):
    # Étape 2: Séparer la phrase en mots
    words = sentence.split()  # ex: "Margaret's toy" -> ["Margaret's", "toy"]
    
    # Étape 3: Initialiser la variable pour le mot le plus long
    max_word = ""
    
    # Étape 4: Parcourir tous les mots
    for word in words:
        # Étape 5: Comparer la longueur du mot actuel avec le maximum
        if len(word) > len(max_word):
            max_word = word  # mettre à jour le mot le plus long trouvé
    
    # Étape 6: Retourner le mot le plus long
    return max_word

# Exemple d'utilisation
print(longest_word("Margaret's toy is a pretty doll."))  # Margaret's
print(longest_word("A thing of beauty is a joy forever."))  # forever.
print(longest_word("Forgetfulness is by all means powerless!"))  # Forgetfulness
