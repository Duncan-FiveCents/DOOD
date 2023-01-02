import pygame
import math as m
from settings import *

class RayCasting:
    def __init__(self,GAME):
        self.game = GAME

    def alignGrid(self,x,y): return (x//tilesize)*tilesize,(y//tilesize)*tilesize

    def castRays(self):
        walls = []
        playerX,playerY = self.alignGrid(self.game.player.x,self.game.player.y)
        startAngle = m.radians(self.game.player.angle) - half_fov

        for ray in range((castedRays[quality])):
            rayX,rayY = False,False
            sinAngle = m.sin(startAngle)
            cosAngle = m.cos(startAngle)
            if not sinAngle: sinAngle = 0.00001
            if not cosAngle: cosAngle = 0.00001

            gridX,dirX = (playerX+tilesize,1) if cosAngle >=0 else (playerX,-1)
            for i in range(0,600,tilesize):
                depthY = (gridX - self.game.player.x)/cosAngle
                y = self.game.player.y + depthY * sinAngle
                tileY = self.alignGrid(gridX + dirX,y)
                if tileY in self.game.map.worldMap:
                    textureY = self.game.map.worldMap[tileY]
                    rayY = True
                    break
            
            gridY,dirY = (playerY+tilesize,1) if sinAngle >=0 else (playerY,-1)
            for i in range(0,600,tilesize):
                depthX = (gridY - self.game.player.y)/sinAngle
                x = self.game.player.x + depthX * cosAngle
                tileX = self.alignGrid(x,gridY+dirY)
                if tileX in self.game.map.worldMap:
                    textureX = self.game.map.worldMap[tileX]
                    rayX = True
                    break
            
            if rayX or rayY:
                depth, offset, texture = (depthY,y,textureY) if depthY < depthX else (depthX,x,textureX)
                offset = int(offset) % tilesize
                depth *= m.cos(m.radians(self.game.player.angle)-startAngle)
                projectedHeight = screenDist / depth + 0.00001

                pygame.draw.rect(self.game.screen,(255,255,255),
                    (ray*scale,halfHeight-projectedHeight//2,scale,projectedHeight))

                