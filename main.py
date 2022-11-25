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
    '11111111111111111111',
    '10000000011111111111',
    '10000111111111111111',
    '10000000011111111111',
    '10111001111111111111',
    '10100000011111111111',
    '10100000011111111111',
    '10000000000000000001',
    '10000000000000000001',
    '10000000000000000001',
    '10000000000000000001',
    '10000000000000000001',
    '10000000000000000001',
    '10000000000000000001',
    '11111111111111111111',
    '11111111111111111111',
    '11111111111111111111',
    '11111111111111111111'
    
]

WINDOW = Window()

RAYS = RayCasting(WINDOW.screen)
PLAYER = Player([WINDOW.screen.get_width()/2,WINDOW.screen.get_width()/2])

if __name__ == "__main__":
    pygame.init()

    while True:
        PRESSED = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        PLAYER.movePlayer(PRESSED)

        WINDOW.clearScreen()

        RAYS.draw3D()
        RAYS.castRays(game_map,PLAYER.pos,PLAYER.angle)

        WINDOW.updateFrame()