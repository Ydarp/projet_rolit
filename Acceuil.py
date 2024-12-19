import fltk

LARGEUR = 800
HAUTEUR = 800
ecart_2 = 120 #(800-H*4)/5
ecart = 10
H = 50
L = len("NOMBRES DE JOUEURS") * 12
xmin, ymin, xmax, ymax = L, H+ecart*3, L+H, H+ecart*3+H #valeur des coins du rectangle
carre_2, carre_3, carre_4 = (xmin, ymin, xmax, ymax), (LARGEUR//2 - 25, ymin, LARGEUR//2 + 25, ymax), (LARGEUR - L - H, ymin, LARGEUR - L, ymax)
case_oui_ia_alea, case_non_ia_alea = (LARGEUR//2 - H, H*2 + ecart*10 + 100, LARGEUR//2 + 20, H*4 + ecart*10 + H), (LARGEUR//2 + 70, H*2 + ecart*10 + 100, LARGEUR//2 + 140, H*4 + ecart*10 + H)
case_oui_ia_contre, case_non_ia_contre = (LARGEUR//2 - H, H*2 + ecart*11 + 100 + H, LARGEUR//2 + 20, H*4 + ecart*11 + H*2), (LARGEUR//2 + 70, H*2 + ecart*11 + 100 + H, LARGEUR//2 + 140, H*4 + ecart*11 + H*2)
case_oui_bonus, case_non_bonus = (LARGEUR//2 - H, H*2 + ecart*12 + 100 + H*2, LARGEUR//2 + 20, H*4 + ecart*12 + H*3), (LARGEUR//2 + 70, H*2 + ecart*12 + 100 + H*2, LARGEUR//2 + 140, H*4 + ecart*12 + H*3)
case_jouer = (ecart, H*7 + ecart*13, ecart + H*2, H*8 + ecart*13)

def fenetre_acceuil() -> None:
    """Cree la fenetre de départ et ajoute les cases d'options
    """
    fltk.cree_fenetre(LARGEUR, HAUTEUR)
    fltk.image(LARGEUR//2, HAUTEUR//2,"image_retro.jpg", LARGEUR, HAUTEUR, tag="image")
    txt = "NOMBRES DE JOUEURS"
    L   = len(txt) * 12
    #Nomre de joueurs
    fltk.rectangle(L, ecart, LARGEUR - L, ecart + H, remplissage="white", tag="case_nombre_joueurs")
    fltk.texte(LARGEUR // 2, 40, "NOMBRES DE JOUEURS", ancrage="center",taille=20, tag="text_nombre_joueurs") #police= pour modifié la police et améliorer la visibilité
    
    # carré 2, 3 et 4
    fltk.rectangle(carre_2[0], carre_2[1], carre_2[2], carre_2[3], remplissage="white", tag="case_2")
    fltk.texte(carre_2[0] + H//2, carre_2[1] + H//2,"2", ancrage="center",taille=20, tag="text_2")
    
    fltk.rectangle(carre_3[0], carre_3[1], carre_3[2], carre_3[3], remplissage="white", tag="case_3")
    fltk.texte(carre_3[0] + H//2, carre_3[1] + H//2,"3", ancrage="center",taille=20, tag="text_3")
    
    fltk.rectangle(carre_4[0], carre_4[1], carre_4[2], carre_4[3], remplissage="white", tag="case_4")
    fltk.texte(carre_4[0] + H//2, carre_4[1] + H//2,"4", ancrage="center",taille=20, tag="text_4")
    
    #Nombre de manches
    txt = "NOMBRES DE MANCHES : "
    L   = len(txt) * 18
    fltk.rectangle(ecart, H*2 + ecart*8, ecart + L, H*2 + ecart*8 + H, remplissage="white", tag="case_manches")
    fltk.texte(LARGEUR//4, H*2 + ecart*8 + H//2, txt, ancrage="center",taille=20, tag="text_manches")
    #Champ de saisie
    fltk.rectangle(LARGEUR//2 + 10, H*2 + ecart*8, LARGEUR - ecart, H*2 + ecart*8 + H, remplissage="white", tag="case_champ_manches")
    
    #Pseudo
    txt = "PSEUDO : "
    fltk.rectangle(ecart,H*2 + ecart*9 + H, LARGEUR//2 - ecart, H*4 + ecart*9, remplissage="white", tag="case_pseudo")
    fltk.texte(LARGEUR//4, H*3 + ecart*9 + H//2, txt, ancrage="center", taille=20, tag="text_pseudo")
    
    #ia aleatoire
    fltk.rectangle(ecart,H*2 + ecart*10 + 100, LARGEUR//2 - 100, H*4 + ecart*10 + H, remplissage="white", tag="case_ia_alea")
    fltk.texte(LARGEUR//4 -H, H*4 + ecart*10 + H//2, "IA ALÉATOIRE", ancrage="center", taille=20, tag="text_ia_alea")
    #yes/no
    fltk.rectangle( case_oui_ia_alea[0], case_oui_ia_alea[1], case_oui_ia_alea[2], case_oui_ia_alea[3], remplissage="white", tag="case_oui_ia_alea")
    fltk.texte(LARGEUR//2 - 15, H*4 + ecart*10 + H//2, "OUI", ancrage="center", taille=20, tag="text_oui_ia_alea")
    fltk.rectangle( case_non_ia_alea[0], case_non_ia_alea[1], case_non_ia_alea[2], case_non_ia_alea[3], remplissage="white", tag="case_non_ia_alea")
    fltk.texte(LARGEUR//2 + 105, H*4 + ecart*10 + H//2, "NON", ancrage="center", taille=20, tag="text_non_ia_alea")
    
    #ia contre
    fltk.rectangle(ecart,H*2 + ecart*11 + 150, LARGEUR//2 - 100, H*5 + ecart*11 + H, remplissage="white", tag="case_ia_contre")
    fltk.texte(LARGEUR//4 -H, H*5 + ecart*11 + H//2, "CONTRE IA", ancrage="center", taille=20, tag="text_ia_contre")
    #yes/no
    fltk.rectangle( case_oui_ia_contre[0], case_oui_ia_contre[1], case_oui_ia_contre[2], case_oui_ia_contre[3], remplissage="white", tag="case_oui_ia_contre")
    fltk.texte(LARGEUR//2 - 15, H*5 + ecart*11 + H//2, "OUI", ancrage="center", taille=20, tag="text_oui_ia_contre")
    fltk.rectangle( case_non_ia_contre[0], case_non_ia_contre[1], case_non_ia_contre[2], case_non_ia_contre[3], remplissage="white", tag="case_non_ia_contre")
    fltk.texte(LARGEUR//2 + 105, H*5 + ecart*11 + H//2, "NON", ancrage="center", taille=20, tag="text_non_ia_contre")
    
    #Bonus
    fltk.rectangle(ecart,H*2 + ecart*12 + 200, LARGEUR//2 - 100, H*6 + ecart*12 + H, remplissage="white", tag="case_bonus")
    fltk.texte(LARGEUR//4 -H, H*6 + ecart*12 + H//2, "BONUS", ancrage="center", taille=20, tag="text_bonus")
    #yes/no
    fltk.rectangle( case_oui_bonus[0], case_oui_bonus[1], case_oui_bonus[2], case_oui_bonus[3], remplissage="white", tag="case_oui_bonus")
    fltk.texte(LARGEUR//2 - 15, H*6 + ecart*12 + H//2, "OUI", ancrage="center", taille=20, tag="text_oui_bonus")
    fltk.rectangle( case_non_bonus[0], case_non_bonus[1], case_non_bonus[2], case_non_bonus[3], remplissage="white", tag="case_non_bonus")
    fltk.texte(LARGEUR//2 + 105, H*6 + ecart*12 + H//2, "NON", ancrage="center", taille=20, tag="text_non_bonus")
    
    #Jouer
    fltk.rectangle(case_jouer[0], case_jouer[1], case_jouer[2], case_jouer[3], remplissage="white", tag="case_jouer")
    fltk.texte(case_jouer[2] - H, case_jouer[1] + H // 2, "JOUER", ancrage="center", taille=20, tag="text_jouer")
    
def clique_dans_rectangle(x1, y1, x2, y2):
    """Vérifie si la souris est dans le rectangle

    Args:
        x1 (xmin): coint haut gauche
        y1 (ymin): coint haut gauche
        x2 (xmax): coint bas droit
        y2 (ymax): coint bas droit

    Returns:
        bool: True si la souris est dans le rectangle, False sinon
    """
    x, y = fltk.abscisse_souris(), fltk.ordonnee_souris()
    return x1 < x < x2 and y1 < y < y2

def modifie_dict_case_grise(case_grise, dict_case_grise):
    """
    Modifie la valeur de la clé (case_grise) a "Grey" et toutes les autres valeur a "White"

    Args:
        case_grise(tuple(int,int,int,int)): La case qui doit etre mis en gris.
        dict_case_grise(dict): Un dictionnaire avec des cases comme clé et des couleur comme valeur.

    Returns:
        dict: La version a jour de dict_case_grise
    """
    for c, v in dict_case_grise.items():
        if c == case_grise:
            dict_case_grise[c] = "Grey"
        else:
            dict_case_grise[c] = "White"
    return dict_case_grise
    
def detecte_gris(d: dict):
    """Vérifie si dans le dictionnaire, il y a au moins une clé avec la valeur "Grey"

    Args:
        d (dict): Le dictionnaire a vérifier

    Returns:
        bool: True si il y a au moins une clé avec la valeur "Grey", False sinon.
    """
    for v in d.values():
        if v == "Grey":
            return True
    return False

def rectangle_text(carre, text, ancrage="center", taille=20, remplissage="white", tag_rectangle=None, tag_text=None, oui_non=False):
    """
    Dessine un rectangle et y ajoute du texte

    Args:
        carre (Tuple[float, float, float, float]): Coordonnes du rectangle
        text (str): Texte a afficher
        ancrage (str, optional): Ancrage du texte (defaut : "center").
        taille (int, optional): Taille de police (defaut : 20).
        remplissage (str, optional): Couleur de remplissage du rectangle (defaut : "white").
        tag_rectangle (str, optional): Tag du rectangle (defaut : None).
        tag_text (str, optional): Tag du texte (d faut : None).
        oui_non (bool, optional): Bool an indiquant si le rectangle doit  tre d cal  de 35 pixels (defaut : False).
    """
    if oui_non:
        fltk.rectangle(carre[0], carre[1], carre[2], carre[3], remplissage=remplissage, tag=tag_rectangle)
        fltk.texte(carre[0] + 35, carre[1] + H // 2, text, ancrage=ancrage, taille=taille, tag=tag_text)
    else:
        fltk.rectangle(carre[0], carre[1], carre[2], carre[3], remplissage=remplissage, tag=tag_rectangle)
        fltk.texte(carre[0] + H // 2, carre[1] + H // 2, text, ancrage=ancrage, taille=taille, tag=tag_text)
    
def pseudo_valide(d: dict, n: int):
    """Regarde si la liste de pseudo est remplie

    Args:
        d (dict): valeur_saisi
        n (int): nb_joueur

    Returns:
        bool: True si la liste est remplie, False sinon
    """
    for i in range(n):
        if d["champ_pseudo"][i]:
            continue
        else:
            return False
    return True

def main() -> dict:
    """Fonction principale qui tant que jouer est faux, va actualiser la page et prendre les données que l'utilisateur va renseigner

    Returns:
        dict: Toutes les données nécessaires au jeu
    """
    fenetre_acceuil()
    taille_manche = 20
    champ_actif = None
    dict_case_grise_234 = {carre_2:"White", carre_3:"White", carre_4:"White"}
    dict_case_grise_oui_non_ia_ale = {case_oui_ia_alea:"White", case_non_ia_alea:"White"}
    dict_case_grise_oui_non_ia_contre = {case_oui_ia_contre:"White", case_non_ia_contre:"White"}
    dict_case_grise_oui_non_bonus = {case_oui_bonus:"White", case_non_bonus:"White"}
    nb_joueurs, nb_manches, pseudo, ia_alea, ia_contre, bonus = 0, "",[], False, False, False #Tous les parametres par defaut
    jouer = False
    while not(jouer):
        valeur_saisi = {"champ_manches": nb_manches, "champ_pseudo": pseudo,"nb_joueurs": nb_joueurs, "ia_alea": ia_alea, "ia_contre": ia_contre, "bonus": bonus}
        ev = fltk.donne_ev()
        if ev:
            nom_ev, param_ev = ev
            #print(nom_ev, param_ev)
            if nom_ev == "ClicGauche":
                # Vérification des clics dans les champs
                # Nombre de manche
                if clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*8, LARGEUR - ecart, H*2 + ecart*8 + H):
                    largeur_champ = (LARGEUR - ecart) - (LARGEUR//2 + 10)
                    taille_manche = taille_manche
                    champ_actif = "champ_manches"
                    tag_champ_actif = "case_text_champ_manches"
                # Pseudo
                #nombre de joueurs = 2
                if clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, (LARGEUR*3)//4 - ecart, H*4 + ecart*9) and nb_joueurs == 2:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_1"
                    largeur_champ = ((LARGEUR*3)//4 - ecart) - (LARGEUR//2 + 10)
                    i = 0
                if clique_dans_rectangle((LARGEUR*3)//4, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9) and nb_joueurs == 2:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_2"
                    largeur_champ =  (LARGEUR - ecart) - ((LARGEUR*3)//4)
                    i = 1
                #nombre de joueurs = 3
                if clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, (LARGEUR*4)//6 - ecart, H*4 + ecart*9) and nb_joueurs == 3:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_1"
                    largeur_champ = ((LARGEUR*4)//6 - ecart) - (LARGEUR//2 + 10)
                    i = 0
                if clique_dans_rectangle((LARGEUR*4)//6, H*2 + ecart*9 + H, (LARGEUR*5)//6 - ecart, H*4 + ecart*9) and nb_joueurs == 3:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_2"
                    largeur_champ = ((LARGEUR*5)//6 - ecart)- ((LARGEUR*4)//6)
                    i = 1
                if clique_dans_rectangle((LARGEUR*5)//6, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9) and nb_joueurs == 3:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_3"
                    largeur_champ = (LARGEUR - ecart) - ((LARGEUR*5)//6)
                    i = 2
                #nombre de joueurs = 4
                if clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, (LARGEUR*5)//8 - ecart, H*4 + ecart*9) and nb_joueurs == 4:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_1"
                    largeur_champ = ((LARGEUR*5)//8 - ecart) - (LARGEUR//2 + 10)
                    i = 0
                if clique_dans_rectangle((LARGEUR*5)//8, H*2 + ecart*9 + H, (LARGEUR*6)//8 - ecart, H*4 + ecart*9) and nb_joueurs == 4:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_2"
                    largeur_champ = ((LARGEUR*6)//8 - ecart) - ((LARGEUR*5)//8)
                    i = 1
                if clique_dans_rectangle((LARGEUR*6)//8, H*2 + ecart*9 + H, (LARGEUR*7)//8 - ecart, H*4 + ecart*9) and nb_joueurs == 4:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_3"
                    largeur_champ = ((LARGEUR*7)//8 - ecart) - ((LARGEUR*6)//8)
                    i = 2
                if clique_dans_rectangle((LARGEUR*7)//8, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9) and nb_joueurs == 4:
                    champ_actif = "champ_pseudo"
                    tag_champ_actif = "case_champ_pseudo_4"
                    largeur_champ = (LARGEUR - ecart) - ((LARGEUR*7)//8)
                    i = 3
                # si cest pas dans les champs de saisies
                if nb_joueurs == 0 and not (clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*8, LARGEUR - ecart, H*2 + ecart*8 + H) or clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9)):
                    champ_actif = None
                # Vérification des clics dans les cases pour 2, 3 et 4
                if clique_dans_rectangle(carre_2[0], carre_2[1], carre_2[2], carre_2[3]):
                    for j in range(1,5):
                        if j > 1:
                            fltk.efface(f"champ_saisie_pseudo_{j}")
                        fltk.efface(f"case_champ_pseudo_{j}")
                    taille = [20, 20]
                    case_grise = carre_2
                    valeur_saisi["champ_pseudo"].clear()
                    valeur_saisi["champ_pseudo"].extend(["", ""])
                    nb_joueurs = 2
                    dict_case_grise_234 = modifie_dict_case_grise(case_grise, dict_case_grise_234)
                    fltk.rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, (LARGEUR*3)//4 - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_2")
                    fltk.rectangle( (LARGEUR*3)//4, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_2")
                if clique_dans_rectangle(carre_3[0], carre_3[1], carre_3[2], carre_3[3]):
                    for j in range(1,5):
                        if j > 1:
                            fltk.efface(f"champ_saisie_pseudo_{j}")
                        fltk.efface(f"case_champ_pseudo_{j}")
                    taille = [20, 20, 20]
                    case_grise = carre_3
                    valeur_saisi["champ_pseudo"].clear()
                    valeur_saisi["champ_pseudo"].extend(["", "", ""])
                    nb_joueurs = 3
                    dict_case_grise_234 = modifie_dict_case_grise(case_grise, dict_case_grise_234) 
                    fltk.rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, (LARGEUR*4)//6 - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_3")
                    fltk.rectangle((LARGEUR*4)//6, H*2 + ecart*9 + H, (LARGEUR*5)//6 - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_3")
                    fltk.rectangle((LARGEUR*5)//6, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_3")
                if clique_dans_rectangle(carre_4[0], carre_4[1], carre_4[2], carre_4[3]):
                    for j in range(1,5):
                        if j > 1:
                            fltk.efface(f"champ_saisie_pseudo_{j}")
                        fltk.efface(f"case_champ_pseudo_{j}")
                    taille = [20, 20, 20, 20]
                    case_grise = carre_4
                    valeur_saisi["champ_pseudo"].clear()
                    valeur_saisi["champ_pseudo"].extend(["", "", "", ""])
                    nb_joueurs = 4
                    dict_case_grise_234 = modifie_dict_case_grise(case_grise, dict_case_grise_234)
                    fltk.rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, (LARGEUR*5)//8 - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_3")
                    fltk.rectangle((LARGEUR*5)//8, H*2 + ecart*9 + H, (LARGEUR*6)//8 - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_3")
                    fltk.rectangle((LARGEUR*6)//8, H*2 + ecart*9 + H, (LARGEUR*7)//8 - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_3")
                    fltk.rectangle((LARGEUR*7)//8, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9, remplissage="white", tag="champ_saisie_pseudo_3")
                # Vérification des clics dans les cases pour oui et non pour ia_alea
                if clique_dans_rectangle(case_oui_ia_alea[0], case_oui_ia_alea[1], case_oui_ia_alea[2], case_oui_ia_alea[3]):
                    case_grise = case_oui_ia_alea
                    ia_alea = True
                    dict_case_grise_oui_non_ia_ale = modifie_dict_case_grise(case_grise, dict_case_grise_oui_non_ia_ale)
                if clique_dans_rectangle(case_non_ia_alea[0], case_non_ia_alea[1], case_non_ia_alea[2], case_non_ia_alea[3]):
                    case_grise = case_non_ia_alea
                    ia_alea = False
                    dict_case_grise_oui_non_ia_ale = modifie_dict_case_grise(case_grise, dict_case_grise_oui_non_ia_ale)
                # Vérification des clics dans les cases pour oui et non pour ia_contre
                if clique_dans_rectangle(case_oui_ia_contre[0], case_oui_ia_contre[1], case_oui_ia_contre[2], case_oui_ia_contre[3]):
                    case_grise = case_oui_ia_contre
                    ia_contre = True
                    dict_case_grise_oui_non_ia_contre = modifie_dict_case_grise(case_grise, dict_case_grise_oui_non_ia_contre)
                if clique_dans_rectangle(case_non_ia_contre[0], case_non_ia_contre[1], case_non_ia_contre[2], case_non_ia_contre[3]):
                    case_grise = case_non_ia_contre
                    ia_contre = False
                    dict_case_grise_oui_non_ia_contre = modifie_dict_case_grise(case_grise, dict_case_grise_oui_non_ia_contre)
                # Vérification des clics dans les cases pour oui et non pour bonus
                if clique_dans_rectangle(case_oui_bonus[0], case_oui_bonus[1], case_oui_bonus[2], case_oui_bonus[3]):
                    case_grise = case_oui_bonus
                    bonus = True
                    dict_case_grise_oui_non_bonus = modifie_dict_case_grise(case_grise, dict_case_grise_oui_non_bonus)
                if clique_dans_rectangle(case_non_bonus[0], case_non_bonus[1], case_non_bonus[2], case_non_bonus[3]):
                    case_grise = case_non_bonus
                    bonus = False
                    dict_case_grise_oui_non_bonus = modifie_dict_case_grise(case_grise, dict_case_grise_oui_non_bonus)
                # Vérication des clics dans la case jouer
                if clique_dans_rectangle(case_jouer[0], case_jouer[1], case_jouer[2], case_jouer[3]):
                    if valeur_saisi["champ_manches"] and pseudo_valide(valeur_saisi, nb_joueurs) and nb_joueurs > 0:
                        jouer = True
                    else:
                        # Affichage du message d'erreur pour le nombre de joueurs
                        if nb_joueurs == 0:
                            txt = "NOMBRES DE JOUEURS"
                            L   = len(txt) * 12
                            fltk.efface("case_nombre_joueurs")
                            fltk.efface("text_nombre_joueurs")
                            fltk.rectangle(L, ecart, LARGEUR - L, ecart + H, remplissage="red", tag="case_nombre_joueurs")
                            fltk.texte(LARGEUR // 2, 40, "NOMBRES DE JOUEURS", ancrage="center",taille=20, tag="text_nombre_joueurs")
                        if nb_joueurs > 0:
                            txt = "NOMBRES DE JOUEURS"
                            L   = len(txt) * 12
                            fltk.efface("case_nombre_joueurs")
                            fltk.efface("text_nombre_joueurs")
                            fltk.rectangle(L, ecart, LARGEUR - L, ecart + H, remplissage="white", tag="case_nombre_joueurs")
                            fltk.texte(LARGEUR // 2, 40, "NOMBRES DE JOUEURS", ancrage="center",taille=20, tag="text_nombre_joueurs")
                        # Affichage du message d'erreur pour le pseudo
                        if not(pseudo_valide(valeur_saisi, nb_joueurs)):
                            fltk.efface("case_pseudo")
                            fltk.efface("text_pseudo")
                            fltk.rectangle(ecart,H*2 + ecart*9 + H, LARGEUR//2 - ecart, H*4 + ecart*9, remplissage="red", tag="case_pseudo")
                            fltk.texte(LARGEUR//4, H*3 + ecart*9 + H//2, "PSEUDO : ", ancrage="center", taille=20, tag="text_pseudo")
                        if pseudo_valide(valeur_saisi, nb_joueurs):
                            fltk.efface("case_pseudo")
                            fltk.efface("text_pseudo")
                            fltk.rectangle(ecart,H*2 + ecart*9 + H, LARGEUR//2 - ecart, H*4 + ecart*9, remplissage="white", tag="case_pseudo")
                            fltk.texte(LARGEUR//4, H*3 + ecart*9 + H//2, "PSEUDO : ", ancrage="center", taille=20, tag="text_pseudo")
                        # Affichage du message d'erreur pour le nombre de manches
                        if not(valeur_saisi["champ_manches"]):
                            fltk.efface("case_manches")
                            fltk.efface("text_manches")
                            txt = "NOMBRES DE MANCHES : "
                            L   = len(txt) * 18
                            fltk.rectangle(ecart, H*2 + ecart*8, ecart + L, H*2 + ecart*8 + H, remplissage="red", tag="case_manches")
                            fltk.texte(LARGEUR//4, H*2 + ecart*8 + H//2, txt, ancrage="center",taille=20, tag="text_manches")
                        if valeur_saisi["champ_manches"]:
                            fltk.efface("case_manches")
                            fltk.efface("text_manches")
                            txt = "NOMBRES DE MANCHES : "
                            L   = len(txt) * 18
                            fltk.rectangle(ecart, H*2 + ecart*8, ecart + L, H*2 + ecart*8 + H, remplissage="white", tag="case_manches")
                            fltk.texte(LARGEUR//4, H*2 + ecart*8 + H//2, txt, ancrage="center",taille=20, tag="text_manches")
            # Gestion des touches
            if nom_ev == "Touche" and champ_actif:
                if param_ev.keysym == "BackSpace":
                    if champ_actif == "champ_pseudo":
                        taille[i] = taille[i] + 1 if taille[i] < 20 else 20 
                        valeur_saisi[champ_actif][i] = valeur_saisi[champ_actif][i][:-1]    
                    elif champ_actif == "champ_manches":
                        taille_manche = taille_manche + 1 if taille_manche < 20 else 20
                        valeur_saisi[champ_actif] = valeur_saisi[champ_actif][:-1] 
                        nb_manches = nb_manches[:-1]
                else:
                    if champ_actif == "champ_pseudo":
                        #passe a la prochaine case
                        if param_ev.keysym == "Return":
                            i = i + 1 if i < nb_joueurs-1 else 0
                            tag_champ_actif = f"case_champ_pseudo_{i+1}"
                        else:
                            largeur, hauteur = fltk.taille_texte( valeur_saisi[champ_actif][i] + param_ev.char, taille=taille[i])
                            if largeur > largeur_champ - 30:
                                if taille[i] > 10:
                                    taille[i] -= 1
                                    valeur_saisi[champ_actif][i] += param_ev.char
                            else:     
                                valeur_saisi[champ_actif][i] += param_ev.char
                    else:
                        if param_ev.char.isdigit():
                            largeur, hauteur = fltk.taille_texte(valeur_saisi["champ_manches"] + param_ev.char, taille=taille_manche)
                            if largeur > largeur_champ - 30:
                                if taille_manche > 10:
                                    taille_manche -= 1
                                    valeur_saisi["champ_manches"] += param_ev.char
                                    nb_manches += param_ev.char
                            else:
                                valeur_saisi["champ_manches"] += param_ev.char
                                nb_manches += param_ev.char
                # Mise à jour de l'affichage
                fltk.efface(tag_champ_actif)
                if champ_actif == "champ_pseudo":
                    if nb_joueurs == 2:
                        fltk.texte(LARGEUR*5//8 if i == 0 else LARGEUR*7//8, H*3 + ecart*9 + H//2, valeur_saisi["champ_pseudo"][i], police="Consolas", ancrage="center", taille=taille[i], tag=tag_champ_actif)
                    elif nb_joueurs == 3:
                        fltk.texte(LARGEUR*7//12 if i == 0 else LARGEUR*9//12 if i == 1 else LARGEUR*11//12, H*3 + ecart*9 + H//2, valeur_saisi["champ_pseudo"][i], police="Consolas", ancrage="center", taille=taille[i], tag=tag_champ_actif)
                    elif nb_joueurs == 4:
                        fltk.texte(LARGEUR*9//16 if i == 0 else LARGEUR*11//16 if i == 1 else LARGEUR*13//16 if i == 2 else LARGEUR*15//16, H*3 + ecart*9 + H//2, valeur_saisi["champ_pseudo"][i], police="Consolas", ancrage="center", taille=taille[i], tag=tag_champ_actif)
                elif champ_actif == "champ_manches":
                    
                    fltk.texte(LARGEUR - LARGEUR//4, H*2 + ecart*8 + H//2 , valeur_saisi["champ_manches"],police="Consolas", ancrage="center", taille=taille_manche, tag=tag_champ_actif)
            elif nom_ev == "Quitte":
                break
                
        #Vérifie si les cases sont grises
        if detecte_gris(dict_case_grise_234):
            for j in range(2,5):
                fltk.efface(f"case_{j}")
                fltk.efface(f"text_{j}")
            rectangle_text(carre_2, "2", remplissage=dict_case_grise_234[carre_2], tag_rectangle="case_2", tag_text="text_2")
            rectangle_text(carre_3, "3", remplissage=dict_case_grise_234[carre_3], tag_rectangle="case_3", tag_text="text_3")
            rectangle_text(carre_4, "4", remplissage=dict_case_grise_234[carre_4], tag_rectangle="case_4", tag_text="text_4")
        if detecte_gris(dict_case_grise_oui_non_ia_ale):
            for j in ["oui","non"]:
                fltk.efface(f"case_{j}_ia_alea")
                fltk.efface(f"text_{j}_ia_alea")
            rectangle_text(case_oui_ia_alea, "OUI", remplissage=dict_case_grise_oui_non_ia_ale[case_oui_ia_alea], tag_rectangle="case_oui_ia_alea", tag_text="text_oui_ia_alea", oui_non=True)
            rectangle_text(case_non_ia_alea, "NON", remplissage=dict_case_grise_oui_non_ia_ale[case_non_ia_alea], tag_rectangle="case_non_ia_alea", tag_text="text_non_ia_alea", oui_non=True)
        if detecte_gris(dict_case_grise_oui_non_ia_contre):
            for j in ["oui","non"]:
                fltk.efface(f"case_{j}_ia_contre")
                fltk.efface(f"text_{j}_ia_contre")
            rectangle_text(case_oui_ia_contre, "OUI", remplissage=dict_case_grise_oui_non_ia_contre[case_oui_ia_contre], tag_rectangle="case_oui_ia_contre", tag_text="text_oui_ia_contre", oui_non=True)
            rectangle_text(case_non_ia_contre, "NON", remplissage=dict_case_grise_oui_non_ia_contre[case_non_ia_contre], tag_rectangle="case_non_ia_contre", tag_text="text_non_ia_contre", oui_non=True)
        if detecte_gris(dict_case_grise_oui_non_bonus):
            for j in ["oui","non"]:
                fltk.efface(f"case_{j}_bonus")
                fltk.efface(f"text_{j}_bonus")
            rectangle_text(case_oui_bonus, "OUI", remplissage=dict_case_grise_oui_non_bonus[case_oui_bonus], tag_rectangle="case_oui_bonus", tag_text="text_oui_bonus", oui_non=True)
            rectangle_text(case_non_bonus, "NON", remplissage=dict_case_grise_oui_non_bonus[case_non_bonus], tag_rectangle="case_non_bonus", tag_text="text_non_bonus", oui_non=True)
        fltk.mise_a_jour() 
    return valeur_saisi 
      
if __name__ == "__main__":
    main()