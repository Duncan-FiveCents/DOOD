# enemy.py

'''
title: enemy stuff!!!
author: Duncan Nickel
date-created: 07/12/2022
'''

import pygame
from common import resource_path
from math import sin,cos,atan2,pi,sqrt

class Enemy(pygame.sprite.Sprite):
    def __init__(self,shift,SPAWN):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.rect.Rect(SPAWN[0]*18,SPAWN[1]*18,20,20)
        self.image = pygame.image.load(resource_path("enemies\skeleton-enemy1.png")).convert()
        self.angle = pi/2
        self.shift = shift # Needed for the raycasting later
