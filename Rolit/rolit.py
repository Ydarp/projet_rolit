import Accueil, jeu, resultat

def rolit():
    game = True
    while game:
        d = Accueil.main() #{"champ_manches": nb_manches, "champ_pseudo": pseudo,"nb_joueurs": nb_joueurs, "ia_alea": ia_alea, "ia_contre": ia_contre, "bonus": bonus}
        values = jeu.main(d)
        if values in [True, False]:
            game = values
        else:
            score_partie, manches_gagnees, c_j, save = values
            game = resultat.resultat(score_partie, manches_gagnees, c_j, save)
#amelioration save: quand la partie est finie, la sauvegarde est effacer.         

if __name__ == "__main__":
    rolit()