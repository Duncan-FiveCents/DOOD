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

        self.health = START[3]
        self.shield = START[4]
        self.shells = START[5]
        self.slugs = START[6]

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
        mouseMovement = pygame.mouse.get_rel()[0]
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
                if self.swapTimer == 8: self.game.sound.weaponSwap1.play()
                if self.swapTimer == 26: self.game.sound.weaponSwap2.play()
            elif self.activeWeapon == 0:
                self.game.screen.blit(self.swapAnim[(self.swapTimer//2)],(0,0))
                if self.swapTimer == 26: self.game.sound.weaponSwap1.play()
                if self.swapTimer == 8: self.game.sound.weaponSwap2.play()
            self.swapTimer -= 1

    def interactionCheck(self,ANGLE,POS):
        # I wrote this and I don't even quite remember how it works
        tempAngles = [ANGLE-(math.pi/2),self.angle,(ANGLE+(math.pi/2))]
        if ANGLE-0.17<0: tempAngles[0] == ANGLE+math.tau-(math.pi/2)
        return (int(self.x),int(self.y)) == POS and pygame.key.get_pressed()[pygame.K_e] and (((tempAngles[0]<tempAngles[1]) or (ANGLE==0 and tempAngles[1]+(math.pi/2)<tempAngles[0]+(math.pi/2))) and tempAngles[1]<tempAngles[2])

    def hitCheck(self,PROJECTILE):
        boundsX = (self.x-playerSize/2,self.x+playerSize/2)
        boundsY = (self.y-playerSize/2,self.y+playerSize/2)
        damage = 0
        if boundsX[0] <= PROJECTILE.x <= boundsX[1] and boundsY[0] <= PROJECTILE.y <= boundsY[1]:
            if PROJECTILE.type in ["skeletonBlast"]:
                if PROJECTILE.type == "skeletonBlast":
                    damage = 10

                if damage:
                    self.shield -= damage
                    if self.shield < 0:
                        self.health -= abs(self.shield)
                        self.shield = 0
                if not self.health <= 0:self.game.sound.doodHurt.play()
                
                return True
            # I can pretty much just reuse the projectile code for pickups
            elif PROJECTILE.type in ["Health","Shield","Shell","Slug"]:
                if PROJECTILE.type == "Health":
                    self.game.sound.healthPickup.play()
                    self.health += 20 if self.health < 100 else 10
                elif PROJECTILE.type == "Shield":
                    self.game.sound.shieldPickup.play()
                    self.shield += 10 if self.shield < 50 else 5
                elif PROJECTILE.type == "Shell":
                    self.shells += 5
                    self.game.sound.ammoPickup.play()
                elif PROJECTILE.type == "Slug":
                    self.slugs += 5
                    self.game.sound.ammoPickup.play()
                return True
        else: return False