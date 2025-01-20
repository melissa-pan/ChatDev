'''
This file contains the implementation of a text-based Minesweeper game playable from the Linux Terminal. The game supports two difficulty levels and allows users to interact via terminal inputs.
'''
import random
class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board_size = 5 if difficulty == 'easy' else 10
        self.num_mines = 5 if difficulty == 'easy' else 20
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.mine_positions = set()
        self.revealed = set()
        self.create_board()
    def create_board(self):
        while len(self.mine_positions) < self.num_mines:
            x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
            self.mine_positions.add((x, y))
    def display_board(self):
        print("   " + " ".join(str(i) for i in range(self.board_size)))
        print("  " + "-" * (self.board_size * 2 + 1))  # Adjusted for better alignment
        for i, row in enumerate(self.board):
            print(f"{i} |" + " ".join(row))
        print()
    def reveal_cell(self, x, y):
        if (x, y) in self.mine_positions:
            print("Boom! You hit a mine.")
            return False
        if (x, y) in self.revealed:
            print("Cell already revealed.")
            return True
        self.revealed.add((x, y))
        mine_count = self.count_mines(x, y)
        self.board[x][y] = str(mine_count)
        if mine_count == 0:
            for nx, ny in self.get_neighbors(x, y):
                if (nx, ny) not in self.revealed:
                    self.reveal_cell(nx, ny)
        return True
    def get_neighbors(self, x, y):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                    neighbors.append((nx, ny))
        return neighbors
    def count_mines(self, x, y):
        return sum((nx, ny) in self.mine_positions for nx, ny in self.get_neighbors(x, y))
    def check_win(self):
        return len(self.revealed) == self.board_size * self.board_size - self.num_mines
def main():
    difficulty = input("Select difficulty (easy/hard): ").strip().lower()
    if difficulty not in ['easy', 'hard']:
        print("Invalid difficulty level. Defaulting to easy.")
        difficulty = 'easy'
    else:
        print(f"Difficulty set to {difficulty}.")
    game = Game(difficulty)
    game.display_board()
    while True:
        try:
            x, y = map(int, input("Enter coordinates to reveal (row col): ").split())
            if not (0 <= x < game.board_size and 0 <= y < game.board_size):
                print("Coordinates out of bounds.")
                continue
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        if not game.reveal_cell(x, y):
            game.display_board()
            print("Game Over!")
            break
        game.display_board()
        if game.check_win():
            print("Congratulations! You've cleared the minefield!")
            break
if __name__ == "__main__":
    main()