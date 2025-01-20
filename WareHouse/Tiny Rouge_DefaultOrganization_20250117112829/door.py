'''
Defines the Door class for the roguelike game.
'''
class Door:
    def __init__(self):
        self.is_open = False
    def open(self):
        self.is_open = True
        print("The door is now open.")
    def interact(self, player, game):
        if not self.is_open:
            self.open()
            print("Player can now proceed to the next level.")
            game.next_level()