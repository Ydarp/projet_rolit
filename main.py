from random import randint

def tableau_depart():
    t = [[None for i in range(8)] for i in range(8)]
    t[3][3],t[3][4],t[4][3],t[4][4] = "r","j","b","v"
    return t

def nb_joueur():
    """Demande le nombre de joueur et le renvoie en entier entre 1 et 4"""
    nb_joueur = int(input("Quel est le nombre de joueur? - "))
    assert nb_joueur == 2 or nb_joueur == 3 or nb_joueur == 4 , "Veuillez choisir un nombre de joueur entre 2 et 4"
    return nb_joueur

def pseudo(nb):
    """Demande le pseudo de chaque joueur, les renvoies dans une liste et renvoie le nombre de joueur"""
    joueur = []
    for i in range (1,nb+1):
        joueur.append(input("Quel est le pseudo du joueur numero "+ str(i) +" - "))
    return nb,joueur

def nb_manche():
    """Demande le nombre de manche et le renvoie en entier"""
    nb_manche = input("Quel est le nombre de manche? - ")
    return nb_manche

def couleur_joueur(joueur):
    "Attribue à chaque joueur une couleur et les renvoies dans une liste"
    p, nb = joueur[1], joueur[0]
    if nb == 2:
        p[0],p[1] = "rouge","vert"
    elif nb == 3:
        p[0],p[1],p[2] = "rouge","jaune","vert"
    else:
        p[0],p[1],p[2],p[4] = "rouge","jaune","vert","bleu"
    return p

def capture(x: int, y: int) -> None:
    """
    Permet au joueur de la bille t[x][y] de changer la couleur des les autres billes honrizontalement, verticalement et diagonalent si possible.
    """
    couleur = t[x][y]
    couleurs_capture = []
    direction = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    for d in direction:
        xs = x
        ys = y 
        couleur_temp = []
        while 0 <= xs + d[0]  <= 7 and 0 <= ys + d[1] <= 7 and t[xs][ys] != "0" and t[xs][ys] != couleur:
            xs += d[0]
            ys += d[1]
            couleur_temp.append((xs,ys))
        if t[xs][ys] == couleur:
            for c in couleur_temp:
                couleurs_capture.append(c)
    for c in couleurs_capture:
        t[c[0]][c[1]] = couleur

def tableau_depart():
    t = [[None for i in range(8)] for i in range(8)]
    t[3][3],t[3][4],t[4][3],t[4][4] = "r","j","b","v"
    return t

def main():
    t = tableau_depart()
