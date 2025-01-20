'''
Board class manages the game board state and operations.
'''
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
    def place_piece(self, x, y, player):
        if self.grid[y][x] == '':
            self.grid[y][x] = player
            return True
        return False
    def is_full(self):
        return all(all(cell != '' for cell in row) for row in self.grid)
    def print_board(self):
        for row in self.grid:
            print(' '.join(cell if cell != '' else '.' for cell in row))