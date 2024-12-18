import fltk

LARGEUR = 800
HAUTEUR = 800
ecart_2 = 120 #(800-H*4)/5
ecart = 10
H = 50
xmin, ymin, xmax, ymax = ecart_2, H+ecart*3, ecart_2+H, H+ecart*3+H #valeur des coins du rectangle
carre_2, carre_3, carre_4 = (xmin*2 + H, ymin, xmax*2, ymax), (xmin*3 + H*2, ymin, xmax*3, ymax), (xmin*4 + H*3, ymin, xmax*4, ymax)

def afficher_text(text: str,x: int, y: int, couleur="black",tag=None):
    fltk.texte(x,y,text,couleur,ancrage="center", taille=20,tag=tag)
    
def fenetre_acceuil() -> None:
    fltk.cree_fenetre(LARGEUR, HAUTEUR)
    
    #Nomre de joueurs
    txt = "NOMBRES DE JOUEURS"
    L = len(txt) * 12
    fltk.rectangle(L, ecart, LARGEUR - L, ecart + H)
    fltk.texte(LARGEUR // 2, 40, "NOMBRES DE JOUEURS", ancrage="center",taille=20) #police= pour modifié la police et améliorer la visibilité
    
    # carré 1, 2, 3 et 4
    
    fltk.rectangle(carre_2[0], carre_2[1], carre_2[2], carre_2[3])
    fltk.texte(xmin*2 + H + H//2, ymin + H//2,"2", ancrage="center")
    
    fltk.rectangle(carre_3[0], carre_3[1], carre_3[2], carre_3[3])
    fltk.texte(xmin*3 + H*2 + H//2, ymin + H//2,"3", ancrage="center")
    
    fltk.rectangle(carre_4[0], carre_4[1], carre_4[2], carre_4[3])
    fltk.texte(xmin*4 + H*3 + H//2, ymin + H//2,"4", ancrage="center")
    
    #Nombre de manches
    txt = "NOMBRES DE MANCHES : "
    L   = len(txt) * 18
    fltk.rectangle(ecart, H*2 + ecart*8, ecart + L, H*2 + ecart*8 + H)
    fltk.texte(LARGEUR//4, H*2 + ecart*8 + H//2, txt, ancrage="center",taille=20)
    #Champ de saisie
    fltk.rectangle(LARGEUR//2 + 10, H*2 + ecart*8, LARGEUR - ecart, H*2 + ecart*8 + H)
    
    #Pseudo
    txt = "PSEUDO : "
    fltk.rectangle(ecart,H*2 + ecart*9 + H, LARGEUR//2 - ecart, H*4 + ecart*9)
    fltk.texte(LARGEUR//4, H*3 + ecart*9 + H//2, txt, ancrage="center", taille=20)
    #Champ de saisie
    fltk.rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9)
    
    #ia aleatoire
    fltk.rectangle(ecart,H*2 + ecart*10 + 100, LARGEUR//2 - 100, H*4 + ecart*10 + H)
    fltk.texte(LARGEUR//4 -H, H*4 + ecart*10 + H//2, "IA ALÉATOIRE", ancrage="center", taille=20)
    #yes/no
    fltk.rectangle( LARGEUR//2 - H, H*2 + ecart*10 + 100, LARGEUR//2 + 20, H*4 + ecart*10 + H)
    fltk.texte(LARGEUR//2 - 15, H*4 + ecart*10 + H//2, "OUI", ancrage="center", taille=20)
    fltk.rectangle( LARGEUR//2 + 70, H*2 + ecart*10 + 100, LARGEUR//2 + 140, H*4 + ecart*10 + H)
    fltk.texte(LARGEUR//2 + 105, H*4 + ecart*10 + H//2, "NON", ancrage="center", taille=20)
    
    #ia contre
    fltk.rectangle(ecart,H*2 + ecart*11 + 150, LARGEUR//2 - 100, H*5 + ecart*11 + H)
    fltk.texte(LARGEUR//4 -H, H*5 + ecart*11 + H//2, "CONTRE IA", ancrage="center", taille=20)
    #yes/no
    fltk.rectangle( LARGEUR//2 - H, H*2 + ecart*11 + 150, LARGEUR//2 + 20, H*5 + ecart*11 + H)
    fltk.texte(LARGEUR//2 - 15, H*5 + ecart*11 + H//2, "OUI", ancrage="center", taille=20)
    fltk.rectangle( LARGEUR//2 + 70, H*2 + ecart*11 + 150, LARGEUR//2 + 140, H*5 + ecart*11 + H)
    fltk.texte(LARGEUR//2 + 105, H*5 + ecart*11 + H//2, "NON", ancrage="center", taille=20)
    
    #Bonus
    fltk.rectangle(ecart,H*2 + ecart*12 + 200, LARGEUR//2 - 100, H*6 + ecart*12 + H)
    fltk.texte(LARGEUR//4 -H, H*6 + ecart*12 + H//2, "BONUS", ancrage="center", taille=20)
    #yes/no
    fltk.rectangle( LARGEUR//2 - H, H*2 + ecart*12 + 200, LARGEUR//2 + 20, H*6 + ecart*12 + H)
    fltk.texte(LARGEUR//2 - 15, H*6 + ecart*12 + H//2, "OUI", ancrage="center", taille=20)
    fltk.rectangle( LARGEUR//2 + 70, H*2 + ecart*12 + 200, LARGEUR//2 + 140, H*6 + ecart*12 + H)
    fltk.texte(LARGEUR//2 + 105, H*6 + ecart*12 + H//2, "NON", ancrage="center", taille=20)
    
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

def est_un_entier(p, d: dict):
    """Essaye de convertir p en entier

    Args:
        p (_type_): str
        d (dict): texte_saisi

    Returns:
        str or None: str si p est un entier, None sinon
    """
    try:
        int(p)  # Tente de convertir en entier
        return str(p)
    except ValueError:
        d["champ_manches"] = ""
        return None

def modifie_dict_case_grise(case_grise, dict_case_grise):
    for c, v in dict_case_grise.items():
        if c == case_grise:
            dict_case_grise[c] = "Grey"
        else:
            dict_case_grise[c] = "White"
    return dict_case_grise
    
def detecte_gris(d: dict):
    for v in d.values():
        if v == "Grey":
            return True
    return False

def rectangle_text(carre, text, ancrage="center", taille=20, remplissage="white", tag=None):
    fltk.rectangle(carre[0], carre[1], carre[2], carre[3], remplissage=remplissage, tag=tag)
    fltk.texte(carre[0] + H// 2, carre[2] + H// 2, text, ancrage=ancrage, taille=taille, tag=tag)
    
def main():
    fenetre_acceuil()
    champ_actif = None
    texte_saisi = {"champ_manches": "", "champ_pseudo": ["", "", "", ""]}
    i = 0
    dict_case_grise = {carre_2:"White", carre_3:"White", carre_4:"White"}
    while True:
        ev = fltk.donne_ev()
        if ev:
            nom_ev, param_ev = ev
            #print(nom_ev, param_ev)
            if nom_ev == "ClicGauche":
                # Vérification des clics dans les champs
                if clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*8, LARGEUR - ecart, H*2 + ecart*8 + H):
                    champ_actif = "champ_manches"
                if clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9):
                    champ_actif = "champ_pseudo"
                if not (clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*8, LARGEUR - ecart, H*2 + ecart*8 + H) or clique_dans_rectangle(LARGEUR//2 + 10, H*2 + ecart*9 + H, LARGEUR - ecart, H*4 + ecart*9)):
                    champ_actif = None
                if clique_dans_rectangle(carre_2[0], carre_2[1], carre_2[2], carre_2[3]):
                    case_grise = carre_2
                    dict_case_grise = modifie_dict_case_grise(case_grise, dict_case_grise)
                if clique_dans_rectangle(carre_3[0], carre_3[1], carre_3[2], carre_3[3]):
                    case_grise = carre_3
                    dict_case_grise = modifie_dict_case_grise(case_grise, dict_case_grise) 
                if clique_dans_rectangle(carre_4[0], carre_4[1], carre_4[2], carre_4[3]):
                    case_grise = carre_4
                    dict_case_grise = modifie_dict_case_grise(case_grise, dict_case_grise)
            elif nom_ev == "Touche" and champ_actif:
                if param_ev.keysym == "Return":
                    if champ_actif == "champ_pseudo":
                        i += 1
                elif param_ev.keysym == "BackSpace":
                    texte_saisi[champ_actif] = texte_saisi[champ_actif][:-1]
                else:
                    if champ_actif == "champ_pseudo":
                        texte_saisi[champ_actif][i] += param_ev.char
                    else:
                        texte_saisi[champ_actif] += param_ev.char
                # Mettre à jour l'affichage
                fltk.efface(champ_actif)
                afficher_text(est_un_entier(texte_saisi[champ_actif], texte_saisi) if champ_actif == "champ_manches" else texte_saisi[champ_actif][i], LARGEUR - LARGEUR//4, H*2 + ecart*8 + H//2 if champ_actif == "champ_manches" else H*3 + ecart*9 + H//2,
                              tag=champ_actif)
            elif nom_ev == "Quitte":
                break
        if texte_saisi["champ_manches"] or texte_saisi["champ_pseudo"][0] or texte_saisi["champ_pseudo"][1] or texte_saisi["champ_pseudo"][2] or texte_saisi["champ_pseudo"][3]:
            print(texte_saisi)
        if detecte_gris(dict_case_grise):
            fltk.efface("1")
            fltk.efface("2")
            fltk.efface("3")
            fltk.efface("4")
            rectangle_text(carre_2, "2", remplissage=dict_case_grise[carre_2], tag="2")
            rectangle_text(carre_3, "3", remplissage=dict_case_grise[carre_3], tag="3")
            rectangle_text(carre_4, "4", remplissage=dict_case_grise[carre_4], tag="4")
        fltk.mise_a_jour()
        
if __name__ == "__main__":
    main()