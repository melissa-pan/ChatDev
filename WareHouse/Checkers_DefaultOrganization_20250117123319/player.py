'''
Player class to represent a player in the game.
'''
from utils import coordinates_to_position
class Player:
    def __init__(self, color):
        self.color = color
    def make_move(self, board, mouse_pos):
        start_pos = coordinates_to_position(mouse_pos)
        piece = board.grid[start_pos[0]][start_pos[1]]
        if piece and piece.color == self.color:
            possible_captures = self.get_possible_captures(board)
            if possible_captures:
                for end_pos in possible_captures.get(start_pos, []):
                    if self.is_valid_capture(board, start_pos, end_pos):
                        board.move_piece(start_pos, end_pos)
                        return True
            else:
                possible_moves = self.get_possible_moves(board, start_pos, piece.king)
                for end_pos in possible_moves:
                    if self.is_valid_move(board, start_pos, end_pos):
                        board.move_piece(start_pos, end_pos)
                        return True
        return False
    def get_possible_moves(self, board, start_pos, is_king):
        directions = [(-1, -1), (-1, 1)] if self.color == 'red' else [(1, -1), (1, 1)]
        if is_king:
            directions += [(d[0] * -1, d[1] * -1) for d in directions]
        possible_moves = [(start_pos[0] + d[0], start_pos[1] + d[1]) for d in directions]
        return [move for move in possible_moves if 0 <= move[0] < 8 and 0 <= move[1] < 8]
    def get_possible_captures(self, board):
        captures = {}
        for row in range(8):
            for col in range(8):
                piece = board.grid[row][col]
                if piece and piece.color == self.color:
                    start_pos = (row, col)
                    possible_moves = self.get_possible_moves(board, start_pos, piece.king)
                    for end_pos in possible_moves:
                        if self.is_valid_capture(board, start_pos, end_pos):
                            if start_pos not in captures:
                                captures[start_pos] = []
                            captures[start_pos].append(end_pos)
        return captures
    def is_valid_move(self, board, start_pos, end_pos):
        if board.grid[end_pos[0]][end_pos[1]] is not None:
            return False
        row_diff = abs(start_pos[0] - end_pos[0])
        col_diff = abs(start_pos[1] - end_pos[1])
        return row_diff == 1 and col_diff == 1
    def is_valid_capture(self, board, start_pos, end_pos):
        if board.grid[end_pos[0]][end_pos[1]] is not None:
            return False
        row_diff = abs(start_pos[0] - end_pos[0])
        col_diff = abs(start_pos[1] - end_pos[1])
        if row_diff == 2 and col_diff == 2:
            mid_row = (start_pos[0] + end_pos[0]) // 2
            mid_col = (start_pos[1] + end_pos[1]) // 2
            mid_piece = board.grid[mid_row][mid_col]
            if mid_piece and mid_piece.color != self.color:
                board.capture_piece((mid_row, mid_col))
                return True
        return False