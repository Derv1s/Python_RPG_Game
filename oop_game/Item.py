class Item():
    def __init__(self, name, armor, attack):
        self.name = name
        self.armor = armor
        self.attack = attack
    
    def attack(self):
        return self.attack

    def armor(self):
        return self.armor