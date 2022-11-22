# raycasting.py

'''
title: this is gonna suck to make
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
import pygame.gfxdraw
from math import sin, cos

class RayCasting:
    def __init__(self,SCREEN):
        self.surface = SCREEN

    def base(self,PLAYERPOS,MAP):
        self.playerPosition = [PLAYERPOS[0],PLAYERPOS[1]]
        for line in MAP:
            pygame.draw.line(self.surface,(255,255,255),line.start,line.end)