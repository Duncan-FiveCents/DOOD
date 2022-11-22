# main.py

'''
title: DOOD
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame

from window import Window
from raycasting import RayCasting
from player import Player
from line import Line

WINDOW = Window()
RAYS = RayCasting(WINDOW.screen)
PLAYER = Player()

TESTMAP = [Line([200,200],[400,200])]

if __name__ == "__main__":
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()

        RAYS.base(PLAYER.pos,TESTMAP)

        WINDOW.updateFrame()