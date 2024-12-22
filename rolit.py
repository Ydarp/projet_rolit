import Acceuil,jeu,resultat,fltk

def rolit():
    game = True
    while game:
        d = Acceuil.main() #{"champ_manches": nb_manches, "champ_pseudo": pseudo,"nb_joueurs": nb_joueurs, "ia_alea": ia_alea, "ia_contre": ia_contre, "bonus": bonus}
        values = jeu.main(d, True)
        if values == True:
            continue
        else:
            score_partie, manches_gagnees = values
            game = resultat.resultat(score_partie, manches_gagnees)
        
if __name__ == "__main__":
    rolit()
    