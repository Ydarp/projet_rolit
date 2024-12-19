from fltk import *

#-----------------------Variables-----------------------#

LONGUEUR = 560
LARGEUR = 560
TAILLE_CASE_X = LONGUEUR // 8
TAILLE_CASE_Y = LARGEUR // 8
DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

#-----------------------Fonctions-----------------------#

def grille():
    grille = []
    for i in range(8):
        ligne = []
        for j in range(8):
            ligne.append('white')
        grille.append(ligne)
    grille[3][3], grille[3][4] = 'red', 'yellow'
    grille[4][3], grille[4][4] = 'blue', 'green'
    return grille

def creation_fenetre():
    cree_fenetre(LONGUEUR, LARGEUR)
    for i in range(8):
        for j in range(8):
            x = i * TAILLE_CASE_X
            y = j * TAILLE_CASE_Y
            rectangle(x, y, x + TAILLE_CASE_X, y + TAILLE_CASE_Y, remplissage='white')

    centre_cases = [(3, 3), (4, 3), (3, 4), (4, 4)]
    couleurs = ['red', 'yellow', 'green', 'blue']
    for i in range(4):
        (case_x, case_y) = centre_cases[i]
        x = case_x * TAILLE_CASE_X
        y = case_y * TAILLE_CASE_Y
        rectangle(x, y, x + TAILLE_CASE_X, y + TAILLE_CASE_Y, remplissage=couleurs[i])
    mise_a_jour()
    
def appuyer_case(grille_jeu, liste_joueur):
    indice = 0
    joueur = liste_joueur[indice]
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == "ClicDroit" or tev == "ClicGauche":
            x = abscisse(ev)
            y = ordonnee(ev)
            indice_x = x // TAILLE_CASE_X
            indice_y = y // TAILLE_CASE_Y
            if coup_possible(indice_x, indice_y, grille_jeu) == True :
                changer_couleur(x, y, grille_jeu, joueur)
                capture(indice_x, indice_y, grille_jeu, joueur)
                indice = (indice + 1) % len(liste_joueur)
                joueur = liste_joueur[indice]
            elif coup_possible(indice_x, indice_y, grille_jeu) == False :
                print("Coup impossible")
        elif tev == 'Quitte':
            break
        mise_a_jour()

def capture(indice_x, indice_y, grille_jeu, joueur):
    for dx, dy in DIRECTION:
        nx, ny = indice_x + dx, indice_y + dy
        mem = []
        while 0 <= nx < 8 and 0 <= ny < 8 and grille_jeu[nx][ny] != joueur and grille_jeu[nx][ny] != 'white':
            mem.append((nx, ny))
            nx, ny = nx + dx, ny + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and grille_jeu[nx][ny] == joueur:
            for co in mem:
                grille_jeu[co[0]][co[1]] = joueur
                couleur_capture(co, joueur)

def couleur_capture(co, joueur):
        x = co[0] * TAILLE_CASE_X
        y = co[1] * TAILLE_CASE_Y
        rectangle(x, y, x + TAILLE_CASE_X, y + TAILLE_CASE_Y, remplissage=joueur)

def changer_couleur(x, y, grille_jeu, joueur):
    x_case = (x // TAILLE_CASE_X)
    y_case = (y // TAILLE_CASE_Y)
    grille_jeu[x_case][y_case] = joueur
    x = x_case * TAILLE_CASE_X
    y = y_case * TAILLE_CASE_Y
    rectangle(x, y, x + TAILLE_CASE_X, y + TAILLE_CASE_Y, remplissage=joueur)

def coup_possible(indice_x, indice_y, grille_jeu):
    if grille_jeu[indice_x][indice_y] == "white" :
        return True
    else : return False

def cree_liste_joueur(n = 2):
    if n == 2:
        tab_joueur = ['red', 'yellow']
    elif n == 3:
        tab_joueur = ['red', 'yellow', 'green']
    elif n == 4:
        tab_joueur = ['red', 'yellow', 'green', 'blue']
    else :
        print("Nombre de joueur entre 2 et 4")
        cree_liste_joueur()
    return tab_joueur

def jouer():
    grille_jeu = grille()
    liste_joueur = cree_liste_joueur()
    creation_fenetre()
    appuyer_case(grille_jeu, liste_joueur)
    ferme_fenetre()

#-----------------------Main-----------------------#

if __name__ == "__main__":
    jouer()