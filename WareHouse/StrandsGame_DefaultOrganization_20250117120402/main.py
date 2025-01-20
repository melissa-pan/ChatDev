'''
Main file to initialize the Strands game and start the GUI.
'''
from strands_game import StrandsGame
from strands_gui import StrandsGUI
def main():
    # Initialize game logic
    game = StrandsGame()
    game.load_strands()
    # Initialize GUI
    gui = StrandsGUI(game)
    gui.setup_gui()
if __name__ == "__main__":
    main()