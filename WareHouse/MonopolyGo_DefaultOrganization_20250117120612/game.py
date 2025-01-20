'''
Contains the Game class which manages the overall game state and logic.
'''
from player import Player
from board import Board
from gui import GUI
class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.board = Board()
        self.gui = GUI(self)
        self.current_player_index = 0
    def start_game(self):
        self.gui.update_display()
        self.gui.run()
    def next_turn(self):
        current_player = self.players[self.current_player_index]
        self.gui.prompt_player_action(current_player)
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.gui.update_display()