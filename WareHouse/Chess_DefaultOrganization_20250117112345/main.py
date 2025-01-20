'''
Main entry point for the chess game application.
'''
from chessboard import ChessBoard
class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.current_turn = 'white'
    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_turn.capitalize()}'s turn. Enter your move (e.g., Ke8):")
            move = input()
            if self.board.move_piece(move, self.current_turn):
                if self.board.is_checkmate(self.current_turn):
                    print(f"Checkmate! {self.current_turn.capitalize()} wins!")
                    break
                elif self.board.is_stalemate(self.current_turn):
                    print("Stalemate! It's a draw!")
                    break
                self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            else:
                print("Invalid move. Try again.")
if __name__ == "__main__":
    game = Game()
    game.play()