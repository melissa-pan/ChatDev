'''
Main file to run the Checkers game using Pygame.
'''
import pygame
from board import Board
from player import Player
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Checkers')
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.players = [Player('red'), Player('black')]
        self.current_player_index = 0
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    move_input = input("Enter your move (e.g., a3-b4): ")
                    start_pos, end_pos = self.parse_notation(move_input)
                    if self.players[self.current_player_index].make_move(self.board, start_pos, end_pos):
                        self.current_player_index = (self.current_player_index + 1) % 2
    def parse_notation(self, move_input):
        start, end = move_input.split('-')
        return self.notation_to_position(start), self.notation_to_position(end)
    def notation_to_position(self, notation):
        col = ord(notation[0]) - ord('a')
        row = 8 - int(notation[1])
        return (row, col)
    def update(self):
        # Update game logic if needed
        pass
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.board.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()