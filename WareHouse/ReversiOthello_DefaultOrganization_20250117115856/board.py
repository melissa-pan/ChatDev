'''
Manages the board state and handles drawing and updating the board.
'''
import pygame
from disc import Disc
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.reset()
    def reset(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.grid[3][3] = Disc('white')
        self.grid[3][4] = Disc('black')
        self.grid[4][3] = Disc('black')
        self.grid[4][4] = Disc('white')
    def draw(self, screen):
        for row in range(8):
            for col in range(8):
                pygame.draw.rect(screen, (0, 0, 0), (col * 100, row * 100, 100, 100), 1)
                if self.grid[row][col] is not None:
                    self.grid[row][col].draw(screen, col * 100, row * 100)
    def is_valid_move(self, row, col, color):
        if self.grid[row][col] is not None:
            return False
        opponent_color = 'white' if color == 'black' else 'black'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            has_opponent_disc = False
            while 0 <= r < 8 and 0 <= c < 8 and self.grid[r][c] is not None:
                if self.grid[r][c].color == opponent_color:
                    has_opponent_disc = True
                elif self.grid[r][c].color == color:
                    if has_opponent_disc:
                        return True
                    break
                r += dr
                c += dc
        return False
    def make_move(self, row, col, color):
        if not self.is_valid_move(row, col, color):
            return
        self.grid[row][col] = Disc(color)
        opponent_color = 'white' if color == 'black' else 'black'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            discs_to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.grid[r][c] is not None:
                if self.grid[r][c].color == opponent_color:
                    discs_to_flip.append((r, c))
                elif self.grid[r][c].color == color:
                    for rr, cc in discs_to_flip:
                        self.grid[rr][cc].color = color
                    break
                r += dr
                c += dc
    def get_valid_moves(self, color):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col, color):
                    valid_moves.append((row, col))
        return valid_moves
    def is_board_full(self):
        for row in self.grid:
            for cell in row:
                if cell is None:
                    return False
        return True