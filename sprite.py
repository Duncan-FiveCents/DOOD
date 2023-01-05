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

        self.health = 100
        self.size = 2 # Default hitbox size for enemies
    
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
    def __init__(self,GAME,POSITION,SPEED,ANGLE,TYPE):
        Sprite.__init__(self,GAME,"resources/enemies/bullet.png",POSITION,0.5,0)
        self.speed = SPEED
        self.angle = ANGLE
        self.x,self.y = POSITION
        self.type = TYPE
        self.size = 1

    def move(self):
        self.x += self.speed*math.cos(self.angle)
        self.y += self.speed*math.sin(self.angle)

class Skeleton(Sprite):
    def __init__(self,GAME,POSITION):
        Sprite.__init__(self,GAME,"resources/enemies/skeleton-enemy1.png",POSITION,1,0.25)
        self.frames = [
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy1.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy3.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy4.png")).convert_alpha()
        ]

    def move(self):
        pass

    def hitCheck(self,PROJECTILE):
        boundsX = (self.x-self.size//2,self.x+self.size//2)
        boundsY = (self.y-self.size//2,self.y+self.size//2)
        if boundsX[0] <= PROJECTILE.x <= boundsX[1] and boundsY[0] <= PROJECTILE.y <= boundsY[1]:
            if PROJECTILE.type == "slug": self.health -= 50
            return True
        else: return False