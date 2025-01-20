'''
Main entry point for the Pong game. Initializes the game and manages the game loop.
'''
import pygame
from paddle import Paddle
from ball import Ball
from score import Score
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong Game")
    clock = pygame.time.Clock()
    # Create game objects
    paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - 60)
    paddle2 = Paddle(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2 - 60)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    score = Score()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down()
        if keys[pygame.K_UP]:
            paddle2.move_up()
        if keys[pygame.K_DOWN]:
            paddle2.move_down()
        # Update game state
        ball.update(paddle1, paddle2, score)
        # Draw everything
        screen.fill((0, 0, 0))
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)
        score.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()