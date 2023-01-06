import pygame
from settings import *

class HUD:
    def __init__(self,GAME):
        self.game = GAME
        self.screen = GAME.screen
        self.image = pygame.image.load(resource_path("resources/UI/DOOD UI1.png")).convert_alpha()
        self.frames = [ # Yes, the 1-2-3-2 is intentional
            pygame.image.load(resource_path("resources/UI/DOOD UI1.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/DOOD UI2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/DOOD UI3.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/DOOD UI2.png")).convert_alpha()
        ]
        self.crosshair = pygame.image.load(resource_path("resources/UI/crosshair.png")).convert_alpha()
        self.font = resource_path("resources/UI/Roboto-Bold.ttf")

        self.mapIcon = pygame.image.load(resource_path("resources/UI/dood map sprite.png")).convert_alpha()

        # These are used for the positioning of text later
        self.healthRect = pygame.rect.Rect(144,402,114,36)
        self.shieldRect = pygame.rect.Rect(386,402,114,36)
        self.primaryAmmoRect = pygame.rect.Rect(16,402,98,36)
        self.secondaryAmmoRect = pygame.rect.Rect(10,364,26,16)

    def drawHud(self):
        # Base Stuff
        self.screen.blit(self.image,(0,0))
        self.screen.blit(self.crosshair,(0,0))

        # Status
        healthText = pygame.font.SysFont(self.font,40).render(str(self.game.player.health),False,(255,0,0))
        self.screen.blit(pygame.font.SysFont(self.font,28).render("WILLPOWER",False,(255,255,255)),(139,450))
        self.screen.blit(healthText,((self.healthRect.left+(self.healthRect.width//2))-healthText.get_width()//2,(self.healthRect.top+(self.healthRect.height//2))-healthText.get_height()//2))

        shieldText = pygame.font.SysFont(self.font,40).render(str(self.game.player.shield),False,(0,255,0))
        self.screen.blit(pygame.font.SysFont(self.font,28).render("SHIELD",False,(255,255,255)),(405,450))
        self.screen.blit(shieldText,((self.shieldRect.left+(self.shieldRect.width//2))-shieldText.get_width()//2,(self.shieldRect.top+(self.shieldRect.height//2))-shieldText.get_height()//2))

        # Ammo Text
        if not self.game.player.swapping:
            if self.game.player.activeWeapon == 0:
                primaryAmmoText = pygame.font.SysFont(self.font,40).render(str(self.game.player.shells),False,(0,0,255))
                secondaryAmmoText = pygame.font.SysFont(self.font,22).render(str(self.game.player.slugs),False,(0,0,255))
                self.screen.blit(pygame.font.SysFont(self.font,28).render("SHELLS",False,(255,255,255)),(24,450))
                self.screen.blit(primaryAmmoText,((self.primaryAmmoRect.left+(self.primaryAmmoRect.width//2))-primaryAmmoText.get_width()//2,(self.primaryAmmoRect.top+(self.primaryAmmoRect.height//2))-primaryAmmoText.get_height()//2))
                self.screen.blit(pygame.font.SysFont(self.font,22).render("SLUGS",False,(255,255,255)),(55,364))
                self.screen.blit(secondaryAmmoText,((self.secondaryAmmoRect.left+(self.secondaryAmmoRect.width//2))-secondaryAmmoText.get_width()//2,(self.secondaryAmmoRect.top+(self.secondaryAmmoRect.height//2))-secondaryAmmoText.get_height()//2))

            if self.game.player.activeWeapon == 1:
                primaryAmmoText = pygame.font.SysFont(self.font,40).render(str(self.game.player.slugs),False,(0,0,255))
                secondaryAmmoText = pygame.font.SysFont(self.font,22).render(str(self.game.player.shells),False,(0,0,255))
                self.screen.blit(pygame.font.SysFont(self.font,28).render("SLUGS",False,(255,255,255)),(29,450))
                self.screen.blit(primaryAmmoText,((self.primaryAmmoRect.left+(self.primaryAmmoRect.width//2))-primaryAmmoText.get_width()//2,(self.primaryAmmoRect.top+(self.primaryAmmoRect.height//2))-primaryAmmoText.get_height()//2))
                self.screen.blit(pygame.font.SysFont(self.font,22).render("SHELLS",False,(255,255,255)),(52,364))
                self.screen.blit(secondaryAmmoText,((self.secondaryAmmoRect.left+(self.secondaryAmmoRect.width//2))-secondaryAmmoText.get_width()//2,(self.secondaryAmmoRect.top+(self.secondaryAmmoRect.height//2))-secondaryAmmoText.get_height()//2))

        else:
            timer = (self.game.player.swapTimer//9)
            if self.game.player.activeWeapon == 1:
                if timer == 0: self.screen.blit(pygame.font.SysFont(self.font,28).render("SLUGS",False,(255,255,255)),(5,450))
                if timer == 1: pass
                if timer == 2: self.screen.blit(pygame.font.SysFont(self.font,28).render("SHELLS",False,(255,255,255)),(-40,450))
                if timer == 3: self.screen.blit(pygame.font.SysFont(self.font,28).render("SHELLS",False,(255,255,255)),(-8,450))
            if self.game.player.activeWeapon == 0:
                if timer == 0: self.screen.blit(pygame.font.SysFont(self.font,28).render("SHELLS",False,(255,255,255)),(-8,450))
                if timer == 1: pass
                if timer == 2: self.screen.blit(pygame.font.SysFont(self.font,28).render("SLUGS",False,(255,255,255)),(-30,450))
                if timer == 3: self.screen.blit(pygame.font.SysFont(self.font,28).render("SLUGS",False,(255,255,255)),(5,450))             
    
    def swapAnim(self):
        self.image = self.frames[(self.game.player.swapTimer//9)]
    
    def drawMinimap(self):
        self.minimap = pygame.surface.Surface((len(self.game.map.levelMap[0])*tilesize,len(self.game.map.levelMap)*tilesize))
        self.minimap.fill((7,7,7))
        for pos in self.game.map.worldMap: pygame.draw.rect(self.minimap,(100,100,100),(pos[0]*tilesize,pos[1]*tilesize,tilesize,tilesize),1)
        self.minimap.blit(self.mapIcon,((self.game.player.x*tilesize)-self.mapIcon.get_width()//2,(self.game.player.y*tilesize)-self.mapIcon.get_height()//2))
        self.minimap = self.minimap.subsurface((
            self.game.player.x*tilesize-5*tilesize*1.48 if self.game.player.x*tilesize-5*tilesize*1.48 >= 0 else 0,
            self.game.player.y*tilesize-5*tilesize if self.game.player.y*tilesize-5*tilesize >= 0 else 0,
            10*tilesize*1.48, # If there's ever an error here, increase the saftey margin on the right and/or bottom of map
            10*tilesize
        ))
        self.minimap = pygame.transform.scale(self.minimap,(98,66))
        self.screen.blit(self.minimap,(528,400))