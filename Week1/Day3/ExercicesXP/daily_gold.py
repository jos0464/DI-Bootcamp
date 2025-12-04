# ==================================================
# Daily Challenge GOLD: Caesar Cipher
# Last Updated: October 7th, 2025
# ==================================================

# Fonction pour chiffrer un texte avec le Caesar Cipher
def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():  # Vérifier si c'est une lettre
            # Gérer les majuscules et minuscules séparément
            if char.isupper():
                # Calcul du décalage avec modulo 26 pour rester dans A-Z
                cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                cipher_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Si ce n'est pas une lettre, on garde le caractère tel quel
            cipher_text += char
    return cipher_text

# Fonction pour déchiffrer un texte avec le Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)  # Le déchiffrement est un chiffrement inverse

# Programme principal
print("Welcome to the Caesar Cipher program!")

# Demander à l'utilisateur s'il veut chiffrer ou déchiffrer
choice = input("Do you want to encrypt or decrypt? ").lower()

# Vérifier que l'utilisateur a entré un choix valide
if choice not in ['encrypt', 'decrypt']:
    print("Invalid choice! Please type 'encrypt' or 'decrypt'.")
else:
    # Demander le message
    message = input("Enter your message: ")
    # Demander le décalage
    try:
        shift = int(input("Enter the shift (number of positions): "))
    except ValueError:
        print("Invalid shift! Please enter an integer.")
        shift = 0

    # Exécuter l'action choisie
    if choice == 'encrypt':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = decrypt(message, shift)
        print("Decrypted message:", result)

# ==================================================
# Explications :
# 1. Chaque lettre est convertie en son code ASCII avec ord()
# 2. Le décalage est appliqué avec modulo 26 pour rester dans l'alphabet
# 3. chr() reconvertit le code ASCII en caractère
# 4. Les majuscules et minuscules sont traitées séparément
# 5. Les caractères non alphabétiques restent inchangés
# ==================================================
