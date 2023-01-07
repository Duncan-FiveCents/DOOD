import pygame
from settings import *

class SoundEngine:
    def __init__(self,GAME):
        self.game = GAME
        pygame.mixer.init()
        self.doodHurt = pygame.mixer.Sound(resource_path("resources/sounds/doodOuch.wav"))