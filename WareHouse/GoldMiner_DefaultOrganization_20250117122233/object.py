'''
Object classes for Gold and Rock.
'''
import pygame
class Object:
    '''
    Base class for objects in the game.
    '''
    def __init__(self, value, position):
        '''
        Initialize the object with a value and position.
        '''
        self.value = value
        self.position = position
    def draw(self, screen):
        '''
        Draw the object on the screen.
        To be implemented by subclasses.
        '''
        pass
class Gold(Object):
    '''
    Gold object with specific drawing method.
    '''
    def draw(self, screen):
        '''
        Draw the gold object as a yellow circle.
        '''
        pygame.draw.circle(screen, (255, 215, 0), self.position, 10)
class Rock(Object):
    '''
    Rock object with specific drawing method.
    '''
    def draw(self, screen):
        '''
        Draw the rock object as a gray circle.
        '''
        pygame.draw.circle(screen, (169, 169, 169), self.position, 10)