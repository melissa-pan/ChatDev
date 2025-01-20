'''
Scoreboard class to display score and time.
'''
import pygame
class Scoreboard:
    def __init__(self):
        self.score = 0
        self.time_left = 60  # 60 seconds for each level
        self.font = pygame.font.Font(None, 36)
        self.start_ticks = pygame.time.get_ticks()  # Start time
    def update_score(self, claw, objects):
        if claw.grabbing and not claw.extending:
            grabbed_object = claw.grab_object(objects)
            if grabbed_object:
                self.score += grabbed_object.value
    def update_time(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000  # Calculate elapsed time
        self.time_left = max(0, 60 - int(seconds))  # Decrease time left
    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        time_text = self.font.render(f"Time: {self.time_left}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))