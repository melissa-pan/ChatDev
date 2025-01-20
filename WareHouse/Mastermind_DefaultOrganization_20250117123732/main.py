'''
Main entry point for the Mastermind game application.
'''
from gui import MastermindGUI
def main():
    '''
    Initializes and runs the Mastermind game with a GUI.
    '''
    game_gui = MastermindGUI()
    game_gui.setup_gui()
if __name__ == "__main__":
    main()