# ==============================
# Mini-Projet : Hangman (Pendu)
# ==============================
# Objectif :
# - Choisir un mot aléatoire
# - Permettre au joueur de deviner les lettres
# - Afficher le mot avec les lettres devinées et "_" pour celles non devinées
# - Compter les tentatives restantes

import random

# Liste des mots possibles
word_list = ["python", "hangman", "developer", "challenge"]
# Choisir un mot au hasard
word_to_guess = random.choice(word_list)
# Lettres déjà devinées
guessed_letters = []
# Nombre d'essais autorisés
attempts = 6

# Fonction pour afficher l'état actuel du mot
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display)

# Boucle principale du jeu
while attempts > 0:
    display_word(word_to_guess, guessed_letters)
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        # Lettre déjà proposée
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)  # Ajouter la lettre à la liste

    if guess in word_to_guess:
        print("Correct!")  # La lettre est dans le mot
    else:
        print("Wrong!")  # La lettre n'est pas dans le mot
        attempts -= 1  # On retire un essai

    # Vérifier si toutes les lettres ont été trouvées
    if all(letter in guessed_letters for letter in word_to_guess):
        print(f"Congratulations! You guessed the word: {word_to_guess}")
        break
else:
    # Si le joueur n'a plus d'essais
    print(f"Game over! The word was: {word_to_guess}")
