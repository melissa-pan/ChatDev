'''
Defines the SudokuSolver class to solve the Sudoku puzzle.
'''
class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self.grid.is_valid(row, col, num):
                self.grid.set_value(row, col, num)
                if self.solve():
                    return True
                self.grid.set_value(row, col, 0)
        return False
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid.grid[i][j] == 0:
                    return (i, j)
        return None