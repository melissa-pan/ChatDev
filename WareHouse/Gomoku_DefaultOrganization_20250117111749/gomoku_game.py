'''
GomokuGame class manages the overall game logic and flow.
'''
from board import Board
from player import Player
from gui import GUI
class GomokuGame:
    def __init__(self, use_gui=True):
        self.board_size = 15
        self.board = Board(self.board_size)
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0
        self.use_gui = use_gui
        if self.use_gui:
            self.gui = GUI(self.board_size)
    def reset_game(self):
        self.board = Board(self.board_size)
        self.current_player_index = 0
    def check_winner(self):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # right, down, diagonal down-right, diagonal down-left
        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.board.grid[y][x] != '':
                    player_symbol = self.board.grid[y][x]
                    for dx, dy in directions:
                        count = 1
                        for step in range(1, 5):
                            nx, ny = x + step * dx, y + step * dy
                            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board.grid[ny][nx] == player_symbol:
                                count += 1
                            else:
                                break
                        if count == 5:
                            return True
        return False
    def make_move(self, x, y):
        player = self.players[self.current_player_index]
        if self.board.place_piece(x, y, player.symbol):
            if self.check_winner():
                print(f"{player.name} wins!")
                self.reset_game()
            else:
                self.current_player_index = (self.current_player_index + 1) % len(self.players)
    def run(self):
        if self.use_gui:
            while True:
                self.gui.handle_events(self)
                self.gui.draw_board(self.board)
                self.gui.draw_pieces(self.board)
        else:
            while True:
                player = self.players[self.current_player_index]
                move = player.get_move(use_gui=False)
                if move:
                    x, y = move
                    self.make_move(x, y)
                    self.board.print_board()
                    if self.check_winner():
                        print(f"{player.name} wins!")
                        self.reset_game()