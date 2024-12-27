import fltk, Accueil, jeu

def resultat(score_partie: dict, manches_gagnees: dict, c_j: dict, save: str) -> None:
    """Affiche le résultat de la partie."""
    
    nb_joueur = len(c_j)
    resultat_partie = jeu.gagant_partie(score_partie, manches_gagnees)
    # Dimensions de la fenêtre
    largeur, hauteur, ecart = 800, 800, 20
    fltk.cree_fenetre(largeur, hauteur)
    
    # Couleur de fond
    fltk.rectangle(0, 0, largeur, hauteur, remplissage="#260d2e")

    # Titre principal
    fltk.rectangle(largeur // 4, ecart, largeur*3//4, 50 + ecart, remplissage="#513d57", couleur="#D9F2D1", epaisseur=5, tag="case_titre")
    Accueil.texte_dans_rectangle(largeur // 4, 20, largeur*3//4, 70, "Resultat de la Partie", couleur="#D9F2D1", ancrage="center", police="Calibri", taille=25, tag="text_titre")

    # Zone de statistiques
    fltk.rectangle(ecart, 50 + ecart*2, largeur - ecart, hauteur//2 - ecart, remplissage="#513d57", couleur="#D9F2D1", epaisseur=5, tag="case_statistique")
    fltk.texte(largeur // 2, 75 + ecart*2, "STATISTIQUES", couleur="#D9F2D1", ancrage="center", police="Calibri", taille=22, tag="text_statistique")

    # Affichage des statistiques
    fltk.texte(largeur/2 - 100, 50*2 + ecart*3, "POINTS", couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")#mauvaise ordonnée
    fltk.texte(largeur/2 + 100, 50*2 + ecart*3, "MANCHES GAGNEES", couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")#mauvaise ordonnée
    fltk.ligne(largeur/2 + 50, 50*2 + ecart*4, largeur/2 + 50, hauteur/2 - ecart - 10, couleur="#D9F2D1", epaisseur=2)
    # Rouge
    Accueil.texte_dans_rectangle(ecart*2, 50*2 + ecart*4, ecart*2 + 100, 50*3 + ecart*4, "Rouge" if "Rouge" not in c_j else c_j["Rouge"], couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    fltk.texte(largeur/2 - 60, 50*3 + ecart*4 - 25, score_partie["Rouge"], couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    fltk.texte(largeur/2 + 220, 50*3 + ecart*4 - 25, manches_gagnees["Rouge"] if nb_joueur > 0 else "0", couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    #Jaune
    Accueil.texte_dans_rectangle(ecart*2, 50*3 + ecart*4, ecart*2 + 100, 50*4 + ecart*4, "Jaune" if "Jaune" not in c_j else c_j["Jaune"], couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    fltk.texte(largeur/2 - 60, 50*4 + ecart*4 - 25, score_partie["Jaune"], couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    fltk.texte(largeur/2 + 220, 50*4 + ecart*4 - 25, manches_gagnees["Jaune"] if nb_joueur > 1 else "0", couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    #Vert
    Accueil.texte_dans_rectangle(ecart*2, 50*4 + ecart*4, ecart*2 + 100, 50*5 + ecart*4, "Vert" if "Vert" not in c_j else c_j["Vert"], couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    fltk.texte(largeur/2 - 60, 50*5 + ecart*4 - 25, score_partie["Vert"], couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    fltk.texte(largeur/2 + 220, 50*5 + ecart*4 - 25, manches_gagnees["Vert"] if nb_joueur > 2 else "0", couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    #Bleu
    Accueil.texte_dans_rectangle(ecart*2, 50*5 + ecart*4, ecart*2 + 100, 50*6 + ecart*4, "Bleu" if "Bleu" not in c_j else c_j["Bleu"], couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    fltk.texte(largeur/2 - 60, 50*6 + ecart*4 - 25, score_partie["Bleu"], couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    fltk.texte(largeur/2 + 220, 50*6 + ecart*4 - 25, manches_gagnees["Bleu"] if nb_joueur > 3 else "0", couleur="#D9F2D1", ancrage="w", police="Calibri", taille=22, tag="text_resultat")
    
    # Bouton "Accueil"
    fltk.rectangle(ecart, ecart, largeur // 4 - ecart, 50 + ecart, remplissage="#513d57", couleur="#D9F2D1", epaisseur=5, tag="case_accueil")
    Accueil.texte_dans_rectangle(ecart, ecart, largeur // 4 - ecart, 50 + ecart, "Accueil", couleur="#D9F2D1", ancrage="center", police="Calibri", taille=25, tag="text_accueil")

    # Podium
    # Joueur 1 (au centre, 1er)
    fltk.rectangle(largeur/2 - 100, hauteur - ecart - 275, largeur/2 + 100, hauteur - 50 - ecart, remplissage="#513d57", couleur="#D9F2D1", epaisseur=5, tag="case_podium")
    Accueil.texte_dans_rectangle(largeur/2 - 125, hauteur - ecart - 325, largeur/2 + 125, hauteur - ecart - 275, c_j[resultat_partie[0][0]] if nb_joueur > 0 else None, couleur="#D9F2D1", ancrage="center", police="Calibri", taille=25, tag="text_podium")#changer pseudo du 1er
    fltk.texte(largeur/2, hauteur - (ecart + 275 + 50 + ecart)/2, "1er", couleur="#D9F2D1", ancrage="center", police="Calibri", taille=40, tag="text_podium")

    # Joueur 2 (à gauche, 2ème)
    fltk.rectangle(largeur/2 - 300, hauteur - ecart - 225, largeur/2 - 100, hauteur - 50 - ecart, remplissage="#513d57", couleur="#D9F2D1", epaisseur=5, tag="case_podium")
    Accueil.texte_dans_rectangle(largeur/2 - 300, hauteur - ecart - 275, largeur/2 - 100, hauteur - ecart - 225, c_j[resultat_partie[1][0]] if nb_joueur > 1 else None, couleur="#D9F2D1", ancrage="center", police="Calibri", taille=25, tag="text_podium")#changer pseudo du 2eme
    fltk.texte(largeur/2 - 200,hauteur - (ecart + 225 + 50 + ecart)/2, "2eme", couleur="#D9F2D1", ancrage="center", police="Calibri", taille=40, tag="text_podium")

    # Joueur 3 (à droite, 3ème)
    fltk.rectangle(largeur/2 + 100, hauteur - ecart - 175, largeur/2 + 300, hauteur - 50 - ecart, remplissage="#513d57", couleur="#D9F2D1", epaisseur=5, tag="case_podium")
    Accueil.texte_dans_rectangle(largeur/2 + 100, hauteur - ecart - 225, largeur/2 + 300, hauteur - ecart - 175, c_j[resultat_partie[2][0]] if nb_joueur > 2 else None, couleur="#D9F2D1", ancrage="center", police="Calibri", taille=25, tag="text_podium")#changer pseudo du 3eme
    fltk.texte(largeur/2 + 200, hauteur - (ecart + 175 + 50 + ecart)/2, "3eme", couleur="#D9F2D1", ancrage="center", police="Calibri", taille=40, tag="text_podium")

    # Joueur 4 (en bas à gauche, 4ème)
    fltk.texte(ecart, hauteur - 35,"4eme : " + c_j[resultat_partie[3][0]] if nb_joueur > 3 else None, couleur="#D9F2D1", ancrage="w", police="Calibri", taille=20, tag="text_podium")
    
    while True:
        ev = fltk.donne_ev()
        if ev != None:
            nom_ev, param_ev = ev
            if nom_ev == "ClicGauche":
                if Accueil.clique_dans_rectangle(ecart, ecart, largeur // 4 - ecart, 50 + ecart):
                    fltk.ferme_fenetre()
                    return True
                else:
                    continue
            elif nom_ev == "Quitte":
                return False
        fltk.mise_a_jour()