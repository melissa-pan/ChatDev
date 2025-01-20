'''
Contains the StrandsGUI class for the graphical user interface using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class StrandsGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Strands Game")
        self.entry = None
        self.submit_button = None
        self.result_label = None
        self.available_strands_label = None
        self.formed_combinations_label = None
    def setup_gui(self):
        # Set up the main window and widgets
        self.available_strands_label = tk.Label(self.root, text="Available Strands: " + ", ".join(self.game.strands))
        self.available_strands_label.pack(pady=10)
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)
        self.formed_combinations_label = tk.Label(self.root, text="Formed Combinations: ")
        self.formed_combinations_label.pack(pady=10)
        self.root.mainloop()
    def on_submit(self):
        # Handle the event when the player submits their combination
        combination = self.entry.get()
        if self.game.check_combination(combination):
            self.result_label.config(text="Correct!")
            self.formed_combinations_label.config(text="Formed Combinations: " + ", ".join(self.game.formed_combinations))
            if self.game.is_complete():
                messagebox.showinfo("Congratulations!", "You have completed the game!")
        else:
            self.result_label.config(text="Try again!")