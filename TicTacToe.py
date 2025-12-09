import random

# Constants
CASE_VIDE = " "
SIGNE_X, SIGNE_O = "X", "O"

# Empty board
plateau = [CASE_VIDE] * 9

# Winning combination
GAGNES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


# ----------------------
# DISPLAY AND LOGIC
# ----------------------

def afficher_plateau():
    for i in range(9):
        case = plateau[i] if plateau[i] != CASE_VIDE else i + 1
        print("|", case, end=" ")
        if i % 3 == 2:
            print("│")
            print("---------")


def victoire():
    for a, b, c in GAGNES:
        if plateau[a] != CASE_VIDE and plateau[a] == plateau[b] == plateau[c]:
            return True
    return False


def match_nul():
    return CASE_VIDE not in plateau


def choisir_case_joueur():
    choix = 0
    while choix not in range(1, 10) or plateau[choix - 1] != CASE_VIDE:
        try:
            choix = int(input("Choisissez une case (1-9) : "))
        except :
            choix = 0
    return choix


# ----------------------
# IA MODE
# ----------------------

def ordinateur(board, signe, mode):


    libres = [i for i in range(9) if board[i] == CASE_VIDE]
    adversaire = SIGNE_X if signe == SIGNE_O else SIGNE_O

    # ------------------------------------------
    # MODE 1 : easy
    # ------------------------------------------
    if mode == 1:
        return random.choice(libres)

    # ------------------------------------------
    # MODE 2 : medium
    # ------------------------------------------
    if mode == 2:

        # 1) Win if possible
        for a, b, c in GAGNES:
            ligne = [board[a], board[b], board[c]]
            if ligne.count(signe) == 2 and ligne.count(CASE_VIDE) == 1:
                return [a, b, c][ligne.index(CASE_VIDE)]

        # 2) Block if the player is about to win
        for a, b, c in GAGNES:
            ligne = [board[a], board[b], board[c]]
            if ligne.count(adversaire) == 2 and ligne.count(CASE_VIDE) == 1:
                return [a, b, c][ligne.index(CASE_VIDE)]

        # 3) Else random
        return random.choice(libres)

    # ------------------------------------------
    # MODE 3 : hard
    # ------------------------------------------
    if mode == 3:

        def case_gagnante(board, joueur):
            for a, b, c in GAGNES:
                trio = [board[a], board[b], board[c]]
                if trio.count(joueur) == 2 and trio.count(CASE_VIDE) == 1:
                    if board[a] == CASE_VIDE: return a
                    if board[b] == CASE_VIDE: return b
                    if board[c] == CASE_VIDE: return c
            return None


        # 1. Win if possible
        coup = case_gagnante(board, signe)
        if coup is not None:
            return coup

        # 2. Block the player
        coup = case_gagnante(board, adversaire)
        if coup is not None:
            return coup

        # 3. Take the middle
        if board[4] == CASE_VIDE:
            return 4

        # 4. Play a corner
        for c in [0, 2, 6, 8]:
            if board[c] == CASE_VIDE:
                return c

        # 5. Play in any empty space
        for i in range(9):
            if board[i] == CASE_VIDE:
                return i




# ----------------------
# Game
# ----------------------

# Define the symbols for the players
SIGNE_X = "X"
SIGNE_O = "O"

# Initialize the board with 9 empty spaces
plateau = [" " for _ in range(9)]

# Choose the starting player
joueur = SIGNE_X

# Ask for the number of players (1 or 2)
nb_joueurs = int(input("Enter the number of players (1 or 2): "))

# Two-player mode
if nb_joueurs == 2:

    # Main game loop
    while True:
        afficher_plateau()  # Display the current board
        choix = choisir_case_joueur()  # Ask the player to choose a square
        plateau[choix - 1] = joueur  # Update the board with the player's symbol

        # Check if the current player has won
        if victoire():
            print(f"\nPlayer {joueur} wins!")
            afficher_plateau()
            break  # Exit loop if there is a winner

        # Check if the board is full without a winner
        if match_nul():
            print("\nIt's a tie!")
            afficher_plateau()
            break  # Exit loop if it's a tie

        # Switch player for the next turn
        joueur = SIGNE_O if joueur == SIGNE_X else SIGNE_X

# Player vs computer mode
else:

    # Ask for the computer difficulty level
    niveau = int(input("Choose the computer's level (1 - easy, 2 - medium, 3 - hard): "))

    # Main game loop
    while True:
        afficher_plateau()  # Display the current board

        if joueur == SIGNE_X:
            # Human player's turn
            choix = choisir_case_joueur()
        else:
            # Computer's turn
            case = ordinateur(plateau, SIGNE_O, niveau)  # AI chooses a square based on difficulty
            choix = case + 1  # Adjust index for display
            print(f"Computer plays {choix}")

        plateau[choix - 1] = joueur  # Update the board with the player's or computer's symbol

        # Check if the current player has won
        if victoire():
            print(f"\nPlayer {joueur} wins!")
            afficher_plateau()
            break

        # Check if the board is full without a winner
        if match_nul():
            print("\nIt's a tie!")
            afficher_plateau()
            break

        # Switch player for the next turn
        joueur = SIGNE_O if joueur == SIGNE_X else SIGNE_X
