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
        self.rect = pygame.rect.Rect(STARTPOS[0],STARTPOS[1],10,10)
        self.speed = 3
        self.angle = pi

        self.sensitivityMult = 5 # Higher number, lower sensitity. We'll probably just use presets for this to avoid confusion

        self.activeWeapon = 1
        self.cooldown = 0

    # - Modifiers - #
    def movePlayer(self,PRESSED,SCREEN_CENTER):
        """Move the player around with WASD and the arrow keys to turn (maybe mouse later)

        Args:
            PRESSED (list): pygame ist of pressed keys
            SCREEN_CENTER (list): Coordinates of the center of the screen
        """
        # Mouse Movement 
        pygame.mouse.set_visible(False) # Makes mouse invisible during gameplay
        mouseMoved = pygame.mouse.get_rel() # Gets distance of mouse movement in pixels
        print(mouseMoved)
        self.angle += (mouseMoved[0]/100*(1/self.sensitivityMult)) # Turns the character
        pygame.mouse.set_pos(SCREEN_CENTER) # Moves the mouse to the center of the screen


        # Turning with arrow keys
        if PRESSED[pygame.K_LEFT]: self.angle -= 0.1
        if PRESSED[pygame.K_RIGHT]: self.angle += 0.1

        # WASD Movement
        if PRESSED[pygame.K_w]:
            # Pygame rects don't allow float coordinates, so rounding it prevents the player from moving sideways if the angle is just slightly off
            self.rect.centerx -= round(sin(self.angle) * self.speed)
            self.rect.centery += round(cos(self.angle) * self.speed)
        if PRESSED[pygame.K_s]:
            self.rect.centerx += round(sin(self.angle) * self.speed)
            self.rect.centery -= round(cos(self.angle) * self.speed)
        if PRESSED[pygame.K_a]:
            self.rect.centerx += round(sin(self.angle+pi/2) * self.speed)
            self.rect.centery -= round(cos(self.angle+pi/2) * self.speed)
        if PRESSED[pygame.K_d]:
            self.rect.centerx += round(sin(self.angle-pi/2) * self.speed)
            self.rect.centery -= round(cos(self.angle-pi/2) * self.speed)
        
        # Collision

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