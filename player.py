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
        mouseMoved = pygame.mouse.get_rel() # Gets distance of mouse movement in pixels
        self.angle += (mouseMoved[0]/100*(1/self.sensitivityMult)) # Turns the character
        pygame.mouse.set_pos(SCREEN_CENTER) # Moves the mouse to the center of the screen

        # Turning with arrow keys
        if PRESSED[pygame.K_LEFT]: self.angle -= 0.1
        if PRESSED[pygame.K_RIGHT]: self.angle += 0.1

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

    def collision(self, MAP, MAPSIZE, TILESIZE, PRESSED):
        """
        Makes sure the player can't just walk through walls
        :param MAPSIZE: int
        :param TILESIZE: int
        :return: None (?)
        """
        for i in range(MAPSIZE): # map rows
            for j in range(MAPSIZE): # map columns
                if MAP[i][j] in ["1", "2", "3"]:
                    if PRESSED[pygame.K_w]:

