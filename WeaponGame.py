class Weapon:

    def __init__(self,name,attack,speed):
        self.name=name
        self.attack=attack
        self.speed=speed

    def get_name(self):
        return self.name

    def get_attack(self):
        return self.attack

    def get_speed(self):
        return self.speed