from numpy import *


submatrix = []
matrix = []
print("Bienvenue sur le programme de calcul matriciel made in AtlaaS\n")
fichier = open("matrix.txt", "a")
fichier.write((str(input("Comment s'appelle ton exercices ?\n")))+"\n\n")
matrix_nbr = int(input("Combien de matrice avez-vous ?\n"))
i = n = m = 0
x = []
if matrix_nbr > 26:
    print("Error trop de matrices")
else:
    while i != matrix_nbr:
        t = int(input("Combien avez-vous de dimension dans la {}e matrice ?\n".format(i+1)))
        k = h = int(input("Combien avez-vous de variable dans la {}e matrice ?\n".format(i+1)))
        while t != 0:
            while k != 0:
                x.append(int(input(f'Donner la {(n + 1)}e variable la {(m + 1)}e dimension de la {(i + 1)}e matrice\n')))
                k -= 1
                n += 1
            n = 0
            k = h
            print(x,"\n")
            m += 1
            t -= 1
            submatrix.append(x)
            print(submatrix,"\n")
            x = []
        fichier.write((str(input("Comment s'appelle cette matrice?"))) + " : {}\n".format(array(submatrix)))
        matrix.append(submatrix)
        submatrix = []
        i += 1
        m = 0
    boucle = True
    while boucle == True:
        m = 0
        k = len(matrix)
        matrix_ = []
        while k != 0:
            print("{} - {} ,\n".format(m+1,array(matrix[len(matrix)-k])))
            k -= 1
            m += 1
        retry = True
        while retry == True:
            choise_nbr = int(input("Combien de matrice voullez vous calculer?\nValeurs entre 0 - {}\n 0 = toutes".format(len(matrix))))
            if choise_nbr == 0:
                matrix_ = matrix
                retry = False
            elif choise_nbr !=0 and choise_nbr < (len(matrix)+1):
                while choise_nbr != 0:
                    k = int(input("Avec quel matrice voullais vous travailler?"))
                    matrix_.append(matrix[k-1])
                    choise_nbr -= 1
                retry = False
            else:
                print("Vous n'avez pas choisi une valeur existante veuillez recommencer")
            choise_calc = int(input("Que voulais vous faire de ses matrices?\n1-Les additionner\n2-Les mutiplier\n3-Les soustraire\n4-L'inverse"))
            k = len(matrix_)
            addit = []
            multi = []
            soust = []
            inv = []
            if choise_calc == 1:
                while k > 1:
                    if len(addit) != 0:
                        addit[0] = ((array(addit[0])) + (array(matrix_[len(matrix_)-1])))
                        k -= 1
                    else:
                        addit.append((array(matrix_[0])) + (array(matrix_[1])))
                        k -= 1
                print(array(addit[0]))
            elif choise_calc == 2:
                while k > 1:
                    if len(multi) != 0:
                        multi[0] = dot((array(multi[0])),(array(matrix_[len(matrix_)-k])))
                        k -= 1
                    else:
                        multi.append(dot((array(matrix_[0])),(array(matrix_[1]))))
                        k -= 1
                print(array(multi[0]))
            elif choise_calc == 3:
                while k > 1:
                    if len(soust) != 0:
                        soust[0] = ((array(soust[0]))-(array(matrix_[len(matrix_)-k])))
                        k -= 1
                    else:
                        soust.append((array(matrix_[0]))-(array(matrix_[1])))
                        k -= 1
                print(array(soust[0]))
            elif choise_calc == 4:
                inv.append(linalg.inv(array(matrix_[0])))
                print(array(inv[0]))
            retry_ = False
            while retry_ == False:
                new = int(input("Souhaiter vous:\n1 - Quitter\n2 - Recalculer en memorisant la valeur calculer\n3-Recalculer sans prendre en compte la valeur calculer"))
                if new == 1:
                    fichier = open("matrix.txt", "r")
                    print(fichier.read())
                    fichier.close()
                    print("A bientot")
                    boucle = False
                    break
                elif new == 2:
                    retry_ = True
                    if len(multi) != 0:
                        fichier.write((str(input("Comment s'appelle cette valeur?")))+" : {}\n".format(multi[0]))
                        matrix.append(multi[0])
                    if len(addit) != 0:
                        fichier.write((str(input("Comment s'appelle cette valeur?"))) + " : {}\n".format(addit[0]))
                        matrix.append(addit[0])
                    if len(soust) != 0:
                        fichier.write((str(input("Comment s'appelle cette valeur?"))) + " : {}\n".format(soust[0]))
                        matrix.append(soust[0])
                    if len(inv) != 0:
                        fichier.write((str(input("Comment s'appelle cette valeur?"))) + " : {}\n".format(inv[0]))
                        matrix.append(inv[0])
                elif new == 3:
                    retry_ = True
                else:
                    print("Vous n'avez pas choisi une valeur inexistante veuillez recommencer")
