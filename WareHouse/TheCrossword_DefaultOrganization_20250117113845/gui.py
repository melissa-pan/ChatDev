'''
CrosswordGUI class to handle the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
class CrosswordGUI:
    def __init__(self, master, crossword_grid):
        self.master = master
        self.crossword_grid = crossword_grid
        self.master.title("Crossword Puzzle")
        self.create_grid()
    def create_grid(self):
        self.entries = {}
        for i in range(self.crossword_grid.size):
            for j in range(self.crossword_grid.size):
                entry = tk.Entry(self.master, width=3, justify='center')
                entry.grid(row=i, column=j)
                self.entries[(i, j)] = entry
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_word)
        self.submit_button.grid(row=self.crossword_grid.size, column=0, columnspan=self.crossword_grid.size)
    def submit_word(self):
        # Use a simple dialog to get user input
        clue_number = simpledialog.askinteger("Input", "Enter clue number:")
        direction = simpledialog.askstring("Input", "Enter direction (across/down):").strip().lower()
        word = simpledialog.askstring("Input", "Enter word:").strip()
        if clue_number is not None and direction and word:
            if self.crossword_grid.validate_word(clue_number, direction, word):
                self.update_grid(clue_number, direction, word)
                messagebox.showinfo("Success", "Correct word!")
                self.check_completion()
            else:
                messagebox.showerror("Error", "Incorrect word, try again.")
        else:
            messagebox.showerror("Error", "Invalid input, please try again.")
    def update_grid(self, clue_number, direction, word):
        start_pos = self.crossword_grid.get_word_start_position(clue_number, direction)
        if start_pos:
            row, col = start_pos
            for i, char in enumerate(word):
                if direction == 'across':
                    self.entries[(row, col + i)].delete(0, tk.END)
                    self.entries[(row, col + i)].insert(0, char)
                elif direction == 'down':
                    self.entries[(row + i, col)].delete(0, tk.END)
                    self.entries[(row + i, col)].insert(0, char)
    def check_completion(self):
        if self.crossword_grid.is_complete():
            messagebox.showinfo("Congratulations", "You have completed the crossword puzzle!")