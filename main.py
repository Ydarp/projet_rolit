from random import randint

def nb_joueur():
    """
    Demande le nombre de joueur et le renvoie en entier entre 1 et 4
    """
    nb_joueur = int(input("Quel est le nombre de joueur? - "))
    assert nb_joueur == 2 or nb_joueur == 3 or nb_joueur == 4 , "Veuillez choisir un nombre de joueur entre 2 et 4"
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
    nb_manche = input("Quel est le nombre de manche? - ")
    return nb_manche

def couleur_joueur(joueur: list, nb: int) -> list:
    """
    Attribue à chaque joueur une couleur et les renvoie dans une liste
    """
    p, nb_j = joueur, nb
    if nb_j == 2:
        p[0],p[1] = "rouge","vert"
    elif nb_j == 3:
        p[0],p[1],p[2] = "rouge","jaune","vert"
    else:
        p[0],p[1],p[2],p[4] = "rouge","jaune","vert","bleu"
    return p

def capture(t: list,x: int, y: int) -> None:
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
        while 0 <= xs + d[0]  <= 7 and 0 <= ys + d[1] <= 7 and t[xs + d[0]][ys + d[1]]  != None and t[xs + d[0]][ys + d[1]] != couleur:
            xs += d[0]
            ys += d[1]
            couleur_temp.append((xs,ys))
        if t[xs][ys] == couleur:
            for c in couleur_temp:
                couleurs_capture.append(c)
    for c in couleurs_capture:
        t[c[0]][c[1]] = couleur
    return t 

def compte_couleur(t):
    """Compte le nombre de pion de chaque couleur actuellement en jeu.

    Args:
        t (list): tableau a double entrée
    Returns:
        int : le nombre de rouge, jaune, bleu, vert
    """
    for i in range(8):
        for j in range(8):
            if t[i][j] == 'r':
                r += 1
            elif t[i][j] == 'j':
                j += 1
            elif t[i][j] == 'b':
                b += 1
            elif t[i][j] == 'V':
                v += 1
    return r, j, b, v

def fin(t):
    """Détermine si la manche est fini ou non.

    Args:
        t (list): tableau a double entrée

    Returns:
        bouléen_: Vrai si la manche est fini, faux sinon
    """
    for i in range(8):
        for j in range(8):   
            if t[i][j] == None:
                return False  
    return True   

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
    t[y][x] = c
    return t

def affichage_tableau(t: list):
    for i in range(8):
        for j in range(8):
            if j == 0 and t[i][j] != None:
                print("|   ", t[i][j], " | ", end="")
            elif j == 0 and t[i][j] == None:
                print("| ", t[i][j], " | ", end="")
            elif j != 0 and t[i][j] != None:
                print("  ",t[i][j], " | ", end="")
            else:
                print(t[i][j], " | ", end="")
        print()
        
def tableau_depart():
    t = [[None for i in range(8)] for i in range(8)]
    t[3][3],t[3][4],t[4][3],t[4][4] = "r","j","b","v"
    return t
   
if __name__ == '__main__':
    nb_j = nb_joueur()
    p = pseudo(nb_j)
    nb_m = nb_manche()
    c_j = couleur_joueur(p, nb_j)
    t = tableau_depart()
    c = 'r'
    while fin(t) is False:
        affichage_tableau(t)
        x, y = int(input("Quel est la coordonnée horizontale de la couleur jouée - ")), int(input("Quel est la coordonnée verticale de la couleur jouée - "))
        t = capture(couleur_jouee(t, x, y, c),x ,y)
    print(pseudo[0]," a gagné !")