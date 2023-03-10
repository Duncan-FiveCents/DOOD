import pygame
from settings import *

class Renderer:
    def __init__(self,GAME):
        self.game = GAME
        self.screen = GAME.screen
        self.textures = {
            "1":pygame.image.load(resource_path("resources/textures/wall-texture-1.png")).convert_alpha(),
            "2":pygame.image.load(resource_path("resources/textures/wall-texture-2.png")).convert_alpha(),
            "3":pygame.image.load(resource_path("resources/textures/door.png")).convert_alpha(),
            "4":pygame.image.load(resource_path("resources/textures/button.png")).convert_alpha(),
            "5":pygame.image.load(resource_path("resources/textures/button_on.png")).convert_alpha(),
            "6":pygame.image.load(resource_path("resources/textures/exit.png")).convert_alpha()
        }

    def renderObjects(self):
        objects = sorted(self.game.raycasting.renderObjects,key=lambda n:n[0],reverse=True)
        if objects:
            for depth, surface, position in objects:
                self.screen.blit(surface,position)

    def drawBackground(self):
        pygame.draw.rect(self.screen,roofColour,(0,-halfHeight*0.85,resX,resY))
        pygame.draw.rect(self.screen,floorColour,(0,halfHeight*0.85,resX,resY))