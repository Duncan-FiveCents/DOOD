import pygame
from settings import *

class Renderer:
    def __init__(self,GAME):
        self.game = GAME
        self.screen = GAME.screen
        self.textures = {
            "1":pygame.image.load(resource_path("resources/textures/wall-texture-1.png")).convert(),
            "2":pygame.image.load(resource_path("resources/textures/wall-texture-2.png")).convert()
        }

    def renderObjects(self):
        objects = self.game.raycasting.renderObjects
        for depth, surface, position in objects:
            self.screen.blit(surface,position)