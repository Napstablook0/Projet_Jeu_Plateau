
# -*- coding: utf-8 -*- 


"""Le plateau de jeu est en 8x8"""




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



def est_grille_valide(grille):
    """renvoie True si grille est valide, False sinon
    une grille es consideree valide si elle est une matrice carre non vide de taille 8"""
    if not type(grille) == list:
        return False
    elif len(grille) != 8:
        return False
    elif len(grille[0]) != 8:
        return False
    elif type(grille[0]) != list:
        return False
    else:
        return True



def afficher_grille(grille, joueur):
    """affiche la grille de jeu a l'ecran ainsi que la personne a qui c'est le tour,
    joueur est un str, 'X' ou 'O'"""
    assert est_grille_valide(grille), "grille doit etre une matrice non vide"
    assert joueur == "0" or joueur == "X", "parametre joueur invalide"

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
    print("C'est au tour du joueur : ", joueur)


def est_au_bon_format(message):
    """revoie True si coordonnees est valide, False sinon,
    message est un str"""
    assert type(message) == str, "message doit etre un str"

    ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H"]
    
    if len(message) != 2:
        return False
    elif message[0] not in ALPHABET:
        return False
    elif message[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        return False
    else:
        return True


def lettre_vers_nombre(lettre):
    """converti une coordonnee en lettre vers sa representation en nombre, A sera converti en 1, B en 2, etc..
    lettre est une des lettres majuscules suivante : ABCDEFGH"""
    assert type(lettre) == str, "lettre doit etre un str"
    assert len(lettre) == 1, "lettre doit etre un unique caractere"
    assert lettre in "ABCDEFGH", "lettre doit etre dans ABCDEFGH"

    if lettre == "A":
        return 1
    elif lettre == "B":
        return 2
    elif lettre == "C":
        return 3
    elif lettre == "D":
        return 4
    elif lettre == "E":
        return 5
    elif lettre == "F":
        return 6
    elif lettre == "G":
        return 7
    elif lettre == "H":
        return 8
    else:
        # Cas impossible
        pass


def est_dans_grille(ligne, colonne,  grille):
    """renvoie vraie si la case aux coordonnes (ligne, colonne) existe dans grille, faux sinon
    ligne est un str,
    colonne est un int,
    grille est une matrice carre non vide"""
    assert type(ligne) == str, "ligne doit etre un str"
    assert type(colonne) == int, "colonne doit etre un int"
    assert est_grille_valide(grille), "grille doit etre une matrice carre non vide"
    assert est_au_bon_format(ligne + str(colonne)), "ligne et colonne doivent etre au bon format"

    nombre_ligne = lettre_vers_nombre(ligne)
    return len(grille) >= colonne and len(grille[0]) >= nombre_ligne



def sont_coordonnees_correctes(coordonnees, grille):
    """renvoie True si coordonnees est au bon format et est dans grille,
    coordonnees est un str,
    grille est une matrice carre non vide"""
    assert type(coordonnees) == str, "coordonnees doit etre un str"
    assert est_grille_valide(grille), "grille doit etre une matrice carre non vide"

    if not est_au_bon_format(coordonnees):
        return False
    elif not est_dans_grille(coordonnees[0], int(coordonnees[1]), grille):
        return False
    else:
        return True
            
            

def demander_coordonnees_piece_a_deplacer(grille):
    """demande a l'utilisateur deux coordonnees de la forme xy
    avec x lettre et y entier correspondant a une case de la grille,
    A0 correspond a la case en bas a gauche
    x est compris enre A et H compris,
    y est compris entre 1 et 8 compris
    renvoie un str"""
    assert est_grille_valide(grille), "grille doit etre une matrice non vide"

    coordonnees_entrees = input("Entrez les coordonnees de la piece a deplacer [A1-H8] > ")

    while not sont_coordonnees_correctes(coordonnees_entrees, grille):
        print("les coordoonnes sont invalides")
        coordonnees_entrees = input("Entrez les coordonnees de la piece a deplacer [A1-H8] > ")
        
    
    return coordonnees_entrees


def demander_coordonnees_case_arrivee(grille):
    """demande a l'utilisateur deux coordonnees de la forme xy
    avec x lettre et y entier correspondant a une case de la grille,
    A0 correspond a la case en bas a gauche
    x est compris enre A et H compris,
    y est compris entre 1 et 8 compris
    renvoie le str xy"""
    assert est_grille_valide(grille), "grille doit etre une matrice non vide"

    coordonnees_entrees = input("Entrez les coordonnees de la case d'arrivee [A1-H8] > ")

    while not sont_coordonnees_correctes(coordonnees_entrees, grille):
        print("les coordoonnes entrees sont invalides")
        coordonnees_entrees = input("Entrez les coordonnees de la case d'arrivee [A1-H8] > ")
    
    return coordonnees_entrees



def atelier_2(grille):
    """Cette fonction ne sert que pour l evaluation par les pairs lors de l atelier 2,
    elle sert a ce que les pairs puissent interagir et tester les fonctions"""
    fin = False
    while not fin:
        print("-"*50)
        print("Que souhaitez vous faire ?\n")
        print("1 > afficher la configuration de debut")
        print("2 > afficher la configuration de milieu")
        print("3 > afficher la configuration de fin")
        print("4 > appeler les fonctions de saisie de coordonnees")
        print("5 > fermer le programme\n")

        entree_utilisateur = input("En attente de votre reponse... > ")

        if entree_utilisateur == "1":
            afficher_grille(grille, "X")
        elif entree_utilisateur == "2":
            afficher_grille(grille, "X")
        elif entree_utilisateur == "3":
            afficher_grille(grille, "X")
        elif entree_utilisateur == "4":
            coordonnes_piece_a_deplacer = demander_coordonnees_piece_a_deplacer(grille)
            coordonnes_case_arrivee = demander_coordonnees_case_arrivee(grille)
            
            print("\nCase de la piece a deplacer : ", coordonnes_piece_a_deplacer)
            print("Case d'arrivee : ", coordonnes_case_arrivee)

        elif entree_utilisateur == "5":
            fin = True
        else:
            pass
            

grille_actuelle = GRILLE_DEBUT
atelier_2(grille_actuelle)