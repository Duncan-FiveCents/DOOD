# main.py

'''
title: DOOD
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame

from window import Window
from raycasting import RayCasting
from player import Player
from userInterface import HUD
from level import Level
from enemy import Enemy
import weapon

level1 = Level(
    [
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111000000000111111111111111',
    '1111111111111111000000000111111111111111',
    '1111111110000001000111000111111111111111',
    '1111111110000001000000000111111111111111',
    '1111111110000000000000000000011111111111',
    '1111111110000000000111000000011111111111',
    '1111111110000000000000000000011111111111',
    '1111111110000011000000000100011111111111',
    '1111111111110011000111000100011111111111',
    '1110000001110011000000000100011111000111',
    '1110000001110011000000000100000000000111',
    '1110000001110011111101111100000000000111',
    '1000000001110011111101111100000000000111',
    '1000000001110011111101111100011111000111',
    '1000000000000011111101111100011111000111',
    '1000000000000011100000001100011110000011',
    '1000000000000011100000001100011100000001',
    '1000000001110011100000001100011100000001',
    '1000000001110011100000001100011100000001',
    '1110000001110011111111111100011111111111',
    '1110000001110011111111111100010001111111',
    '1110000001110011111111111100010001111111',
    '1111111111110011111110000000000001111111',
    '1111110000000000111110000000000000000111',
    '1111110000000000111110000000000000000111',
    '1111110000000000111110000000000000000001',
    '1111110000000000111110000000000000000001',
    '1111110000000000111110000000000000000001',
    '1111110000000000111111100000000000000111',
    '1111111111111111111111100000000000000111',
    '1111111111111111111111100000011110000111',
    '1111111111111111111111100000011110000111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111'
    ],
    2,22
)

levels = [level1]
activeLevel = 0

WINDOW = Window()

SHOTGUN = weapon.Shotgun()
UI = HUD(WINDOW,SHOTGUN)
RAYS = RayCasting(WINDOW.screen,4,UI.minimap)
minimapActive = False

PLAYER = Player(levels[activeLevel].start)
ENEMY = Enemy()

if __name__ == "__main__":
    pygame.init()

    while True:
        PRESSED = pygame.key.get_pressed()
        MOUSE = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or PRESSED[pygame.K_ESCAPE]: # ESC will be used to pause later
                pygame.quit()
                exit()
        
        if (PRESSED[pygame.K_SPACE] or MOUSE[0]) and PLAYER.cooldown == 0:
            PLAYER.cooldown = 15
        
        if PRESSED[pygame.K_m]: # Still a little janky
            if minimapActive == False: minimapActive = True
            else: minimapActive = False

        PLAYER.turnPlayer(PRESSED,(WINDOW.screen.get_width()/2,WINDOW.screen.get_height()/2))
        PLAYER.movePlayer(PRESSED,levels[activeLevel].rects)

        WINDOW.clearScreen()

        # Raycasting
        RAYS.draw3D()
        RAYS.castRays(levels[activeLevel].worldMap,PLAYER,[]) # Enemies will be added later i guess

        # Weapon Animation
        if PLAYER.cooldown != 0:
            SHOTGUN.playAnim(PLAYER.cooldown//3)
            PLAYER.cooldown -= 1
        UI.weaponHud(PLAYER.activeWeapon)

        # User Interface
        UI.mainHud(PLAYER.health,PLAYER.sheild)

        RAYS.drawMap(levels[activeLevel].rects,PLAYER.rect,PLAYER.angle)

        if minimapActive:
            MINIMAP = pygame.transform.scale(UI.minimap,(300,300))
            WINDOW.screen.blit(MINIMAP,(WINDOW.screen.get_width()/2 - 150,0))

        WINDOW.updateFrame()