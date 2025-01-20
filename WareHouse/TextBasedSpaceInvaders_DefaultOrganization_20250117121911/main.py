'''
Main module to run the Space Invaders game using Pygame.
'''
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
import game_functions as gf
def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    # Create an instance of Ship and a group for bullets and aliens
    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()
    aliens = Group()
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens)
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
if __name__ == '__main__':
    run_game()