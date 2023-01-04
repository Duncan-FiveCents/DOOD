import pygame
import sys
from settings import *
from levels import *
from player import *
from raycasting import *
from renderer import *
from sprite import *
from hud import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(resolution,pygame.SCALED|pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.deltaTime = 1
        self.newGame()
    
    def newGame(self):
        self.map = Map(self,level1)
        self.player = Player(self,self.map.metadata)
        self.renderer = Renderer(self)
        self.raycasting = RayCasting(self)
        self.HUD = HUD(self)
        self.sprite = Sprite(self,"resources/enemies/skeleton-enemy1.png",(4.5,21.5),1,0.25)

    def update(self):
        self.player.movement()
        self.raycasting.castRays()
        self.sprite.locateSprite()
        if not self.player.swapping: self.player.weaponSwap()
        if not self.player.swapping: self.player.weapons[self.player.activeWeapon].fire()
        self.deltaTime = self.clock.tick(fps)
        pygame.display.flip()
    
    def draw(self):
        self.renderer.drawBackground()
        self.renderer.renderObjects()
        if self.player.swapping: self.player.weaponSwapAnim()
        else: self.player.weapons[self.player.activeWeapon].draw()
        self.HUD.drawHud()
        #self.map.draw()
        #self.player.draw()
    
    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

    def run(self):
        while True:
            self.eventLoop()
            self.update()
            self.draw()

if __name__ == "__main__":
    GAME = Game()
    GAME.run()