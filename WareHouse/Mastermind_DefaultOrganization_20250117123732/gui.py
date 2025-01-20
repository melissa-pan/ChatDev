'''
Contains the MastermindGUI class which handles the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
from game_logic import MastermindGame
class MastermindGUI:
    '''
    Manages the graphical user interface for the Mastermind game.
    '''
    def __init__(self):
        self.game = MastermindGame()
        self.root = tk.Tk()
        self.root.title("Mastermind Game")
        self.guess_entries = []
        self.feedback_labels = []
        self.setup_gui()
    def setup_gui(self):
        '''
        Initializes the GUI components.
        '''
        tk.Label(self.root, text="Enter your guess:").grid(row=0, column=0, columnspan=4)
        for i in range(4):
            entry = tk.Entry(self.root, width=10)
            entry.grid(row=1, column=i)
            self.guess_entries.append(entry)
        submit_button = tk.Button(self.root, text="Submit Guess", command=self.submit_guess)
        submit_button.grid(row=2, column=0, columnspan=4)
        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.grid(row=3, column=0, columnspan=4)
        self.root.mainloop()
    def submit_guess(self):
        '''
        Handles the event when the player submits a guess.
        '''
        guess = [entry.get() for entry in self.guess_entries]
        if len(guess) != 4 or not all(color in self.game.colors for color in guess):
            messagebox.showerror("Invalid Guess", "Please enter a valid guess with 4 colors.")
            return
        self.game.attempts += 1
        correct_position, correct_color = self.game.check_guess(guess)
        self.feedback_label.config(text=f"Correct Position: {correct_position}, Correct Color: {correct_color}")
        if correct_position == 4:
            messagebox.showinfo("Congratulations!", "You've guessed the correct code!")
            self.root.quit()
        elif self.game.attempts >= self.game.max_attempts:
            messagebox.showinfo("Game Over", f"You've used all attempts! The correct code was: {self.game.secret_code}")
            self.root.quit()