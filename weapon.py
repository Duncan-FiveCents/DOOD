import pygame
from sprite import *

class WeaponBase:
    def __init__(self,GAME):
        self.game = GAME
        self.screen = GAME.screen
        self.image = None
        self.frames = None
        self.cooldown = False
        self.timer = 0
    
    def draw(self):
        self.screen.blit(self.image,(0,0))

    def fire(self):
        if pygame.mouse.get_pressed()[0] and not self.cooldown:
            self.cooldown = True
            self.timer = 18
        elif self.timer != 0: 
            self.image = self.frames[(self.timer//3)-1]
            self.timer -= 1
        else:
            self.cooldown = False

class Shotgun(WeaponBase):
    def __init__(self,GAME):
        WeaponBase.__init__(self,GAME)
        self.image = pygame.image.load(resource_path("resources/UI/ShellGun/DOOD Shell Gun.png")).convert_alpha()
        self.frames = [
            pygame.image.load(resource_path("resources/UI/ShellGun/DOOD Shell Gun.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/ShellGun/DOOD Shell Gun2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/ShellGun/DOOD Shell Gun3.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/ShellGun/DOOD Shell Gun4.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/ShellGun/DOOD Shell Gun5.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/ShellGun/DOOD Shell Gun6.png")).convert_alpha()
        ]

class Sluggun(WeaponBase):
    def __init__(self,GAME):
        WeaponBase.__init__(self,GAME)
        self.image = pygame.image.load(resource_path("resources/UI/SlugGun/DOOD Slug Gun1.png")).convert_alpha()
        self.frames = [
            pygame.image.load(resource_path("resources/UI/SlugGun/DOOD Slug Gun1.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/SlugGun/DOOD Slug Gun2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/SlugGun/DOOD Slug Gun3.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/SlugGun/DOOD Slug Gun4.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/SlugGun/DOOD Slug Gun5.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/SlugGun/DOOD Slug Gun6.png")).convert_alpha()
        ]
