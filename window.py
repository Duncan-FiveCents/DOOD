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
        self.frame = pygame.time.Clock() # clock object that measures fps
        self.screen = pygame.display.set_mode((800,400))
        self.bg = pygame.Color(0,0,0)
        self.screen.fill(self.bg)
        pygame.display.set_caption(self.title) # sets the title of the window to title value

    def updateFrame(self):
        self.frame.tick(60)
        pygame.display.flip()

    def clearScreen(self):
        self.screen.fill(self.bg)