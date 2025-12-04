# Coffee Shop Menu Manager

# ------------------ Initial Data ------------------
# On commence avec un menu contenant trois boissons avec leur prix
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

# ------------------ Functions ------------------

def show_menu(menu_dict):
    """
    Affiche tous les items du menu avec leur prix.
    Si le menu est vide, affiche un message approprié.
    """
    if not menu_dict:  # Vérifie si le dictionnaire est vide
        print("The menu is empty.")
    else:
        print("Current menu:")
        for drink, price in menu_dict.items():  # Parcourt tous les items
            print(f"{drink} - {price}₪")  # Affiche le nom et le prix

def add_item(menu_dict):
    """
    Ajoute un nouvel item au menu.
    Demande le nom de la boisson et son prix.
    Vérifie que le prix est positif et que l'item n'existe pas déjà.
    """
    drink = input("Enter new drink name: ").strip()  # Récupère le nom et enlève les espaces
    if drink in menu_dict:
        print("Item already exists!")  # L'item existe déjà
    else:
        try:
            price = float(input("Enter price: "))  # Récupère le prix et le convertit en float
            if price < 0:  # Vérifie que le prix n'est pas négatif
                print("Invalid price.")
                return
            menu_dict[drink] = price  # Ajoute l'item au dictionnaire
            print(f'"{drink}" added!')
        except ValueError:  # Gestion des erreurs si l'utilisateur ne met pas un nombre
            print("Invalid input for price.")

def update_price(menu_dict):
    """
    Met à jour le prix d'une boisson existante.
    Vérifie que la boisson existe et que le nouveau prix est valide.
    """
    drink = input("Which drink do you want to update? ").strip()
    if drink in menu_dict:
        try:
            price = float(input("Enter the new price: "))
            if price < 0:
                print("Invalid price.")
                return
            menu_dict[drink] = price  # Met à jour le prix
            print("Price updated!")
        except ValueError:
            print("Invalid input for price.")
    else:
        print("Item not found.")  # La boisson n'existe pas

def delete_item(menu_dict):
    """
    Supprime une boisson du menu.
    Vérifie que la boisson existe avant de la supprimer.
    """
    drink = input("Which drink do you want to delete? ").strip()
    if drink in menu_dict:
        del menu_dict[drink]  # Supprime l'item du dictionnaire
        print("Item deleted!")
    else:
        print("Item not found.")  # La boisson n'existe pas

def show_options():
    """
    Affiche le menu principal des actions disponibles pour l'utilisateur.
    """
    print("\nWhat would you like to do?")
    print("1. Show menu")       # Afficher le menu
    print("2. Add item")        # Ajouter une boisson
    print("3. Update price")    # Mettre à jour le prix d'une boisson
    print("4. Delete item")     # Supprimer une boisson
    print("5. Exit")            # Quitter le programme

def run_coffee_shop():
    """
    Fonction principale qui contrôle le programme.
    Boucle infinie jusqu'à ce que l'utilisateur choisisse de quitter.
    Selon le choix de l'utilisateur, appelle la fonction correspondante.
    """
    while True:
        show_options()  # Affiche les options à chaque tour
        choice = input("> ").strip()  # Récupère le choix de l'utilisateur
        if choice == "1":  # Afficher le menu
            show_menu(menu)
        elif choice == "2":  # Ajouter une boisson
            add_item(menu)
        elif choice == "3":  # Mettre à jour le prix
            update_price(menu)
        elif choice == "4":  # Supprimer une boisson
            delete_item(menu)
        elif choice == "5":  # Quitter le programme
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")  # Si choix invalide

# ------------------ Start Program ------------------
# Lancement du programme
run_coffee_shop()
