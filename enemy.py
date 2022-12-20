# enemy.py

'''
title: enemy stuff!!!
author: Duncan Nickel
date-created: 07/12/2022
'''

import pygame
from common import resource_path
from math import pi

class Enemy(pygame.sprite.Sprite):
    def __init__(self,SPAWN):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.rect.Rect(0,0,10,10)
        self.rect.center = SPAWN[0]*18,SPAWN[1]*18
        self.image = pygame.image.load(resource_path("enemies\skeleton-enemy1.png")).convert()
        self.angle = pi/2

        self.shift = 0.6 # Adjusts the perceived height of the enemy
        self.scale = 20 # Seems to adjust the rate at which the enemy shrinks with distance
