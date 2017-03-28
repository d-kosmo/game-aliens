import game_functions as gf
from ship import Ship
import pygame
from settings import Settings
import bullet
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import pyganim

def run_game():
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        boltAnim = pyganim.PygAnimation(ai_settings.anim_bg)
        boltAnim.play()
        play_button = Button(ai_settings, screen, "Play")
        stats = GameStats(ai_settings)
        sb = Scoreboard(ai_settings,screen, stats)
        ship = Ship(ai_settings,screen)
        alien = Alien(ai_settings,screen)
        bullets = Group()
        aliens = Group()
        gf.create_fleet(ai_settings,screen,aliens,ship)
        sound = pygame.mixer.Sound('sound\\laser.ogg')
        sound_2 = pygame.mixer.Sound('sound\\explosion.ogg')
        while True:
                gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,sound)
                if stats.game_active:
                        ship.update(ai_settings)
                        gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_2)
                        gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
                gf.update_screen(boltAnim,ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
                #boltAnim.blit(screen, (100, 50))
                #pygame.display.update()
run_game()
