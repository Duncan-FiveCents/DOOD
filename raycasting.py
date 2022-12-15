# raycasting.py

'''
title: this is gonna suck to make
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
from math import sin, cos, tan, atan2, sqrt, pi, degrees
from common import *

# I had to jump between a couple tutorials and modify things to work with our mechanics
# So I can't take full credit for this, but it wasn't like I copy-pasted it in and it just worked
class RayCasting:
    def __init__(self,SCREEN,QUALITY,MINIMAP):
        self.surface = SCREEN
        self.height = self.surface.get_height()
        self.width = self.surface.get_width()

        self.tileSize = 18

        self.FOV = pi / 2 # Math uses radians by default, so this comes out to 90 degrees
        self.half_FOV = self.FOV / 2 # Yes this is used often enough to warrant this

        PRESETS = {1:32,2:80,3:128,4:160,5:320}

        self.castedRays = PRESETS[QUALITY] # Number of rays to be cast, user can select this
        self.stepAngle = self.FOV / self.castedRays # Angle to rotate between rays

        self.scale = self.width // self.castedRays # Scales textures and stuff to the right width
        self.wallHeight = 4 * (self.castedRays / (2*tan(self.half_FOV))) * self.scale # Sets max wall height

        self.spriteRays = 100 # Raycasting for sprites is handled seperately
        self.spriteRaysRange = self.castedRays - 1 + 2 * self.spriteRays

        self.textures = {
            "1":pygame.image.load(resource_path("textures/wall-texture-1.png")).convert(),
            "2":pygame.image.load(resource_path("textures/wall-texture-2.png")).convert()
        }

        self.minimap = MINIMAP

    # - Modifiers? I guess? - #
    def drawMap(self,MAP,PLAYERRECT,PLAYERANGLE): # Minimap idea: make map move around player???
        pygame.draw.rect(self.minimap,(100,100,100),(0,0,1600,1600))
        for i in range(len(MAP)):
            pygame.draw.rect(
                self.minimap,
                (200,200,200),
                MAP[i]
            )

        pygame.draw.rect(self.minimap,(255,0,0),PLAYERRECT)
    
    def draw3D(self): # Maybe put the other 3D rendering code into here?
        # Ceiling and floor
        pygame.draw.rect(self.surface,(100,100,150),(0,self.height/3,self.surface.get_width(),self.height)) # Floor
        pygame.draw.rect(self.surface,(55,55,175),(0,-self.height/1.75,self.surface.get_width(),self.height)) # Ceiling

    def alignGrid(self,x,y):
        """Aligns the given coordinates to the nearest grid line (helps with raycasting optimisation)

        Args:
            x (int): starting x coordinate
            y (int): starting y coordinate

        Returns:
            int: aligned x coordinate
            int: aligned y coordinate
        """
        return (x//self.tileSize) * self.tileSize, (y//self.tileSize) * self.tileSize

    def castRays(self,MAP,PLAYER): # I rewrote this too many times
        walls = []
        playerX, playerY = self.alignGrid(PLAYER.rect.centerx,PLAYER.rect.centery)
        startAngle = PLAYER.angle - self.half_FOV
        textureX, textureY = MAP[self.alignGrid(1,1)], MAP[self.alignGrid(1,1)] # Placeholder values

        for ray in range(self.castedRays):
            rayX, rayY = False, False
            sinAngle = sin(startAngle + pi/2)
            cosAngle = cos(startAngle + pi/2)
            # Prevents zero values
            if not sinAngle: sinAngle = 0.00001
            if not cosAngle: cosAngle = 0.00001

            # Y axis walls
            gridX,dirX = (playerX + self.tileSize,1) if cosAngle >= 0 else (playerX,-1)
            for i in range(0,1600,int(self.tileSize)): # 1600 is the maximum render distance in pixels (map is 1600x1600, so long hallways will always render)
                depthY = (gridX - PLAYER.rect.centerx) / cosAngle
                y = PLAYER.rect.centery + depthY * sinAngle
                tileY = self.alignGrid(gridX + dirX,y)
                if tileY in MAP:
                    textureY = MAP[tileY]
                    rayY = True
                    break
                gridX += dirX * self.tileSize
            
            # X axis walls
            gridY,dirY = (playerY + self.tileSize,1) if sinAngle >= 0 else (playerY,-1)
            for i in range(0,1600,int(self.tileSize)):
                depthX = (gridY - PLAYER.rect.centery) / sinAngle
                x = PLAYER.rect.centerx + depthX * cosAngle
                tileX = self.alignGrid(x,gridY + dirY)
                if tileX in MAP:
                    textureX = MAP[tileX]
                    rayX = True
                    break
                gridY += dirY * self.tileSize

            # Rendering time!!
            if rayX or rayY:
                depth, offset, texture = (depthY, y, textureY) if depthY < depthX else (depthX, x, textureX)
                offset = int(offset) % self.tileSize
                depth *= cos(PLAYER.angle - startAngle)
                depth /= 4
                depth = max(depth, 0.00001) # Prevents a zero value
                projectedHeight = min(int(self.wallHeight/depth), 2 * 480)

                wallColumn = self.textures[texture].subsurface(offset * (480 // self.tileSize),0,(480 // self.tileSize),480)
                wallColumn = pygame.transform.scale(wallColumn,(self.scale,projectedHeight))
                wallPosition = (ray * self.scale,(240 - projectedHeight // 2)*0.85) # The multiplier at the end adjusts the "height" of the player

                walls.append([depth,wallColumn,wallPosition])            

            startAngle += self.stepAngle
        
        return walls

    def castSprites(self,PLAYER,SPRITE):
        centerRay = self.castedRays // 2 - 1
        distanceX,distanceY = SPRITE.rect.centerx - PLAYER.rect.centerx, SPRITE.rect.centery - PLAYER.rect.centery
        totalDistance = sqrt(distanceX**2 + distanceY**2) # Simple pythagoras to find the distance from the player to the sprite

        angle = atan2(distanceY,distanceX)
        offsetAngle = angle - PLAYER.angle

        if distanceX > 0 and 180 <= degrees(PLAYER.angle) <= 360 or distanceX < 0 and distanceY < 0: offsetAngle += pi*2 

        deltaRays = int(offsetAngle/self.stepAngle)
        currentRay = centerRay + deltaRays
        totalDistance *= cos(self.half_FOV - centerRay * self.stepAngle)

        spriteRay = currentRay + self.spriteRays
        if 0 <= spriteRay <= self.spriteRaysRange and totalDistance > 30: # No idea what the 30 does, I should look into that
            projectedHeight = min(int(self.wallHeight/totalDistance*self.scale),480*2)
            offset = projectedHeight//2 * SPRITE.shift

            spriteSurface = pygame.transform.scale(SPRITE.image,(projectedHeight,projectedHeight))
            spritePosition = (currentRay*self.scale-projectedHeight//2,(240-projectedHeight//2)+offset)

            return totalDistance, spriteSurface, spritePosition
        else: return False

    def drawObjects(self,OBJECTS):
        SORT_STUFF = []
        for i in range(len(OBJECTS[0])): SORT_STUFF.append(OBJECTS[0][i])
        SORT_STUFF = quickSort(SORT_STUFF,0,len(SORT_STUFF)-1)

        for object in SORT_STUFF:
            AAAAAA, objectSurface, objectPos = object
            self.surface.blit(objectSurface,objectPos)