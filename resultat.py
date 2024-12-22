import fltk,Acceuil

def resultat(score_partie, manches_gagnees) -> None:
    fltk.cree_fenetre(800, 800)
    fltk.texte(400, 400, str(score_partie), ancrage="center", taille=20, tag="text_resultat")
    fltk.texte(400, 500, str(manches_gagnees), ancrage="center", taille=20, tag="text_resultat")
    
    fltk.rectangle(10, 10, 80, 60, remplissage="white", tag="case_retour")
    Acceuil.texte_dans_rectangle(10, 10, 80, 60, "NEW GAME", ancrage="center", police="Calibri", tag="text_retour")
    #case_retour
    while True:
        ev = fltk.donne_ev()
        if ev != None:
            nom_ev, param_ev = ev
            if nom_ev == "ClicGauche":
                if Acceuil.clique_dans_rectangle(10, 10, 80, 60):
                    fltk.ferme_fenetre()
                    return True
                else:
                    continue
            elif nom_ev == "Quitte":
                return False
        fltk.mise_a_jour()