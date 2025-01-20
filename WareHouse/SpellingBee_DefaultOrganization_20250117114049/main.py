'''
Main application file for the Spelling Bee puzzle game.
'''
import tkinter as tk
from game_logic import SpellingBeeGame
class SpellingBeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spelling Bee Puzzle")
        self.game = SpellingBeeGame()
        self.setup_gui()
    def setup_gui(self):
        # Create GUI components
        self.central_letter_label = tk.Label(self.root, text=f"Central Letter: {self.game.central_letter}")
        self.central_letter_label.pack()
        self.surrounding_letters_label = tk.Label(self.root, text=f"Surrounding Letters: {' '.join(self.game.surrounding_letters)}")
        self.surrounding_letters_label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_word)
        self.submit_button.pack()
        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack()
        self.score_label = tk.Label(self.root, text=f"Score: {self.game.score}")
        self.score_label.pack()
    def submit_word(self):
        word = self.entry.get().strip().lower()
        feedback = self.game.submit_word(word)
        self.feedback_label.config(text=feedback)
        self.score_label.config(text=f"Score: {self.game.score}")
        self.entry.delete(0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingBeeApp(root)
    root.mainloop()