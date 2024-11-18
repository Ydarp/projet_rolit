from random import randint

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

def compte_couleur(t):
    """Compte le nombre de pion de chaque couleur actuellement en jeu.

    Args:
        t (list): tableau a double entrée
    Returns:
        compteur (dict): nombre de fois que chaque couleur apparait dans t
    """
    compteur  = {'R': 0, 'J': 0, 'V': 0,'B': 0}
    for e in t:
        for c in e:
            if c in compteur:
                compteur[c] += 1
    return compteur

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

def open_game(d: dict, t: list):
    """tourne t un nombre de fois aléartoire

    Args:
        d (dict): dictionnaire qui attribut une couleur a chaque joueur
        t (list): tabeau de couleur

    Returns:
        list: tableau de couleur
    """
    dc = randint(1,4)
    for i in range(dc):
        t = t[1:] + [t[0]]
    return t

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
        x, y = randint(0, 7), randint(0, 7)
        while not(case_jouable(t,x,y,True)):
            x, y = randint(0, 7), randint(0, 7)
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

def tableau_depart():
    """tableau de départ

    Returns:
        t (list): tableau a double entrée
    """
    t = [[None for i in range(8)] for i in range(8)]
    t[3][3],t[3][4],t[4][3],t[4][4] = "R","J","B","V"
    return t

def init_partie():
    """initialisation de la partie (demande le nombre de joueur, le nombre de manche, l'ia ou non, le pseudo des joueurs)

    Returns:
        tuple: nombre de joueur, ia ou non, couleur -> pseudo, nombre de point, nombre de manche gagnée
    """
    nb_j, nb_m, alea = nb_joueur(),nb_manche(),ia_alea() #nombre de joueur, nombre de manche et ia alea ou non
    p = pseudo(nb_j) #pseudo joueur
    c_j = couleur_joueur(p) #dictionnaire couleur -> joueur
    points_gagnes = {c: 0 for c in list(c_j.keys())}
    manches_gagnees = {c: 0 for c in list(c_j.keys())} #dictionnaire nombre de manche gagnée
    return nb_m, alea, c_j, points_gagnes, manches_gagnees

def jouer_manche(t: list, c_j: dict, alea: bool):
    """joue une manche

    Args:
        t (list): tableau de départ
        c_j (dict): couleur -> pseudo
        alea (bool): True si ia False sinon

    Returns:
        _type_: _description_
    """
    t_c = open_game(c_j,list(c_j.keys())) #tableau de couleur
    while sum(compte_couleur(t).values()) != 64:
        c = t_c[0] 
        affichage_tableau(t) 
        print("Tour de ", c_j[c],"qui est ",c,".")
        x, y = obtenir_coordonnees(t,alea)
        t[x][y] = c
        capture(t,x,y)
        t_c = t_c[1:] + [t_c[0]]
    return t

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
    g = gagant_partie(score, manches_gagnees) #gagnant de la partie
    print(c_j[g[0]],"a gagné la partie avec un score de", score[g[0]], "\n Voici le nombre de point :", score, "\n Voici le nombre de manche gagnée :", manches_gagnees)

def main():
    """fonction principale de jeu"""
    nb_m, alea, c_j, score, manches_gagnees = init_partie()
    for k in range(nb_m):
        print("Manche numéro", k+1, "sur", nb_m)
        t = jouer_manche(tableau_depart(), c_j, alea)
        affichage_tableau(t)
        afficher_resultat_manche(score, manches_gagnees, c_j)
    afficher_resultat_partie(score, manches_gagnees, c_j)
    
if __name__ == '__main__':
    main()