import Accueil, jeu, resultat, json

def rolit():
    game = True
    while game:
        d = Accueil.main() #{"champ_manches": nb_manches, "champ_pseudo": pseudo,"nb_joueurs": nb_joueurs, "ia_alea": ia_alea, "ia_contre": ia_contre, "bonus": bonus}
        values = jeu.main(d, True)
        if values == True:
            game = True
        if values == False:
            writer = open("save.json", "w")
            contenue = json.dumps(d)
            game = False
        else:
            score_partie, manches_gagnees = values
            game = resultat.resultat(score_partie, manches_gagnees)
        
if __name__ == "__main__":
    rolit()
    