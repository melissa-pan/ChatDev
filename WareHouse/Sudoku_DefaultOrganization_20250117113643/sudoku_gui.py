'''
Defines the SudokuGUI class to manage the GUI for the Sudoku application.
'''
import tkinter as tk
from tkinter import messagebox
from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver
class SudokuGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku Solver/Creator")
        self.grid = SudokuGrid()
        self.entries = [[None] * 9 for _ in range(9)]
        self.create_grid()
    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j] = entry
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=3)
        check_button = tk.Button(self.root, text="Check", command=self.check_solution)
        check_button.grid(row=9, column=3, columnspan=3)
        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid)
        clear_button.grid(row=9, column=6, columnspan=3)
    def input_value(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit() and 1 <= int(value) <= 9:
                    if self.grid.is_valid(i, j, int(value)):
                        self.grid.set_value(i, j, int(value))
                    else:
                        self.show_message(f"Invalid input at row {i+1}, column {j+1}.")
                        self.entries[i][j].delete(0, tk.END)
                else:
                    self.grid.set_value(i, j, 0)
    def solve(self):
        self.input_value()
        solver = SudokuSolver(self.grid)
        if solver.solve():
            self.update_grid()
        else:
            self.show_message("No solution exists!")
    def check_solution(self):
        self.input_value()
        if self.grid.is_complete():
            self.show_message("Congratulations! You have completed the puzzle.")
        else:
            self.show_message("The puzzle is not complete or contains errors.")
    def update_grid(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.grid.grid[i][j]))
    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.grid.set_value(i, j, 0)
    def show_message(self, message):
        messagebox.showinfo("Sudoku", message)
    def run(self):
        self.root.mainloop()