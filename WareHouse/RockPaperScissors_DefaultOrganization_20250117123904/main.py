'''
main.py
'''
import tkinter as tk
from tkinter import messagebox
import random
class RockPaperScissorsGame:
    '''
    A class to represent the Rock-Paper-Scissors game with a GUI.
    '''
    def __init__(self):
        '''
        Initialize the game and set up the GUI.
        '''
        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissors Game")
        self.label = tk.Label(self.window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.label.pack(pady=10)
        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.user_choice("Rock"), width=10)
        self.rock_button.pack(pady=5)
        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.user_choice("Paper"), width=10)
        self.paper_button.pack(pady=5)
        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.user_choice("Scissors"), width=10)
        self.scissors_button.pack(pady=5)
        self.result_label = tk.Label(self.window, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)
        self.play_again_button = tk.Button(self.window, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.pack(pady=5)
        self.window.mainloop()
    def user_choice(self, choice):
        '''
        Handle the user's choice and determine the outcome.
        '''
        computer = self.computer_choice()
        result = self.determine_winner(choice, computer)
        self.update_result(result)
    def computer_choice(self):
        '''
        Randomly select Rock, Paper, or Scissors for the computer.
        '''
        return random.choice(["Rock", "Paper", "Scissors"])
    def determine_winner(self, user, computer):
        '''
        Compare choices and determine the winner.
        '''
        if user == computer:
            return f"Both chose {user}. It's a tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Scissors" and computer == "Paper") or \
             (user == "Paper" and computer == "Rock"):
            return f"You chose {user}, computer chose {computer}. You win!"
        else:
            return f"You chose {user}, computer chose {computer}. You lose!"
    def update_result(self, result):
        '''
        Update the GUI with the result of the game.
        '''
        self.result_label.config(text=result)
        self.play_again_button.config(state=tk.NORMAL)
    def play_again(self):
        '''
        Reset the game for another round.
        '''
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)
def main():
    '''
    Entry point to start the application.
    '''
    RockPaperScissorsGame()
if __name__ == "__main__":
    main()