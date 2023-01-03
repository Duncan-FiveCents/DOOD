import pygame
from settings import *

class Sprite:
    def __init__(self,GAME,PATH,POSITION):
        self.game = GAME
        self.player = GAME.player
        self.x,self.y = POSITION
        self.image = pygame.image.load(resource_path(PATH)).convert_alpha()
        self.imageRatio = self.image.get_width()/self.image.get_height()
    
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
            projection = screenDist / totalDistance
            projectionWidth,projectionHeight = projection*self.imageRatio,projection # Needed for sprites with a non-1:1 aspect ratio

            spriteImage = pygame.transform.scale(self.image,(projectionWidth,projectionHeight))
            spritePos = screenX - projectionWidth//2,halfHeight - projectionHeight//2

            self.game.raycasting.renderObjects.append((totalDistance,spriteImage,spritePos))