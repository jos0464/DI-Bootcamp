# anagrams.py
from anagram_checker import AnagramChecker

def clean_input(word):
    """
    Nettoie et valide l'entrée utilisateur.
    - Supprime les espaces
    - Vérifie que c’est un mot unique et alphabétique
    """
    word = word.strip()
    if " " in word:
        print("❌ Erreur : entrez un seul mot.")
        return None
    if not word.isalpha():
        print("❌ Erreur : le mot doit contenir uniquement des lettres.")
        return None
    return word

def main():
    checker = AnagramChecker()

    print("=== 🔠 Anagram Checker ===")
    while True:
        print("\nMenu :")
        print("1️⃣  Entrer un mot")
        print("2️⃣  Quitter")
        choice = input("Votre choix : ")

        if choice == "2":
            print("👋 Fin du programme. À bientôt !")
            break

        elif choice == "1":
            word = input("Entrez un mot : ")
            word = clean_input(word)
            if not word:
                continue

            print(f"\nYOUR WORD : “{word.upper()}”")

            if checker.is_valid_word(word):
                print("✅ C’est un mot anglais valide.")
                anagrams = checker.get_anagrams(word)
                if anagrams:
                    print("🔁 Anagrams for your word:", ", ".join(anagrams))
                else:
                    print("😅 Aucun anagram trouvé.")
            else:
                print("❌ Ce mot n’existe pas dans la liste anglaise.")
        else:
            print("⚠️ Choix invalide. Essayez encore.")

if __name__ == "__main__":
    main()
