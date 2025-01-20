'''
Tetromino class represents the falling tetrominoes and handles their movement and rotation.
'''
import random
import pygame
from constants import *
class Tetromino:
    shape_bag = []
    @staticmethod
    def get_random_shape():
        if not Tetromino.shape_bag:
            Tetromino.shape_bag = SHAPES.copy()
            random.shuffle(Tetromino.shape_bag)
        return Tetromino.shape_bag.pop()
    def __init__(self):
        self.shape = self.get_random_shape()
        self.color = random.choice(COLORS)
        self.position = [COLS // 2 - len(self.shape[0]) // 2, 0]
    def rotate(self, board):
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        if board.can_place(new_shape, self.position):
            self.shape = new_shape
    def move(self, dx, dy, board):
        new_position = [self.position[0] + dx, self.position[1] + dy]
        if board.can_place(self.shape, new_position):
            self.position = new_position
            return True
        return False
    def draw(self, surface):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(surface, self.color, ((self.position[0] + x) * BLOCK_SIZE, (self.position[1] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))