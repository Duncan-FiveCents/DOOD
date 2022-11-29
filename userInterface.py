# userInterface.py

'''
title: HUD
author: Duncan Nickel
date-created: 29/11/2022
'''

import pygame

class HUD:
    def __init__(self,SCREEN):
        pygame.font.init()
        self.window = SCREEN
        self.surface = self.window.screen
        self.font = "UI\Pixel Combat.otf"

    def mainHud(self,WEAPONS,ACTIVE_WEAPON,HEALTH,SHIELD,FPSCOUNTER):
        # Weapon
        GUN = pygame.image.load("UI\Gun placeholder.png").convert()
        GUN = pygame.transform.scale2x(GUN)
        self.surface.blit(GUN,(0,0))

        # Base Hud
        HUD = pygame.image.load("UI\DOOD UI1.png").convert()
        self.surface.blit(HUD,(0,0))

        self.surface.blit(pygame.font.SysFont(self.font,28).render("WILLPOWER",False,(255,0,0)),(139,450))
        self.surface.blit(pygame.font.SysFont(self.font,28).render("SHEILD",False,(255,0,0)),(405,450))

        if FPSCOUNTER: self.surface.blit(pygame.font.SysFont(self.font,30).render(str(int(self.window.frame.get_fps())),False,(0,0,0)),(616,364))