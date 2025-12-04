case_vide = " "

plateau = [ case_vide for i in range(9)]

signes = ("X" , "O")
numero_case = ("1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9")

joueur = signes[0]

def afficher_plateau():
    print(" ----------- ")
    for i in range(9):
        print("|" , plateau[i] if plateau[i] != case_vide else numero_case[i] , end=" ")
        if i % 3 == 2:
            print("|")
            print(" ---|---|--- ")

while True:
    afficher_plateau()
    choix_joueur = 0

    while choix_joueur < 1 or choix_joueur > 9 or plateau[choix_joueur - 1] != case_vide:
        choix_joueur = int(input("Joueur, choisissez une case 1-9: "))

    plateau[choix_joueur - 1] = joueur

    if case_vide != plateau[0] == plateau[1] == plateau[2] \
    or case_vide != plateau[3] == plateau[4] == plateau[5] \
    or case_vide != plateau[6] == plateau[7] == plateau[8] \
    or case_vide != plateau[0] == plateau[3] == plateau[6] \
    or case_vide != plateau[1] == plateau[4] == plateau[7] \
    or case_vide != plateau[2] == plateau[5] == plateau[8] \
    or case_vide != plateau[2] == plateau[4] == plateau[8] \
    or case_vide != plateau[2] == plateau[4] == plateau[6]:
        print("Le joueur", joueur, "Gagne la partie !!")
        afficher_plateau()
        break

    if case_vide not in plateau:
        print("Match nul...")
        afficher_plateau()
        break

    joueur = signes[1] if joueur == signes[0] else signes[0]

