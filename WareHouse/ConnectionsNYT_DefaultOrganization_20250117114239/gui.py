'''
Graphical User Interface for the NYT Connections-style puzzle game using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from game import Game
class GameGUI:
    def __init__(self):
        self.game = Game()
        self.root = tk.Tk()
        self.root.title("NYT Connections Puzzle Game")
        self.selected_words = []
        self.create_widgets()
    def create_widgets(self):
        # Create buttons for each word
        self.buttons = {}
        for word in self.game.words:
            button = tk.Button(self.root, text=word, command=lambda w=word: self.on_word_select(w))
            button.pack(side=tk.LEFT)
            self.buttons[word] = button
        # Create a label to display the status
        self.status_label = tk.Label(self.root, text="Select words to form a group.")
        self.status_label.pack()
    def update_status(self, message):
        # Update the status label
        self.status_label.config(text=message)
    def on_word_select(self, word):
        # Handle word selection
        if word in self.selected_words:
            self.selected_words.remove(word)
            self.buttons[word].config(relief=tk.RAISED)
        else:
            self.selected_words.append(word)
            self.buttons[word].config(relief=tk.SUNKEN)
        if len(self.selected_words) == 4:
            self.game.tries += 1
            valid, category = self.game.check_group(self.selected_words)
            if valid:
                messagebox.showinfo("Correct!", f"You found the {category} category!")
                for word in self.selected_words:
                    self.buttons[word].config(state=tk.DISABLED)
            else:
                messagebox.showerror("Incorrect", "This is not a valid group.")
            self.selected_words.clear()
            self.update_status(f"Tries: {self.game.tries}/{self.game.max_tries}")
            if self.game.is_game_over():
                if len(self.game.found_categories) == len(self.game.categories):
                    messagebox.showinfo("Game Over", "Congratulations! You found all categories!")
                else:
                    messagebox.showinfo("Game Over", "You've run out of tries. Better luck next time!")
                self.root.quit()
    def run(self):
        # Run the main loop
        self.root.mainloop()