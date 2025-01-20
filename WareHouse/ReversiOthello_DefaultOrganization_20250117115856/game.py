'''
Manages the game state, including the board, current player, and game logic.
'''
import pygame
from board import Board
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()
        self.current_player = 'black'
        self.game_over = False
    def reset_game(self):
        self.board.reset()
        self.current_player = 'black'
        self.game_over = False
    def handle_click(self, x, y):
        if not self.game_over:
            row, col = y // 100, x // 100
            if self.board.is_valid_move(row, col, self.current_player):
                self.board.make_move(row, col, self.current_player)
                self.current_player = 'white' if self.current_player == 'black' else 'black'
                # Check if the current player has any valid moves
                if not self.board.get_valid_moves(self.current_player):
                    # If not, switch back to the other player
                    self.current_player = 'white' if self.current_player == 'black' else 'black'
                    # Check if the other player also has no valid moves
                    if not self.board.get_valid_moves(self.current_player):
                        self.game_over = True
            elif not self.board.get_valid_moves(self.current_player):
                # If the current player has no valid moves, switch to the other player
                self.current_player = 'white' if self.current_player == 'black' else 'black'
                # Check if the other player also has no valid moves
                if not self.board.get_valid_moves(self.current_player):
                    self.game_over = True
    def update(self):
        self.screen.fill((0, 128, 0))
        self.board.draw(self.screen)