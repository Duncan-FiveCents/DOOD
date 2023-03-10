import pygame
from time import sleep
from settings import *
from levels import *
from player import *
from raycasting import *
from renderer import *
from sprite import *
from hud import *
from pathfinding import *
from sound import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(resolution,pygame.SCALED|pygame.FULLSCREEN)
        pygame.display.set_caption("DOOD")
        pygame.event.set_grab(True)
        self.clock = pygame.time.Clock()
        self.activeLevel = 0
        self.levels = [level1,level2]
        self.newGame()
    
    def newGame(self):
        self.map = Map(self,self.levels[self.activeLevel])
        self.player = Player(self,self.map.metadata)
        self.renderer = Renderer(self)
        self.raycasting = RayCasting(self)
        self.HUD = HUD(self)
        self.enemies = []
        self.sprites = []
        self.projectiles = []
        for enemy in self.map.metadata[7]:
            if enemy[0] == "Skeleton": self.enemies.append(Skeleton(self,enemy[1]))
        for sprite in self.map.metadata[8]:
            self.sprites.append(Item(self,sprite[0],sprite[1]))
        self.pathfinding = Pathfinding(self)
        self.sound = SoundEngine(self)

    def update(self):
        # Basic Stufffffffff
        self.player.movement()
        self.raycasting.castRays()

        # Health, Shield, and Ammo Pickups
        for sprite in self.sprites:
            sprite.locateSprite()
            if self.player.hitCheck(sprite):
                self.sprites.remove(sprite)
                del sprite

        # Projectiles
        for projectile in self.projectiles:
            forDeletion = False
            projectile.move()
            projectile.locateSprite()
            # Bug here: having 2 living enemies will double damage, 3 will triple, so on
            for enemy in self.enemies:
                if enemy.hitCheck(projectile) or self.player.hitCheck(projectile):
                    forDeletion = True
                    break
            if (int(projectile.x),int(projectile.y)) in self.map.worldMap or forDeletion:
                self.projectiles.remove(projectile)
                del projectile
        
        # Enemies
        for enemy in self.enemies:
            enemy.locateSprite()
            enemy.runLogic()
            if enemy.health <= 0:
                self.enemies.remove(enemy)
                del enemy

        if not self.player.swapping and not self.player.weapons[self.player.activeWeapon].cooldown: self.player.weaponSwap()
        if not self.player.swapping: self.player.weapons[self.player.activeWeapon].fire()
        self.clock.tick(fps)
        pygame.display.flip()
    
    def draw(self):
        self.renderer.drawBackground()
        self.renderer.renderObjects()
        if self.player.swapping:
            self.HUD.swapAnim()
            self.player.weaponSwapAnim()
        else: self.player.weapons[self.player.activeWeapon].draw()
        self.HUD.drawHud()
        self.HUD.drawMinimap()
    
    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p: print(int(self.player.x),int(self.player.y)) # Used to test player tile

    def newLevel(self):
        self.screen.blit(pygame.image.load(resource_path("resources/UI/loading_screen.png")).convert_alpha(),(0,0))
        pygame.display.flip()
        sleep(3) # Yes the loading screen is fake, but we need the retro aesthetic shut up
        self.activeLevel += 1
        self.levels[self.activeLevel][1][3:7] = self.player.health,self.player.shield,self.player.shells,self.player.slugs
        self.newGame()
        self.sound.doodinTime.play()

    def run(self):
        # Main Menu Shenanigans
        currentChoice = 0
        cooldown = 0
        menuBase = [
            pygame.image.load(resource_path("resources/UI/TitleScreen/TitleScreen BG.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/TitleScreen/TitleScreen Dood.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/TitleScreen/TitleScreen Fade.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/TitleScreen/TitleScreen Logo.png")).convert_alpha()
        ]
        menuOptions = [
            pygame.image.load(resource_path("resources/UI/TitleScreen/TitleScreen Buttons2.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/TitleScreen/TitleScreen Buttons3.png")).convert_alpha(),
            pygame.image.load(resource_path("resources/UI/TitleScreen/TitleScreen Buttons4.png")).convert_alpha()
        ]
        while True:
            for item in menuBase: self.screen.blit(item,(0,0))
            self.screen.blit(menuOptions[currentChoice],(0,0))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_s] and cooldown == 0:
                if currentChoice != 2: currentChoice += 1
                cooldown = 5
                self.sound.buttonPress.play()
            elif keys[pygame.K_w] and not cooldown:
                if currentChoice != 0: currentChoice -= 1
                cooldown = 5
                self.sound.buttonPress.play()
            else:
                if cooldown != 0: cooldown -= 1

            if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
                self.sound.buttonPress.play()
                if currentChoice == 0:
                    self.screen.blit(pygame.image.load(resource_path("resources/UI/loading_screen.png")).convert_alpha(),(0,0))
                    pygame.display.flip()
                    sleep(3)
                    self.sound.doodinTime.play()
                    break
                if currentChoice == 1: pass # Yes, there is currently no settings menu
                if currentChoice == 2:
                    pygame.quit()
                    exit()

            self.eventLoop()
            self.clock.tick(fps)
            pygame.display.flip()

        # The actual game
        button1,button2,button3 = False,False,False

        while True:
            self.eventLoop()
            self.update()
            if self.player.health <= 0:
                self.sound.doodDeath.play()
                self.screen.blit(pygame.image.load(resource_path("resources/UI/game_over.png")).convert_alpha(),(0,0))
                self.clock.tick(fps)
                pygame.display.flip()
                sleep(5)
                break
            self.draw()
            # Level-Specific Exit and Buttons (these must be done manually because I can't be bothered to add a framework for it)
            if self.activeLevel == 0:
                if self.player.interactionCheck(math.pi*3/2,(20,6)) and not button1:
                    self.sound.buttonPress.play()
                    button1 = True
                    level1[0][5][20] = '5'
                    level1[0][17][20] = '0'
                    self.map = Map(self,level1)
                if self.player.interactionCheck(0,(38,32)):
                    self.sound.levelExit.play()
                    try: self.newLevel()
                    except IndexError:
                        self.sound.doodTude.play()
                        self.screen.blit(pygame.image.load(resource_path("resources/UI/complete.png")).convert_alpha(),(0,0))
                        self.clock.tick(fps)
                        pygame.display.flip()
                        sleep(5)
                        break
            if self.activeLevel == 1:
                if self.player.interactionCheck(math.pi/2,(5,19)) and not button2:
                    self.sound.buttonPress.play()
                    button2 = True
                    level2[0][20][5] = '5'
                    level2[0][18][12] = '0'
                    self.map = Map(self,level2)
                if self.player.interactionCheck(math.pi,(38,6)) and not button3:
                    button3 = True
                    self.sound.buttonPress.play()
                    level2[0][6][37] = '5'
                    level2[0][8][29] = '0'
                    self.map = Map(self,level2)
                if self.player.interactionCheck(math.pi*3/2,(21,1)):
                    self.sound.levelExit.play()
                    try: self.newLevel()
                    except IndexError:
                        self.sound.doodTude.play()
                        self.screen.blit(pygame.image.load(resource_path("resources/UI/complete.png")).convert_alpha(),(0,0))
                        self.clock.tick(fps)
                        pygame.display.flip()
                        sleep(5)
                        break

if __name__ == "__main__":
    GAME = Game()
    while True:
        GAME.run()
        del GAME
        GAME = Game()