import random
import fltk

#Variables de la fenetre graphique
LONGUEUR, LARGEUR = 800, 800
TAILLE_CASE_X = 500 / 8
TAILLE_CASE_Y = 500 / 8
couleurs = {"R":"red","J":'yellow',"V":"green","B":"blue"}

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

def compte_couleur(t: list,bonus: list) -> dict:
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

def case_jouable(t: list, x: int, y: int, ia: bool, graphique: bool = False):
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

def obtenir_coordonnees(t: list, alea: bool, graphique: bool = False):
    """Demande les coordonnés de la case joué a l'utilisateur

    Args:
        t (list): tableau a double entrée
        alea (bool): True si ia False sinon

    Returns:
        tuple: coordonnées x, y
    """
    if not graphique:
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
    else:
        if alea:
            x, y = random.randint(0, 7), random.randint(0, 7)
            x, y = random.randint(0, 7), random.randint(0, 7)
            while not(case_jouable(t,x,y,True, True)):
                x, y = random.randint(0, 7), random.randint(0, 7)
                x, y = random.randint(0, 7), random.randint(0, 7)
            return x, y
        else:
            while True:
                ev = fltk.donne_ev()
                tev = fltk.type_ev(ev)
                if tev == 'Quitte':
                    break
                elif tev == 'ClicGauche':
                    xs, ys = fltk.abscisse(ev), fltk.ordonnee(ev)
                    if xs <= 150 or xs >= 650 or ys <= 150 or ys >= 650:
                        print("non")
                    else:
                        numero_ligne = (ys - 150)// TAILLE_CASE_Y
                        numero_colonne = (xs - 150) // TAILLE_CASE_X
                        if case_jouable(t, int(numero_colonne), int(numero_ligne),False):
                            return int(numero_colonne), int(numero_ligne)
                fltk.mise_a_jour()

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

def capture_ia(t: list, ia: str,bonus: list, graphique: bool = False):
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
                if graphique:
                    capture_fenetre(tclone, True, ia)
                if not graphique:
                    capture(tclone,i,j)
                if compte_couleur(tclone,bonus)[ia] > point:
                    point = compte_couleur(tclone,bonus)[ia]
                    list_alea = []
                    list_alea.append((i,j))
                elif compte_couleur(tclone,bonus)[ia] == point:
                    list_alea.append((i,j))
    indice = random.randint(0,len(list_alea) - 1)
    t[list_alea[indice][0]][list_alea[indice][1]] = ia
    capture(t,list_alea[indice][0],list_alea[indice][1]) # manque peut etre la capture_fenetre

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

def jouer_manche(t: list, c_j: dict, alea: bool,contre_ia: bool,bonus: list, graphique: bool = False):
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
        score = compte_couleur(t, bonus)
        if not graphique:
            affichage_tableau(t) 
            print("Tour de ", c_j[c],"qui est ",c,".")
        if graphique:
            #grille()
            pion(t)
            fltk.efface("text_tour")
            fltk.efface("text_score")
            fltk.texte(LARGEUR//2, 45, "Tour de "+c_j[c]+" qui est "+c+".", ancrage="center", taille=20, tag="text_tour")
            couleur = []
            for cle, val in score.items():
                couleur.append(cle)
            for i in range(len(score)):
                fltk.texte(LARGEUR*3//4 + 25, 30 + i*10, couleur[i]+" : "+str(score[couleur[i]]), taille=10, police="Consolas", tag="text_score")
        if contre_ia and not alea:
            if joueur == t_c[0]:
                x, y = obtenir_coordonnees(t, False, graphique)
                t[x][y] = c
                capture(t,x,y)
            else:
                capture_ia(t, t_c[0], bonus, graphique)
        else:
            x, y = obtenir_coordonnees(t, alea_temp, graphique)
            t[x][y] = c
            capture(t,x,y)
            #si alea_temp retarder le jeu
        t_c = t_c[1:] + [t_c[0]]
        if alea and contre_ia:
            if joueur == t_c[0]:
                alea_temp = False
            else:
                alea_temp = True

def afficher_resultat_manche(score: dict, manches_gagnees: dict, c_j: dict, graphique: bool = False):
    """affiche le gagnant de la manche et augmente le nombre de manche gagnée

    Args:
        score (dict): nombre de point de chaque couleur
        manches_gagnees (dict): nombre de manche gagnée par chaque couleur
        c_j (dict): couleur -> pseudo
    """
    g = valeur_dict_plus_grande(score) #gagnant de la manche
    manches_gagnees[g[0]] += 1
    if not graphique:
        print(c_j[g[0]],"a gagné la manche avec un score de", score[g[0]]) 
    else:
        #fltk.efface("text_gagnant_manche")
        #fltk.texte(LARGEUR*3//4 + 20, 25, g[0]+" a gagné la manche \nprécédente avec un score de "+str(score[g[0]]), taille=10, tag="text_gagnant_manche")   
        pass
        
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

#graphique
def grille():
    """
    Créer une grille de jeu
    """
    for i in range(9):
        y = i * TAILLE_CASE_Y
        fltk.ligne(150,150 + y,LONGUEUR-150,150 + y)
    for i in range(9):
        x = i * TAILLE_CASE_X
        fltk.ligne(x + 150, 150, x + 150,LARGEUR - 150)
    
def pion(t: list):
    """
    Met les couleurs de la liste t dans la grille de jeu
    """
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j]:
                fltk.cercle(150 + (TAILLE_CASE_X / 2) + i * TAILLE_CASE_X, 150 + (TAILLE_CASE_Y / 2) + j * TAILLE_CASE_Y , 25, couleur = couleurs[t[i][j]] ,remplissage = couleurs[t[i][j]], tag="pion")

def capture_fenetre(t: list, alea: bool, couleur: str):
    x,y = obtenir_coordonnees(t, alea, True)
    t[x][y] = couleur
    capture(t,x,y)
   
def fenetre_jeu() -> None:
    fltk.cree_fenetre(LONGUEUR,LARGEUR)
    fltk.image(LONGUEUR//2, LARGEUR//2, "image_retro_2.webp", LONGUEUR, LARGEUR)
    fltk.rectangle(150,150,LARGEUR-150,LARGEUR-150,remplissage="white")
    
    fltk.rectangle(LARGEUR//4,20,LARGEUR*3//4,20 + 50,remplissage="white")#rectangle pour le joueur qui joue
    fltk.rectangle(LARGEUR*3//4 + 20, 20, LARGEUR - 20, 150 - 20, remplissage="white")#rectangle du score
    
#main 
def main(d: dict, graphique: bool):
    """fonction principale de jeu"""
    if not graphique:
        nb_j, nb_m, alea, c_j, manches_gagnees, contre_ia, avec_b = init_partie()
        for k in range(nb_m):
            if avec_b:
                b = bonus(nb_j)
                print("Les bonus sont :", b)#case a mettre en couleur pour les bonus
            else:
                b = []
            t = tableau_depart()
            print("Manche numéro", k+1, "sur", nb_m)
            jouer_manche(t, c_j, alea,contre_ia,b, False)
            affichage_tableau(t)
            score_m = compte_couleur(t,b)
            afficher_resultat_manche(score_m, manches_gagnees, c_j, graphique=False)
            score_p = score_m if k == 0 else additionne_dict(score_p,score_m)
        afficher_resultat_partie(score_p, manches_gagnees, c_j)
    else:
        fenetre_jeu()
        manches_gagnees, c_j = {c: 0 for c in list(couleur_joueur(d["champ_pseudo"]).keys())}, couleur_joueur(d["champ_pseudo"])
        for k in range(int(d["champ_manches"])):
            t = tableau_depart()
            if d["bonus"]:
                b = bonus(int(d["nb_joueurs"]))
                for e in b:
                    fltk.rectangle(150 + e[0]*TAILLE_CASE_X, 150 + e[1]*TAILLE_CASE_Y, 150 + e[0]*TAILLE_CASE_X + TAILLE_CASE_X, 150 + e[1]*TAILLE_CASE_Y + TAILLE_CASE_Y, remplissage="purple", tag="bonus")
            else:
                b = []
            grille()
            jouer_manche(t, c_j, d["ia_alea"],d["ia_contre"],b, graphique=True)
            score_m = compte_couleur(t,b)
            afficher_resultat_manche(score_m, manches_gagnees, c_j, graphique=True)
            score_p = score_m if k == 0 else additionne_dict(score_p,score_m)
            fltk.efface("pion")
            fltk.efface("bonus")
        fltk.ferme_fenetre()
        
if __name__ == '__main__':
    main({"champ_manches": 2, "champ_pseudo": [],"nb_joueurs": 4, "ia_alea": False, "ia_contre": False, "bonus": False}, graphique=True)