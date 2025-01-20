'''
Board class to manage drawing the snake and food on the screen.
'''
import pygame
class Board:
    def __init__(self, screen, screen_width, screen_height, block_size):
        # Initialize the board with screen and dimensions
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
    def draw(self, snake, food):
        # Draw the snake and food on the screen
        self.screen.fill((0, 0, 0))
        for segment in snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, self.block_size, self.block_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (*food.position, self.block_size, self.block_size))