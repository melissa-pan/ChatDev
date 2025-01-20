'''
Main file to run the Snake game using Pygame.
'''
import pygame
import sys
from snake import Snake
from food import Food
from board import Board
# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 10
def main():
    # Initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    # Create game objects
    snake = Snake(BLOCK_SIZE)
    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
    board = Board(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Handle snake movement and game logic
        snake.handle_keys()
        snake.move()
        if snake.check_collision(SCREEN_WIDTH, SCREEN_HEIGHT):
            break
        if snake.eat_food(food.position):
            food.spawn(snake.body)
        # Draw the game board
        board.draw(snake, food)
        pygame.display.update()
        clock.tick(FPS)
if __name__ == '__main__':
    main()