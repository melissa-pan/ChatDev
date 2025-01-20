'''
Food class to manage the food's position and spawning.
'''
import random
class Food:
    def __init__(self, screen_width, screen_height, block_size):
        # Initialize food position and screen dimensions
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.position = self.spawn([])
    def spawn(self, snake_body):
        # Spawn food at a random position not occupied by the snake
        while True:
            x = random.randint(0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
            y = random.randint(0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
            if (x, y) not in snake_body:
                self.position = (x, y)
                return self.position