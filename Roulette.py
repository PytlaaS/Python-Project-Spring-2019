from copy import deepcopy
from random import choices
from donneeRoulette import *


pseudo = input("Quel est votre pseudo?")
print("Bien le bonjour à vous {} et bonne chance pour enrichir votre fortune actuelle..".format(pseudo))
New = True
while New == True:
    jetons = int(jetons)
    Nombre_choice = []
    Mise_choise = []
    Mise_select = {}
    type1 = True
    type2 = True
    type3 = True
    type4 = True
    type5 = True
    repeaterror = True
    while repeaterror == True:
        try:
            Type_select = int(input("Sur quoi souhaitez-vous miser ?\n"
                                    "1- Un nombre (1/37)\n"
                                    "2- Une couleurs (1/2)\n"
                                    "3- Une moitié (1/2)\n"
                                    "4- Une douzaine (1/3)\n"
                                    "5- Un Type pair/impair (1/2)\n"))

            if Type_select == 1 and type1 == True:
                Nombre_access = deepcopy(Nombre_de_la_roulette)
                retry1 = "o"
                while retry1 == "o":
                    print("La liste de nombre selectionnable est compris entre 0 et 36")
                    repeaterror1 = True
                    while repeaterror1 == True:
                        choice1 = int(input("Sur quel nombre souhaitez-vous miser ?"))
                        if choice1 not in Nombre_access:
                            print("Veuillez choisir un nombre entre 0 et 36 que vous n'avez pas selectionné avant")
                        else:
                            repeaterror1 = False
                    repeaterror1 = True
                    Nombre_access.remove(choice1)
                    while repeaterror1 == True:
                        mise1 = int(input("Il vous reste {} jetons, combien souhaitez vous miser sur le {} ?".format(jetons, choice1)))
                        if mise1 not in range(1,jetons):
                            print("Veuillez entrez une valeur de jetons valable que vous possédez")
                        else:
                            repeaterror1 = False
                    jetons -= mise1
                    Mise_select[choice1] = mise1
                    repeaterror1 = True
                    while repeaterror1 == True:
                        retry1 = input("Souhaitez-vous miser sur un autre nombre? (o/n)")
                        if retry1 != "o" and retry1 != "n":
                            print("Veuillez repondre par 'o' ou 'n' ")
                        elif retry1 == "o":
                            repeaterror1 = False
                        else:
                            type1 = False
                            while repeaterror1 == True:
                                retry = input("Souhaitez vous misez sur un autre type valeur o/n?")
                                if retry == "n":
                                    repeaterror = False
                                    repeaterror1 = False
                                elif retry != "o":
                                    print("Veuillez entrer une veleur exact (o/n)")
                                else:
                                    repeaterror1 = False


            elif Type_select == 2 and type2 == True:
                    print("Les couleurs selectionnables sont le noir est le rouge")
                    repeaterror2 = True
                    while repeaterror2 == True:
                        choice2 = str(input("Sur quel couleur souhaitez-vous miser (r/n)?"))
                        if choice2 != "n" and choice2 != "r":
                            print("Veuillez choisir une couleur entre 'r' et 'n' ")
                        else:
                            repeaterror2 = False
                    repeaterror2 = True
                    while repeaterror2 == True:
                        mise2 = int(input("Il vous reste {} jetons, combien souhaitez vous miser sur le {} ?".format(jetons, choice2)))
                        if mise2 not in range(1,jetons):
                            print("Veuillez entrez une valeur de jetons valable que vous possédez")
                        else:
                            repeaterror2 = False
                    jetons -= mise2
                    Mise_select[choice2] = mise2
                    type2 = False
                    repeaterror2 = True
                    while repeaterror2 == True:
                        retry = input("Souhaitez vous misez sur un autre type valeur o/n?")
                        if retry == "n":
                            repeaterror = False
                            repeaterror2 = False
                        elif retry != "o":
                            print("Veuillez entrer une veleur exact (o/n)")
                        else:
                            repeaterror2 = False


            elif Type_select == 3 and type3 == True:
                print("Les demis selectionnables sont de 0 à 18 et 19 à 36")
                repeaterror3 = True
                while repeaterror3 == True:
                    choice3 =("d"+ str(int(input("Sur quel partie souhaitez-vous miser (1/2)?"))))
                    if choice3 != "d1" and choice3 != "d2":
                        print("Veuillez choisir une demi entre '1' et '2' ")
                    else:
                        repeaterror3 = False
                repeaterror3 = True
                while repeaterror3 == True:
                    mise3 = int(input("Il vous reste {} jetons, combien souhaitez vous miser sur le {} ?".format(jetons, choice3)))
                    if mise3 not in range(1, jetons):
                        print("Veuillez entrez une valeur de jetons valable que vous possédez")
                    else:
                        repeaterror3 = False
                jetons -= mise3
                Mise_select[choice3] = mise3
                type3 = False
                repeaterror3 = True
                while repeaterror3 == True:
                    retry = input("Souhaitez vous misez sur un autre type valeur o/n?")
                    if retry == "n":
                        repeaterror = False
                        repeaterror3 = False
                    elif retry != "o":
                        print("Veuillez entrer une veleur exact (o/n)")
                    else:
                        repeaterror3 = False


            elif Type_select == 4 and type4 == True:
                print("Les tiers selectionnables sont de 0 à 12 , 12 à 24 et 25 à 36")
                repeaterror4 = True
                while repeaterror4 == True:
                    choice4 =("t"+ str((int(input("Sur quel partie souhaitez-vous miser (1/2/3)?")))))
                    if choice4 != "t1" and choice4 != "t2" and choice4 != "t3":
                        print("Veuillez choisir une demi entre '1' , '2' et '3'")
                    else:
                        repeaterror4 = False
                repeaterror4 = True
                while repeaterror4 == True:
                    mise4 = int(input("Il vous reste {} jetons, combien souhaitez vous miser sur le {} ?".format(jetons, choice4)))
                    if mise4 not in range(1, jetons):
                        print("Veuillez entrez une valeur de jetons valable que vous possédez")
                    else:
                        repeaterror4 = False
                jetons -= mise4
                Mise_select[choice4] = mise4
                type4 = False
                repeaterror4 = True
                while repeaterror4 == True:
                    retry = input("Souhaitez vous misez sur un autre type valeur o/n?")
                    if retry == "n":
                        repeaterror = False
                        repeaterror4 = False
                    elif retry != "o":
                        print("Veuillez entrer une veleur exact (o/n)")
                    else:
                        repeaterror4 = False


            elif Type_select == 5 and type5 == True:
                print("Les parité selectionnables sont paire et impaire")
                repeaterror5 = True
                while repeaterror5 == True:
                    choice5 = str(input("Sur quel partie souhaitez-vous miser (i/p)?"))
                    if choice5 != "i" and choice5 != "p":
                        print("Veuillez choisir une parité entre 'i' et 'p' ")
                    else:
                        repeaterror5 = False
                repeaterror5 = True
                while repeaterror5 == True:
                    mise5 = int(input("Il vous reste {} jetons, combien souhaitez vous miser sur le {} ?".format(jetons, choice5)))
                    if mise5 not in range(1, jetons):
                        print("Veuillez entrez une valeur de jetons valable que vous possédez")
                    else:
                        repeaterror5 = False
                jetons -= mise5
                Mise_select[choice5] = mise5
                type5 = False
                repeaterror5 = True
                while repeaterror5 == True:
                    retry = input("Souhaitez vous misez sur un autre type valeur o/n?")
                    if retry == "n":
                        repeaterror = False
                        repeaterror5 = False
                    elif retry != "o":
                        print("Veuillez entrer une veleur exact (o/n)")
                    else:
                        repeaterror5 = False

            else:
                print("Veuillez choisir une valeur valable et non utiliser(1-5)")
        except ValueError:
            print(" Veuillez entrer un chiffre")
            continue

    for k,v in Mise_select.items():
        if k in range(0,36):
            Nombre_choice.append(k)
            Mise_choise.append(v)
        elif "d" in k:
            v = [float(v / 18)]
            v = (v * 18)
            if k == "d1":
                Nombre_choice += Nombre_4
                Mise_choise += v
            elif k == "d2":
                Nombre_choice += Nombre_5
                Mise_choise += v

        elif "t" in k:
            v = [float(v / 12)]
            v = (v * 12)
            if k == "t1":
                Nombre_choice += Nombre_1
                Mise_choise += v
            if k == "t2":
                Nombre_choice += Nombre_2
                Mise_choise += v
            if k == "t3":
                Nombre_choice += Nombre_3
                Mise_choise += v

        elif "i" in k or "p" in k:
            v = [float(v / 18)]
            v = (v * 18)
            if k == "i":
                Nombre_choice += Nombre_impair
                Mise_choise += v
            elif k == "p":
                Nombre_choice += Nombre_pair
                Mise_choise += v

        elif "r" in k or "n" in k:
            v = [float(v/18)]
            v = (v*18)
            if k == "r":
                Nombre_choice += Nombre_rouge
                Mise_choise += v
            elif k == "n":
                Nombre_choice += Nombre_noir
                Mise_choise += v

    print(Nombre_choice)
    print(Mise_choise)
    select_nombre = choices(Nombre_de_la_roulette)
    print(select_nombre)
    if select_nombre[0] in Nombre_choice:
        for k,v in enumerate(Nombre_choice):
            if v == select_nombre[0]:
                add_jetons = Mise_choise[k]*36
                jetons += add_jetons
    print("Vous avez maintenant {} jetons".format(jetons))
    repeaterrorf = True
    while repeaterrorf == True:
        recommencer = input("Souhaitez vous retenté votre chance (o/n)")
        if recommencer == "o":
            repeaterrorf = False
        elif recommencer == "n":
            repeaterrorf = False
            New = False
            print("à la prochaine!")
        else:
            print("Veuillez entrez une valeur correste (o/n)")