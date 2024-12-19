import main,fltk, random

LONGUEUR, LARGEUR = 800, 800
TAILLE_CASE_X = 500 / 8
TAILLE_CASE_Y = 500 / 8
couleurs = {"R":"red","J":'yellow',"V":"green","B":"blue"}

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
                fltk.cercle(150 + (TAILLE_CASE_X / 2) + i * TAILLE_CASE_X, 150 + (TAILLE_CASE_Y / 2) + j * TAILLE_CASE_Y , 25, couleur = couleurs[t[i][j]] ,remplissage = couleurs[t[i][j]])

def touche(t: list):
    """
    Permet de recupérer les coordonées de la touche pour pouvoir jouer dans une case

    return:
        numero_colonne: int, numero_ligne: int
    """
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

def capture_fenetre(t: list,couleur: str):
    x,y = touche(t)
    t[x][y] = couleur
    main.capture(t,x,y)


def jouer(d: dict): #{"champ_manches": nb_manches, "champ_pseudo": pseudo,"nb_joueurs": nb_joueurs, "ia_alea": ia_alea, "ia_contre": ia_contre, "bonus": bonus}
    fltk.cree_fenetre(LONGUEUR,LARGEUR)
    for i in range(int(d["champ_manches"])):
        t = main.tableau_depart()
        if d["bonus"]:
            b = main.bonus(int(d["nb_joueurs"]))
        else:
            b = []
        list_couleur = list(main.couleur_joueur(d["champ_pseudo"]).keys())
        random.shuffle(list_couleur)
        grille()
        pion(t)
        while not main.end(t):
            capture_fenetre(t,list_couleur[0])
            pion(t)
            list_couleur = list_couleur[1:] + [list_couleur[0]]
        fltk.efface_tout()
    fltk.ferme_fenetre()


if __name__ == "__main__":
    jouer({"champ_manches": 2, "champ_pseudo": [],"nb_joueurs": 4, "ia_alea": False, "ia_contre": False, "bonus": False})