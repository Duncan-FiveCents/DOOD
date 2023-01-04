import pygame
from settings import *

class HUD:
    def __init__(self,GAME):
        self.game = GAME
        self.screen = GAME.screen
        self.image = pygame.image.load(resource_path("resources/UI/DOOD UI1.png")).convert_alpha()
        self.frames = [
            pygame.image.load(resource_path("resources/UI/DOOD UI1.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/DOOD UI2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/DOOD UI3.png")).convert_alpha
        ]

    def drawHud(self):
        self.screen.blit(self.image,(0,0))