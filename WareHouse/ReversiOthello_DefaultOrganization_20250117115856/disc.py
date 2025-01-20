'''
Represents a disc on the board with a color and position.
'''
import pygame
class Disc:
    def __init__(self, color):
        self.color = color
    def draw(self, screen, x, y):
        color = (0, 0, 0) if self.color == 'black' else (255, 255, 255)
        pygame.draw.circle(screen, color, (x + 50, y + 50), 40)