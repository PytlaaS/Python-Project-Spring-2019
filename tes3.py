from random import shuffle


def main():
    Rebelote = 0
    print("Bienvenue,le jeu que je vais te presenter est assez simple ")
    print("Il s'agit d'un jeu de chanceux")
    print("Tu va devoir choisir une carte a partir d'un jeu de carte")
    print("Et esperer que ce sera celle qui finnira en tete du paquet")
    print("Il y aura trois tirage et a chaque tirage la premiere carte sera suprimmé")
    print("Sympa Non ?")
    while Rebelote == 0:
        Card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "AS"]
        print("Voici donc les cartes:")
        print(Card)
        Justesse = 0
        while Justesse == 0:
            Choix_Joueur = str(input("Quel carte carte choisi tu ?"))
            if Choix_Joueur in Card:
                Justesse = 1
                shuffle(Card)
                shuffle(Card)
                print(Card)
                if Choix_Joueur == Card[0]:
                    print("Il est des notres il sait deviner comme les autres")
                else:
                    del Card[0]  # .remove pour supprimer par le nom ou .pop pour del par la position
                    Card.append(Choix_Joueur)  # .extend pour plusieurs valeur
                    shuffle(Card)
                    shuffle(Card)
                    print(Card)
                    if Choix_Joueur == Card[0]:
                        print("Il est des notres il sait deviner comme les autres")
                    else:
                        del Card[0]
                        Card.append(Choix_Joueur)
                        shuffle(Card)
                        shuffle(Card)
                        print(Card)
                        if Choix_Joueur == Card[0]:
                            print("Il est des notres il sait deviner comme les autres")
                        else:
                            print("TeTeTeTTryyy Again")
                Retry = str(input("Tu te sens de la refaire ?Y/N"))
                if Retry == "Y" or Retry == "y":
                    print("Et c'est Repartie")
                else:
                    print("Bon Vent et surtout qu'il te rammene")
                    Rebelote = 1
            else:
                print("Nique ta mere")
                print("Vas-y mon petit reessaye")


if __name__ == '__main__':
    main()
