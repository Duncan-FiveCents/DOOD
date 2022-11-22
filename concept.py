# concept.py

'''
title: proof of concept/testing for rendering
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
import pygame.gfxdraw

from window import Window

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.screen.fill(WINDOW.bg)
        WINDOW.frame.tick(60)
        pygame.display.flip()