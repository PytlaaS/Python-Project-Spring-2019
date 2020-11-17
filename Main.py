from matrix.Calcul import *
from numpy import *


print("Bienvenue sur le programme de calcul matriciel made in AtlaaS\n")
while 1 == 1:
    bouclage = True
    while bouclage == True:
        wrt = str(input("Voullez vous enregistrer les valeurs de matrices ? o/n\n"))
        if wrt == 'o' or wrt == 'O':
            bouclage = False
            name = ((str(input("Comment s'appelle ton exercices ?\n"))) + "\n\n")
            write_txt(wrt, name)
        elif wrt == 'n' or wrt == 'N':
            bouclage = False
        else:
            print("Choix erroné veuillez recommencer")
    main(wrt)