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
        self.size = 1 # Default hitbox size for enemies
        self.speed = 0.075
        self.theta,self.playerDistance = 0,0
    
    def locateSprite(self):
        distanceX,distanceY = self.x - self.player.x,self.y - self.player.y
        self.theta = math.atan2(distanceY,distanceX)
        
        delta = self.theta - self.player.angle
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
    
    def playerSight(self):
        if (int(self.x),int(self.y)) == (int(self.game.player.x),int(self.game.player.y)): return True

        verticalWallDistance,horizontalWallDistance = 0,0
        verticalPlayerDistance,horizontalPlayerDistance = 0,0

        playerX,playerY = self.game.player.x,self.game.player.y
        mapX,mapY = int(playerX),int(playerY)

        startAngle = self.theta

        for ray in range(castedRays):
            sinAngle = math.sin(startAngle)
            cosAngle = math.cos(startAngle)
            if not sinAngle: sinAngle = 0.00001
            if not cosAngle: cosAngle = 0.00001

            # Horizontals
            horzY,dirY = (mapY+1,1) if sinAngle >= 0 else (mapY-0.00001,-1)
            horizontalDepth = (horzY - playerY) / sinAngle
            horzX = playerX + horizontalDepth * cosAngle
            deltaDepth = dirY / sinAngle
            dirX = deltaDepth * cosAngle

            for i in range(15):
                horizontalTile = int(horzX),int(horzY)
                if horizontalTile == (int(self.x),int(self.y)):
                    horizontalPlayerDistance = horizontalDepth
                    break
                if horizontalTile in self.game.map.worldMap:
                    horizontalWallDistance = horizontalDepth
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

            for i in range(15):
                verticalTile = int(vertX),int(vertY)
                if verticalTile == (int(self.x),int(self.y)):
                    verticalPlayerDistance = verticalDepth
                    break
                if verticalTile in self.game.map.worldMap:
                    verticalWallDistance = verticalDepth
                    break
                vertX += dirX
                vertY += dirY
                verticalDepth += deltaDepth
            
            self.playerDistance = max(verticalPlayerDistance,horizontalPlayerDistance)
            wallDistance = max(verticalWallDistance,horizontalWallDistance)

            if 0 < self.playerDistance < wallDistance or not wallDistance:
                return True
            return False

class Item(Sprite):
    def __init__(self,GAME,TYPE,POSITION):
        spriteDictionary = {
            "Health":"resources/pickups/DOOD HP Pickup.png",
            "Shield":"resources/pickups/DOOD Shield Pickup.png",
            "Shell":"resources/pickups/DOOD Shell Pickup.png",
            "Slug":"resources/pickups/DOOD Slug Pickup.png"
        }
        Sprite.__init__(self,GAME,spriteDictionary[TYPE],POSITION,0.5,0.75)
        self.type = TYPE

class Skeleton(Sprite):
    def __init__(self,GAME,POSITION):
        Sprite.__init__(self,GAME,"resources/enemies/skeleton-enemy1.png",POSITION,1,0.25)
        self.frames = [
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy1.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy3.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/enemies/skeleton-enemy4.png")).convert_alpha()
        ]
        self.walkTimer,self.walkFrame = 10,0
        self.playerSearch = False
        self.cooldown = 60

    def hitCheck(self,PROJECTILE):
        boundsX = (self.x-self.size/2,self.x+self.size/2)
        boundsY = (self.y-self.size/2,self.y+self.size/2)
        if boundsX[0] <= PROJECTILE.x <= boundsX[1] and boundsY[0] <= PROJECTILE.y <= boundsY[1]:
            if PROJECTILE.type in ["shell","slug"]:
                self.game.sound.skeletonHurt.play()
                if PROJECTILE.type == "slug": self.health -= 50
                if PROJECTILE.type == "shell": self.health -= 20
                return True
        else: return False
    
    def movement(self):
        nextPosition =self.game.pathfinding.getPath((int(self.x),int(self.y)),(int(self.player.x),int(self.player.y)))
        nextX,nextY = nextPosition
        angle = math.atan2(nextY+0.5-self.y,nextX+0.5-self.x)
        distanceX = math.cos(angle)*self.speed
        distanceY = math.sin(angle)*self.speed
        if (int(self.x + distanceX * self.size),int(self.y)) not in self.game.map.worldMap:
            self.x += distanceX
        if (int(self.x),int(self.y + distanceY * self.size)) not in self.game.map.worldMap:
            self.y += distanceY
        if self.walkTimer == 0:
            if self.walkFrame == 0: self.image,self.walkFrame = self.frames[2],1
            else: self.image,self.walkFrame = self.frames[1],0
            self.walkTimer = 10
        else: self.walkTimer -= 1

    def attack(self):
        if not self.cooldown:
            self.firing = True
            self.image = self.frames[3]
            self.cooldown = 60

    def runLogic(self):
        self.vision = self.playerSight()
        if self.vision and self.playerDistance <= 6 and not self.cooldown:
            self.image = self.frames[0]
            self.attack()
        elif self.vision and self.playerDistance <= 6 and self.cooldown == 40:
            angle = (math.atan2(self.y-self.player.y,self.x-self.player.x)+math.pi) % math.tau
            self.game.projectiles.append(Projectile(self.game,(self.x+math.cos(angle)*0.5,self.y+math.sin(angle)*0.5),0.3,angle,"skeletonBlast"))
        elif self.vision and self.playerDistance > 6 and not self.cooldown:
            self.playerSearch = True
            self.movement()
        elif self.playerSearch and not self.vision and not self.cooldown:
            self.movement()
        if self.cooldown: self.cooldown -= 1

class Projectile(Sprite):
    def __init__(self,GAME,POSITION,SPEED,ANGLE,TYPE):
        Sprite.__init__(self,GAME,"resources/enemies/bullet.png",POSITION,0.5,0)
        self.speed = SPEED
        self.angle = ANGLE
        self.x,self.y = POSITION
        self.type = TYPE
        self.size = 0.25

    def move(self):
        self.x += self.speed*math.cos(self.angle)
        self.y += self.speed*math.sin(self.angle)