# ---------------- Exercise 1: What's your name? ----------------
def get_full_name(first_name, last_name, middle_name=""):
    """Retourne le nom complet, avec middle_name optionnel"""
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

# Exemple d'utilisation
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))  # John Hooker Lee
print(get_full_name(first_name="bruce", last_name="lee"))  # Bruce Lee


# ---------------- Exercise 2: From English to Morse ----------------
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----','1': '.----','2': '..---','3': '...--','4': '....-',
    '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.',
    ' ': '/'  # espace entre mots
}

def english_to_morse(text):
    """Convertit un texte anglais en code morse"""
    text = text.upper()
    morse = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    return morse

def morse_to_english(morse_code):
    """Convertit un code morse en texte anglais"""
    inverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = morse_code.split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(inverse_dict.get(letter, '') for letter in letters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

# Exemple d'utilisation
text = "Hello World"
morse = english_to_morse(text)
print("Morse:", morse)
print("Decoded:", morse_to_english(morse))


# ---------------- Exercise 3: Box of stars ----------------
def box_printer(*args):
    """Affiche les mots dans un cadre rectangulaire"""
    max_len = max(len(word) for word in args)
    border = '*' * (max_len + 4)
    print(border)
    for word in args:
        print(f"* {word.ljust(max_len)} *")
    print(border)

# Exemple d'utilisation
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


# ---------------- Exercise 4: Purpose of insertion sort ----------------
def insertion_sort(alist):
    """
    Tri par insertion :
    Cette fonction trie la liste alist dans l'ordre croissant.
    Chaque élément est inséré à sa position correcte dans la partie déjà triée de la liste.
    """
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentvalue

# Exemple
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print("Sorted list:", alist)
