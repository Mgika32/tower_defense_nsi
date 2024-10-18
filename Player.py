
class Player:
    """
    la class player
    """
    def __init__(self):
        self.vie = 100
        self.ig_money = 200
        self.gasha_money = 0
        self.in_life = True
    
    def take_damage(self, enemy):
        self.vie -= enemy.damage
    
    def set_money(self, enemy):
        '''modify the value of the miney when a enemy die'''
        self.ig_money += enemy.give_money

    def can_buy_turret(self):
        '''return a boolean if the player can buy the turret'''
        return (self.ig_money > 10)
    