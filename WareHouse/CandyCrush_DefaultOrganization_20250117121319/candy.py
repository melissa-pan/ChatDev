'''
Candy class that represents individual candies on the board.
'''
import pygame
class Candy:
    def __init__(self, candy_type, position):
        self.candy_type = candy_type
        self.position = position
        self.size = 50
        self.color = self.get_color()
    def get_color(self):
        # Return a color based on the candy type
        colors = [
            (255, 0, 0),    # Red
            (0, 255, 0),    # Green
            (0, 0, 255),    # Blue
            (255, 255, 0),  # Yellow
            (255, 165, 0),  # Orange
            (255, 192, 203) # Pink
        ]
        return colors[self.candy_type]
    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(screen, self.color, (x * self.size, y * self.size, self.size, self.size))