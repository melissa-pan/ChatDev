'''
Claw class to handle movement and grabbing.
'''
import pygame
class Claw:
    def __init__(self):
        self.position = [400, 50]
        self.direction = 1
        self.grabbing = False
        self.extending = False
        self.max_extension = 300  # Maximum extension length
        self.original_position = self.position[1]
    def move(self):
        if not self.grabbing:
            self.position[0] += self.direction * 5
            if self.position[0] <= 0 or self.position[0] >= 800:
                self.direction *= -1
        elif self.extending:
            self.position[1] += 5
            if self.position[1] >= self.max_extension:
                self.extending = False
        else:
            self.position[1] -= 5
            if self.position[1] <= self.original_position:
                self.grabbing = False
    def grab_object(self, objects):
        for obj in objects:
            if self.position[0] in range(obj.position[0] - 10, obj.position[0] + 10) and self.position[1] in range(obj.position[1] - 10, obj.position[1] + 10):
                objects.remove(obj)
                return obj
        return None
    def grab(self, objects):
        if not self.grabbing:
            self.grabbing = True
            self.extending = True
        else:
            grabbed_object = self.grab_object(objects)
            if grabbed_object:
                self.grabbing = False
                self.extending = False
    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (self.position[0], self.original_position), (self.position[0], self.position[1]), 2)