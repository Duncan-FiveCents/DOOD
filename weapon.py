# weapon.py

'''
title: shooty shooty pew pew
author: Duncan Nickel
date-created: 05/12/2022
'''

import pygame
from common import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = pygame.rect.Rect(0,0,640,480)
    
    def playAnim(self,FRAME):
        for i in range(5): self.image = self.animation[FRAME]

class Shotgun(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.image = pygame.image.load(resource_path("UI\ShellGun\DOOD Shell Gun.png")).convert()
        self.animation = [
            pygame.image.load(resource_path("UI\ShellGun\DOOD Shell Gun.png")).convert(),
            pygame.image.load(resource_path("UI\ShellGun\DOOD Shell Gun2.png")).convert(),
            pygame.image.load(resource_path("UI\ShellGun\DOOD Shell Gun3.png")).convert(),
            pygame.image.load(resource_path("UI\ShellGun\DOOD Shell Gun4.png")).convert(),
            pygame.image.load(resource_path("UI\ShellGun\DOOD Shell Gun5.png")).convert(),
            pygame.image.load(resource_path("UI\ShellGun\DOOD Shell Gun6.png")).convert()
        ]

class Slug(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.image = pygame.image.load(resource_path("UI\SlugGun\DOOD Slug Gun1.png")).convert()
        self.animation = [
            pygame.image.load(resource_path("UI\SlugGun\DOOD Slug Gun1.png")).convert(),
            pygame.image.load(resource_path("UI\SlugGun\DOOD Slug Gun2.png")).convert(),
            pygame.image.load(resource_path("UI\SlugGun\DOOD Slug Gun3.png")).convert(),
            pygame.image.load(resource_path("UI\SlugGun\DOOD Slug Gun4.png")).convert(),
            pygame.image.load(resource_path("UI\SlugGun\DOOD Slug Gun5.png")).convert(),
            pygame.image.load(resource_path("UI\SlugGun\DOOD Slug Gun6.png")).convert()
        ]