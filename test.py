import time, fltk
fltk.cree_fenetre(800, 800)
for i in range(10):
    fltk.rectangle(10*i,10*i,10*i+10,10*i+10,remplissage="purple")
    time.sleep(1)
    fltk.mise_a_jour()
fltk.attend_ev()
fltk.ferme_fenetre()