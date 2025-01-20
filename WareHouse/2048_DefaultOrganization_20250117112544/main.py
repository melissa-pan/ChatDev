'''
Main file to run the 2048 game with a 10x10 grid using tkinter for GUI.
'''
from game2048 import Game2048
from gamegui import GameGUI
def main():
    # Initialize the game logic with a 10x10 grid
    game = Game2048(size=10)
    # Initialize the GUI with the game logic
    gui = GameGUI(game)
    # Start the GUI main loop
    gui.run()
if __name__ == "__main__":
    main()