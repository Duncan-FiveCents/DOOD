# main.py

'''
title: DOOD
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
from math import sin,cos

from window import Window
from raycasting import RayCasting
from player import Player



game_map = [
    '11111111',
    '10000001',
    '10000111',
    '10000001',
    '10100001',
    '10100001',
    '10100001',
    '11111111',
    
]

WINDOW = Window()

RAYS = RayCasting(WINDOW.screen)
PLAYER = Player([(WINDOW.screen.get_width()/2)/2,(WINDOW.screen.get_width()/2)/2]) # Remove the extra /2 later, its for the map view

if __name__ == "__main__":
    pygame.init()

    while True:
        PRESSED = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        # Move this into player.py later
        speed = 3
        if PRESSED[pygame.K_a]: PLAYER.angle -= 0.1
        if PRESSED[pygame.K_d]: PLAYER.angle += 0.1
        if PRESSED[pygame.K_w]:
            PLAYER.pos[0] -= sin(PLAYER.angle) * speed
            PLAYER.pos[1] += cos(PLAYER.angle) * speed

        if PRESSED[pygame.K_s]:
            PLAYER.pos[0] += sin(PLAYER.angle) * speed
            PLAYER.pos[1] -= cos(PLAYER.angle) * speed

        WINDOW.clearScreen()

        RAYS.drawMap(game_map,PLAYER.pos,PLAYER.angle)
        RAYS.draw3D()
        RAYS.castRays(game_map,PLAYER.pos,PLAYER.angle)

        WINDOW.updateFrame()