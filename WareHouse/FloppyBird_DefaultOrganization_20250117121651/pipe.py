'''
Defines the Pipe class for the Flappy Bird clone.
'''
import pygame
import random
class Pipe:
    def __init__(self):
        self.image = pygame.Surface((50, 400))
        self.image.fill((0, 255, 0))  # Green pipe
        self.gap = random.randint(120, 180)  # Randomized gap size
        self.top_height = random.randint(50, 350)
        self.bottom_height = 600 - self.top_height - self.gap
        self.rect_top = self.image.get_rect(midbottom=(450, self.top_height))
        self.rect_bottom = self.image.get_rect(midtop=(450, self.top_height + self.gap))
    def update(self):
        '''
        Moves the pipes to the left and updates their position.
        '''
        self.rect_top.x -= 5
        self.rect_bottom.x -= 5
    def off_screen(self):
        '''
        Checks if the pipe has moved off the screen.
        '''
        return self.rect_top.right < 0
    def collides_with(self, bird):
        '''
        Checks for collision with the bird using bounding box collision detection.
        '''
        return self.rect_top.colliderect(bird.rect) or self.rect_bottom.colliderect(bird.rect)
    def draw(self, screen):
        screen.blit(self.image, self.rect_top)
        screen.blit(self.image, self.rect_bottom)