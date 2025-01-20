'''
Game class that manages the overall game logic, including initialization, input handling, and updating the game state.
'''
import pygame
from board import Board
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Match-3 Puzzle Game")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.running = True
        self.selected_candy = None
    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos[0] // 50, pos[1] // 50
                if self.selected_candy:
                    if self.board.is_valid_swap(self.selected_candy, (x, y)):
                        self.board.swap(self.selected_candy, (x, y))
                    self.selected_candy = None
                else:
                    self.selected_candy = (x, y)
    def update(self):
        # Update game state, check for matches, and update score
        self.board.update()
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.board.draw(self.screen)
        pygame.display.flip()