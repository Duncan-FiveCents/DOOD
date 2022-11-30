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

        self.HUD = pygame.image.load("UI\DOOD UI1.png").convert()

        self.weapons = [
            [pygame.image.load("UI\Gun placeholder.png").convert(),pygame.image.load("UI\shooting gun placeholder.png").convert()]
            ]

    def mainHud(self,HEALTH,SHIELD,FPSCOUNTER):
        # Base Hud
        self.surface.blit(self.HUD,(0,0))

        # These are rendered in real time to allow for graphical effects
        self.surface.blit(pygame.font.SysFont(self.font,28).render("WILLPOWER",False,(255,0,0)),(139,450))
        self.surface.blit(pygame.font.SysFont(self.font,28).render("SHIELD",False,(255,0,0)),(405,450))

        if FPSCOUNTER: self.surface.blit(pygame.font.SysFont(self.font,30).render(str(int(self.window.frame.get_fps())),False,(0,0,0)),(616,364))

    def weaponHud(self,ACTIVE_WEAPON,SHOOT):
        # Weapon
        if SHOOT: self.surface.blit(self.weapons[ACTIVE_WEAPON-1][1],(0,0))
        else: self.surface.blit(self.weapons[ACTIVE_WEAPON-1][0],(0,0))