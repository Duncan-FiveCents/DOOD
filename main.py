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
frame = pygame.transform.scale(WINDOW.screen,(800,600))

RAYS = RayCasting(WINDOW.screen)
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

        frame = pygame.transform.scale(WINDOW.screen,(800,600))
        WINDOW.screen.blit(frame,frame.get_rect())

        WINDOW.updateFrame()