import Acceuil,jeu,fltk

if __name__ == "__main__":
    d = Acceuil.main() #{"champ_manches": nb_manches, "champ_pseudo": pseudo,"nb_joueurs": nb_joueurs, "ia_alea": ia_alea, "ia_contre": ia_contre, "bonus": bonus}
    fltk.ferme_fenetre()
    jeu.main(d, True)