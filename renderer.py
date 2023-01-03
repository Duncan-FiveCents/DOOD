import pygame
from settings import *

class Renderer:
    def __init__(self,GAME):
        self.game = GAME
        self.screen = GAME.screen
        self.textures = {
            "1":pygame.image.load(resource_path("resources/textures/wall-texture-1.png")).convert_alpha(),
            "2":pygame.image.load(resource_path("resources/textures/wall-texture-2.png")).convert_alpha()
        }

    def renderObjects(self):
        objects = self.game.raycasting.renderObjects
        for depth, surface, position in objects:
            self.screen.blit(surface,position)

    def drawBackground(self):
        pygame.draw.rect(self.screen,roofColour,(0,-halfHeight,resX,resY))
        pygame.draw.rect(self.screen,floorColour,(0,halfHeight,resX,resY))