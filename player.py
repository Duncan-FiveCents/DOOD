# player.py

'''
title: The Dood Man Guy
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
from math import sin,cos,pi,radians
from common import *

class Player:
    def __init__(self,STARTPOS):
        self.rect = pygame.rect.Rect(STARTPOS[0],STARTPOS[1],20,20)
        self.velocity = 0
        self.angle = 90

        self.sensitivityMult = 5 # Higher number, lower sensitity. We'll probably just use presets for this to avoid confusion

        self.activeWeapon = 1
        self.cooldown = 0

        self.health = 100
        self.sheild = 100

        self.minimapIcon = pygame.image.load(resource_path("UI\dood map sprite.png")).convert()

    # - Modifiers - #
    def movePlayer(self,PRESSED,MAP):
        """Move the player around with WASD

        Args:
            PRESSED (list): pygame ist of pressed keys
            MAP (list): list of map rects for collision
        """

        # WASD Movement

        currentPos = self.rect.center
        self.angle %= 360 # Resets the angle to a value between 0 and 360
        moved = False

        if PRESSED[pygame.K_w]:
            # Pygame rects don't allow float coordinates, so rounding it prevents the player from moving sideways if the angle is just slightly off
            # It does cause the player to move unnaturally at times, but I had no better solution
            if not self.velocity > 2: self.velocity += 0.5
            self.rect.centerx -= round(sin(radians(self.angle)) * self.velocity)
            self.rect.centery += round(cos(radians(self.angle)) * self.velocity)
            moved = True
        if PRESSED[pygame.K_s]:
            if not self.velocity > 2: self.velocity += 0.5
            self.rect.centerx += round(sin(radians(self.angle)) * self.velocity)
            self.rect.centery -= round(cos(radians(self.angle)) * self.velocity)
            moved = True
        if PRESSED[pygame.K_a]:
            if not self.velocity > 2: self.velocity += 0.5
            self.rect.centerx += round(sin(radians(self.angle)+pi/2) * self.velocity)
            self.rect.centery -= round(cos(radians(self.angle)+pi/2) * self.velocity)
            moved = True
        if PRESSED[pygame.K_d]:
            if not self.velocity > 2: self.velocity += 0.5
            self.rect.centerx += round(sin(radians(self.angle)-pi/2) * self.velocity)
            self.rect.centery -= round(cos(radians(self.angle)-pi/2) * self.velocity)
            moved = True
        
        # Hilariously ineffecient collision code since it checks every wall on the map
        for i in range(len(MAP)):
            if MAP[i].collidepoint(self.rect.center): self.rect.centerx = currentPos[0]
        for i in range(len(MAP)):
            if MAP[i].collidepoint(self.rect.center): self.rect.centery = currentPos[1]

        # The player currently accelerates properly, but deccelerates instantly
        # I might fix this later, we'll see
        if self.velocity != 0: self.velocity -= 0.25
        if not moved: self.velocity = 0

    def turnPlayer(self,PRESSED,SCREENCENTER):
        """Turns the player either with the mouse or with the arrow keys

        Args:
            PRESSED (list): Pygame list of pressed keys
            SCREENCENTER (list): Coordinates of the center of the screen
        """
        # Mouse Movement
        pygame.mouse.set_visible(False) # Makes mouse invisible during gameplay
        mouseMoved = pygame.mouse.get_rel() # Gets distance of mouse movement in pixels
        self.angle += (mouseMoved[0]/self.sensitivityMult) # Turns the character
        pygame.mouse.set_pos(SCREENCENTER) # Locks the mouse to the center of the screen

        # Turning with arrow keys
        if PRESSED[pygame.K_LEFT]: self.angle -= 10
        if PRESSED[pygame.K_RIGHT]: self.angle += 10

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