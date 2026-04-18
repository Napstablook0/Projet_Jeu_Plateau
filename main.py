
# -*- coding: utf-8 -*- 


"""Le plateau de jeu est en 8x8,
coordonnees grille :

    1   2   3   4   5   6   7   8
A
B
C
D
E
F
G
H

le joueur X est en bas et le joueur O en haut"""


# ---------------- variables de configurations de tests ----------------

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



GRILLE_FIN = [["", "", "", "O", "", "", "", ""],
             ["X", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "O", "", "", ""],
             ["", "O", "", "", "", "", "", ""],
             ["", "", "", "", "X", "", "", ""]]


# -------------------------------- fonctions de verifications de valeurs --------------------------------

def est_grille_valide(grille):
    """renvoie True si grille est valide, False sinon
    une grille est consideree valide si elle est une matrice carre de taille 8 de taille 8"""

    VALEURS_VALIDES = ["", "X", "O"]

    if not type(grille) == list:
        return False
    
    for ligne in grille:
        if type(ligne) != list:
            return False
        elif len(ligne) != 8:
            return False
        
        for valeur in ligne:
            if valeur not in VALEURS_VALIDES:
                return False
            
    return len(grille) == 8


def est_au_bon_format(message):
    """revoie True si les coordonnees message est au bon format, False sinon,
    message est un str
    J8 est au bon format alors que AA, 77, 8J ne le sont pas"""
    assert type(message) == str, "message doit etre un str"

    LETTRES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    CHIFFRES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if len(message) != 2:
        return False
    elif message[0] not in LETTRES:
        return False
    elif message[1] not in CHIFFRES:
        return False
    else:
        return True
    

def sont_coordonnees_correctes(coordonnees, grille):
    """renvoie True si coordonnees est au bon format et est dans grille,
    coordonnees est un str, e.g : A3
    grille est une matrice carre de taille 8"""
    assert type(coordonnees) == str, "coordonnees doit etre un str"
    assert est_grille_valide(grille), "grille doit etre une matrice carre de taille 8"

    if not est_au_bon_format(coordonnees):
        return False
    elif not est_dans_grille(coordonnees[0], int(coordonnees[1]), grille):
        return False
    else:
        return True
    

def est_dans_grille(ligne, colonne,  grille):
    """renvoie True si la case aux coordonnes (ligne, colonne) existe dans grille, False sinon
    ligne est un str,
    colonne est un int,
    grille est une matrice carre de taille 8"""
    assert type(ligne) == str, "ligne doit etre un str"
    assert type(colonne) == int, "colonne doit etre un int"
    assert est_grille_valide(grille), "grille doit etre une matrice carre de taille 8"

    i_ligne = lettre_vers_nombre(ligne)
    return len(grille) >= colonne and len(grille[0]) >= i_ligne


def est_deplacement(grille, depart, arrivee, joueur):
    """renvoie True si le mouvement depart - arrivee est un deplacement,
    !!! une capture n est pas un deplacement !!!
    depart et arrivee sont des coordonnees valides :
    depart est un str,
    arrivee est un str,
    joueur est un str, X ou O"""
    assert est_grille_valide(grille), "grille invalide"
    assert sont_coordonnees_correctes(depart, grille), "coordonnees de depart non valide"
    assert sont_coordonnees_correctes(arrivee, grille), "coordonnees d arrivee non valide"
    assert joueur == "X" or joueur == "O", "joueur invalide"


    depart_i, depart_j = coordonnees_vers_indices(depart)
    arrivee_i, arrivee_j = coordonnees_vers_indices(arrivee)

    

    if grille[depart_i][depart_j] != joueur:
        return False
    elif grille[arrivee_i][arrivee_j] != "":
        return False
    elif depart_i != arrivee_i - 1 and depart_i != arrivee_i + 1:
        return False
    elif depart_j != arrivee_j - 1 and depart_j != arrivee_j + 1:
        return False
    else:
        return True
        
    


def est_capture(grille, depart, arrivee, joueur):
    """renvoie True si le mouvement depart - arrivee est une capture
    depart et arrivee sont des coordonnees valides :
    depart est un str,
    arrivee est un str,
    joueur est un str, X ou O"""
    assert est_grille_valide(grille), "grille invalide"
    assert sont_coordonnees_correctes(depart, grille), "coordonnees de depart non valide"
    assert sont_coordonnees_correctes(arrivee, grille), "coordonnees d arrivee non valide"
    assert joueur == "X" or joueur == "O", "joueur invalide"

    depart_i, depart_j = coordonnees_vers_indices(depart)
    arrivee_i, arrivee_j = coordonnees_vers_indices(arrivee)
    
    if joueur == "X":
        if grille[depart_i][depart_j] != "X":
            return False
        elif grille[arrivee_i][arrivee_j] != "":
            return False
        elif arrivee_i != depart_i - 2:
            return False
        elif depart_j != arrivee_j - 2 and depart_j != arrivee_j + 2:
            return False
        elif depart_j == arrivee_j - 2 and grille[depart_i - 1][depart_j + 1] != "O":
            return False
        elif depart_j == arrivee_j + 2 and grille[depart_i - 1][depart_j - 1] != "O":
            return False
        else:
            return True
        
    elif joueur == "O":
        if grille[depart_i][depart_j] != "O":
            return False
        elif grille[arrivee_i][arrivee_j] != "":
            return False
        elif arrivee_i != depart_i + 2:
            return False
        elif depart_j != arrivee_j - 2 and depart_j != arrivee_j + 2:
            return False
        elif depart_j == arrivee_j - 2 and grille[depart_i + 1][depart_j + 1] != "X":
            return False
        elif depart_j == arrivee_j + 2 and grille[depart_i + 1][depart_j - 1] != "X":
            return False
        else:
            return True
        
    else:
        # cas impossible
        return False



def est_capture_possible_depart(grille, depart, joueur):
    """renvoie True si le joueur joueur peut effectuer une capture avec la piece a la position depart, False sinon
    depart est des coordonnees valides, e.g : A3
    joueur est un str, 'X" ou 'O"""
    assert est_grille_valide(grille), "grille invalide"
    assert joueur == "X" or joueur == "O", "joueur invalide"
    assert est_au_bon_format(depart), "depart mauvais format"


    depart_i, depart_j = coordonnees_vers_indices(depart)
    
    if joueur == "X":
        if depart_i - 2 >= 0 and depart_j - 2 >= 0 and depart_i - 2 < 8 and depart_j - 2 < 8:
            arrivee = indices_vers_coordoonees(depart_i - 2, depart_j - 2)
            if est_capture(grille, depart, arrivee, joueur):
                return True
            
        if depart_i - 2 >= 0 and depart_j + 2 >= 0 and depart_i - 2 < 8 and depart_j + 2 < 8:
            arrivee = indices_vers_coordoonees(depart_i - 2, depart_j + 2)
            if est_capture(grille, depart, arrivee, joueur):
                return True
        
        return False
        
    elif joueur == "O":
        if depart_i + 2 >= 0 and depart_j - 2 >= 0 and depart_i - 2 < 8 and depart_j - 2 < 8:
            arrivee = indices_vers_coordoonees(depart_i + 2, depart_j - 2)
            if est_capture(grille, depart, arrivee, joueur):
                return True
            
        if depart_i + 2 >= 0 and depart_j + 2 >= 0 and depart_i - 2 < 8 and depart_j + 2 < 8:
            arrivee = indices_vers_coordoonees(depart_i + 2, depart_j + 2)
            if est_capture(grille, depart, arrivee, joueur):
                return True
        
        return False
    else:
        # cas impossible
        return False
    

def est_capture_possible(grille, joueur):
    """renvoie True si le joueur joueur peut effecteur une capture, False sinon"""
    assert est_grille_valide(grille), "grille invalide"
    assert joueur == "X"  or joueur == "O", "joueur invalide"

    for i in range(len(grille)):
        for j in range(len(grille[0])):
            case = grille[i][j]
            
            if case == joueur:
                depart = indices_vers_coordoonees(i, j)
                if est_capture_possible_depart(grille, depart, joueur):
                    return True
                
    return False



# -------------------------------- fonctions d affichage --------------------------------


def afficher_ligne(grille, i_ligne):
    """affiche une ligne de la grille
    i_ligne est un int correspondant a un indice de grille de la ligne a afficher"""
    assert est_grille_valide(grille), "grille doit etre une matrice carre non vide"
    assert type(i_ligne) == int, "i_ligne doit etre un entier correspondant a un indice de grille"
    assert i_ligne >= 0 and i_ligne < len(grille), "i_ligne doit etre un entier correspondant a un indice de grille"

    LETTRES = ["A", "B", "C", "D", "E", "F", "G", "H"]

    # afficher la lettre de la ligne actuelle
    print(LETTRES[i_ligne] + " ", end="")

    # affichage de la ligne
    for i_colonne in range(len(grille[0])):

        case = grille[i_ligne][i_colonne]
        # separation des cases
        print("| ", end="")
        
        # affichage de la case
        if case == "":
            print("  ", end="")
        else:
            print(case + " ", end="")

    # fin de la ligne
    print("|")


def afficher_grille(grille, pieces_capturees_X, pieces_capturees_O):
    """affiche l etat actuel de la partie tel que le plateau, a qui c est le tour et les nombres de pieces capturees,
    joueur est un str, 'X' ou 'O' correspondant du joueur qui doit jouer ce tour ci
    pieces_capturees_X est un int correspondant au nombre de pieces (X) capturees par le joueur O
    pieces_capturees_O est un int correspondant au nombre de pieces (O) capturees par le joueur X"""
    assert est_grille_valide(grille), "grille doit etre une matrice de taille 8"
    

    

    # afficher les numero des colonnes
    print("    1   2   3   4   5   6   7   8")
    print("  " + "-"*33)

    for i_ligne in range(len(grille)):

        afficher_ligne(grille, i_ligne)

    print("  " + "-"*33)

    # affichage des pieces capturees
    print("Pieces capturees :")
    print("   " + "X " * pieces_capturees_X)
    print("   " + "O " * pieces_capturees_O)
    print()

    



# -------------------------------- fonctions de conversion --------------------------------


def lettre_vers_nombre(lettre):
    """converti une coordonnee en lettre vers sa representation en nombre, A sera converti en 1, B en 2, etc..
    lettre est une des lettres majuscules suivante : ABCDEFGHI"""
    assert type(lettre) == str, "lettre doit etre un str"
    assert len(lettre) == 1, "lettre doit etre un unique caractere"
    LETTRES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    assert lettre in LETTRES, "lettre doit etre une majuscule seule"

    dico_convertion = {LETTRES[i]:i+1 for i in range(len(LETTRES))}
    # = {'A': 1, 'B': 2, ..., 'Z': 26}

    return dico_convertion[lettre]


def coordonnees_vers_indices(coordonnees):
    """converti des coordonnes vers des indices de liste, e.g : A3 sera converti en [0, 4]
    coordonnees est un str
    renvoie une liste de 2 int"""
    assert est_au_bon_format(coordonnees), "coordonnees doit etre au bon format"

    return [lettre_vers_nombre(coordonnees[0]) - 1, int(coordonnees[1]) - 1]


def indices_vers_coordoonees(i, j):
    """converti des indices vers leur coordonnees dans une grille, e.g : 1, 2 sera converti en B3
    i et j sont des int
    renvoie un str"""
    assert type(i) == int and type(j) == int, "indices doivent etre des int"
    assert i >= 0 and i < 8 and j >= 0 and j < 8, "indices invalides"

    LETTRES = ["A", "B", "C", "D", "E", "F", "G", "H"]
    return LETTRES[i] + str(j + 1)


# -------------------------------- fonctions d entrees utilisateur --------------------------------


def demander_coordonnees_piece_a_deplacer(grille):
    """demande a l'utilisateur deux coordonnees de la forme xy
    avec x lettre et y entier correspondant a une case de la grille,
    A0 correspond a la case en bas a gauche
    x est compris enre A et H compris,
    y est compris entre 1 et 8 compris
    renvoie un str"""
    assert est_grille_valide(grille), "grille doit etre une matrice de taille 8"

    coordonnees_entrees = input("Entrez les coordonnees de la piece a deplacer [A1-H8] > ")

    # indication pour les pairs (pour le bareme) : la fonction sont_coordonnees_correctes utilise la fonction est_dans_grille
    while not sont_coordonnees_correctes(coordonnees_entrees, grille):
        print("les coordoonnes entrees sont invalides")
        coordonnees_entrees = input("Entrez les coordonnees de la piece a deplacer [A1-H8] > ")
        
    return coordonnees_entrees


def demander_coordonnees_case_arrivee(grille):
    """demande a l'utilisateur deux coordonnees de la forme xy
    avec x lettre et y entier correspondant a une case de la grille,
    A0 correspond a la case en bas a gauche
    x est compris enre A et H compris,
    y est compris entre 1 et 8 compris
    renvoie le str xy entre par l utilisateur"""
    assert est_grille_valide(grille), "grille doit etre une matrice de taille 8"

    coordonnees_entrees = input("Entrez les coordonnees de la case d'arrivee [A1-H8] > ")

    # indication pour les pairs : la fonction sont_coordonnees_correctes utilise la fonction est_dans_grille
    while not sont_coordonnees_correctes(coordonnees_entrees, grille):
        print("les coordoonnes entrees sont invalides")
        coordonnees_entrees = input("Entrez les coordonnees de la case d'arrivee [A1-H8] > ")
    
    return coordonnees_entrees



# -------------------------------- fonctions de deplacements --------------------------------


def deplacement(grille, depart, arrivee, joueur):
    """effectue un deplacement si il est valide
    depart et arrivee sont des coordonnees valides :
    depart est un str, correspond a des coordonnees de grille
    arrivee est un str, correspond a des coordonnees de grille
    joueur est un str, 'X' ou 'O'
    renvoie un str, 'deplacement' si le mouvement effectuee est un deplacement, 'capture' si c est une capture et '' si le mouvement est invalide"""
    assert est_grille_valide(grille), "grille non valide"
    assert sont_coordonnees_correctes(depart, grille), "coordonnees de depart non valide"
    assert sont_coordonnees_correctes(arrivee, grille), "coordonnees d arrivee non valide"
    assert joueur == "X" or joueur == "O", "joueur invalide"

    depart_i, depart_j = coordonnees_vers_indices(depart)
    arrivee_i, arrivee_j = coordonnees_vers_indices(arrivee)

    if est_deplacement(grille, depart, arrivee, joueur):
        grille[depart_i][depart_j] = ""
        if arrivee_i == 0 or arrivee_i == len(grille) - 1:
            # cas mort subite
            # TODO : creer fonction trouver indices arrivee
            pass
        else:
            grille[arrivee_i][arrivee_j] = joueur

        return "deplacement"
    
    elif est_capture(grille, depart, arrivee, joueur):
        grille[depart_i][depart_j] = ""
        grille[arrivee_i][arrivee_j] = joueur

        #calcul des indices correspondant a l emplacement de la piece capturee
        piece_capturee_i = (depart_i + arrivee_i) // 2
        piece_capturee_j = (depart_j + arrivee_j) // 2
        grille[piece_capturee_i][piece_capturee_j] = ""

        return "capture"
    
    else:
        return ""


# -------------------------------- fonctions de controle --------------------------------


def compter_pieces(grille, joueur):
    """compte le nombre de pieces restant au joueur joueur
    joueur est un str, 'X" ou 'O'"""
    assert est_grille_valide(grille), "grille invalide"
    assert joueur == "X" or joueur == "O", "joueur invalide"

    compteur = 0
    for ligne in grille:
        for case in ligne:
            compteur += case == joueur

    return compteur


def gagnant(grille):
    """renvoie le str 'X' si le joueur X a gagne, 'O' si le joueur O a gagne, un str vide si la partie n est pas finie"""
    assert est_grille_valide(grille), "grille invalide"


    if compter_pieces(grille, "O") == 0:
        return "X"
        
    elif compter_pieces(grille, "X") == 0:
        return "O"
    else:
        return ""




def effectuer_tour(grille, joueur, pieces_capturees_X, pieces_capturees_O):
    """realise le tour d un joueur :
    demande le deplacement souhaite a l utilisateur et modifie grille en consequence, cette fonction fait des affichages de la grille
    cette fonction pre-suppose que le tour d avant a ete effectue de facon valide (i.e : le joueur adverse actuel ne peut pas faire de capture, sinon il l aurait fait au tour d avant)
    joueur est un str, 'X' ou 'O'"""
    assert est_grille_valide(grille), "grille invalide"
    assert joueur == "X" or joueur == "O", "joueur invalide"

    print("C est au tour du joueur " + joueur)

    depart = demander_coordonnees_piece_a_deplacer(grille)
    arrivee = demander_coordonnees_case_arrivee(grille)


    fini = False
    while not fini:

        while est_capture_possible(grille, joueur) and not est_capture(grille, depart, arrivee, joueur):
            print("Une capture est possible et donc obligatoire !")
            depart = demander_coordonnees_piece_a_deplacer(grille)
            arrivee = demander_coordonnees_case_arrivee(grille)
        
        coup = deplacement(grille, depart, arrivee, joueur)
        
        if coup == "deplacement":
            fini = True

        elif coup == "":
            print("Coup illegal !")
            depart = demander_coordonnees_piece_a_deplacer(grille)
            arrivee = demander_coordonnees_case_arrivee(grille)

        elif coup == "capture":
            if joueur == "X": pieces_capturees_O -= 1
            elif joueur == "O": pieces_capturees_X -= 1
            
            if est_capture_possible(grille, joueur):
                print("une capture successive est possible et donc obligatoire")
                depart = demander_coordonnees_piece_a_deplacer(grille)
                arrivee = demander_coordonnees_case_arrivee(grille)
            else:
                fini = True
                

        else:
            # cas impossible
            pass
    
    
    afficher_grille(grille, pieces_capturees_X, pieces_capturees_O)
        








# -------------------------------- fonctions de tests --------------------------------


# ------------ fonctions de tests unitaire ------------

def test_lettre_vers_nombre():
    assert lettre_vers_nombre("A") == 1, "test lettre_vers_nombre"
    assert lettre_vers_nombre("B") == 2, "test lettre_vers_nombre"
    assert lettre_vers_nombre("C") == 3, "test lettre_vers_nombre"
    assert lettre_vers_nombre("D") == 4, "test lettre_vers_nombre"
    assert lettre_vers_nombre("E") == 5, "test lettre_vers_nombre"
    assert lettre_vers_nombre("F") == 6, "test lettre_vers_nombre"
    assert lettre_vers_nombre("G") == 7, "test lettre_vers_nombre"
    assert lettre_vers_nombre("H") == 8, "test lettre_vers_nombre"
    assert lettre_vers_nombre("I") == 9, "test lettre_vers_nombre"


def test_sont_coordonnees_correctes():
    GRILLE = [["", "O", "", "O", "", "O", "", "O"],
             ["O", "", "O", "", "O", "", "O", ""],
             ["", "O", "", "O", "", "O", "", "O"],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["X", "", "X", "", "X", "", "X", ""],
             ["", "X", "", "X", "", "X", "", "X"],
             ["X", "", "X", "", "X", "", "X", ""]]
    
    assert sont_coordonnees_correctes("A1", GRILLE) == True, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("C8", GRILLE) == True, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("H8", GRILLE) == True, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("H1", GRILLE) == True, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("D5", GRILLE) == True, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("A9", GRILLE) == False, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("I9", GRILLE) == False, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("J8", GRILLE) == False, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("C11", GRILLE) == False, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("3A", GRILLE) == False, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("AAA", GRILLE) == False, "test sont_coordonnees_correctes"
    assert sont_coordonnees_correctes("3333", GRILLE) == False, "test sont_coordonnees_correctes"


def test_est_dans_grille():
    GRILLE = [["", "O", "", "O", "", "O", "", "O"],
             ["O", "", "O", "", "O", "", "O", ""],
             ["", "O", "", "O", "", "O", "", "O"],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["X", "", "X", "", "X", "", "X", ""],
             ["", "X", "", "X", "", "X", "", "X"],
             ["X", "", "X", "", "X", "", "X", ""]]
    
    assert est_dans_grille("A", 1, GRILLE) == True, "test est_dans_grille"
    assert est_dans_grille("C", 8, GRILLE) == True, "test est_dans_grille"
    assert est_dans_grille("H", 8, GRILLE) == True, "test est_dans_grille"
    assert est_dans_grille("H", 1, GRILLE) == True, "test est_dans_grille"
    assert est_dans_grille("D", 5, GRILLE) == True, "test est_dans_grille"
    assert est_dans_grille("A", 9, GRILLE) == False, "test est_dans_grille"
    assert est_dans_grille("I", 9, GRILLE) == False, "test est_dans_grille"
    assert est_dans_grille("J", 8, GRILLE) == False, "test est_dans_grille"


def test_est_au_bon_format():
    assert est_au_bon_format("C11") == False, "test est_au_bon_format"
    assert est_au_bon_format("AAA") == False, "test est_au_bon_format"
    assert est_au_bon_format("3333") == False, "test est_au_bon_format"
    assert est_au_bon_format("J8") == True, "test est_au_bon_format"
    assert est_au_bon_format("A0") == True, "test est_au_bon_format"
    assert est_au_bon_format("C3") == True, "test est_au_bon_format"
    assert est_au_bon_format("3C") == False, "test est_au_bon_format"


def test_est_grille_valide():

    # 8 lignes et 8 colonnes donc format valide
    grille1 = [["", "O", "", "O", "", "O", "", "O"],
             ["O", "", "O", "", "O", "", "O", ""],
             ["", "O", "", "O", "", "O", "", "O"],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["X", "", "X", "", "X", "", "X", ""],
             ["", "X", "", "X", "", "X", "", "X"],
             ["X", "", "X", "", "X", "", "X", ""]]
    
    # il y a 7 colonnes donc format invalide
    grille2 = [["", "O", "", "O", "", "O", ""],
             ["O", "", "O", "", "O", "", "O"],
             ["", "O", "", "O", "", "O", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["X", "", "X", "", "X", "", "X"],
             ["", "X", "", "X", "", "X", ""],
             ["X", "", "X", "", "X", "", "X"]]
    
    # il y a 7 lignes donc format invalide
    grille3 = [["", "O", "", "O", "", "O", ""],
             ["O", "", "O", "", "O", "", "O"],
             ["", "O", "", "O", "", "O", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["X", "", "X", "", "X", "", "X"],
             ["", "X", "", "X", "", "X", ""]]
    
    # grille vide donc invalide
    grille4 = []

    # grille vide donc invalide
    grille5 = [[]]
    
    assert est_grille_valide(grille1) == True, "test est_grille_valide"
    assert est_grille_valide(grille2) == False, "test est_grille_valide"
    assert est_grille_valide(grille3) == False, "test est_grille_valide"
    assert est_grille_valide(grille4) == False, "test est_grille_valide"
    assert est_grille_valide(grille5) == False, "test est_grille_valide"


def test_est_deplacement():
    grille = [["", "O", "", "O", "", "O", "", "O"],
             ["O", "", "O", "", "O", "", "O", ""],
             ["", "O", "", "O", "", "O", "", "O"],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["X", "", "X", "", "X", "", "X", ""],
             ["", "X", "", "X", "", "X", "", "X"],
             ["X", "", "X", "", "X", "", "X", ""]]
    
    
    # deplacements valides
    assert est_deplacement(grille, "F1", "E2", "X"), "test est_deplacement"
    assert est_deplacement(grille, "F3", "E2", "X"), "test est_deplacement"
    assert est_deplacement(grille, "F3", "E4", "X"), "test est_deplacement "

    assert est_deplacement(grille, "C2", "D1", "O"), "test est_deplacement"
    assert est_deplacement(grille, "C2", "D3", "O"), "test est_deplacement"
    assert est_deplacement(grille, "C4", "D5", "O"), "test est_deplacement"

    # deplacements invalides
    assert est_deplacement(grille, "F2", "E3", "X") == False, "test est_deplacement"
    assert est_deplacement(grille, "G2", "F1", "X") == False, "test est_deplacement"
    assert est_deplacement(grille, "F3", "E3", "X") == False, "test est_deplacement "
    assert est_deplacement(grille, "D2", "A3", "X") == False, "test est_deplacement "

    assert est_deplacement(grille, "B1", "C2", "O") == False, "test est_deplacement"
    assert est_deplacement(grille, "A2", "B1", "O") == False, "test est_deplacement"
    assert est_deplacement(grille, "B7", "C8", "O") == False, "test est_deplacement"
    assert est_deplacement(grille, "D2", "E3", "O") == False, "test est_deplacement"


def test_est_capture():
    grille =    [["", "", "", "O", "", "O", "", "O"],
                ["", "", "O", "", "O", "", "", ""],
                ["", "O", "", "X", "", "", "", "O"],
                ["", "", "", "", "", "", "X", ""],
                ["", "O", "", "", "", "O", "", ""],
                ["X", "", "X", "", "", "", "X", ""],
                ["", "", "", "X", "", "X", "", ""],
                ["X", "", "X", "", "X", "", "", ""]]

    # captures valides
    assert est_capture(grille, "F1", "D3", "X"), "test est_capture"
    assert est_capture(grille, "F3", "D1", "X"), "test est_capture"
    assert est_capture(grille, "F7", "D5", "X"), "test est_capture"


    assert est_capture(grille, "B5", "D3", "O"), "test est_capture"
    assert est_capture(grille, "E6", "G8", "O"), "test est_capture"
    assert est_capture(grille, "B3", "D5", "O"), "test est_capture"



    # capture invalides
    assert est_capture(grille, "C4", "A6", "X") == False, "test est_capture"
    assert est_capture(grille, "F3", "D5", "X") == False, "test est_capture"


    assert est_capture(grille, "E2", "F5", "O") == False, "test est_capture"
    assert est_capture(grille, "C2", "E4", "O") == False, "test est_capture"

    
def test_deplacement():
    grille =    [["", "", "", "O", "", "O", "", "O"],
                ["", "", "O", "", "O", "", "", ""],
                ["", "O", "", "X", "", "", "", "O"],
                ["", "", "", "", "", "", "X", ""],
                ["", "O", "", "", "", "O", "", ""],
                ["X", "", "X", "", "", "", "X", ""],
                ["", "", "", "X", "", "X", "", ""],
                ["X", "", "X", "", "X", "", "", ""]]
    
    assert deplacement(grille, "F3", "E4", "X") == "deplacement", "test deplacement"
    assert grille ==    [["", "", "", "O", "", "O", "", "O"],
                        ["", "", "O", "", "O", "", "", ""],
                        ["", "O", "", "X", "", "", "", "O"],
                        ["", "", "", "", "", "", "X", ""],
                        ["", "O", "", "X", "", "O", "", ""],
                        ["X", "", "", "", "", "", "X", ""],
                        ["", "", "", "X", "", "X", "", ""],
                        ["X", "", "X", "", "X", "", "", ""]], "test deplacement"
    
    assert deplacement(grille, "E4", "D3", "X") == "deplacement", "test deplacement"
    assert grille ==    [["", "", "", "O", "", "O", "", "O"],
                        ["", "", "O", "", "O", "", "", ""],
                        ["", "O", "", "X", "", "", "", "O"],
                        ["", "", "X", "", "", "", "X", ""],
                        ["", "O", "", "", "", "O", "", ""],
                        ["X", "", "", "", "", "", "X", ""],
                        ["", "", "", "X", "", "X", "", ""],
                        ["X", "", "X", "", "X", "", "", ""]], "test deplacement"
    
    assert deplacement(grille, "F1", "E3", "X") == "", "test deplacement"
    assert grille ==    [["", "", "", "O", "", "O", "", "O"],
                        ["", "", "O", "", "O", "", "", ""],
                        ["", "O", "", "X", "", "", "", "O"],
                        ["", "", "X", "", "", "", "X", ""],
                        ["", "O", "", "", "", "O", "", ""],
                        ["X", "", "", "", "", "", "X", ""],
                        ["", "", "", "X", "", "X", "", ""],
                        ["X", "", "X", "", "X", "", "", ""]], "test deplacement"
    
    assert deplacement(grille, "F7", "D5", "X") == "capture"
    assert grille ==    [["", "", "", "O", "", "O", "", "O"],
                        ["", "", "O", "", "O", "", "", ""],
                        ["", "O", "", "X", "", "", "", "O"],
                        ["", "", "X", "", "X", "", "X", ""],
                        ["", "O", "", "", "", "", "", ""],
                        ["X", "", "", "", "", "", "", ""],
                        ["", "", "", "X", "", "X", "", ""],
                        ["X", "", "X", "", "X", "", "", ""]], "test deplacement"
    

    assert deplacement(grille, "C2", "E4", "O") == "capture", "test deplacement"
    assert grille ==    [["", "", "", "O", "", "O", "", "O"],
                        ["", "", "O", "", "O", "", "", ""],
                        ["", "", "", "X", "", "", "", "O"],
                        ["", "", "", "", "X", "", "X", ""],
                        ["", "O", "", "O", "", "", "", ""],
                        ["X", "", "", "", "", "", "", ""],
                        ["", "", "", "X", "", "X", "", ""],
                        ["X", "", "X", "", "X", "", "", ""]], "test deplacement"
    
    assert deplacement(grille, "B5", "C6", "O") == "deplacement", "test deplacement"
    assert grille ==    [["", "", "", "O", "", "O", "", "O"],
                        ["", "", "O", "", "", "", "", ""],
                        ["", "", "", "X", "", "O", "", "O"],
                        ["", "", "", "", "X", "", "X", ""],
                        ["", "O", "", "O", "", "", "", ""],
                        ["X", "", "", "", "", "", "", ""],
                        ["", "", "", "X", "", "X", "", ""],
                        ["X", "", "X", "", "X", "", "", ""]], "test deplacement"
    
    assert deplacement(grille, "C6", "D5", "O") == "", "test deplacement"
    assert grille ==    [["", "", "", "O", "", "O", "", "O"],
                        ["", "", "O", "", "", "", "", ""],
                        ["", "", "", "X", "", "O", "", "O"],
                        ["", "", "", "", "X", "", "X", ""],
                        ["", "O", "", "O", "", "", "", ""],
                        ["X", "", "", "", "", "", "", ""],
                        ["", "", "", "X", "", "X", "", ""],
                        ["X", "", "X", "", "X", "", "", ""]], "test deplacement"
    

def test_est_capture_depart_possible():
    grille = [["O", "", "", "", "", "", "", "O"],
             ["", "", "", "O", "", "O", "O", ""],
             ["", "", "X", "", "O", "", "", ""],
             ["", "", "", "X", "", "", "", ""],
             ["O", "", "X", "", "", "", "", "O"],
             ["", "X", "", "", "", "", "X", ""],
             ["X", "", "", "", "", "", "", "X"],
             ["", "", "", "", "", "", "", ""]]
    

    # capture possible
    assert est_capture_possible_depart(grille, "C3", "X"), "test est_capture_possible"
    assert est_capture_possible_depart(grille, "B4", "O"), "test est_capture_possible"
    assert est_capture_possible_depart(grille, "E8", "O"), "test est_capture_possible"

    # capture impossible
    assert est_capture_possible_depart(grille, "A1", "O") == False, "test est_capture_possible"
    assert est_capture_possible_depart(grille, "A8", "O") == False, "test est_capture_possible"
    assert est_capture_possible_depart(grille, "G1", "X") == False, "test est_capture_possible"
    assert est_capture_possible_depart(grille, "G8", "X") == False, "test est_capture_possible"
    assert est_capture_possible_depart(grille, "C5", "O") == False, "test est_capture_possible"
    assert est_capture_possible_depart(grille, "D4", "X") == False, "test est_capture_possible"


def test_est_capture_possible():
    grille1 = [["", "O", "", "", "", "", "", ""],
             ["", "", "", "O", "", "", "", ""],
             ["", "O", "", "", "", "O", "", ""],
             ["", "", "X", "", "", "", "", ""],
             ["", "", "", "", "", "X", "", ""],
             ["O", "", "", "", "", "", "X", ""],
             ["", "", "", "X", "", "", "", ""],
             ["", "", "X", "", "", "", "", ""]]
    
    grille2 = [["", "O", "", "", "", "", "", ""],
             ["", "", "", "O", "", "", "", ""],
             ["", "O", "", "", "", "O", "", ""],
             ["", "", "X", "", "", "", "", ""],
             ["", "", "", "X", "", "X", "", ""],
             ["O", "", "", "", "", "", "X", ""],
             ["", "", "", "X", "", "", "", ""],
             ["", "", "X", "", "", "", "", ""]]
    
    grille3 = [["", "O", "", "", "", "", "", ""],
             ["", "", "", "O", "", "", "", ""],
             ["", "", "", "", "", "O", "", ""],
             ["", "", "X", "", "", "", "", ""],
             ["", "", "", "", "", "X", "", ""],
             ["O", "", "", "", "", "", "X", ""],
             ["", "", "", "X", "", "", "", ""],
             ["", "", "X", "", "", "", "", ""]]
    

    assert est_capture_possible(grille1, "X"), "test est_capture"
    assert est_capture_possible(grille1, "O"), "test est_capture"

    assert est_capture_possible(grille2, "X"), "test est_capture"
    assert est_capture_possible(grille2, "O") == False, "test est_capture"

    assert est_capture_possible(grille3, "X") == False, "test est_capture"
    assert est_capture_possible(grille3, "O") == False, "test est_capture"

    



def tests():
    """effectue tous les tests des fonctions unitaires"""
    print("Debuts des tests ...")
    test_sont_coordonnees_correctes()
    test_est_au_bon_format()
    test_est_dans_grille()
    test_est_grille_valide()
    test_lettre_vers_nombre()
    test_est_deplacement()
    test_est_capture()
    test_deplacement()
    test_est_capture_depart_possible()
    test_est_capture_possible()
    print("Tests effectues")




# fonction pour effectuer des verification d affichage et d entree utilisateur
def debug_verifications(grille_debut, grille_milieu, grille_fin):
    """Cette fonction ne sert que pour l evaluation par les pairs et effectuer des tests plus facilement"""
    assert est_grille_valide(grille_debut), "grille_debut doit etre une matrice carre de taille 8"
    assert est_grille_valide(grille_milieu), "grille_milieu doit etre une matrice carre de taille 8"
    assert est_grille_valide(grille_fin), "grille_fin doit etre une matrice carre de taille 8"

    fin = False
    while not fin:
        print("-"*50)
        print("Que souhaitez vous faire ?\n")
        print("1 > jouer un tour dans la configuration de debut")
        print("2 > jouer un tour dans la configuration de milieu")
        print("3 > jouer un tour dans la configuration de fin")
        print("4 > appeler les fonctions de saisie de coordonnees")
        print("5 > appeler la fonction principale de tests")
        print("6 > fermer le programme\n")

        entree_utilisateur = input("En attente de votre reponse... > ")
        print()

        # suivant le choix de l utilisateur on appelle les fonctions correspondantes
        if entree_utilisateur == "1":
            afficher_grille(grille_debut, 0, 0)
            effectuer_tour(grille_debut, "X", 0, 0)
        elif entree_utilisateur == "2":
            afficher_grille(grille_milieu, 3, 3)
            effectuer_tour(grille_milieu, "X", 3, 3)
        elif entree_utilisateur == "3":
            afficher_grille(grille_fin, 10, 9)
            effectuer_tour(grille_fin, "X", 10, 9)

        elif entree_utilisateur == "4":
            coordonnes_piece_a_deplacer = demander_coordonnees_piece_a_deplacer(grille_debut)
            coordonnes_case_arrivee = demander_coordonnees_case_arrivee(grille_debut)
            
            print("\nCase de la piece a deplacer :", coordonnes_piece_a_deplacer)
            print("Case d'arrivee :", coordonnes_case_arrivee)
        
        elif entree_utilisateur == "5":
            tests()
        elif entree_utilisateur == "6":
            fin = True
        else:
            # si l'utilisateur entre quelque chose d autres, on redemande lors du prochain passage en boucle
            pass




debug_verifications(GRILLE_DEBUT, GRILLE_MILIEU, GRILLE_FIN)
