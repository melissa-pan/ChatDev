'''
Main file to run the Connect Four game with a GUI using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class ConnectFourGame:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'Red'
    def make_move(self, column):
        for row in reversed(range(self.rows)):
            if self.board[row][column] is None:
                self.board[row][column] = self.current_player
                if self.check_winner(row, column):
                    return 'win'
                if self.check_draw():
                    return 'draw'
                self.current_player = 'Yellow' if self.current_player == 'Red' else 'Red'
                return 'continue'
        return 'invalid'
    def check_winner(self, row, column):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 4):
                r, c = row + dr*i, column + dc*i
                if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            for i in range(1, 4):
                r, c = row - dr*i, column - dc*i
                if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False
    def check_draw(self):
        return all(self.board[0][col] is not None for col in range(self.columns))
    def reset_game(self):
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'Red'
class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.game = ConnectFourGame()
        self.buttons = [tk.Button(root, text=f"Column {i+1}", command=lambda i=i: self.handle_click(i)) for i in range(self.game.columns)]
        for i, button in enumerate(self.buttons):
            button.grid(row=0, column=i)
        self.labels = [[tk.Label(root, text=" ", width=10, height=5, bg="white", relief="ridge") for _ in range(self.game.columns)] for _ in range(self.game.rows)]
        for r in range(self.game.rows):
            for c in range(self.game.columns):
                self.labels[r][c].grid(row=r+1, column=c)
    def update_board(self):
        for r in range(self.game.rows):
            for c in range(self.game.columns):
                color = self.game.board[r][c]
                self.labels[r][c].config(bg=color if color else "white")
    def handle_click(self, column):
        result = self.game.make_move(column)
        self.update_board()
        if result == 'win':
            self.show_winner()
        elif result == 'draw':
            self.show_draw()
    def show_winner(self):
        messagebox.showinfo("Game Over", f"{self.game.current_player} wins!")
        self.game.reset_game()
        self.update_board()
    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.game.reset_game()
        self.update_board()
if __name__ == "__main__":
    root = tk.Tk()
    gui = ConnectFourGUI(root)
    root.mainloop()