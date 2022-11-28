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



game_map = [
    '1111111111',
    '1000000001',
    '1000011111',
    '1000000001',
    '1011100111',
    '1010000001',
    '1010000001',
    '1111111111'
]

WINDOW = Window()

RAYS = RayCasting(WINDOW.screen,5)
PLAYER = Player([WINDOW.screen.get_width()/2,WINDOW.screen.get_width()/2])

if __name__ == "__main__":
    pygame.init()

    while True:
        PRESSED = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or PRESSED[pygame.K_ESCAPE]: # ESC will be used to pause later
                pygame.quit()
                exit()
    
        PLAYER.movePlayer(PRESSED,(WINDOW.screen.get_width()/2,WINDOW.screen.get_height()/2))

        WINDOW.clearScreen()

        RAYS.draw3D()
        RAYS.castRays(game_map,PLAYER.pos,PLAYER.angle)
        
        WINDOW.frame.get_fps()
        FPS = pygame.font.Font(pygame.font.get_default_font(),10)
        WINDOW.screen.blit(FPS.render(str(int(WINDOW.frame.get_fps())),False,(0,0,0)),(0,0))

        # TestHUD, remove later
        HUD = pygame.image.load("UI/UI placeholder.png").convert()
        HUD = pygame.transform.scale2x(HUD)
        WINDOW.screen.blit(HUD,(0,0))

        GUN = pygame.image.load("UI/Gun placeholder.png").convert()
        GUN = pygame.transform.scale2x(GUN)
        WINDOW.screen.blit(GUN,(0,0))

        WINDOW.updateFrame()