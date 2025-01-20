'''
Defines the Paddle class for the Pong game, which represents a player's paddle.
'''
import pygame
# Constants
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 120
PADDLE_SPEED = 5
SCREEN_HEIGHT = 600
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PADDLE_SPEED
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)