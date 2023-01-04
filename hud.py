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
        self.font = resource_path("resources/UI/Pixel Combat.otf")

    def drawHud(self):
        # Base Stuff
        self.screen.blit(self.image,(0,0))
        self.screen.blit(self.crosshair,(0,0))

        # Status
        self.screen.blit(pygame.font.SysFont(self.font,28).render("WILLPOWER",False,(255,0,0)),(139,450))
        self.screen.blit(pygame.font.SysFont(self.font,28).render("SHIELD",False,(255,0,0)),(405,450))

        # Ammo Text
        if not self.game.player.swapping:
            if self.game.player.activeWeapon == 0:
                self.screen.blit(pygame.font.SysFont(self.font,28).render("SHELLS",False,(255,0,0)),(24,450))
                self.screen.blit(pygame.font.SysFont(self.font,22).render("SLUGS",False,(255,0,0)),(55,364))
            if self.game.player.activeWeapon == 1:
                self.screen.blit(pygame.font.SysFont(self.font,28).render("SLUGS",False,(255,0,0)),(29,450))
                self.screen.blit(pygame.font.SysFont(self.font,22).render("SHELLS",False,(255,0,0)),(52,364))
        else:
            timer = (self.game.player.swapTimer//9)
            if self.game.player.activeWeapon == 1:
                if timer == 0: self.screen.blit(pygame.font.SysFont(self.font,28).render("SLUGS",False,(255,0,0)),(5,450))
                if timer == 1: pass
                if timer == 2: self.screen.blit(pygame.font.SysFont(self.font,28).render("SHELLS",False,(255,0,0)),(-40,450))
                if timer == 3: self.screen.blit(pygame.font.SysFont(self.font,28).render("SHELLS",False,(255,0,0)),(-8,450))
            if self.game.player.activeWeapon == 0:
                if timer == 0: self.screen.blit(pygame.font.SysFont(self.font,28).render("SHELLS",False,(255,0,0)),(-8,450))
                if timer == 1: pass
                if timer == 2: self.screen.blit(pygame.font.SysFont(self.font,28).render("SLUGS",False,(255,0,0)),(-30,450))
                if timer == 3: self.screen.blit(pygame.font.SysFont(self.font,28).render("SLUGS",False,(255,0,0)),(5,450))             
    
    def swapAnim(self):
        self.image = self.frames[(self.game.player.swapTimer//9)]