# exercises_xp.py

from datetime import datetime
import string, random
from faker import Faker

# ---------------- Exercice 1 : Currency ----------------
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    __repr__ = __str__

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, (int, float)):
            return self.amount + other
        else:
            raise TypeError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            raise TypeError("Unsupported type for addition")
        return self

def exercice_currency():
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)

    print(c1)
    print(int(c1))
    print(repr(c1))
    print(c1 + 5)
    print(c1 + c2)
    c1 += 5
    print(c1)
    c1 += c2
    print(c1)
    try:
        print(c1 + c3)
    except TypeError as e:
        print("Erreur :", e)

# ---------------- Exercice 2 : Import (simulé ici) ----------------
def add_numbers(a, b):
    print(f"Le résultat est : {a + b}")

def exercice_import():
    add_numbers(5, 7)

# ---------------- Exercice 3 : String aléatoire ----------------
def exercice_random_string():
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(5))
    print("Chaîne aléatoire :", random_string)

# ---------------- Exercice 4 : Date actuelle ----------------
def exercice_date():
    today = datetime.today()
    print("Date actuelle :", today.strftime("%Y-%m-%d"))

# ---------------- Exercice 5 : Temps restant jusqu’au 1er janvier ----------------
def exercice_temps_restant():
    maintenant = datetime.now()
    annee_prochaine = datetime(maintenant.year + 1, 1, 1)
    delta = annee_prochaine - maintenant
    print("Temps restant jusqu'au 1er janvier :", delta)

# ---------------- Exercice 6 : Minutes vécues ----------------
def exercice_minutes():
    birthdate_str = input("Entrez votre date de naissance (JJ/MM/AAAA) : ")
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    maintenant = datetime.now()
    minutes = (maintenant - birthdate).total_seconds() / 60
    print(f"Vous avez vécu environ {int(minutes)} minutes.")

# ---------------- Exercice 7 : Faker ----------------
def exercice_faker():
    fake = Faker()
    users = []
    n = int(input("Combien d'utilisateurs voulez-vous générer ? "))
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)
    for u in users:
        print(u)

# ---------------- Menu principal ----------------
def main():
    while True:
        print("\n--- Menu des Exercices XP ---")
        print("1: Currency")
        print("2: Import")
        print("3: String aléatoire")
        print("4: Date actuelle")
        print("5: Temps restant jusqu'au 1er janvier")
        print("6: Minutes vécues")
        print("7: Faker")
        print("0: Quitter")
        choice = input("Choisissez un exercice : ")

        if choice == "1":
            exercice_currency()
        elif choice == "2":
            exercice_import()
        elif choice == "3":
            exercice_random_string()
        elif choice == "4":
            exercice_date()
        elif choice == "5":
            exercice_temps_restant()
        elif choice == "6":
            exercice_minutes()
        elif choice == "7":
            exercice_faker()
        elif choice == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")

if __name__ == "__main__":
    main()
