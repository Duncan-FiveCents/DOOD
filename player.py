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

        self.sensitivityMult = 5 # Higher number, lower sensitity. We'll probably just use presets for this to avoid confusion
        pygame.mouse.set_visible(False)

    # - Modifiers - #
    def movePlayer(self,PRESSED,SCREEN_CENTER):
        """Move the player around with WASD and the arrow keys to turn (maybe mouse later)

        Args:
            PRESSED (list): pygame ist of pressed keys
        """
        # Mouse Movement 
        mouseMoved = pygame.mouse.get_rel()

        self.angle += (mouseMoved[0]/100*(1/self.sensitivityMult))

        pygame.mouse.set_pos(SCREEN_CENTER)

        # WASD
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