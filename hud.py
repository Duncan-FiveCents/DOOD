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

    def drawHud(self):
        self.screen.blit(self.image,(0,0))
        self.screen.blit(self.crosshair,(0,0))
    
    def swapAnim(self):
        self.image = self.frames[(self.game.player.swapTimer//9)]