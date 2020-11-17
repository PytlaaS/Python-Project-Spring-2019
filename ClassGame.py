class Player:

    def __init__(self,pseudo,health,attack,speed):
        self.pseudo=pseudo
        self.health=health
        self.attack=attack
        self.speed=speed

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_speed(self):
        return self.speed

    def attack_player(self,target_player):
        target_player.damage(self.attack)

    def damage(self, damage):
        self.health -= damage