import game_functions as gf
from ship import Ship
import pygame
from settings import Settings
import bullet
from pygame.sprite import Group
from alien import Alien

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("test")
	ship = Ship(ai_settings,screen)
	alien = Alien(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	gf.create_fleet(ai_settings,screen,aliens,ship)
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)		
		
run_game()
