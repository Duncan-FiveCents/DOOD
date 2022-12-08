# enemy.py

'''
title: enemy stuff!!!
author: Duncan Nickel
date-created: 07/12/2022
'''

import pygame
from resource_path import resource_path
from math import sin,cos,atan2,pi,sqrt

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.rect.Rect(4*40,22*40,20,20)
        self.image = pygame.image.load(resource_path("enemies\placeholder enemy.png")).convert()
        self.angle = pi/2
