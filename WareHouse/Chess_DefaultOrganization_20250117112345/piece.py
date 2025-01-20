'''
Defines the Piece class and its subclasses for each type of chess piece.
'''
class Piece:
    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color
    def valid_moves(self, position, board):
        # Return a list of valid moves for the piece
        return []
    def symbol(self):
        return self.piece_type.upper() if self.color == 'white' else self.piece_type.lower()
class King(Piece):
    def __init__(self, color):
        super().__init__('k', color)
class Queen(Piece):
    def __init__(self, color):
        super().__init__('q', color)
class Rook(Piece):
    def __init__(self, color):
        super().__init__('r', color)
class Bishop(Piece):
    def __init__(self, color):
        super().__init__('b', color)
class Knight(Piece):
    def __init__(self, color):
        super().__init__('n', color)
class Pawn(Piece):
    def __init__(self, color):
        super().__init__('p', color)