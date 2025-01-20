'''
Piece class to represent a single checkers piece.
'''
import pygame
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.king = False
    def draw(self, screen):
        x, y = self.position[1] * 100 + 50, self.position[0] * 100 + 50
        pygame.draw.circle(screen, pygame.Color(self.color), (x, y), 40)
        if self.king:
            pygame.draw.circle(screen, (255, 215, 0), (x, y), 20)