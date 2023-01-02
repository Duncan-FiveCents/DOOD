import pygame
import sys
from settings import *
from levels import *
from player import *
from raycasting import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution,pygame.SCALED|pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.deltaTime = 1
        self.newGame()
    
    def newGame(self):
        self.map = Map(self,level1)
        self.player = Player(self,self.map.metadata)
        self.raycasting = RayCasting(self)
        print(self.map.worldMap)

    def update(self):
        self.player.movement()
        self.raycasting.castRays()
        pygame.display.flip()
        self.deltaTime = self.clock.tick(fps)
    
    def draw(self):
        self.screen.fill((0,0,0))
        #self.map.draw()
        #self.player.draw()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()

            self.update()
            self.draw()

if __name__ == "__main__":
    GAME = Game()
    GAME.run()