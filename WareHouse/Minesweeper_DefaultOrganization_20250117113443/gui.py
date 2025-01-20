'''
This module contains the MinesweeperGUI class, which handles the graphical user interface for Minesweeper.
'''
import tkinter as tk
from tkinter import messagebox
from minesweeper import MinesweeperGame
class MinesweeperGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Minesweeper")
        self.game = MinesweeperGame()
        self.buttons = [[None for _ in range(self.game.cols)] for _ in range(self.game.rows)]
        self.create_widgets()
    def create_widgets(self):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                button = tk.Button(self.master, width=3, height=1, command=lambda r=r, c=c: self.on_cell_click(r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button
    def update_display(self):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                if (r, c) in self.game.uncovered:
                    if self.game.board[r][c] == -1:
                        self.buttons[r][c].config(text='*', state='disabled')
                    else:
                        self.buttons[r][c].config(text=str(self.game.board[r][c]), state='disabled')
    def on_cell_click(self, r, c):
        if not self.game.uncover_cell(r, c, self):
            self.buttons[r][c].config(text='*', bg='red')
            self.end_game(False)
        else:
            if self.game.check_win():
                self.end_game(True)
    def end_game(self, won):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                self.buttons[r][c].config(state='disabled')
        if won:
            messagebox.showinfo("Minesweeper", "Congratulations! You won!")
        else:
            messagebox.showinfo("Minesweeper", "Game Over! You hit a mine.")