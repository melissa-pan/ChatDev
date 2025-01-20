'''
Game class that manages the game loop and transitions between narrative segments.
'''
from narrative_segment import NarrativeSegment
from game_state import GameState
from gui import GUI
class Game:
    def __init__(self):
        self.state = GameState()
        self.gui = GUI(self.make_choice)
    def start_game(self):
        # Initialize the first narrative segment
        first_segment = NarrativeSegment("Welcome to the adventure!", ["Start"])
        self.state.current_segment = first_segment
        self.gui.update_display(first_segment.text, first_segment.get_choices())
        self.gui.start_gui()  # Start the GUI main loop here
    def make_choice(self, choice):
        # Update the game state based on the player's choice
        self.state.update_state(choice)
        current_segment = self.state.get_current_segment()
        self.gui.update_display(current_segment.display(), current_segment.get_choices())