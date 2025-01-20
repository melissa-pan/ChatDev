'''
Defines the Ball class for the Pong game, which represents the ball that bounces between paddles.
'''
import pygame
import random
# Constants
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
    def update(self, paddle1, paddle2, score):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Ball collision with top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y
        # Ball collision with paddles
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.speed_x = -self.speed_x
        # Ball out of bounds
        if self.rect.left <= 0:
            score.increment_player2()
            self.reset()
        elif self.rect.right >= SCREEN_WIDTH:
            score.increment_player1()
            self.reset()
    def reset(self):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        # Increase speed slightly, up to a maximum
        max_speed = 10
        self.speed_x = min(BALL_SPEED_X + random.uniform(0, 1), max_speed) * random.choice([-1, 1])
        self.speed_y = min(BALL_SPEED_Y + random.uniform(0, 1), max_speed) * random.choice([-1, 1])
    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)