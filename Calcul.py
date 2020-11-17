from numpy import *
from string import *
import numbers

def main(wrt):
    if wrt == "n" or wrt == "N":
        name = ""
    matrix = []
    matrix_nbr = n = int(input("Combien de matrice avez-vous ?\n"))
    bouclage = True
    while bouclage == True:
        while n !=0 :
            recup_matrix(matrix)
            print("{} : {}\n".format((matrix_nbr-n+1), (matrix[matrix_nbr-n])))
            if wrt == 'o' or wrt == 'O':
                name = (str(input("Comment s'appelle la matrice ?")))
                name = ("{} :\n {}\n".format(name, array(matrix[matrix_nbr-n])))
                write_txt(wrt, name)
            n -= 1
        matrice = []
        calcul(matrix, matrice, wrt, name)




def calcul(matrix, matrice, wrt, name):
    prenumber = []
    calc = []
    calcul = str(input("Veuillez noter votre calcul de la sorte : 2 (1) + 5 (2)"))
    recup_calcul(calc, matrice, prenumber, calcul)
    multi_prenum(prenumber, matrice, matrix)
    y = len(calc)
    while y != 0:
        if calc[y - 1] == 'inv':
            inv_calc(calc, y, matrice)
            y -= 1
        else:
            y -= 1
    if len(calc) == len(matrice):
        first_calc(matrice, calc)
        calc_chaine(calc, matrice, wrt, matrix, name)
        print(matrice[0])
        error = False
    elif len(calc) == (len(matrice) - 1):
        calc_chaine(calc, matrice, wrt, matrix, name)
        print(matrice[0])
        error = False
    else:
        print("probleme de calcul")
        error = True
    select_menu(wrt, matrix, matrice, error, name)

def recup_matrix(matrix):
    chaine = str(input("Veuillez écrit la matrice de la sorte: 1,2,3 4,0,5\n"))
    caractere = ","
    caractere2 = " "
    submatrix = []
    xmatrix = []
    interne = []
    for x in chaine.split(caractere2):
        variable = x
        for x in variable.split(caractere):
            if "/" in x and "sqrt" in x:
                element = x.replace("sqrt","")
                for x in element.split("/"):
                    interne.append(x)
                    if len(interne) == 1:
                        squared(interne)
                    print(interne)
                division(interne)
                x = interne[0]
                interne = []
            elif "/" in x:
                element = x
                for x in element.split("/"):
                    if x != "/":
                        interne.append(x)
                    else:
                         x=0
                division(interne)
                x = interne[0]
                interne = []
            elif "sqrt" in x:
                element = x.replace("sqrt","")
                interne.append(element)
                squared(interne)
                x = interne[0]
                interne = []
            xmatrix.append(float(x))
        if len(submatrix) == 0 or len(submatrix[0]) == len(xmatrix):
            submatrix.append(xmatrix)
        else:
            print("Nombre de variable different d'une colonne a l'autre")
            recup_matrix(matrix)
        print(submatrix)
        xmatrix = []
    matrix.append(submatrix)
    submatrix = []


def squared(interne):
        if len(interne) == 1:
            x_ = float(interne[0])
            print(x_)
            print(sqrt(4))
            interne[0] = sqrt((x_))
            print(interne[0])
        else:
            print("Erreur nombre de valeur de mise a la racine carré")




def division(interne):
    if interne !=2:
        x_ = float(interne[0]) / float(interne[1])
        interne[0] = x_
    else:
        print("Erreur nombre de valeur de mise a la racine carré")

def recup_calcul(calc, matrice, prenumber,calcul):
    matrice_calc = ['x', '+', '-', 'inv']
    division = []
    for x in calcul.split(" "):
        print(x)
        if "/" in x:
            interne = x
            for x in interne.split("/"):
                if x != "/":
                    division.append(int(x))
                else:
                    x = 0
            print(division)
            x = (division[0] / division[1])
            prenumber.append(float(x))
            print(x)
            division = []
        else:
            if "(" in x:
                variable = x
                print(variable)
                for x in variable.strip("("):
                    variable = x
                    for x in variable.strip(")"):
                        print(x)
                        matrice.append(int(x))
                        if len(matrice) != len(prenumber):
                            prenumber.append(1)
            elif x in matrice_calc:
                calc.append((x))
                print(x)
            elif 0 < float(x) and float(x) < 999 or "-" in x and len(x) > 1:
                prenumber.append(float(x))
                print(x)
            else:
                print("tu t'es trompé")
    print(prenumber)
    print(matrice)
    print(calc)


def multi_prenum(prenumber,matrice,matrix):
    k = len(prenumber)
    while k != 0:
        matrice[(len(matrice))-(k)] = (float(prenumber[len(prenumber)-(k)])) * array(matrix[int(matrice[len(prenumber)-(k)])-1])
        k -= 1


def inv_calc(calc,y,matrice):
    matrice[(int(y/len(calc)*len(matrice)))-1] = linalg.inv(matrice[(int(y/len(calc)*len(matrice)))-1])
    del(calc[y-1])


def first_calc(matrice,calc):
    if calc[0] == '-':
        matrice[0] = (0 - matrice[0])
        del(calc[0])
    else:
        del(calc[0])
    print(matrice)

def calc_chaine(calc,matrice,wrt,matrix, name):
    y = len(calc)
    while len(matrice) != 1:
        while y != 0:
            if calc[(len(calc)-y)] == '-':
                soustraction(matrice)
                y -= 1
            elif calc[(len(calc) - 1)] == '+':
                addition(matrice)
                y -= 1
            elif calc[(len(calc) - 1)] == 'x':
                multiplication(matrice,wrt,matrix,name)
                y -= 1
            else:
                print("probleme de calcul")


def soustraction(matrice):
    matrice[0] = ((array(matrice[0])) - (array(matrice[1])))
    del(matrice[1])


def addition(matrice):
    matrice[0] = ((array(matrice[0])) + (array(matrice[1])))
    del(matrice[1])


def multiplication(matrice,wrt,matrix, name):
    try:
        matrice[0] = (dot((matrice[0]), (matrice[1])))
        del(matrice[1])
    except ValueError:
        print("La multiplication de matrice ne peut se faire que si le nombre de variable de A est égal au nombre de dimensions de B")
        error = True
        select_menu(wrt, matrix, matrice,error, name)


def recommence(matrix,matrice,name,wrt,error):
    if error == False:
        boucle =True
        while boucle == True:
            ret = str(input("Voulez-vous gardez la valeur calculer precedement? (O/N)\n"))
            if ret == 'o' or ret == 'O':
                name = str(input("Comment s'appelle cette matrice ?"))
                matrix.append(matrice[0])
                boucle = False
                name = ("{} = \n{}\n\n".format(name, matrice[0]))
                write_txt(wrt, name)
            elif ret == 'n' or ret == 'N':
                boucle =False
            else:
                print("Choix éroné veuillez recommencer")
    y = len(matrix)
    while y != 0:
        print("{}: {}\n".format((len(matrix)-y)+1, (array(matrix[(len(matrix)-y)]))))
        y -= 1
    matrice = []
    calcul(matrix, matrice, wrt, name)

def write_txt(wrt,name):
    fichier = open("matrix.txt", "a")
    if wrt == 'o' or wrt == 'O':
        fichier.write(name)


def select_menu(wrt,matrix,matrice,error,name):
        boucle = True
        while boucle == True:
            choise = int(input("Que souhaiter vous faire :\n1-Quitter\n2-Continuer\n3-Recommencer avec d'autre matrice\n"))
            if choise == 1:
                print("A la prochaine!")
                quit()
            elif choise == 2:
                boucle = False
                recommence(matrix, matrice, name, wrt, error)
            elif choise == 3:
                boucle = False
                main(wrt)
            else:
                print("Choix erroné veuillez recommencer")