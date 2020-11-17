from GameTest.ClassGame import Player
from GameTest.WeaponGame import Weapon
from random import shuffle


def main():
    pseudo_players=[]
    challengers="Y"
    x=0
    while challengers=="Y" or challengers=="y" or x<2:
        pseudo=str(input("Bienvenue cher joueur, Quel es votre pseudo?"))
        pseudo_players.append(pseudo)
        x+=1
        if x>=2:
            challengers=str(input("Y a t'il un autre joueur ?Y/N"))
    print("Les joueurs participant sont donc {}".format(pseudo_players))
    number_players=len(pseudo_players)
    x=0
    n=0
    player=[]
    Masse= Weapon("Hammer",10,3)
    Epee= Weapon("Sword",7,2)
    Dague= Weapon("Knife",3,1)
    while number_players !=0:
        player.append(Player(str(pseudo_players[(number_players)-1]),30,0,0))
        print("Player",str(n)," votre pseudo est ",player[n].get_pseudo()," et vous avez {} point de vie ".format(player[n].get_health()))
        print("Les armes proposé sont:")
        print("La Masse d'attack 10 et de délais 3 tours")
        print("La Dague d'attack 3 et de délais 1 tours")
        print("L'Eppée d'attack 7 et de délais 2 tours")
        cond =0
        while cond == 0:
            reply = str(input("Veuillez choisir une de ses armes(Eppée/Masse/Dague)"))
            if reply == "Epée":
                cond=1
                player[n] = Player(str(pseudo_players[((number_players) - 1)]), 30, 7, 2)
                print("Vous avez choisi l'Epee")
            elif reply == "Masse":
                cond=1
                player[n] = Player(str(pseudo_players[((number_players) - 1)]), 30, 10, 3)
                print("Vous avez choisi la Masse")
            elif reply == "Dague":
                cond=1
                player[n] = Player(str(pseudo_players[((number_players) - 1)]), 30, 3, 1)
                print("Vous avez choisi la Dague")
            else:
                print("Veuilleez reilterer votre demande")
        x+=1
        n+=1
        number_players-=1
        y=0
    while x!= 0:
        print("Voici le joueur :{}".format(player[(x-1)].get_pseudo()))
        print("Avec une vie de {}".format(player[(x - 1)].get_health()))
        print("Avec une attack de {}".format(player[(x - 1)].get_attack()))
        print("Avec une reaction de {} tours".format(player[(x - 1)].get_speed()))
        x-=1
        y+=1
    print ("Je vais maintenant mellangé pour en deduire un ordre de jeu")
    shuffle (player)
    k=1
    attente = []
    while (y+1)!=k:
        print("Voici le joueur"+ str(k)+" :{}".format(player[(k - 1)].get_pseudo()))
        attente.append(int(player[(k-1)].get_speed()))
        k+=1
    supress=0
    k=k-1
    print (str(k)+str(supress))
    while supress!=(k-1):
        x=1
        while x<= (k-supress):
            bouclage=0
            if (int(player[(x - 1)].get_speed())) != 1 and attente[(x-1)] != 1:
                print ((player[(x-1)].get_pseudo())," il vous reste {} tours a attendre".format(attente[(x-1)]-1))
                if attente[(x-1)] == (int(player[(x - 1)].get_speed())):
                    attente[(x - 1)] = (int(player[(x - 1)].get_speed()) - 1)
                    x+=1
                else:
                    attente[(x-1)]-=1
                    print((player[(x - 1)].get_pseudo()), " il vous reste {} tours a attendre".format(attente[(x-1)]-1))
                    x+=1
            else:
                while bouclage ==0:
                    m=(k-supress)
                    while m != 0 :
                        print ("Le joueur "+ str(m)+ "est {}.".format(player[(m-1)].get_pseudo()))
                        m-=1
                    choix=int(input("Joueur "+str(x)+" qui souhaitez vous attaquez?n°Joueur"))
                    if choix<1 or choix > (k-supress) or choix == x :
                        print("Veuilleez reilterer votre demande")
                    else:
                        bouclage=1
                        player[(x-1)].attack_player(player[(choix-1)])
                        print("Vous avez choisis d'attaqué {}".format(player[(choix - 1)].get_pseudo()))
                        print("Il lui reste {} point de vie".format(player[(choix - 1)].get_health()))
                        if int(player[(choix - 1)].get_health()) <=0:
                            print("Le joueur {} est éliminé".format(player[(choix - 1)].get_pseudo()))
                            supress+=1
                            if int(player[(x - 1)].get_speed()) != attente[(x-1)]:
                                attente[(x - 1)] = int(player[(x - 1)].get_speed())
                                del player[(choix - 1)]
                                del attente[(choix - 1)]
                            else:
                                del player[(choix - 1)]
                                del attente[(choix - 1)]
                        else:
                            if int(player[(x - 1)].get_speed()) != attente[(x-1)]:
                                attente[(x-1)]= int(player[(x - 1)].get_speed())
                                x += 1
                            else:
                                x+=1
    print("Bravo {} vous avais gagné".format(player[0].get_pseudo()))


if __name__ == '__main__':
    main()