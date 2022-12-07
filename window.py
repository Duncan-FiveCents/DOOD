# window.py

'''
title: Michaelsoft Binbows
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame

class Window:
    def __init__(self):
        self.title = "DOOD"
        self.frame = pygame.time.Clock()
        # The game looks at feels better at this low of a resolution
        self.screen = pygame.display.set_mode((640,480),pygame.FULLSCREEN|pygame.SCALED|pygame.HWSURFACE|pygame.DOUBLEBUF,8,0,1)
        self.bg = pygame.Color(0,0,0)
        self.screen.fill(self.bg)
        pygame.display.set_caption(self.title)

    def updateFrame(self):
        self.frame.tick(30)
        pygame.display.flip()

    def clearScreen(self):
        self.screen.fill(self.bg)