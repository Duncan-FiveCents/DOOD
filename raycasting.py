import pygame
import math as m
from settings import *

class RayCasting:
    def __init__(self,GAME):
        self.game = GAME
        self.renderObjects = []
        self.textures = self.game.renderer.textures

    def castRays(self):
        self.renderObjects = []
        playerX,playerY = self.game.player.x,self.game.player.y
        mapX,mapY = int(playerX),int(playerY)
        startAngle = self.game.player.angle - half_fov + 0.00001
        verticalTexture,horizontalTexture = "1","1"

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
                    horizontalTexture = self.game.map.worldMap[horizontalTile]
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
                    verticalTexture = self.game.map.worldMap[verticalTile]
                    break
                vertX += dirX
                vertY += dirY
                verticalDepth += deltaDepth


            if verticalDepth < horizontalDepth:
                depth, texture = verticalDepth, verticalTexture
                vertY %= 1
                offset = vertY if cosAngle > 0 else (1-vertY)
            else:
                depth, texture = horizontalDepth, horizontalTexture
                horzX %= 1
                offset = (1-horzX) if sinAngle > 0 else horzX
            
            depth *= m.cos(self.game.player.angle - startAngle)

            projectedHeight = screenDist / depth + 0.00001
            projectedHeight = min(projectedHeight,resY*2)

            wallColumn = self.textures[texture].subsurface(offset * (480-scale),0,scale,480)
            wallColumn = pygame.transform.scale(wallColumn,(scale,projectedHeight))
            wallPosition = (ray * scale,(240 - projectedHeight // 2)*0.85)

            self.renderObjects.append((depth,wallColumn,wallPosition))

            startAngle += stepAngle