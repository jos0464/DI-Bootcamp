import random

# ---------------- Exercise 1: What Are You Learning? ----------------
def display_message():
    """Affiche un message sur ce que vous apprenez"""
    print("I am learning about functions in Python.")

# Appel de la fonction
display_message()


# ---------------- Exercise 2: What's Your Favorite Book? ----------------
def favorite_book(title):
    """Affiche un message sur un livre préféré"""
    print(f"One of my favorite books is {title}.")

# Appel avec un argument
favorite_book("Alice in Wonderland")


# ---------------- Exercise 3: Some Geography ----------------
def describe_city(city, country="Unknown"):
    """Affiche un message décrivant une ville et son pays"""
    print(f"{city} is in {country}.")

# Appels de la fonction
describe_city("Reykjavik", "Iceland")
describe_city("Paris")  # Utilise la valeur par défaut "Unknown"


# ---------------- Exercise 4: Random Number Comparison ----------------
def compare_random(user_number):
    """Compare un nombre donné à un nombre aléatoire"""
    rand_number = random.randint(1, 100)
    if user_number == rand_number:
        print("Success! Numbers match!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {rand_number}")

# Exemple d'appel
compare_random(50)


# ---------------- Exercise 5: Personalized Shirts ----------------
def make_shirt(size="large", text="I love Python"):
    """Affiche un résumé d'un t-shirt avec sa taille et son texte"""
    print(f"The size of the shirt is {size} and the text is {text}.")

# Appels avec valeurs par défaut et personnalisées
make_shirt()  # grand avec message par défaut
make_shirt(size="medium")  # moyen avec message par défaut
make_shirt(size="small", text="Custom message")  # petit avec message personnalisé


# ---------------- Exercise 6: Magicians ----------------
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    """Affiche tous les magiciens"""
    for name in names:
        print(name)

def make_great(names):
    """Ajoute 'the Great' à chaque nom"""
    for i in range(len(names)):
        names[i] += " the Great"

# Modification et affichage
make_great(magician_names)
show_magicians(magician_names)


# ---------------- Exercise 7: Temperature Advice ----------------
def get_random_temp():
    """Retourne une température aléatoire entre -10 et 40°C"""
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    elif 32 < temp <= 40:
        print("It's really hot! Stay cool.")

# Appel de la fonction principale
main()
