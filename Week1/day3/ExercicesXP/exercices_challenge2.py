# ==========================================
# Timed Challenge #2: Perfect Number
# Last Updated: October 7th, 2025
# ==========================================

# Demander à l'utilisateur de saisir un nombre
x = int(input("Enter the Number: "))

# Initialiser une variable pour stocker la somme des diviseurs
sum_of_divisors = 0

# Parcourir tous les nombres de 1 à x-1 pour vérifier s'ils sont des diviseurs
for i in range(1, x):
    if x % i == 0:  # Si i divise x exactement
        sum_of_divisors += i  # Ajouter i à la somme

# Vérifier si la somme des diviseurs est égale au nombre
if sum_of_divisors == x:
    print(True)  # C'est un nombre parfait
else:
    print(False)  # Ce n'est pas un nombre parfait

# ==========================================
# Explications :
# 1. Un nombre parfait est égal à la somme de ses diviseurs (excluant lui-même).
# 2. La boucle for parcourt tous les nombres de 1 à x-1.
# 3. On utilise le modulo (%) pour vérifier si i divise x exactement.
# 4. On additionne tous les diviseurs trouvés.
# 5. Enfin, on compare la somme au nombre initial pour déterminer si c'est un nombre parfait.
# ==========================================
