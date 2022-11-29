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
        self.font = pygame.font.SysFont("UI\Pixel Combat.otf",30)

    def mainHud(self,WEAPONS,ACTIVE_WEAPON,HEALTH,SHIELD,FPSCOUNTER):
        GUN = pygame.image.load("UI\Gun placeholder.png").convert()
        GUN = pygame.transform.scale2x(GUN)
        self.surface.blit(GUN,(0,0))

        HUD = pygame.image.load("UI\DOOD UI1.png").convert()
        self.surface.blit(HUD,(0,0))

        if FPSCOUNTER: self.surface.blit(self.font.render(str(int(self.window.frame.get_fps())),False,(0,0,0)),(0,0)) 