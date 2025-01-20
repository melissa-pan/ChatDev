'''
Main game file that initializes and runs the Flappy Bird clone.
'''
import pygame
from bird import Bird
from pipe import Pipe
from score import Score
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = [Pipe()]
        self.score = Score()
        self.running = True
        self.pipe_timer = 0  # Timer to control pipe generation
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()
    def update(self):
        if self.bird.update():  # Check if the bird has collided with the ground
            self.running = False
        for pipe in self.pipes:
            pipe.update()
            if pipe.off_screen():
                self.pipes.remove(pipe)
            if pipe.collides_with(self.bird):
                self.running = False
        self.pipe_timer += 1
        # Dynamic pipe generation based on score
        pipe_interval = max(60, 90 - self.score.value)  # Decrease interval as score increases
        if self.pipe_timer > pipe_interval:
            self.pipes.append(Pipe())
            self.pipe_timer = 0
            self.score.increase()
    def draw(self):
        self.screen.fill((135, 206, 235))  # Sky blue background
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()
if __name__ == "__main__":
    Game().run()