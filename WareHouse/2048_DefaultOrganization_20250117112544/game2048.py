'''
Game logic for the 2048 game with a 10x10 grid.
'''
import random
class Game2048:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
        self.score = 0
        self.reset()
    def reset(self):
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
    def add_random_tile(self):
        empty_positions = [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] == 0]
        if empty_positions:
            r, c = random.choice(empty_positions)
            self.grid[r][c] = random.choice([2, 4])
    def move(self, direction):
        def merge(row):
            non_zero = [num for num in row if num != 0]
            merged = []
            skip = False
            for i in range(len(non_zero)):
                if skip:
                    skip = False
                    continue
                if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                    merged.append(2 * non_zero[i])
                    self.score += 2 * non_zero[i]
                    skip = True
                else:
                    merged.append(non_zero[i])
            return merged + [0] * (self.size - len(merged))
        moved = False
        if direction in ('left', 'right'):
            for i in range(self.size):
                original = self.grid[i][:]
                if direction == 'left':
                    self.grid[i] = merge(self.grid[i])
                else:
                    self.grid[i] = merge(self.grid[i][::-1])[::-1]
                if self.grid[i] != original:
                    moved = True
        elif direction in ('up', 'down'):
            for i in range(self.size):
                original = [self.grid[j][i] for j in range(self.size)]
                if direction == 'up':
                    merged = merge(original)
                else:
                    merged = merge(original[::-1])[::-1]
                for j in range(self.size):
                    self.grid[j][i] = merged[j]
                if [self.grid[j][i] for j in range(self.size)] != original:
                    moved = True
        if moved:
            self.add_random_tile()
    def can_move(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return True
                if c < self.size - 1 and self.grid[r][c] == self.grid[r][c + 1]:
                    return True
                if r < self.size - 1 and self.grid[r][c] == self.grid[r + 1][c]:
                    return True
        return False