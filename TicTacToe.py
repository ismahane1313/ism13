import random

# Constantes
CASE_VIDE = " "
SIGNE_X, SIGNE_O = "X", "O"

# Plateau vide
plateau = [CASE_VIDE] * 9

# Combinaisons gagnantes
GAGNES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


# ----------------------
# AFFICHAGE ET LOGIQUE
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
        except ValueError:
            choix = 0
    return choix


# ----------------------
# IA : 3 modes (facile / moyen / difficile)
# ----------------------

def ordinateur(board, signe, mode):
    
    """
    mode = 1 : facile
    mode = 2 : moyen
    mode = 3 : difficile (Minimax imbattable)
    Retourne un index 0–8.
    """

    libres = [i for i in range(9) if board[i] == CASE_VIDE]
    adversaire = SIGNE_X if signe == SIGNE_O else SIGNE_O

    # ------------------------------------------
    # MODE 1 : facile (aléatoire)
    # ------------------------------------------
    if mode == 1:
        return random.choice(libres)

    # ------------------------------------------
    # MODE 2 : moyen (gagne / bloque / aléatoire)
    # ------------------------------------------
    if mode == 2:

        # 1) Gagner si possible
        for a, b, c in GAGNES:
            ligne = [board[a], board[b], board[c]]
            if ligne.count(signe) == 2 and ligne.count(CASE_VIDE) == 1:
                return [a, b, c][ligne.index(CASE_VIDE)]

        # 2) Bloquer si le joueur va gagner
        for a, b, c in GAGNES:
            ligne = [board[a], board[b], board[c]]
            if ligne.count(adversaire) == 2 and ligne.count(CASE_VIDE) == 1:
                return [a, b, c][ligne.index(CASE_VIDE)]

        # 3) Sinon aléatoire
        return random.choice(libres)

    # ------------------------------------------
    # MODE 3 : difficile (MINIMAX intégrÉ)
    # ------------------------------------------
    if mode == 3:

        # Évalue l'état du plateau : +1 IA gagne, -1 joueur gagne, 0 sinon
        def eval_board(b):
            for a, b2, c in GAGNES:
                if b[a] != CASE_VIDE and b[a] == b[b2] == b[c]:
                    return +1 if b[a] == signe else -1
            return 0

        def minimax(b, isMax):
            score = eval_board(b)

            if score != 0:
                return score
            if CASE_VIDE not in b:
                return 0

            if isMax:  # tour de l'IA
                best = -999
                for i in range(9):
                    if b[i] == CASE_VIDE:
                        b[i] = signe
                        best = max(best, minimax(b, False))
                        b[i] = CASE_VIDE
                return best

            else:  # tour de l'adversaire
                best = 999
                for i in range(9):
                    if b[i] == CASE_VIDE:
                        b[i] = adversaire
                        best = min(best, minimax(b, True))
                        b[i] = CASE_VIDE
                return best

        meilleur_score = -999
        meilleur_coup = libres[0]

        for i in libres:
            board[i] = signe
            score = minimax(board, False)
            board[i] = CASE_VIDE

            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = i

        return meilleur_coup


# ----------------------
# JEU PRINCIPAL
# ----------------------

joueur = SIGNE_X
nb_joueurs = int(input("Entrez le nombre de joueurs (1 ou 2) : "))

if nb_joueurs == 2:

    while True:
        afficher_plateau()
        choix = choisir_case_joueur()
        plateau[choix - 1] = joueur

        if victoire():
            print(f"\nLe joueur {joueur} gagne la partie !")
            afficher_plateau()
            break

        if match_nul():
            print("\nMatch nul !")
            afficher_plateau()
            break

        joueur = SIGNE_O if joueur == SIGNE_X else SIGNE_X

else:

    niveau = int(input("Choisissez le niveau de l'ordinateur (1 - facile, 2 - moyen, 3 - difficile) : "))

    while True:
        afficher_plateau()

        if joueur == SIGNE_X:
            choix = choisir_case_joueur()

        else:
            case = ordinateur(plateau, SIGNE_O, niveau)
            choix = case + 1
            print(f"L'ordinateur joue {choix}")

        plateau[choix - 1] = joueur

        if victoire():
            print(f"\nLe joueur {joueur} gagne la partie !")
            afficher_plateau()
            break

        if match_nul():
            print("\nMatch nul !")
            afficher_plateau()
            break

        joueur = SIGNE_O if joueur == SIGNE_X else SIGNE_X