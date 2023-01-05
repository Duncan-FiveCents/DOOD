import pygame
from settings import *
import os
from collections import deque

class Sprite:
    def __init__(self,GAME,PATH,POSITION,SCALE,SHIFT):
        self.game = GAME
        self.player = GAME.player
        self.x,self.y = POSITION
        self.image = pygame.image.load(resource_path(PATH)).convert_alpha()
        self.imageRatio = self.image.get_width()/self.image.get_height()
        self.spriteScale = SCALE # Simple scaling (ie 0.5 is half size)
        self.spriteShift = SHIFT # Adjusts vertical offset, 0.25 seems decent for standard enemies
    
    def locateSprite(self):
        distanceX,distanceY = self.x - self.player.x,self.y - self.player.y
        theta = math.atan2(distanceY,distanceX)
        
        delta = theta - self.player.angle
        if (distanceX > 0  and self.player.angle > math.pi) or (distanceX < 0 and distanceY < 0): delta += math.tau

        deltaRays = delta / stepAngle
        screenX = (half_rays + deltaRays) * scale

        totalDistance = math.hypot(distanceX,distanceY)
        totalDistance *= math.cos(delta)

        if -self.image.get_width()//2 < screenX < (resX + self.image.get_width()//2) and totalDistance > 0.5:
            projection = screenDist / totalDistance * self.spriteScale
            projectionWidth,projectionHeight = projection*self.imageRatio,projection # Needed for sprites with a non-1:1 aspect ratio

            spriteImage = pygame.transform.scale(self.image,(projectionWidth,projectionHeight))
            spritePos = screenX - projectionWidth//2,((halfHeight - projectionHeight//2) + projectionHeight*self.spriteShift)*0.85

            self.game.raycasting.renderObjects.append((totalDistance,spriteImage,spritePos))

class Projectile(Sprite):
    def __init__(self,GAME,POSITION,SPEED,ANGLE):
        Sprite.__init__(self,GAME,"resources/enemies/bullet.png",POSITION,0.5,0)
        self.speed = SPEED
        self.angle = ANGLE

class Skeleton(Sprite):
    def __init__(self,GAME,POSITION):
        Sprite.__init__(self,GAME,"resources/enemies/skeleton-enemy1.png",POSITION,1,0.25)
        self.frames = [
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy1.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy3.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy4.png")).convert_alpha()
        ]
        self.health = 100

    def move(self):
        pass