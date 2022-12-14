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
        self.tileSize = 18
        self.start = (START_X*self.tileSize,START_Y*self.tileSize)

        self.rects = [] # Used for collision detection and minimap rendering
        for i in range(len(LAYOUT)):
            for j in range(len(LAYOUT)):
                if self.layout[i][j] in ["1","2","3"]:
                    self.rects.append(pygame.rect.Rect(
                        j * self.tileSize,
                        i * self.tileSize,
                        self.tileSize,
                        self.tileSize
                    ))
        
        # Stuff needed for raycasting
        self.worldMap = {}
        for i, row in enumerate(self.layout):
            for j, char in enumerate(row):
                if char != "0":
                    if char == "1": self.worldMap[(j*self.tileSize,i*self.tileSize)] = "1"
                    elif char == "2": self.worldMap[(j*self.tileSize,i*self.tileSize)] = "2"
                    elif char == "3": self.worldMap[(j*self.tileSize,i*self.tileSize)] = "3"
