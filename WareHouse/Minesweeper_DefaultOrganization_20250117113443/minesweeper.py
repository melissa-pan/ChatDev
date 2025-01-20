'''
This module contains the MinesweeperGame class, which handles the game logic for Minesweeper.
'''
import random
class MinesweeperGame:
    def __init__(self, rows=9, cols=9, mines=10):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self.uncovered = set()
        self.place_mines()
        self.calculate_adjacent_mines()
    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r, c) not in self.mine_positions:
                self.mine_positions.add((r, c))
                self.board[r][c] = -1
    def calculate_adjacent_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols and self.board[nr][nc] == -1:
                            count += 1
                self.board[r][c] = count
    def uncover_cell(self, r, c, gui):
        if (r, c) in self.uncovered:
            return True
        if (r, c) in self.mine_positions:
            return False  # Indicate that a mine was uncovered
        self.uncovered.add((r, c))
        gui.update_display()  # Update the display after uncovering the cell
        if self.board[r][c] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        self.uncover_cell(nr, nc, gui)
        return True
    def check_win(self):
        return len(self.uncovered) == self.rows * self.cols - self.mines