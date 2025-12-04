# ==========================================
# Timed Challenge #1: Reverse the Sentence
# Last Updated: October 7th, 2025
# ==========================================

# Demander à l'utilisateur de saisir une phrase
# Pour Python 3, on utilise input() au lieu de raw_input()
sentence = input("Enter a sentence: ")

# Diviser la phrase en mots (séparés par des espaces)
words = sentence.split()

# Inverser la liste de mots
words_reversed = words[::-1]

# Rejoindre les mots inversés pour recréer la phrase inversée
reversed_sentence = " ".join(words_reversed)

# Afficher la phrase inversée
print(reversed_sentence)
