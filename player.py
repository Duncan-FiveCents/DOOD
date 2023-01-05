import pygame
import math
from settings import *
from weapon import *

class Player():
    def __init__(self,GAME,START):
        self.game = GAME
        self.x,self.y = START[0],START[1]
        self.angle = START[2]
        self.speed = 0.10
        self.weapons = [Shotgun(GAME),Sluggun(GAME)]
        self.activeWeapon = 0

        self.swapAnim = [
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap1.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap3.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap4.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap5.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap6.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap7.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap8.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap9.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap10.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap11.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap12.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap13.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap14.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap15.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap16.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap17.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/GunTransition/DOOD Gun Swap18.png")).convert_alpha()
        ]
        self.swapping = False
        self.swapTimer = 0

        self.health = 100
        self.shield = 0

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
    
    def weaponSwap(self):
        keys = pygame.key.get_pressed()
        if self.activeWeapon == 1 and keys[pygame.K_1] and self.swapping == False:
            self.swapping = True
            self.activeWeapon = 0
            self.swapTimer = 35
        elif self.activeWeapon == 0 and keys[pygame.K_2] and self.swapping == False:
            self.swapping = True
            self.activeWeapon = 1
            self.swapTimer = 35
    
    def weaponSwapAnim(self):
        if self.swapTimer == 0: self.swapping = False
        if self.swapping:
            if self.activeWeapon == 1:
                self.game.screen.blit(self.swapAnim[(35-self.swapTimer)//2],(0,0))
            elif self.activeWeapon == 0:
                self.game.screen.blit(self.swapAnim[(self.swapTimer//2)],(0,0))
            self.swapTimer -= 1