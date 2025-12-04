from anagram_checker import AnagramChecker

def show_menu():
    print("\n===== ANAGRAM CHECKER =====")
    print("1. Enter a word")
    print("2. Exit")
    return input("Choose an option: ").strip()

def get_clean_word():
    user_input = input("Enter a word: ").strip()

    # Remove extra spaces
    cleaned = user_input.strip()

    # Validate word count
    if " " in cleaned:
        print("Error: Only one word allowed.")
        return None

    # Validate characters
    if not cleaned.isalpha():
        print("Error: Only alphabetic characters allowed.")
        return None

    return cleaned.lower()

def main():
    checker = AnagramChecker()

    while True:
        choice = show_menu()

        if choice == "2":
            print("Goodbye!")
            break

        elif choice == "1":
            word = get_clean_word()
            if not word:
                continue

            print("\nYOUR WORD :", word.upper())

            if checker.is_valid_word(word):
                print("This is a valid English word.")
            else:
                print("This is NOT a valid English word.")
                continue

            # Get anagrams
            anagrams = checker.get_anagrams(word)
            if anagrams:
                print("Anagrams for your word:", ", ".join(anagrams))
            else:
                print("No anagrams found.")

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
