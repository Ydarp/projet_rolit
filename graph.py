import main,fltk

LONGUEUR, LARGEUR = 800, 800
TAILLE_CASE_X = 500 / 8
TAILLE_CASE_Y = 500 / 8
couleurs = {"R":"red","B":"blue","J":'yellow',"V":"green"}

def grille():
    for i in range(9):
        y = i * TAILLE_CASE_Y
        fltk.ligne(150,150 + y,LONGUEUR-150,150 + y)
    for i in range(9):
        x = i * TAILLE_CASE_X
        fltk.ligne(x + 150, 150, x + 150,LARGEUR - 150)
    
def pion(t):
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j]:
                fltk.cercle(150 + (TAILLE_CASE_X / 2) + i * TAILLE_CASE_X, 150 + (TAILLE_CASE_Y / 2) + j * TAILLE_CASE_Y , 25, couleur = couleurs[t[i][j]] ,remplissage = couleurs[t[i][j]])

def touche(t):
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'Quitte':
            break
        elif tev == 'ClicGauche':
            xs, ys = fltk.abscisse(ev), fltk.ordonnee(ev)
            print(xs,ys)
            if xs <= 150 or xs >= 650 or ys <= 150 or ys >= 650:
                print("non")
            else:
                numero_ligne = (ys - 150)// TAILLE_CASE_Y
                numero_colonne = (xs - 150) // TAILLE_CASE_X
                if main.case_jouable(t, int(numero_colonne), int(numero_ligne),False):
                    return int(numero_colonne), int(numero_ligne)
        fltk.mise_a_jour()

def capture_fenetre(t,couleur):
    x,y = touche(t)
    t[x][y] = couleur
    if main.capture(t,x,y):
        pion(t)



if __name__ == "__main__":
    fltk.cree_fenetre(LONGUEUR,LARGEUR)
    t = main.tableau_depart()
    joueur = ["R","J","B","V"]
    while not main.end(t):
        grille()
        pion(t)
        capture_fenetre(t,joueur[0])
        joueur = joueur[1:] + [joueur[0]]
    fltk.attend_ev()
    fltk.ferme_fenetre()