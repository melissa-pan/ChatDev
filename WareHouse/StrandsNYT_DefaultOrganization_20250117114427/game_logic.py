'''
Contains the GameLogic class for managing the logic of the NYT Strands puzzle game.
'''
class GameLogic:
    def __init__(self, selected_segments):
        self.selected_segments = selected_segments
        # Example list of valid solutions
        self.valid_solutions = {"python", "programming", "pythonprogramming"}
    def is_valid_solution(self):
        selected_text = "".join(segment.get_text() for segment in self.selected_segments)
        return selected_text in self.valid_solutions