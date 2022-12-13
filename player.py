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
        self.rect = pygame.rect.Rect(STARTPOS[0],STARTPOS[1],20,20)
        self.speed = 1
        self.angle = pi/2

        self.sensitivityMult = 5 # Higher number, lower sensitity. We'll probably just use presets for this to avoid confusion

        self.activeWeapon = 1
        self.cooldown = 0

        self.health = 100
        self.sheild = 100

    # - Modifiers - #
    def movePlayer(self,PRESSED,MAP):
        """Move the player around with WASD

        Args:
            PRESSED (list): pygame ist of pressed keys
            MAP (list): list of map rects for collision
        """

        # WASD Movement

        currentPos = self.rect.center

        if PRESSED[pygame.K_w]:
            # Pygame rects don't allow float coordinates, so rounding it prevents the player from moving sideways if the angle is just slightly off
            # It does cause the player to move unnaturally at times, but I had no better solution
            self.rect.centerx -= round(sin(self.angle) * self.speed)
            # This collision code is hilariously ineffecient as it checks EVERY WALL ON THE MAP, but it works
            for i in range(len(MAP)):
                if MAP[i].collidepoint(self.rect.center): self.rect.centerx = currentPos[0]
            self.rect.centery += round(cos(self.angle) * self.speed)
            for i in range(len(MAP)):
                if MAP[i].collidepoint(self.rect.center): self.rect.centery = currentPos[1]
        if PRESSED[pygame.K_s]:
            self.rect.centerx += round(sin(self.angle) * self.speed)
            for i in range(len(MAP)):
                if MAP[i].collidepoint(self.rect.center): self.rect.centerx = currentPos[0]
            self.rect.centery -= round(cos(self.angle) * self.speed)
            for i in range(len(MAP)):
                if MAP[i].collidepoint(self.rect.center): self.rect.centery = currentPos[1]
        if PRESSED[pygame.K_a]:
            self.rect.centerx += round(sin(self.angle+pi/2) * self.speed)
            for i in range(len(MAP)):
                if MAP[i].collidepoint(self.rect.center): self.rect.centerx = currentPos[0]
            self.rect.centery -= round(cos(self.angle+pi/2) * self.speed)
            for i in range(len(MAP)):
                if MAP[i].collidepoint(self.rect.center): self.rect.centery = currentPos[1]
        if PRESSED[pygame.K_d]:
            self.rect.centerx += round(sin(self.angle-pi/2) * self.speed)
            for i in range(len(MAP)):
                if MAP[i].collidepoint(self.rect.center): self.rect.centerx = currentPos[0]
            self.rect.centery -= round(cos(self.angle-pi/2) * self.speed)
            for i in range(len(MAP)):
                if MAP[i].collidepoint(self.rect.center): self.rect.centery = currentPos[1]


    def turnPlayer(self,PRESSED,SCREENCENTER):
        """Turns the player either with the mouse or with the arrow keys

        Args:
            PRESSED (list): Pygame list of pressed keys
            SCREENCENTER (list): Coordinates of the center of the screen
        """
        # Mouse Movement
        pygame.mouse.set_visible(False) # Makes mouse invisible during gameplay
        mouseMoved = pygame.mouse.get_rel() # Gets distance of mouse movement in pixels
        self.angle += (mouseMoved[0]/100/self.sensitivityMult) # Turns the character
        pygame.mouse.set_pos(SCREENCENTER) # Locks the mouse to the center of the screen

        # Turning with arrow keys
        if PRESSED[pygame.K_LEFT]: self.angle -= 0.1 * 5  / self.sensitivityMult
        if PRESSED[pygame.K_RIGHT]: self.angle += 0.1 * 5 / self.sensitivityMult

    def swapWeapon(self,WEAPON):
        if WEAPON == 1 and self.activeWeapon != 1:
            self.activeWeapon = 1
        elif WEAPON == 2 and self.activeWeapon != 2:
            self.activeWeapon = 2
        elif WEAPON == 3 and self.activeWeapon != 3:
            self.activeWeapon = 3
        elif WEAPON == 4 and self.activeWeapon != 4:
            self.activeWeapon = 4
    
    def pewpew(self):
        pass