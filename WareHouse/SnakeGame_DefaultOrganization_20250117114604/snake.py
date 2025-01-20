'''
Snake class to manage the snake's position, movement, and growth.
'''
import pygame
class Snake:
    def __init__(self, block_size):
        # Initialize the snake with a default body and direction
        self.block_size = block_size
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = pygame.K_RIGHT
    def handle_keys(self):
        # Handle key inputs to change the snake's direction
        keys = pygame.key.get_pressed()
        opposite_directions = {
            pygame.K_UP: pygame.K_DOWN,
            pygame.K_DOWN: pygame.K_UP,
            pygame.K_LEFT: pygame.K_RIGHT,
            pygame.K_RIGHT: pygame.K_LEFT
        }
        for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            if keys[key] and self.direction != opposite_directions[key]:
                self.direction = key
                break
    def move(self):
        # Move the snake in the current direction
        x, y = self.body[0]
        if self.direction == pygame.K_UP:
            y -= self.block_size
        elif self.direction == pygame.K_DOWN:
            y += self.block_size
        elif self.direction == pygame.K_LEFT:
            x -= self.block_size
        elif self.direction == pygame.K_RIGHT:
            x += self.block_size
        new_head = (x, y)
        self.body = [new_head] + self.body[:-1]
    def grow(self):
        # Grow the snake by adding a new segment at the tail
        self.body.append(self.body[-1])
    def eat_food(self, food_position):
        # Check if the snake's head is at the food position
        if self.body[0] == food_position:
            self.grow()
            return True
        return False
    def check_collision(self, screen_width, screen_height):
        # Check if the snake collides with the walls or itself
        x, y = self.body[0]
        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False