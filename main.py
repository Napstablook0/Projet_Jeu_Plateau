
# -*- coding: utf-8 -*- 


"""Le plateau de jeu est en 8x8"""


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



GRILLE_FIN = [["", "", "O", "", "", "", "", ""],
             ["X", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "O", "", ""],
             ["", "O", "", "", "", "", "", ""],
             ["", "", "", "", "", "X", "", ""]]


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
            
    return True


def est_au_bon_format(message):
    """revoie True si coordonnees est au bon format, False sinon,
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
        print("| ", end="")
        if case == "":
            print("  ", end="")
        else:
            print(case + " ", end="")

    print("|")


def afficher_grille(grille, joueur, pieces_capturees_X, pieces_capturees_O):
    """affiche l etat actuel de la partie tel que le plateau, a qui c est le tour et les nombres de pieces capturees,
    joueur est un str, 'X' ou 'O' correspondant du joueur qui doit jouer ce tour ci
    pieces_capturees_X est un int correspondant au nombre de pieces (X) capturees par le joueur O
    pieces_capturees_O est un int correspondant au nombre de pieces (O) capturees par le joueur X"""
    assert est_grille_valide(grille), "grille doit etre une matrice de taille 8"
    assert joueur == "0" or joueur == "X", "parametre joueur invalide"

    

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

    print("C'est au tour du joueur : ", joueur)



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

    # indication pour les pairs : la fonction sont_coordonnees_correctes utilise la fonction est_dans_grille
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
    
    assert est_grille_valide(grille1) == True, "test est_grille_valide"
    assert est_grille_valide(grille2) == False, "test est_grille_valide"
    assert est_grille_valide(grille3) == False, "test est_grille_valide"


def tests():
    """effectue tous les tests des fonctions unitaires"""
    print("Debuts des tests ...")
    test_sont_coordonnees_correctes()
    test_est_au_bon_format()
    test_est_dans_grille()
    test_est_grille_valide()
    test_lettre_vers_nombre()
    print("Tests effectues")


# fonction pour effectuer des verification d affichage et d entree utilisateur
def atelier_2(grille_debut, grille_milieu, grille_fin):
    """Cette fonction ne sert que pour l evaluation par les pairs lors de l atelier 2 et effectuer des tests plus facilement"""
    assert est_grille_valide(grille_debut), "grille_debut doit etre une matrice carre de taille 8"
    assert est_grille_valide(grille_milieu), "grille_milieu doit etre une matrice carre de taille 8"
    assert est_grille_valide(grille_fin), "grille_fin doit etre une matrice carre de taille 8"

    fin = False
    while not fin:
        print("-"*50)
        print("Que souhaitez vous faire ?\n")
        print("1 > afficher la configuration de debut")
        print("2 > afficher la configuration de milieu")
        print("3 > afficher la configuration de fin")
        print("4 > appeler les fonctions de saisie de coordonnees")
        print("5 > appeler la fonction principale de tests")
        print("6 > fermer le programme\n")

        entree_utilisateur = input("En attente de votre reponse... > ")
        print()

        # suivant le choix de l utilisateur on appelle les fonctions correspondantes
        if entree_utilisateur == "1":
            afficher_grille(grille_debut, "X", 0, 0)
        elif entree_utilisateur == "2":
            afficher_grille(grille_milieu, "X", 3, 3)
        elif entree_utilisateur == "3":
            afficher_grille(grille_fin, "X", 10, 9)

        elif entree_utilisateur == "4":
            coordonnes_piece_a_deplacer = demander_coordonnees_piece_a_deplacer(grille_debut)
            coordonnes_case_arrivee = demander_coordonnees_case_arrivee(grille_debut)
            
            print("\nCase de la piece a deplacer : ", coordonnes_piece_a_deplacer)
            print("Case d'arrivee : ", coordonnes_case_arrivee)
        
        elif entree_utilisateur == "5":
            tests()
        elif entree_utilisateur == "6":
            fin = True
        else:
            # si l'utilisateur entre quelque chose d autres, on redemande lors du prochain passage en boucle
            pass




atelier_2(GRILLE_DEBUT, GRILLE_MILIEU, GRILLE_FIN)
