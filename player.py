# player.py

'''
title: The Dood Man Guy
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
from math import sin,cos,pi

class Player:
    def __init__(self,STARTPOS):
        self.pos = STARTPOS # Player position within the world
        self.speed = 3
        self.angle = pi

    # - Modifiers - #
    def movePlayer(self,PRESSED):
        if PRESSED[pygame.K_LEFT]: self.angle -= 0.1
        if PRESSED[pygame.K_RIGHT]: self.angle += 0.1
        if PRESSED[pygame.K_w]:
            self.pos[0] -= sin(self.angle) * self.speed
            self.pos[1] += cos(self.angle) * self.speed

        if PRESSED[pygame.K_s]:
            self.pos[0] += sin(self.angle) * self.speed
            self.pos[1] -= cos(self.angle) * self.speed

        if PRESSED[pygame.K_a]:
            self.pos[0] += sin(self.angle+pi/2) * self.speed
            self.pos[1] -= cos(self.angle+pi/2) * self.speed
        
        if PRESSED[pygame.K_d]:
            self.pos[0] += sin(self.angle-pi/2) * self.speed
            self.pos[1] -= cos(self.angle-pi/2) * self.speed