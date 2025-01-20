'''
Defines the Bird class for the Flappy Bird clone.
'''
import pygame
class Bird:
    def __init__(self):
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 255, 0))  # Yellow bird
        self.rect = self.image.get_rect(center=(100, 300))
        self.velocity = 0
        self.gravity = 0.5
    def flap(self):
        self.velocity = -10
    def update(self):
        '''
        Updates the bird's position based on its velocity and gravity.
        Checks for collision with the ground.
        '''
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.y > 570:  # Ground collision
            self.rect.y = 570
            return True  # Signal that the bird has collided with the ground
        return False
    def draw(self, screen):
        screen.blit(self.image, self.rect)