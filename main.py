GRILLE_DEBUT = [["", "O", "", "O", "", "O", "", "O"],
                ["O", "", "O", "", "O", "", "O", ""],
                ["", "O", "", "O", "", "O", "", "O"],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["X", "", "X", "", "X", "", "X", ""],
                ["", "X", "", "X", "", "X", "", "X"],
                ["X", "", "X", "", "X", "", "X", ""]]


GRILLE_MILIEU = [["", "", "", "O", "", "O", "", "O"],
                ["", "", "", "", "O", "", "", ""],
                ["", "O", "", "", "", "", "", "O"],
                ["", "", "", "", "", "", "X", ""],
                ["", "O", "", "", "", "O", "", ""],
                ["X", "", "X", "", "", "", "X", ""],
                ["", "", "", "X", "", "X", "", "O"],
                ["X", "", "X", "", "X", "", "", ""]]



GRILLE_FIN = [["", "", "O", "", "", "", "", ""],
            ["X", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "O", "", ""],
            ["", "O", "", "", "", "", "", ""],
            ["", "", "", "", "", "X", "", ""]]


grille_actuelle = GRILLE_DEBUT


def est_grille_valide(grille):
    """renvoie True si grille est valide, False sinon"""
    if not type(grille) == list:
        return False
    elif len(grille) >= 1:
        return False
    elif len(grille[0]) >= 1:
        return False
    elif type(grille[0]) == list:
        return False
    else:
        return True


def afficher_grille(grille):
    """affiche la grille de jeu a l'ecran"""
    assert est_grille_valide(grille), "grille doit etre une matrice non vide"

    print("-"*33)

    for i_ligne in range(len(grille)):

        for i_colonne in range(len(grille[0])):

            case = grille[i_ligne][i_colonne]
            print("| ", end="")
            if case == "":
                print("  ", end="")
            else:
                print(case + " ", end="")

        print("|")

    print("-"*33)


def est_coordonnees_valide(coordonnees):
    """revoie True si coordonnees est valide, False sinon"""

    ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

    if len(coordonnees) != 2:
        return False
    elif coordonnees[0] in ALPHABET:
        pass # TODO

def demander_coordonnees(grille):
    """demande a l'utilisateur des coordonnees de la forme xy
    avec x lettre et y entier correspondant a une case de la grille,
    A0 correspond a la case en bas a gauche"""
    assert est_grille_valide(grille), "grille doit etre une matrice non vide"

    coordonnees_entrees = input("Entrez les coordonnees de la piece a deplacer > ")

    while not est_coordonnees_valide(coordonnees_entrees):
        print("coordoonnes invalides, ex : B7")
        coordonnees_entrees = input("Entrez les coordonnees de la piece a deplacer > ")
    
    return coordonnees_entrees