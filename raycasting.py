# raycasting.py

'''
title: this is gonna suck to make
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
from math import sin, cos, atan2, pi, sqrt
from resource_path import resource_path

# I had to jump between tutorials and modify things to work with our mechanics
# So I can't take full credit for this, but it wasn't like I copy-pasted it in and it just worked
class RayCasting:
    def __init__(self,SCREEN,QUALITY,MINIMAP):
        self.surface = SCREEN
        self.height = self.surface.get_height()
        self.width = self.surface.get_width()

        self.mapSize = 40
        self.tileSize = int(1600 / self.mapSize)

        self.FOV = pi / 2 # Math uses radians by default, so this comes out to 90 degrees
        self.half_FOV = self.FOV / 2 # Yes this is used often enough to warrant this

        PRESETS = {1:32,2:80,3:128,4:160}

        self.castedRays = PRESETS[QUALITY] # Number of rays to be cast, user can select this
        self.stepAngle = self.FOV / self.castedRays
        self.maxDepth = self.mapSize * self.tileSize # Prevents the ray from casting out of bounds

        self.scale = self.width / self.castedRays

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
        pygame.draw.rect(self.surface,(100,100,100),(0,self.height/3,self.surface.get_width(),self.height))
        pygame.draw.rect(self.surface,(200,200,200),(0,-self.height/1.75,self.surface.get_width(),self.height))

    def castRays(self,MAP,PLAYER,SPRITES): # This is where the fun begins
        startAngle = PLAYER.angle - self.half_FOV
        
        for ray in range(self.castedRays):
            for depth in range(self.maxDepth):
                # Find the next square that the ray hits
                targetX = PLAYER.rect.centerx - sin(startAngle) * depth
                targetY = PLAYER.rect.centery + cos(startAngle) * depth

                column = int(targetX/self.tileSize)
                row = int(targetY/self.tileSize)

                depthX = (column - PLAYER.rect.centerx) / cos(startAngle)
                depthY = (row - PLAYER.rect.centery) / sin(startAngle)

                if MAP[row][column] in ["1","2","3"] and depthX > 0:
                    # Fixes the weird fish eye effect
                    depth *= cos(PLAYER.angle-startAngle)

                    # Calculate height of wall
                    wallHeight = 21000 / (depthX+0.0001) # Initial value is absurdly high to ensure walls are big enough
                    if wallHeight > self.surface.get_height(): wallHeight = self.surface.get_height() # Cuts the walls down if they're too big

                    # Textures/Wall Rendering
                    wallColumn = self.textures[MAP[row][column]].subsurface(int(targetX)%self.tileSize * self.scale,0,int(self.scale),480) # Gets the chunk of the texture to show
                    wallColumn = pygame.transform.scale(wallColumn,(self.scale,wallHeight)) # Scales the texture to the correct size
                    self.surface.blit(wallColumn,(ray*self.scale,((self.height/2)-wallHeight/2)*0.8,self.scale*1.5,wallHeight)) # Renders the wall!
                    break # Stops the ray from being cast any further

                if MAP[row][column] in ["1","2","3"] and depthY > 0:
                    # Same stuff as before, but on the Y axis
                    depth *= cos(PLAYER.angle-startAngle)

                    wallHeight = 21000 / (depthY+0.0001)
                    if wallHeight > self.surface.get_height(): wallHeight = self.surface.get_height()
                    
                    wallColumn = self.textures[MAP[row][column]].subsurface(int(targetY)%self.tileSize * self.scale,0,int(self.scale),480)
                    wallColumn = pygame.transform.scale(wallColumn,(self.scale,wallHeight))
                    self.surface.blit(wallColumn,(ray*self.scale,((self.height/2)-wallHeight/2)*0.8,self.scale*1.5,wallHeight))
                    break

                for sprite in SPRITES: # This is a broken mess
                    distanceX,distanceY = sprite.rect.centerx-PLAYER.rect.centerx,sprite.rect.centery-PLAYER.rect.centery
                    distance = sqrt(distanceX**2 + distanceY**2)

                    angle = atan2(distanceY,distanceX)
                    offset = angle - sprite.angle

                    distance *= cos(self.half_FOV - ray * angle)
                    if distance == 0: distance = 1

                    spriteHeight = wallHeight/distance*self.scale
                    offset *= spriteHeight

                    image = pygame.transform.scale(sprite.image,(spriteHeight,spriteHeight))
                    self.surface.blit(image,(ray * self.scale*1.5 - spriteHeight/2,self.surface.get_height()/2 - spriteHeight/2 + offset))



            
            startAngle += self.stepAngle