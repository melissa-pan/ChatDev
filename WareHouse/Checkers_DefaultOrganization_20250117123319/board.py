'''
Board class to manage the checkers board and pieces.
'''
import pygame
from piece import Piece
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_pieces()
    def initialize_pieces(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('black', (row, col))
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('red', (row, col))
    def draw(self, screen):
        for row in range(8):
            for col in range(8):
                color = (209, 139, 71) if (row + col) % 2 == 0 else (255, 206, 158)
                pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))
                piece = self.grid[row][col]
                if piece:
                    piece.draw(screen)
    def move_piece(self, start_pos, end_pos):
        piece = self.grid[start_pos[0]][start_pos[1]]
        self.grid[end_pos[0]][end_pos[1]] = piece
        self.grid[start_pos[0]][start_pos[1]] = None
        piece.position = end_pos
        self.king_piece(end_pos)
    def capture_piece(self, pos):
        self.grid[pos[0]][pos[1]] = None
    def king_piece(self, pos):
        piece = self.grid[pos[0]][pos[1]]
        if piece and ((piece.color == 'red' and pos[0] == 0) or (piece.color == 'black' and pos[0] == 7)):
            piece.king = True