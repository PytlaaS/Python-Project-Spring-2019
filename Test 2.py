def main() :
    print("Bonjour Mr/Mme et Bienvenue au Cinema CaBraBra")
    total=0
    Nbre_Visiteur= int(input("Combien de place souhaitez-vous?"))
    while Nbre_Visiteur >0:
        Age_visiteur = int(input("Quel age avait vous?"))
        if Age_visiteur < 18 :
            total=total+7
        else:
            total=total+12
        Etape_2 = 1
        while Etape_2 >0:
            pop_corn= str(input ("Souhaitez vous du popcorn en accompagnement ? Y/N"))
            if pop_corn == "Y" or pop_corn == "y":
                total=total+5
                Etape_2=0
            elif pop_corn == "N" or pop_corn == "n":
                total=total
                Etape_2=0
            else :
                print("Je n'ai pas compris votre demande, veuillez la reiltérer")
        Nbre_Visiteur=Nbre_Visiteur-1
    print("Le total de votre commande est de " + str(total) + " € ")


if __name__ == '__main__':
    main()
