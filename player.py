import pygame
import math
from settings import *

class Player():
    def __init__(self,GAME,START):
        self.game = GAME
        self.x,self.y = START[0],START[1]
        self.angle = START[2]
        self.speed = 0.15

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
        
        # Collision
        if (int(self.x + dx * playerSize),int(self.y)) not in self.game.map.worldMap:
            self.x += dx
        if (int(self.x),int(self.y + dy * playerSize)) not in self.game.map.worldMap:
            self.y += dy

        # Key based turning
        if keysPressed[pygame.K_LEFT]:
            self.angle -= 0.1
        if keysPressed[pygame.K_RIGHT]:
            self.angle += 0.1
        self.angle %= math.tau

        # Mouse Turning
        mouseX,mouseY = pygame.mouse.get_pos()
        if mouseX < mouseBorderLeft or mouseX > mouseBorderRight: pygame.mouse.set_pos(halfWidth,halfHeight)
        mouseMovement = pygame.mouse.get_rel()[0]
        mouseMovement = max(-maxTurn,min(maxTurn,mouseMovement))
        self.angle += mouseMovement * sensitivity
    
    def draw(self):
        pygame.draw.circle(self.game.screen,(255,255,0),(self.x*tilesize,self.y*tilesize),2)