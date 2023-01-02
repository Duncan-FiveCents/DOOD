import pygame
import math as m
from settings import *

class RayCasting:
    def __init__(self,GAME):
        self.game = GAME

    def castRays(self):
        walls = []
        playerX,playerY = self.game.player.x,self.game.player.y
        mapX,mapY = int(playerX),int(playerY)
        startAngle = self.game.player.angle - half_fov + 0.00001

        for ray in range(castedRays):
            sinAngle = m.sin(startAngle)
            cosAngle = m.cos(startAngle)
            if not sinAngle: sinAngle = 0.00001
            if not cosAngle: cosAngle = 0.00001

            # Horizontals
            horzY,dirY = (mapY+1,1) if sinAngle >= 0 else (mapY-0.00001,-1)

            horizontalDepth = (horzY - playerY) / sinAngle
            horzX = playerX + horizontalDepth * cosAngle

            deltaDepth = dirY / sinAngle
            dirX = deltaDepth * cosAngle

            for i in range(40):
                horizontalTile = int(horzX),int(horzY)
                if horizontalTile in self.game.map.worldMap:
                    break
                horzX += dirX
                horzY += dirY
                horizontalDepth += deltaDepth

            # Verticals
            vertX,dirX = (mapX+1,1) if cosAngle >= 0 else (mapX-0.00001,-1)
            
            verticalDepth = (vertX - playerX) / cosAngle
            vertY = playerY + verticalDepth * sinAngle

            deltaDepth = dirX / cosAngle
            dirY = deltaDepth * sinAngle

            for i in range(40):
                verticalTile = int(vertX),int(vertY)
                if verticalTile in self.game.map.worldMap:
                    break
                vertX += dirX
                vertY += dirY
                verticalDepth += deltaDepth

            depth = min(verticalDepth,horizontalDepth)

            pygame.draw.line(self.game.screen,(255,255,0),(tilesize*self.game.player.x,tilesize*self.game.player.y),(tilesize*self.game.player.x+tilesize*depth*cosAngle,tilesize*self.game.player.y+tilesize*depth*sinAngle),1)

            projectedHeight = screenDist / depth + 0.00001

            #pygame.draw.rect(self.game.screen,(255,255,255),
                #(ray*scale,halfHeight-projectedHeight//2,scale,projectedHeight))

            startAngle += stepAngle