'''
Board class that represents the game board and handles operations related to it, such as swapping candies and finding matches.
'''
import pygame
import random
from candy import Candy
class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.candies = [[Candy(random.randint(0, 5), (x, y)) for x in range(self.cols)] for y in range(self.rows)]
        self.matches = set()
    def swap(self, pos1, pos2):
        # Temporarily swap two candies on the board
        x1, y1 = pos1
        x2, y2 = pos2
        self.candies[y1][x1], self.candies[y2][x2] = self.candies[y2][x2], self.candies[y1][x1]
    def is_valid_swap(self, pos1, pos2):
        # Check if swapping pos1 and pos2 results in a match
        self.swap(pos1, pos2)
        self.find_matches()
        valid = bool(self.matches)
        self.swap(pos1, pos2)  # Revert the swap
        return valid
    def find_matches(self):
        # Find and return all unique matches on the board
        self.matches = set()
        # Check horizontal matches
        for y in range(self.rows):
            for x in range(self.cols - 2):
                if self.candies[y][x].candy_type == self.candies[y][x + 1].candy_type == self.candies[y][x + 2].candy_type:
                    self.matches.update({(x, y), (x + 1, y), (x + 2, y)})
        # Check vertical matches
        for x in range(self.cols):
            for y in range(self.rows - 2):
                if self.candies[y][x].candy_type == self.candies[y + 1][x].candy_type == self.candies[y + 2][x].candy_type:
                    self.matches.update({(x, y), (x, y + 1), (x, y + 2)})
        return list(self.matches)
    def clear_matches(self):
        # Clear matched candies and update the board
        for x, y in self.matches:
            self.candies[y][x] = None
        self.matches = set()
    def drop_candies(self):
        # Drop candies to fill empty spaces
        for x in range(self.cols):
            for y in range(self.rows - 1, -1, -1):
                if self.candies[y][x] is None:
                    for k in range(y - 1, -1, -1):
                        if self.candies[k][x] is not None:
                            self.candies[y][x], self.candies[k][x] = self.candies[k][x], None
                            break
    def refill(self):
        # Refill the board with new candies
        for y in range(self.rows):
            for x in range(self.cols):
                if self.candies[y][x] is None:
                    self.candies[y][x] = Candy(random.randint(0, 5), (x, y))
    def update(self):
        # Update the board state
        self.find_matches()
        if self.matches:
            self.clear_matches()
            self.drop_candies()
            self.refill()
    def draw(self, screen):
        for row in self.candies:
            for candy in row:
                if candy is not None:
                    candy.draw(screen)