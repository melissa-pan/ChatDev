'''
Defines the Player class for the roguelike game.
'''
import pygame
from monster import Monster
from treasure import Treasure
from door import Door
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 100
    def move(self, dx, dy, game_map):
        new_x = self.x + dx
        new_y = self.y + dy
        if game_map.is_walkable(new_x, new_y):
            self.x = new_x
            self.y = new_y
            obj = game_map.get_object_at(new_x, new_y)
            if obj:
                self.interact_with_object(obj, game_map.game)
    def interact_with_object(self, obj, game):
        if isinstance(obj, Monster):
            self.hp -= obj.hp
            if self.hp <= 0:
                self.hp = 0
                print("Player defeated by monster!")
        elif isinstance(obj, Treasure):
            restored_hp = obj.restore_hp()
            self.hp += restored_hp
            print(f"Player restored {restored_hp} HP from treasure!")
        elif isinstance(obj, Door):
            obj.interact(self, game)
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x * 10, self.y * 10, 10, 10))