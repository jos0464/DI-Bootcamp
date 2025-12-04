import random

# ---------------- Exercise 1: When will I retire? ----------------
def get_age(year, month, day):
    """Calcule l'âge en fonction de la date de naissance"""
    current_year = 2025  # Année actuelle (hard-codée)
    current_month = 11   # Mois actuel (hard-codé)
    
    age = current_year - year
    if month > current_month:  # Si le mois de naissance n'est pas encore passé cette année
        age -= 1
    return age

def can_retire(gender, date_of_birth):
    """Détermine si une personne peut prendre sa retraite"""
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)
    
    # Retraite: 67 pour hommes, 62 pour femmes (born after April 1947)
    if gender.lower() == 'm':
        retirement_age = 67
    elif gender.lower() == 'f':
        retirement_age = 62
    else:
        return False  # Genre invalide
    
    return age >= retirement_age

# Exemple d'utilisation
gender = input("Enter your gender (m/f): ")
dob = input("Enter your date of birth (yyyy/mm/dd): ")
if can_retire(gender, dob):
    print("You can retire!")
else:
    print("You cannot retire yet.")


# ---------------- Exercise 2: Sum X+XX+XXX+XXXX ----------------
def sum_pattern(x):
    """Calcule X + XX + XXX + XXXX"""
    total = int(str(x)) + int(str(x)*2) + int(str(x)*3) + int(str(x)*4)
    return total

# Exemple d'utilisation
num = int(input("Enter a number: "))
print("Result of X+XX+XXX+XXXX:", sum_pattern(num))


# ---------------- Exercise 3: Double Dice ----------------
def throw_dice():
    """Simule le lancer d'un dé (1 à 6)"""
    return random.randint(1, 6)

def throw_until_doubles():
    """Lance deux dés jusqu'à obtenir des doubles"""
    count = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        count += 1
        if die1 == die2:
            break
    return count

def main():
    """Simule 100 sessions de doubles et calcule les statistiques"""
    results = []
    for _ in range(100):
        throws = throw_until_doubles()
        results.append(throws)
    
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    
    print(f"Total throws to get 100 doubles: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# Appel de la fonction principale
main()
