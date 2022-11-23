# raycasting.py

'''
title: this is gonna suck to make
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
import pygame.gfxdraw
from math import sin, cos, pi

# I had to jump between tutorials and modify things to work with our mechanics
# So I can't take full credit for this, but it wasn't like I copy-pasted it in and it just worked
class RayCasting:
    def __init__(self,SCREEN):
        self.surface = SCREEN
        self.height = SCREEN.get_height()
        self.width = SCREEN.get_width()

        self.mapSize = 20 # Width and height of map in tiles
        self.tileSize = 20 # Should theoretically be dependent on window size, but I don't plan to change that

        self.FOV = pi / 2 # This is 90 degrees
        self.half_FOV = self.FOV / 2

        self.castedRays = 50 # Number of rays to be cast
        self.stepAngle = self.FOV / self.castedRays
        self.maxDepth = self.mapSize * self.tileSize # Prevents the ray from casting out of bounds

        self.scale = self.surface.get_width() / 2 / self.castedRays

    # - Modifiers? I guess? - #
    def drawMap(self,MAP,PLAYERPOS,PLAYERANGLE): # For testing purposes. Either make into a minimap, or remove entirely.
        for i in range(self.mapSize): # Rows
            for j in range(self.mapSize): # Columns
                pygame.draw.rect(
                    self.surface,
                    (200,200,200) if MAP[i][j] in ["1","2","3"] else (100,100,100),
                    (j*self.tileSize,i*self.tileSize,self.tileSize,self.tileSize)
                )

        pygame.draw.circle(self.surface,(255,0,0),PLAYERPOS,8)
        pygame.draw.line(self.surface,(255,255,255),(PLAYERPOS),(PLAYERPOS[0]-sin(PLAYERANGLE)*30,PLAYERPOS[1]+cos(PLAYERANGLE)*50),3)

        pygame.draw.line(self.surface,(0,255,0),(PLAYERPOS),(PLAYERPOS[0]-sin(PLAYERANGLE+self.half_FOV)*50,PLAYERPOS[1]+cos(PLAYERANGLE+self.half_FOV)*50),3)
        pygame.draw.line(self.surface,(0,255,0),(PLAYERPOS),(PLAYERPOS[0]-sin(PLAYERANGLE-self.half_FOV)*50,PLAYERPOS[1]+cos(PLAYERANGLE-self.half_FOV)*50),3)
    
    def draw3D(self):
        pygame.draw.rect(self.surface,(100,100,100),(self.surface.get_width()/2,self.surface.get_height()/2,self.surface.get_width(),self.surface.get_height()))
        pygame.draw.rect(self.surface,(200,200,200),(self.surface.get_width()/2,-self.surface.get_height()/2,self.surface.get_width(),self.surface.get_height()))

    def castRays(self,MAP,PLAYERPOS,PLAYERANGLE): # This is where the fun begins.
        startAngle = PLAYERANGLE - self.half_FOV
        
        for ray in range(self.castedRays):
            for depth in range(self.maxDepth):
                targetX = PLAYERPOS[0] - sin(startAngle) * depth
                targetY = PLAYERPOS[1] + cos(startAngle) * depth

                column = int(targetX/self.tileSize)
                row = int(targetY/self.tileSize)

                if MAP[row][column] in ["1","2","3"]:
                    pygame.draw.rect(
                    self.surface,
                    (0,255,0),
                    (column*self.tileSize,row*self.tileSize,self.tileSize,self.tileSize))

                    pygame.draw.line(self.surface,(255,255,0),(PLAYERPOS),(targetX,targetY))

                    # Fixes the weird fish eye effect
                    depth *= cos(PLAYERANGLE-startAngle)

                    wallHeight = 10000 / (depth+0.0001) # Decimal is to prevent accidentally dividing by zero
                    colour = 255/(1+depth*depth*0.0001)
                    if wallHeight > self.surface.get_height(): wallHeight = self.surface.get_height()
                    pygame.draw.rect(self.surface,(colour,colour,colour),(self.surface.get_height()+ray*self.scale,(self.surface.get_height()/2)-wallHeight/2,self.scale,wallHeight))

                    break

            startAngle += self.stepAngle