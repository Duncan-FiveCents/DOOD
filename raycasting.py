# raycasting.py

'''
title: this is gonna suck to make
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
from math import sin, cos, tan, pi
from resource_path import resource_path

# I had to jump between tutorials and modify things to work with our mechanics
# So I can't take full credit for this, but it wasn't like I copy-pasted it in and it just worked
class RayCasting:
    def __init__(self,SCREEN,QUALITY,MINIMAP):
        self.surface = SCREEN
        self.height = self.surface.get_height()
        self.width = self.surface.get_width()

        self.mapSize = 40
        self.tileSize = 1600 / self.mapSize

        self.FOV = pi / 2 # Math uses radians by default, so this comes out to 90 degrees
        self.half_FOV = self.FOV / 2 # Yes this is used often enough to warrant this

        PRESETS = {1:32,2:80,3:128,4:160}

        self.castedRays = PRESETS[QUALITY] # Number of rays to be cast, user can select this
        self.stepAngle = self.FOV / self.castedRays
        self.maxDepth = self.mapSize * self.tileSize # Prevents the ray from casting out of bounds

        self.scale = self.width // self.castedRays
        self.wallHeight = 4 * (self.castedRays / (2*tan(self.half_FOV))) * self.scale

        self.textures = {
            "1":pygame.image.load(resource_path("textures/wall-texture-1.png")).convert()
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
        pygame.draw.line(self.minimap,(255,255,255),((PLAYERRECT.centerx,PLAYERRECT.centery)),(PLAYERRECT.centerx-sin(PLAYERANGLE)*30,PLAYERRECT.centery+cos(PLAYERANGLE)*50),3)
    
    def draw3D(self): # Maybe put the other 3D rendering code into here?
        # Ceiling and floor
        pygame.draw.rect(self.surface,(100,100,150),(0,self.height/3,self.surface.get_width(),self.height)) # Floor
        pygame.draw.rect(self.surface,(55,55,175),(0,-self.height/1.75,self.surface.get_width(),self.height)) # Ceiling

    def alignGrid(self,x,y):
        """Aligns the given coordinates to the nearest grid line (helps optimisation)

        Args:
            x (int): starting x coordinate
            y (int): starting y coordinate

        Returns:
            int: aligned x coordinate
            int: aligned y coordinate
        """
        return (x//self.tileSize) * self.tileSize, (y//self.tileSize) * self.tileSize

    def castRays(self,MAP,PLAYER,SPRITES): # This is where the fun begins
        playerX, playerY = self.alignGrid(PLAYER.rect.centerx,PLAYER.rect.centery)
        currentAngle = PLAYER.angle - self.half_FOV
        textureX, textureY = self.alignGrid(1,1), self.alignGrid(1,1) # Placeholder values
        
        for ray in range(self.castedRays):
            rayX, rayY = False, False
            sinAngle = sin(currentAngle)
            cosAngle = cos(currentAngle)
            # Prevents zero values
            if not sinAngle: sinAngle = 0.000001
            if not cosAngle: cosAngle = 0.000001

            # Y axis walls
            gridX,dirX = (playerX + self.tileSize,1) if cosAngle >= 0 else (playerX,-1)
            for i in range(0,1600,int(self.tileSize)):
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
                depth *= cos(PLAYER.angle - currentAngle)
                depth = max(depth, 0.000001) # Prevents a zero value
                projectedHeight = min(int(self.wallHeight/depth), 2 * 480)

                print((offset * (640 // self.tileSize),0,(640 // self.tileSize),480))
                wallColumn = self.textures[texture].subsurface(offset * (480 // self.tileSize),0,(640 // self.tileSize),480)
                wallColumn = pygame.transform.scale(wallColumn,(self.scale,projectedHeight))
                self.surface.blit(wallColumn,(ray * self.scale,240 - projectedHeight // 2))
            
            currentAngle += self.stepAngle

