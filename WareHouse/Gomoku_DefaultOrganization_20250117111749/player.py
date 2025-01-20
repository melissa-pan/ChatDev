'''
Player class represents a player in the game.
'''
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    def get_move(self, use_gui=False):
        if use_gui:
            # GUI mode will handle moves through mouse events
            return None
        else:
            # Console input for move
            while True:
                try:
                    x, y = map(int, input(f"{self.name} ({self.symbol}), enter your move as 'x y': ").split())
                    return x, y
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space.")