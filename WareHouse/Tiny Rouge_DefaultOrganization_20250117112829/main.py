'''
Main entry point for the roguelike game.
'''
import pygame
from player import Player
from map import Map
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Tower of the Sorcerer")
        self.clock = pygame.time.Clock()
        self.map = Map()
        self.player = Player(self.map.start_x, self.map.start_y)
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.move(0, -1, self.map)
                elif event.key == pygame.K_s:
                    self.player.move(0, 1, self.map)
                elif event.key == pygame.K_a:
                    self.player.move(-1, 0, self.map)
                elif event.key == pygame.K_d:
                    self.player.move(1, 0, self.map)
    def update(self):
        # Update game logic here
        # Currently, no additional logic is needed
        pass
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
    def next_level(self):
        # Reset or update the map for a new level
        self.map = Map()
        # Reset player position to start
        self.player.x, self.player.y = self.map.start_x, self.map.start_y
        print("Welcome to the next level!")
if __name__ == "__main__":
    game = Game()
    game.run()