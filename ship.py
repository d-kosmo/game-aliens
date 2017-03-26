import pygame
from pygame.sprite import Sprite
import game_functions as gf
import pyganim

class Ship(Sprite):
	
        def __init__(self,ai_settings,screen,lives=None):
                super(Ship, self).__init__()
                self.screen = screen
                if lives:
                        self.image = pygame.image.load('image\\ship_small.bmp')
                else:
                        self.image = pygame.image.load('image\\ship.bmp')
                self.rect = self.image.get_rect()
                self.screen_rect = screen.get_rect()
                self.rect.centerx = self.screen_rect.centerx
                self.rect.bottom = self.screen_rect.bottom
                self.moving_right = False
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.ai_settings = ai_settings
                self.center = float(self.rect.centerx)
                self.centery = float(self.rect.centery)
                self.stop = True
                
                boltAnim = []
                for anim in ai_settings.ship_left:
                        boltAnim.append((anim, ai_settings.anim_delay))
                self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
                self.boltAnimLeft.play()

                boltAnim = []
                for anim in ai_settings.ship_right:
                        boltAnim.append((anim, ai_settings.anim_delay))
                self.boltAnimRight = pyganim.PygAnimation(boltAnim)
                self.boltAnimRight.play()

                self.boltAnimStop = pyganim.PygAnimation(ai_settings.ship_stop)
                self.boltAnimStop.play()
                
        def center_ship(self):
                self.center = self.screen_rect.centerx
                
        def blitme(self):
                self.screen.blit(self.image, self.rect)
	
        def update(self,ai_settings):
                if self.moving_right and self.rect.right < self.screen_rect.right:
                        self.center += self.ai_settings.ship_speed_factor
                        self.image.fill(ai_settings.black_color)
                        self.boltAnimRight.blit(self.image, (0, 0))
                if self.moving_left and self.rect.left > 0:
                        self.center -= self.ai_settings.ship_speed_factor
                        self.image.fill(ai_settings.black_color)
                        self.boltAnimLeft.blit(self.image, (0, 0))
                if self.moving_up and self.rect.top > self.screen_rect.top:
                        self.centery -= self.ai_settings.ship_speed_factor	
                if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                        self.centery += self.ai_settings.ship_speed_factor
                if self.stop:
                        self.boltAnimStop.blit(self.image, (0, 0))
                        
                self.rect.centerx = self.center
                self.rect.centery = self.centery

