'''
Defines the Map class for the roguelike game.
'''
import pygame
import random
from monster import Monster
from treasure import Treasure
from door import Door
class Map:
    def __init__(self):
        self.width = 80
        self.height = 80
        self.grid = [['wall' for _ in range(self.width)] for _ in range(self.height)]
        self.start_x = 1
        self.start_y = 1
        self.generate_map()
    def generate_map(self):
        # Use a randomized DFS to generate a maze
        stack = [(self.start_x, self.start_y)]
        self.grid[self.start_x][self.start_y] = 'floor'
        last_cell = (self.start_x, self.start_y)
        while stack:
            x, y = stack[-1]
            neighbors = self.get_unvisited_neighbors(x, y)
            if neighbors:
                nx, ny = random.choice(neighbors)
                self.grid[nx][ny] = 'floor'
                self.grid[(x + nx) // 2][(y + ny) // 2] = 'floor'
                stack.append((nx, ny))
                last_cell = (nx, ny)
            else:
                stack.pop()
        # Place the door at the end of the path
        self.grid[last_cell[0]][last_cell[1]] = Door()
        # Randomly place monsters and treasures
        self.place_objects(Monster, 10)
        self.place_objects(Treasure, 10)
    def get_unvisited_neighbors(self, x, y):
        neighbors = []
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < self.width and 0 < ny < self.height and self.grid[nx][ny] == 'wall':
                neighbors.append((nx, ny))
        return neighbors
    def place_objects(self, obj_type, count):
        for _ in range(count):
            while True:
                x = random.randint(1, self.width - 2)
                y = random.randint(1, self.height - 2)
                if self.grid[x][y] == 'floor':
                    self.grid[x][y] = obj_type(20) if obj_type == Monster else obj_type()
                    break
    def is_walkable(self, x, y):
        return self.grid[x][y] == 'floor' or isinstance(self.grid[x][y], (Monster, Treasure, Door))
    def get_object_at(self, x, y):
        if isinstance(self.grid[x][y], (Monster, Treasure, Door)):
            return self.grid[x][y]
        return None
    def draw(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] == 'wall':
                    pygame.draw.rect(screen, (255, 255, 255), (x * 10, y * 10, 10, 10))
                elif self.grid[x][y] == 'floor':
                    pygame.draw.rect(screen, (50, 50, 50), (x * 10, y * 10, 10, 10))