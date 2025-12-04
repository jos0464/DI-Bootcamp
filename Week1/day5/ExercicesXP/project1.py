# ==============================
# Mini-Projet : Tic Tac Toe
# ==============================
# Objectif :
# - Créer un plateau de jeu 3x3
# - Permettre à deux joueurs de jouer à tour de rôle
# - Vérifier victoire ou égalité
# - Utiliser des fonctions pour organiser le code

# Initialisation du plateau avec un dictionnaire
# Les clés sont les positions de 1 à 9
board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

# Fonction pour afficher le plateau
def display_board(board):
    # Affiche chaque ligne du plateau
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[7]} | {board[8]} | {board[9]}")

# Fonction pour gérer le tour d'un joueur
def player_turn(player_symbol):
    position = int(input(f"Player {player_symbol}, choose a position (1-9): "))
    if board[position] == " ":
        # La case est libre, on place le symbole
        board[position] = player_symbol
    else:
        # La case est déjà occupée
        print("Position already taken! Try again.")
        player_turn(player_symbol)  # Redemander au joueur

# Fonction pour vérifier s'il y a un gagnant
def check_winner():
    # Toutes les combinaisons gagnantes
    winning_combinations = [
        [1,2,3], [4,5,6], [7,8,9],  # Lignes
        [1,4,7], [2,5,8], [3,6,9],  # Colonnes
        [1,5,9], [3,5,7]            # Diagonales
    ]
    # Vérifier chaque combinaison
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True  # Il y a un gagnant
    return False  # Pas de gagnant

# Boucle principale du jeu
def main():
    turn = "X"  # Premier joueur
    for _ in range(9):  # Maximum 9 tours
        display_board(board)
        player_turn(turn)
        if check_winner():
            display_board(board)
            print(f"Player {turn} wins!")  # Annonce du gagnant
            return
        # Alterner entre X et O
        turn = "O" if turn == "X" else "X"
    display_board(board)
    print("It's a tie!")  # Si aucune victoire après 9 tours

# Lancer le jeu
main()
