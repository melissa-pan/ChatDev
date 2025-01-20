'''
Main game loop and initialization.
'''
import pygame
from claw import Claw
from object import Gold, Rock
from scoreboard import Scoreboard
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Gold Miner")
        self.clock = pygame.time.Clock()
        self.claw = Claw()
        self.objects = [Gold(100, (200, 300)), Rock(50, (400, 300))]
        self.scoreboard = Scoreboard()
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
            if self.scoreboard.time_left <= 0:
                self.running = False
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.claw.grab(self.objects)
    def update(self):
        self.claw.move()
        self.scoreboard.update_score(self.claw, self.objects)
        self.scoreboard.update_time()
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.claw.draw(self.screen)
        for obj in self.objects:
            obj.draw(self.screen)
        self.scoreboard.draw(self.screen)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()