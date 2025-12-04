# ======================================
# Définition de la classe Farm
# ======================================
class Farm:
    def __init__(self, farm_name):
        """
        Constructeur : initialise le nom de la ferme et le dictionnaire d'animaux vide
        """
        self.name = farm_name
        self.animals = {}  # dictionnaire : clé = type d'animal, valeur = quantité

    # Méthode pour ajouter un animal
    def add_animal(self, animal_type, count=1):
        """
        Ajoute un animal à la ferme.
        Si l'animal existe déjà, on incrémente son nombre.
        """
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    # Méthode pour afficher les informations complètes de la ferme
    def get_info(self):
        """
        Retourne une chaîne avec le nom de la ferme, les animaux et leurs quantités
        et la phrase E-I-E-I-0!
        """
        output = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            output += f"{animal} : {count}\n"
        output += "\n    E-I-E-I-0!"
        return output

    # Méthode pour retourner une liste triée des types d'animaux
    def get_animal_types(self):
        """
        Retourne la liste triée des types d'animaux
        """
        return sorted(self.animals.keys())

    # Méthode pour retourner un résumé court
    def get_short_info(self):
        """
        Retourne une phrase résumant la ferme et ses animaux,
        en ajoutant un 's' si le nombre d'animaux est > 1
        """
        types = self.get_animal_types()
        parts = []
        for animal in types:
            # Ajouter 's' si plus d'un animal
            name = animal + "s" if self.animals[animal] > 1 else animal
            parts.append(name)
        
        # Formater la phrase avec des virgules et 'and'
        if len(parts) > 1:
            sentence = ", ".join(parts[:-1]) + " and " + parts[-1]
        else:
            sentence = parts[0]
        
        return f"{self.name}'s farm has {sentence}."


# ======================================
# Test du code
# ======================================

# Création de la ferme
macdonald = Farm("McDonald")

# Ajouter des animaux un par un
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Afficher les informations complètes
print(macdonald.get_info())

print("\n--- Short info ---")
# Afficher le résumé court
print(macdonald.get_short_info())
