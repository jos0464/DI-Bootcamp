# --------------------------
# EXERCICE 1 : Pets et chats
# --------------------------
import random

# Classe principale Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

# Classe Cat
class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

# Classes dérivées de Cat
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1: Classe Siamese qui hérite de Cat
class Siamese(Cat):
    pass  # Pas d'attribut spécifique pour l'instant

# Step 2: Liste de tous les chats
bengal_obj = Bengal("Leo", 3)
chartreux_obj = Chartreux("Charly", 2)
siamese_obj = Siamese("Luna", 4)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Step 3: Instance de Pets
sara_pets = Pets(all_cats)

# Step 4: Faire marcher les chats
sara_pets.walk()


# --------------------------
# EXERCICE 2 : Chiens
# --------------------------

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            return f"{self.name} wins the fight"
        else:
            return f"{other_dog.name} wins the fight"

# Création de 3 chiens
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Max", 4, 18)

# Test des méthodes
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


# --------------------------
# EXERCICE 3 : PetDog
# --------------------------

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = ", ".join([dog.name if isinstance(dog, Dog) else dog for dog in args])
        print(f"{names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


# --------------------------
# EXERCICE 4 : Family et Person
# --------------------------

# Classe Person
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

# Classe Family
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    # Ajouter un membre
    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    # Vérifier la majorité
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found in the family.")

    # Présentation de la famille
    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")

# Test Family
my_family = Family("Smith")
my_family.born("Alice", 20)
my_family.born("Bob", 15)
my_family.family_presentation()
my_family.check_majority("Alice")
my_family.check_majority("Bob")
