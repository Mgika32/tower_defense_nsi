
class Player:
    def __init__(self):
        self.vie = 100
        self.ig_money = 200
        self.gasha_money = 0
        self.in_life = True
    
    def take_damage(self, enemy):
        self.vie -= enemy.damage
    
    def set_money(self, enemy):
        self.ig_money += enemy.give_money
    