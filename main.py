import random
#code
def tableau_depart():
    """tableau de départ

    Returns:
        t (list): tableau a double entrée
    """
    t = [[None for i in range(8)] for i in range(8)]
    t[3][3],t[3][4],t[4][3],t[4][4] = "R","J","B","V"
    return t

def nb_joueur():
    """Demande le nombre de joueur

    Returns:
        int: nombre de joueur
    """
    nb_joueur = int(input("Quel est le nombre de joueur? - "))
    while nb_joueur not in (2, 3, 4):
        nb_joueur = int(input("Choisisez un nombre de joueur entre 2, 3 et 4 - "))
    return nb_joueur

def pseudo(nb: int) :
    """Demande le pseudo de chaque joueur

    Args:
        nb (int): nombre de joueur

    Returns:
        list: tableau des pseudo
    """
    joueur = []
    for i in range (nb):
        joueur.append(input("Quel est le pseudo du joueur numero "+ str(i+1) +" - "))
    return joueur

def nb_manche():
    """Demande le nombre de manche

    Returns:
        int: nombre de manche
    """
    nb_manche = int(input("Quel est le nombre de manche? - "))
    while nb_manche < 1 :
        nb_manche = int(input("Choisisez un nombre de manche positif - "))
    return nb_manche

def couleur_joueur(joueur: list) -> dict:
    """Attribue à chaque couleur le pseudo d'un joueur

    Args:
        joueur (list): liste des pseudo des joueurs

    Returns:
        dict: dictionnaire avec comme cle une couleur et comme valeur le pseudo d'un joueur
    """
    couleurs, d = ["R", "J", "V", "B"], {}
    if len(joueur) == 2:
        d = {"R": joueur[0], "V": joueur[1]}
        return d
    for i in range(len(joueur)):
        d[couleurs[i]] = joueur[i]
    return d

def capture(t: list, x: int, y: int) -> None:
    """Capture les billes adjacentes de couleurs différentes et les change en couleur de la bille jouée

    Args:
        t (list): tableau a double entree
        x (int): coordonnée vertical de la couleur
        y (int): coordonnée horizontal de la couleur
    """
    couleur = t[x][y]
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    captures = []
    for dx, dy in directions:
        xs, ys, temp = x, y, []
        while 0 <= xs + dx <= 7 and 0 <= ys + dy <= 7 and t[xs + dx][ys + dy] != couleur and t[xs + dx][ys + dy] is not None:
            xs += dx
            ys += dy
            temp.append((xs, ys))
        if 0 <= xs + dx <= 7 and 0 <= ys + dy <= 7 and t[xs + dx][ys + dy] == couleur:
            captures.extend(temp)
    for cx, cy in captures:
        t[cx][cy] = couleur
    if len(captures) == 0:
        return False
    return True

def compte_couleur(t: list,bonus: list):
    """Compte le nombre de pion de chaque couleur actuellement en jeu.

    Args:
        t (list): tableau a double entrée
        bonus (list): liste des couleurs bonus
    Returns:
        compteur (dict): nombre de fois que chaque couleur apparait dans t
    """
    compteur  = {'R': 0, 'J': 0, 'V': 0,'B': 0}
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j] in compteur:
                if (i,j) in bonus:
                    compteur[t[i][j]] += 5
                else:
                    compteur[t[i][j]] += 1
    return compteur

def clone(t: list):
    """
    Créer un clone du plateau.

    Args:
        t (list): tableau a double entrée
    Returns:
        tclone (list): tableau a double entée
    """
    tclone = tableau_depart()
    for i in range(len(t)):
        for j in range(len(t)):
            tclone[i][j] = t[i][j]
    return tclone

def couleur_affichage(t: list, x: int, y: int):
    """Retourne la couleur de t[x][y]

    Args:
        t (list): tableau a double entrée
        x (int): coordonnee vertical de la couleur
        y (int): coordonnee horizontal de la couleur

    Returns:
        str: couleur de t[x][y]
    """
    c = t[x][y]
    if c == "R":
        return "\x1b[31m"
    elif c == "J":
        return "\x1b[33m"
    elif c == "V":
        return "\x1b[32m"
    elif c == "B":
        return "\x1b[34m"

def affichage_tableau(t: list):
    """affiche un tableau lisible

    Args:
        t (list): tableau a double entrée
    """
    for i in range(8):
        if i == 0:
            print("|       |    0  |    1  |    2  |    3  |    4  |    5  |    6  |    7  |")
        for j in range(9):
            if j == 0:
                print("|   ", i," | ", end="")
            elif t[i][j-1] is not None:
                print("  ", couleur_affichage(t,i,j-1) + t[i][j-1] + "\x1b[0m", " | ", end="")
            else:
                print(t[i][j-1], " | ", end="")
        print()

def valeur_dict_plus_grande(d: dict):
    """Détermine qu'elle cle du dictionnaire a la plus grande valeure

    Args:
        d (dict): dictionnaire

    Returns:
        list: tableau contenant les cle avec la plus grande valeur
    """
    max_valeur = max(d.values())
    c_max = []
    for cle, val in d.items():
        if val == max_valeur:
            c_max.append(cle)
    return c_max
 
def additionne_dict(d1: dict,d2: dict):
    """Additionne les valeures de 2 dictionnaires avec les mêmes clés, avec les clés correspondantent. 

    Args:
        d1 (dict)
        d2 (dict)

    Returns:
        r (dict): somme des valeurs des deux dictionnaires avec les clés correspondantent.
    """
    r = {}
    for cle in d1:
        r[cle] = d1[cle] + d2[cle]
    return r

def case_jouable(t: list, x: int, y: int, ia: bool):
    """Détermine si t[x][y] est jouable

    Args:
        t (list): tableau a double entree
        x (int): coordonnée vertical
        y (int): coordonnée horizontal

    Returns:
        bool: True si t[x][y] est jouable, False sinon
    """
    if (0 > x or 7 < x) or (0 > y or 7 < y):
        if ia is False:
            print("Case pas dans le tableau. Réessayez.")
        return False
    elif t[x][y] is not None:
        if ia is False:
            print("Case déjà occupée. Réessayez.")
        return False
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0: #case jouée
                continue 
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and t[nx][ny] is not None: #vérifie si t[nx][ny] est dans le tableau et est vide
                return True
    if ia is False:
        print("Case pas adjacente a une couleur. Réessayez.")
    return False

def obtenir_coordonnees(t: list, alea: bool):
    """Demande les coordonnés de la case joué a l'utilisateur

    Args:
        t (list): tableau a double entrée
        alea (bool): True si ia False sinon

    Returns:
        tuple: coordonnées x, y
    """
    if alea:
        x, y = random.randint(0, 7), random.randint(0, 7)
        x, y = random.randint(0, 7), random.randint(0, 7)
        while not(case_jouable(t,x,y,True)):
            x, y = random.randint(0, 7), random.randint(0, 7)
            x, y = random.randint(0, 7), random.randint(0, 7)
        return x, y
    else:
        x, y = int(input("Coordonnée verticale de la couleur jouée: ")), int(input("Coordonnée horizontale de la couleur jouée: "))
        while not(case_jouable(t,x,y,False)):
            x, y = int(input("Coordonnée verticale: ")), int(input("Coordonnée horizontale: "))
        return x, y

def ia_alea():
    """Demande si l'utilisateur veut une ia aléatoire ou non

    Returns:
        bool: True si ia False sinon
    """
    a = str(input("ia aléatoire ? oui ou non - ")).strip().lower()
    while a not in ("oui","non"):
        a = str(input("ia aléatoire ? oui ou non - ")).strip().lower()
    if a == "oui":
        return True
    return False

def demande_contre_ia():
    """Demande si l'utilisateur veut jouer contre une ia

    Returns:
        bool: True si ia False sinon
    """

    a = str(input("contre ia ? oui ou non - ")).strip().lower()
    while a not in ("oui","non"):
        a = str(input("contre ia ? oui ou non - ")).strip().lower()
    if a == "oui":
        return True
    return False

def capture_ia(t: list, ia: str,bonus: list):
    """Execute la fontction capture pour la couleur de l'ia en ayant le plus de couleur sur le plateau.

    Args:
        t (list): _description_
        ia (str): _description_
        bonus (list): liste des coordonnées des bonus
    """
    point = 0
    x,y = 0,0
    list_alea = []
    for i in range(len(t)):
        for j in range(len(t)):
            tclone = clone(t)
            if case_jouable(t, i, j, True):
                tclone[i][j] = ia
                capture(tclone,i,j)
                if compte_couleur(tclone,bonus)[ia] > point:
                    point = compte_couleur(tclone,bonus)[ia]
                    list_alea = []
                    list_alea.append((i,j))
                elif compte_couleur(tclone,bonus)[ia] == point:
                    list_alea.append((i,j))
    indice = random.randint(0,len(list_alea) - 1)
    t[list_alea[indice][0]][list_alea[indice][1]] = ia
    capture(t,list_alea[indice][0],list_alea[indice][1])

def gagant_partie(d1: dict, d2: dict):
    """_summary_

    Args:
        d1 (dict): _description_
        d2 (dict): _description_

    Returns:
        list:
    """
    g = valeur_dict_plus_grande(d1) #gagnant de la partie par manche
    if len(g) > 1:
        g = valeur_dict_plus_grande(d2) #gagnant de la partie par point
    return g

def avec_bonus():
    """Demande si l'utilisateur veut jouer avec des bonus

    Returns:
        bool: True si oui False sinon
    """
    a = str(input("avec bonus ? oui ou non - ")).strip().lower()
    while a not in ("oui","non"):
        a = str(input("avec bonus ? oui ou non - ")).strip().lower()
    if a == "oui":
        return True
    return False

def init_partie():
    """initialisation de la partie (demande le nombre de joueur, le nombre de manche, l'ia ou non, le pseudo des joueurs)

    Returns:
        tuple: nombre de joueur, ia ou non, couleur -> pseudo, nombre de manche gagnée, tableau de départ
    """
    nb_j, nb_m, alea, contre_ia, b = nb_joueur(),nb_manche(),ia_alea(),demande_contre_ia(),avec_bonus() #nombre de joueur, nombre de manche et ia alea ou non
    p = pseudo(nb_j) #pseudo joueur
    c_j = couleur_joueur(p) #dictionnaire couleur -> joueur
    manches_gagnees = {c: 0 for c in list(c_j.keys())} #dictionnaire nombre de manche gagnée
    return nb_j,nb_m, alea, c_j, manches_gagnees , contre_ia, b

def jouer_manche(t: list, c_j: dict, alea: bool,contre_ia: bool,bonus: list):
    """joue une manche

    Args:
        t (list): tableau de départ
        c_j (dict): couleur -> pseudo
        alea (bool): True si ia False sinon
    """
    t_c = list(c_j.keys()) #tableau de couleur
    random.shuffle(t_c)
    joueur = t_c[random.randint(0,len(t_c)-1)]
    if joueur == t_c[0] and contre_ia:
        alea_temp = not alea
    else:
        alea_temp = alea
    while not end(t):
        c = t_c[0] 
        affichage_tableau(t) 
        print("Tour de ", c_j[c],"qui est ",c,".")
        if contre_ia and not alea:
            if joueur == t_c[0]:
                x, y = obtenir_coordonnees(t,False)
                t[x][y] = c
                capture(t,x,y)
            else:
                capture_ia(t, t_c[0],bonus)
        else:
            x, y = obtenir_coordonnees(t,alea_temp)
            t[x][y] = c
            capture(t,x,y)
        t_c = t_c[1:] + [t_c[0]]
        if alea and contre_ia:
            if joueur == t_c[0]:
                alea_temp = False
            else:
                alea_temp = True

def afficher_resultat_manche(score: dict, manches_gagnees: dict, c_j: dict):
    """affiche le gagnant de la manche et augmente le nombre de manche gagnée

    Args:
        score (dict): nombre de point de chaque couleur
        manches_gagnees (dict): nombre de manche gagnée par chaque couleur
        c_j (dict): couleur -> pseudo
    """
    g = valeur_dict_plus_grande(score) #gagnant de la manche
    manches_gagnees[g[0]] += 1
    print(c_j[g[0]],"a gagné la manche avec un score de", score[g[0]])    

def afficher_resultat_partie(score: dict, manches_gagnees: dict, c_j: dict):
    """affiche le gagnant de la partie

    Args:
        score (dict): nombre de point de chaque couleur
        manches_gagnees (dict): nombre de manche gagnée par chaque couleur
        c_j (dict): couleur -> pseudo
    """
    g = gagant_partie(manches_gagnees, score) #gagnant de la partie

    print(c_j[g[0]],"a gagné la partie avec un score de", score[g[0]], "\n Voici le nombre de point :", score, "\n Voici le nombre de manche gagnée :", manches_gagnees)


def bonus(nbre_joueur):
    """ fonction qui donne un tableau de bonus

    Args:
        nbre_joueur (_type_): nombre de joueur
    Returns:
        list: list de coordonnées
    """
    l = []
    for i in range(nbre_joueur):
        (x,y) = random.randint(0,7),random.randint(0,7)
        while (x,y) in l:
            (x,y) = random.randint(0,7),random.randint(0,7)
        l.append((x,y))
    return l

def end(t):
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j] is None:
                return False
    return True

def main():
    """fonction principale de jeu"""
    nb_j, nb_m, alea, c_j, manches_gagnees, contre_ia, avec_b = init_partie()
    for k in range(nb_m):
        if avec_b:
            b = bonus(nb_j)
            print("Les bonus sont :", b)
        else:
            b = []
        t = tableau_depart()
        print("Manche numéro", k+1, "sur", nb_m)
        jouer_manche(t, c_j, alea,contre_ia,b)
        affichage_tableau(t)
        score_m = compte_couleur(t,b)
        afficher_resultat_manche(score_m, manches_gagnees, c_j)
        score_p = score_m if k == 0 else additionne_dict(score_p,score_m)
    afficher_resultat_partie(score_p, manches_gagnees, c_j)
    
if __name__ == '__main__':
    main()
