
import time
from test6 import player
import keyboard


def main():
    print("Bienvenue dans l'Attaque des titans.\nIl n'en tient qu'a vous pour gagner !\n"
          "Soyer vif et la victoire sera a vous !")
    punch = 0
    players = []
    pseudo = []
    while len(pseudo) < 2:
        pseudo.append(str(input("Quel est votre nom combattant ?")))
    print("Ce combat opposera donc {} à {}".format(pseudo[0], pseudo[1]))
    n = m = 0
    while n < 2:
        players.append(player(str(pseudo[n]), 250, punch))
        print("Le combattant qui entre dans l'arene est {} et il a actuellement {} point de vie \n"
              "sortira t'il vainqueurs ?\nSeul l'avenir nous le dira\n".format((players[n].get_pseudo()),
                                                                               (players[n].get_life())))
        n += 1
        time.sleep(1)
    print("Bon maintenant les presentation faite\nPlace au combat!\n")
    while n > 1:
        print("{} c'est a toi que revient le droit de frapper".format((players[m].get_pseudo())))
        while punch <= 100:
            punch += 1
            print(punch, sep=' ', end="\r")
            if keyboard.is_pressed("ENTER"):
                break
            else:
                if punch == 100:
                    time.sleep(0.01)
                    punch = 0
                else:
                    time.sleep(0.01)
        players[m] = (player(str(players[m].get_pseudo()), (players[m].get_life()), punch))
        if m == 1:
            players[m].attack_player(players[m - 1])
            print("Vous avez infliger {} degats a {} il lui reste plus que {} point de vie".format(punch,
                                                                                                   (players[
                                                                                                        m - 1].get_pseudo()),
                                                                                                   (players[
                                                                                                        m - 1].get_life())))
            if int(players[m - 1].get_life()) < 0:
                del players[m - 1]
                n -= 1
                punch = 0
                keyboard.release("ENTER")
                time.sleep(2)
                m = 0
            else:
                punch = 0
                keyboard.release("ENTER")
                time.sleep(2)
                m = 0
        else:
            players[m].attack_player(players[m + 1])
            print("Vous avez infliger {} degats a {} il lui reste plus que {} point de vie".format(punch,
                                                                                                   (players[
                                                                                                        m + 1].get_pseudo()),
                                                                                                   (players[
                                                                                                        m + 1].get_life())))
            if int(players[m + 1].get_life()) < 0:
                del players[m + 1]
                n -= 1
                punch = 0
                keyboard.release("ENTER")
                time.sleep(2)
                m = 1
            else:
                punch = 0
                keyboard.release("ENTER")
                time.sleep(2)
                m = 1
    print("bravo {} vous avez gagner".format(players[0].get_pseudo()))


main()
