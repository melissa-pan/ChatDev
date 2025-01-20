'''
Main entry point for the NYT Connections-style puzzle game.
'''
from gui import GameGUI
def main():
    # Initialize and run the game GUI
    game_gui = GameGUI()
    game_gui.run()
if __name__ == "__main__":
    main()