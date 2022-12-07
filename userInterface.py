# userInterface.py

'''
title: HUD
author: Duncan Nickel
date-created: 29/11/2022
'''

import pygame

class HUD:
    def __init__(self,SCREEN,SHOTGUN):
        pygame.font.init()
        self.window = SCREEN
        self.surface = self.window.screen
        self.font = "UI\Pixel Combat.otf"

        self.HUD = pygame.image.load("UI\DOOD UI1.png").convert()
        self.crosshair = pygame.image.load("UI\crosshair.png").convert()

        self.weapons = [
            SHOTGUN
            ]

        self.minimap = pygame.surface.Surface((1600,1600))

    def mainHud(self,HEALTH,SHIELD):
        # Base Hud
        self.surface.blit(self.HUD,(0,0))

        # These are rendered in real time to allow for graphical effects
        self.surface.blit(pygame.font.SysFont(self.font,28).render("WILLPOWER",False,(255,0,0)),(139,450))
        self.surface.blit(pygame.font.SysFont(self.font,28).render("SHIELD",False,(255,0,0)),(405,450))

        self.surface.blit(self.crosshair,(0,0))

        # This WAS an FPS counter, but now its needed to prevent the mouse from locking up?
        # I genuinely have no idea why it does this
        # It just renders offscreen
        self.surface.blit(pygame.font.SysFont(self.font,30).render(str(pygame.mouse.get_rel()[0]/100/self.sensitivityMult),False,(0,0,0)),(800,800))

    def weaponHud(self,ACTIVE_WEAPON):
        # Weapon
        self.surface.blit(self.weapons[ACTIVE_WEAPON-1].image,self.weapons[ACTIVE_WEAPON-1].rect)