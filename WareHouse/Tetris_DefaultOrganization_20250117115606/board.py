'''
Board class represents the Tetris board and handles line clearing and tetromino placement.
'''
import pygame
from constants import *
class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.score = 0
    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for i in lines_to_clear:
            del self.grid[i]
            self.grid.insert(0, [0 for _ in range(COLS)])
            self.score += 100
    def can_place(self, shape, offset):
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if x + off_x < 0 or x + off_x >= COLS or y + off_y >= ROWS:
                        return False
                    if self.grid[y + off_y][x + off_x]:
                        return False
        return True
    def place_tetromino(self, tetromino):
        shape = tetromino.shape
        offset = tetromino.position
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[y + offset[1]][x + offset[0]] = tetromino.color
    def draw(self, surface):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(surface, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))