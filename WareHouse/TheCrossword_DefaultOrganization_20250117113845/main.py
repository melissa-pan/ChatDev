'''
Main entry point for the crossword puzzle application.
'''
from crossword import CrosswordGrid
from gui import CrosswordGUI
import tkinter as tk
def main():
    # Define the crossword size and clues
    size = 5
    clues = {
        'across': {
            1: "A fruit",
            2: "A color",
        },
        'down': {
            1: "A type of vehicle",
            3: "A day of the week",
        }
    }
    answers = {
        'across': {
            1: "apple",
            2: "green",
        },
        'down': {
            1: "car",
            3: "monday",
        }
    }
    # Initialize the crossword grid
    crossword_grid = CrosswordGrid(size, clues, answers)
    # Set up the GUI
    root = tk.Tk()
    app = CrosswordGUI(root, crossword_grid)
    root.mainloop()
if __name__ == "__main__":
    main()