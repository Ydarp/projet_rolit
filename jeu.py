import Acceuil,graph,main,fltk

if __name__ == "__main__":
    d = Acceuil.main() #{"champ_manches": nb_manches, "champ_pseudo": pseudo,"nb_joueurs": nb_joueurs, "ia_alea": ia_alea, "ia_contre": ia_contre, "bonus": bonus}
    fltk.ferme_fenetre()
    if d["bonus"]:
        b = main.bonus(d["nb_joueurs"])
    t = main.tableau_depart()
    fltk.cree_fenetre(800,800)
    graph.grille()
    graph.pion(t)
    while not main.end(t):
        pass
    fltk.attend_ev()
 
