# main.py

'''
title: DOOD
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
from math import sin,cos,pi

from window import Window
from raycasting import RayCasting
from player import Player
from userInterface import HUD



game_map = [
    '1111111111',
    '1000000001',
    '1000011111',
    '1000000001',
    '1011100111',
    '1010000001',
    '1010000001',
    '1000000001',
    '1000000001',
    '1111111111'
]

WINDOW = Window()

RAYS = RayCasting(WINDOW.screen,4,len(game_map))
PLAYER = Player([WINDOW.screen.get_width()/2,WINDOW.screen.get_width()/2])
UI = HUD(WINDOW)

if __name__ == "__main__":
    pygame.init()

    while True:
        PRESSED = pygame.key.get_pressed()
        MOUSE = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or PRESSED[pygame.K_ESCAPE]: # ESC will be used to pause later
                pygame.quit()
                exit()
    
        if PRESSED[pygame.K_SPACE] or MOUSE[0]:
            PLAYER.pewpew()

        PLAYER.movePlayer(PRESSED,(WINDOW.screen.get_width()/2,WINDOW.screen.get_height()/2))

        WINDOW.clearScreen()

        RAYS.draw3D()
        RAYS.castRays(game_map,PLAYER.pos,PLAYER.angle)

        # User Interface
        UI.mainHud(None,None,True)

        if PRESSED[pygame.K_SPACE] or MOUSE[0]: UI.weaponHud(PLAYER.activeWeapon,True)
        else: UI.weaponHud(PLAYER.activeWeapon,False)

        WINDOW.updateFrame()