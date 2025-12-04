# --------------------------
# EXERCICE 1 : Chats
# --------------------------

# Définition de la classe Cat
class Cat:
    def __init__(self, cat_name, cat_age):
        # Attributs : nom et âge du chat
        self.name = cat_name
        self.age = cat_age

# Création de 3 objets Cat avec différents noms et âges
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Tom", 5)
cat3 = Cat("Garfield", 7)

# Fonction pour trouver le chat le plus âgé
def find_oldest_cat(cat1, cat2, cat3):
    # On commence par supposer que le premier chat est le plus âgé
    oldest = cat1
    # Comparaison avec le deuxième chat
    if cat2.age > oldest.age:
        oldest = cat2
    # Comparaison avec le troisième chat
    if cat3.age > oldest.age:
        oldest = cat3
    # Retourner le chat le plus âgé
    return oldest

# Appel de la fonction et affichage du résultat
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# --------------------------
# EXERCICE 2 : Chiens
# --------------------------

class Dog:
    def __init__(self, name, height):
        # Attributs du chien
        self.name = name
        self.height = height

    # Méthode pour aboyer
    def bark(self):
        print(f"{self.name} goes woof!")

    # Méthode pour sauter
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Création des objets Dog
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Buddy", 40)

# Affichage des détails et appel des méthodes
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

# Comparaison des tailles
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else:
    print(f"{sarahs_dog.name} is bigger")


# --------------------------
# EXERCICE 3 : Chanson
# --------------------------

class Song:
    def __init__(self, lyrics):
        # Attribut pour stocker les paroles
        self.lyrics = lyrics

    # Méthode pour chanter
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Création d'un objet Song
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Appel de la méthode pour afficher les paroles
stairway.sing_me_a_song()


# --------------------------
# EXERCICE 4 : Zoo
# --------------------------

class Zoo:
    def __init__(self, zoo_name):
        # Nom du zoo
        self.name = zoo_name
        # Liste pour stocker les animaux
        self.animals = []

    # Ajouter un ou plusieurs animaux
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    # Afficher tous les animaux
    def get_animals(self):
        print(self.animals)

    # Vendre (retirer) un animal
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    # Trier et grouper les animaux par première lettre
    def sort_animals(self):
        self.animals.sort()
        grouped = {}
        for animal in self.animals:
            key = animal[0].upper()
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(animal)
        self.grouped_animals = grouped

    # Afficher les groupes
    def get_groups(self):
        for key, value in self.grouped_animals.items():
            print(f"{key}: {value}")

# Création d'un objet Zoo
brooklyn_safari = Zoo("Brooklyn Safari")

# Ajouter plusieurs animaux en une seule fois grâce à *args
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar")
brooklyn_safari.get_animals()

# Vendre un animal
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

# Trier et grouper les animaux
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
