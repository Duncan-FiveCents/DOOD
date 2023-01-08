import pygame
from settings import *

class SoundEngine:
    def __init__(self,GAME):
        self.game = GAME
        pygame.mixer.init()
        self.doodHurt = pygame.mixer.Sound(resource_path("resources/sounds/doodOuch.wav"))
        self.doodDeath = pygame.mixer.Sound(resource_path("resources/sounds/doodDeath.wav"))
        self.skeletonHurt = pygame.mixer.Sound(resource_path("resources/sounds/skeletonHurt.wav"))

        self.shellFire = pygame.mixer.Sound(resource_path("resources/sounds/shellFire.wav"))
        self.slugFire = pygame.mixer.Sound(resource_path("resources/sounds/shellFire.wav"))
        self.weaponSwap1 = pygame.mixer.Sound(resource_path("resources/sounds/switch1.wav"))
        self.weaponSwap2 = pygame.mixer.Sound(resource_path("resources/sounds/switch2.wav"))

        self.healthPickup = pygame.mixer.Sound(resource_path("resources/sounds/healthPickup.wav"))
        self.shieldPickup = pygame.mixer.Sound(resource_path("resources/sounds/shieldPickup.wav"))
        self.ammoPickup = pygame.mixer.Sound(resource_path("resources/sounds/ammoPickup.wav"))

        self.buttonPress = pygame.mixer.Sound(resource_path("resources/sounds/buttonPress.wav"))
        self.levelExit = pygame.mixer.Sound(resource_path("resources/sounds/levelFinish.wav"))

        self.doodinTime = pygame.mixer.Sound(resource_path("resources/sounds/doodinTime.wav"))
        self.doodTude = pygame.mixer.Sound(resource_path("resources/sounds/doodTude.wav"))