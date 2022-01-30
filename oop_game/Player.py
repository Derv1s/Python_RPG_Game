class Player():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.items = { }

        self.base_armor = 0
        self.base_attack = 10

        self.total_attack = 0
        self.total_armor = 0

    def updateStats(self):
        self.total_attack = self.base_attack
        self.total_armor = self.base_armor
        for key in self.items.keys():
            item = self.items[key]
            self.total_attack += item.attack()
            self.total_armor += item.armor()
    
    def attackValue(self):
        return self._value(self.base_attack, self.items, "attack")

    def armorValue(self):
        return self._value(self.base_armor, self.items, "armor")

    def _value(self, base, items, _type):
        total = base
        for key in items.keys():
            item = items[key]
            total += item.attributes[_type]()
        return total

    def wear(self, item):
        self.items[item.type()] = item
        self.updateStats()
    
    def unwear(self, _type):
        del self.items[_type]
        self.updateStats()

    def attack(self, target):
        target.attacked(self)

    def attacked(self, enemy):
        enemyAttack = enemy.attackValue()
        damage = max(enemyAttack - self.armorValue(), 0)
        self.hp = max(self.hp - damage, 0)

    def isAlive(self):
        return self.hp > 0

    def isDead(self):
        return not self.isAlive()
    
    def act(self, field):
        pass

    def info(self):
        print(f"    name: {self.name} HP: {self.hp}")