'''
Defines the Treasure class for the roguelike game.
'''
import random
class Treasure:
    def __init__(self):
        self.restore_value = random.randint(20, 30)
    def restore_hp(self):
        return self.restore_value