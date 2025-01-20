'''
Contains the HangmanGUI class, which manages the graphical user interface for the Hangman game.
'''
import tkinter as tk
from hangman_game import HangmanGame
class HangmanGUI:
    def __init__(self):
        self.game = HangmanGame()
        self.root = tk.Tk()
        self.root.title("Hangman Game")
        self.word_label = tk.Label(self.root, text=self.game.get_display_word(), font=("Helvetica", 18))
        self.word_label.pack(pady=20)
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack(pady=10)
        self.guess_button = tk.Button(self.root, text="Guess", command=self.handle_guess)
        self.guess_button.pack(pady=10)
        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=20)
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)
    def run(self):
        self.root.mainloop()
    def update_display(self):
        self.word_label.config(text=self.game.get_display_word())
        if self.game.is_game_over():
            if self.game.is_word_guessed():
                self.message_label.config(text="Congratulations! You've won!")
            else:
                self.message_label.config(text=f"Game Over! The word was '{self.game.selected_word}'.")
            self.guess_button.config(state=tk.DISABLED)
        else:
            self.message_label.config(text=f"Attempts left: {self.game.attempts_left}")
    def handle_guess(self):
        guess = self.guess_entry.get().lower()
        if len(guess) == 1 and guess.isalpha():
            self.game.make_guess(guess)
            self.update_display()
            self.guess_entry.delete(0, tk.END)
        else:
            self.message_label.config(text="Please enter a valid single letter.")
    def reset_game(self):
        self.game.reset_game()
        self.update_display()
        self.guess_button.config(state=tk.NORMAL)
        self.message_label.config(text="")