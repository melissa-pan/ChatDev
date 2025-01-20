'''
This module implements a simple Tic-Tac-Toe game with a graphical user interface using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, position):
        if self.board[position] == ' ' and self.winner is None:
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.switch_player()
            return True
        return False
    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return ' ' not in self.board
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game = TicTacToeGame()
        self.buttons = []
        self.create_widgets()
    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text=' ', font='Arial 20', width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        reset_button = tk.Button(self.root, text='Reset', font='Arial 15', command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3)
    def update_button(self, position):
        self.buttons[position].config(text=self.game.current_player)
    def on_button_click(self, position):
        if self.game.make_move(position):
            self.update_button(position)
            if self.game.winner:
                self.show_winner(f"Player {self.game.winner} wins!")
            elif ' ' not in self.game.board:
                self.show_winner("It's a draw!")
    def show_winner(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()
    def reset_game(self):
        self.game.reset_game()
        for button in self.buttons:
            button.config(text=' ')
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()