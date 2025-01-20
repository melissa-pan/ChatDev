'''
Defines the SudokuGrid class to manage the Sudoku grid.
'''
class SudokuGrid:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]
    def set_value(self, row, col, value):
        self.grid[row][col] = value
    def is_valid(self, row, col, value):
        # Check row
        if value in self.grid[row]:
            return False
        # Check column
        if value in [self.grid[i][col] for i in range(9)]:
            return False
        # Check 3x3 subgrid
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.grid[i][j] == value:
                    return False
        return True
    def is_complete(self):
        for row in self.grid:
            if 0 in row:
                return False
        return True