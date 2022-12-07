# level.py

'''
title: Level layout and data
author: Duncan Nickel
date-created: 07/12/2022
'''

import pygame

class Level:
    def __init__(self,LAYOUT,START_X,START_Y):
        self.layout = LAYOUT
        self.tileSize = 1600 / 40
        self.start = (START_X*self.tileSize,START_Y*self.tileSize)
        
        self.rects = [] # Currently just used internally for collision detection
        for i in range(len(LAYOUT)):
            for j in range(len(LAYOUT)):
                if self.layout[i][j] in ["1","2","3"]:
                    self.rects.append(pygame.rect.Rect(
                        i * self.tileSize,
                        j * self.tileSize,
                        self.tileSize,
                        self.tileSize
                    ))