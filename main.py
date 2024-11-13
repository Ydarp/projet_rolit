from random import randint

def nb_joueur():
    """
    Demande le nombre de joueur et le renvoie en entier entre 1 et 4
    """
    nb_joueur = int(input("Quel est le nombre de joueur? - "))
    while nb_joueur not in (2, 3, 4):
        nb_joueur = int(input("Choisisez un nombre de joueur entre 2, 3 et 4 - "))
    return nb_joueur

def pseudo(nb: int) :
    """
    Demande le pseudo de chaque joueur et les renvoies dans une liste
    """
    joueur = []
    for i in range (nb):
        joueur.append(input("Quel est le pseudo du joueur numero "+ str(i+1) +" - "))
    return joueur

def nb_manche():
    """
    Demande le nombre de manche et le renvoie en entier
    """
    nb_manche = int(input("Quel est le nombre de manche? - "))
    while nb_manche < 1 :
        nb_manche = int(input("Choisisez un nombre de manche positif - "))
    return nb_manche

def couleur_joueur(joueur: list) -> dict:
    """
    Attribue à chaque couleur le pseudo d'un joueur et les renvoie dictionnaire
    """
    couleurs, d = ["R", "J", "V", "B"], {}
    for i in range(len(joueur)):
        d[couleurs[i]] = joueur[i]
    return d

def capture(t: list, x: int, y: int) -> None:
    """Capture les billes adjacentes de couleurs différentes et les change en couleur de la bille jouée"""
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

def couleur_jouee(t: list, x: int, y: int, c: str):
    """Remplace t[x][y] par c

    Args:
        t (list): tableau a double entrée
        x (int): coordonnée horizontale de la couleur
        y (int): coordonnée verticale de la couleur
        c (str): couleur 

    Returns:
        list: tableau avec la couleur jouée
    """
    t[x][y] = c
    return t

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
                print("  ", t[i][j-1], " | ", end="")
            else:
                print(t[i][j-1], " | ", end="")
        print()
        
def tourne_tableau(t: list):
    """met le premier indice du tableau a la fin

    Args:
        t (list): tableau a double entree

    Returns:
        t (list): tableau a double entree
    """
    t.append(t.pop(0))
    return t

def gagnant(d: dict):
    """Détermine qu'elle cle du dictionnaire a la plus grande valeure

    Args:
        d (dict): dictionnaire

    Returns:
        tuple: (c: str,v: int)
    """
    v, c = 0, ""
    for cle, val in d.items():
        if val > v:
            v, c = val, cle
    return c, v  
 
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

def obtenir_coordonnees(t: list, alea: bool):
    if alea:
        x, y = randint(0, 7), randint(0, 7)
        while t[x][y] is not None:
            x, y = randint(0, 7), randint(0, 7)
        return x, y
    else:
        x, y = int(input("Coordonnée verticale de la couleur jouée: ")), int(input("Coordonnée horizontale de la couleur jouée: "))
        while t[x][y] is not None:
            print("Case déjà occupée. Réessayez.")
            x, y = int(input("Coordonnée verticale: ")), int(input("Coordonnée horizontale: "))
        return x, y


def ia_alea():
    a = str(input("ia aléatoire ? oui ou non - ")).strip().lower()
    while a not in ("oui","non"):
        a = str(input("ia aléatoire ? oui ou non - ")).strip().lower()
    if a == "oui":
        return True
    return False

def tableau_depart():
    """tableau de départ

    Returns:
        t (list): tableau a double entrée
    """
    t = [[None for i in range(8)] for i in range(8)]
    t[3][3],t[3][4],t[4][3],t[4][4] = "R","J","B","V"
    return t

if __name__ == '__main__':
    k = 0 #compteur de manche
    d_g = {} #dictionnaire du score de la partie
    nb_j, nb_m, alea = nb_joueur(),nb_manche(),ia_alea()
    p = pseudo(nb_j)
    c_j = couleur_joueur(p)
    t_c = list(c_j.keys())
    while k < nb_m:
        t = tableau_depart()
        print("Manche numéro", k+1, "sur", nb_m)
        while sum(compte_couleur(t).values()) != 64:
            c = t_c[0]
            affichage_tableau(t)
            print("Tour de ", c_j[c],"qui est ",c,".")
            x, y = obtenir_coordonnees(t,alea)
            capture(couleur_jouee(t, x, y, c),x ,y)
            t_c = tourne_tableau(t_c)
        affichage_tableau(t)
        g = gagnant(compte_couleur(t))
        d_g = compte_couleur(t) if k == 0 else additionne_dict(d_g, compte_couleur(t))
        print(c_j[g[0]],"a gagné la manche avec un score de", g[1])
        k += 1
    g = gagnant(d_g)
    print(c_j[g[0]],"a gagné la partie avec un score de", g[1])
    