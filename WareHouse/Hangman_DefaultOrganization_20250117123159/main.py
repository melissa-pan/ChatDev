'''
Main entry point for the Hangman game application. Initializes the GUI and starts the game.
'''
from hangman_gui import HangmanGUI
def main():
    game_gui = HangmanGUI()
    game_gui.run()
if __name__ == "__main__":
    main()