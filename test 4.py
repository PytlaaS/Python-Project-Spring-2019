from random import choices


def main():
    print("Bienvenue au Jeu du juste prix, vou connaisez le concept")
    print("Choisissez un chiffre compris entre 0 et 1000")
    print("Une fois que Gustave aura choisie, vous pourrez essayer de trouver le meme que lui")
    number = list(range(0, 1001))
    Gustav = choices(number)
    Gustave = Gustav[0]
    print("Gustave a fais son choix a ton tour")
    trying = 1
    Pedro = int(input("C'est a toi de choisir, que choisis tu ?"))
    if Pedro == Gustave:
        print("Bravo Pedro El Chico tu est le maitre de ce jeu")
    else:
        while Pedro != Gustave:
            print("Ouhh Pas loiiin")
            if Pedro < Gustave:
                print("C'est plus mon Garcon")
            else:
                print("C'est moins mon Garcon")
            trying += 1
            Pedro = int(input("Alors tu dirais quoi cette fois ci?"))
        print("Bravo Pedro tu sais maintenant combien de briques il te faut pour ériger ton mur")
    print("Tu as effectué {} essaies avant d'arrivé au juste prix".format(trying))
    yo = trying
    x = 1
    t = 1000
    k = 0.999
    while yo != 0:
        if yo > 1:
            yo = yo - 1
            x = x * k
            t = t - 1
            k = (1 - (1 / t))
        else:
            yo = yo - 1
            x = x * (1 - k)
    x = x * 100
    print("Tu avais " + str(x) + " % de chance de trouver en {} essais.".format(trying))


if __name__ == '__main__':
    main()
