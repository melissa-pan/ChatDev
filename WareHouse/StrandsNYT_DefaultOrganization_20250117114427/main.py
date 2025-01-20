'''
Main application file for the NYT Strands puzzle game.
'''
import tkinter as tk
from word_segment import WordSegment
from game_logic import GameLogic
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NYT Strands Puzzle")
        self.segments = []
        self.selected_segments = []
        self.setup_ui()
        self.start_game()
        self.root.mainloop()
    def setup_ui(self):
        self.segment_frame = tk.Frame(self.root)
        self.segment_frame.pack(pady=20)
        self.check_button = tk.Button(self.root, text="Check Solution", command=self.check_solution)
        self.check_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
    def start_game(self):
        # Example word segments
        words = ["py", "thon", "pro", "gram", "ming"]
        self.segments = [WordSegment(word) for word in words]
        for segment in self.segments:
            button = tk.Button(self.segment_frame, text=segment.get_text(), command=lambda s=segment: self.select_segment(s))
            button.pack(side=tk.LEFT, padx=5)
    def select_segment(self, segment):
        if segment not in self.selected_segments:
            self.selected_segments.append(segment)
    def check_solution(self):
        game_logic = GameLogic(self.selected_segments)  # Pass selected segments
        if game_logic.is_valid_solution():
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text="Try Again!")
        self.selected_segments.clear()
if __name__ == "__main__":
    app = MainApp()