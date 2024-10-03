def tableau_depart():
    t = [[None for i in range(8)] for i in range(8)]
    t[3][3],t[3][4],t[4][3],t[4][4] = "r","j","b","v"
    return t
print(tableau_depart())   