'''
Defines the Score class for the Pong game, which manages and displays the scores for both players.
'''
import pygame
# Constants
SCREEN_WIDTH = 800
FONT_SIZE = 36
class Score:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.font = pygame.font.Font(None, FONT_SIZE)
    def increment_player1(self):
        self.player1_score += 1
    def increment_player2(self):
        self.player2_score += 1
    def draw(self, screen):
        score_text = f"{self.player1_score} - {self.player2_score}"
        text_surface = self.font.render(score_text, True, (255, 255, 255))
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 20))