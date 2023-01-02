import pygame
import math
from settings import *

class Player():
    def __init__(self,GAME,START):
        self.game = GAME
        self.x,self.y = START[0]*tilesize,START[1]*tilesize
        self.angle = START[2]
        self.speed = 3

    def movement(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)
        dx,dy = 0,0

        speed = self.speed
        speedSin = speed*sinA
        speedCos = speed*cosA

        # Good ol' WASD
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_w]:
            dx += speedCos
            dy += speedSin
        if keysPressed[pygame.K_s]:
            dx -= speedCos
            dy -= speedSin
        if keysPressed[pygame.K_a]:
            dx += speedSin
            dy -= speedCos
        if keysPressed[pygame.K_d]:
            dx -= speedSin
            dy += speedCos
        
        if (int(self.x + dx)//tilesize,int(self.y)//tilesize) not in self.game.map.worldMap:
            self.x += dx
        if (int(self.x)//tilesize,int(self.y + dy)//tilesize) not in self.game.map.worldMap:
            self.y += dy

        # Key based turning
        if keysPressed[pygame.K_LEFT]:
            self.angle -= sensitivity
        if keysPressed[pygame.K_RIGHT]:
            self.angle += sensitivity
        self.angle %= math.tau
    
    def draw(self):
        pygame.draw.circle(self.game.screen,(255,255,0),(self.x,self.y),2)