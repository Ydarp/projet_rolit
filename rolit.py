import Acceuil,jeu,resultat,fltk

def rolit():
    game = True
    while game:
        d = Acceuil.main() #{"champ_manches": nb_manches, "champ_pseudo": pseudo,"nb_joueurs": nb_joueurs, "ia_alea": ia_alea, "ia_contre": ia_contre, "bonus": bonus}
        score_partie, manches_gagnees = jeu.main(d, True)
        game = resultat.resultat(score_partie, manches_gagnees)
        
if __name__ == "__main__":
    rolit()
    