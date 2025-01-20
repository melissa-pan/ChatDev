'''
Game class manages the main game loop, event handling, and rendering.
'''
import pygame
from board import Board
from tetromino import Tetromino
from constants import *
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.current_tetromino = Tetromino()
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.current_tetromino.move(-1, 0, self.board)
                elif event.key == pygame.K_RIGHT:
                    self.current_tetromino.move(1, 0, self.board)
                elif event.key == pygame.K_DOWN:
                    self.current_tetromino.move(0, 1, self.board)
                elif event.key == pygame.K_UP:
                    self.current_tetromino.rotate(self.board)
    def update(self):
        if not self.current_tetromino.move(0, 1, self.board):
            self.board.place_tetromino(self.current_tetromino)
            self.board.clear_lines()
            self.current_tetromino = Tetromino()
            if not self.board.can_place(self.current_tetromino.shape, self.current_tetromino.position):
                self.display_game_over()
                self.running = False  # End the game if a new tetromino cannot be placed
    def draw(self):
        self.screen.fill(BLACK)
        self.board.draw(self.screen)
        self.current_tetromino.draw(self.screen)
        pygame.display.flip()
    def display_game_over(self):
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before quitting