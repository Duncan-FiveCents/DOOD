import pygame
from settings import *

level1 = [[
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111111111111111111111111111',
    '1111111111111111000000000111111111111111',
    '1111111111111111000000000111111111111111',
    '1111111110000011000222000111111111111111',
    '1111111110000011000000000111111111111111',
    '1111111110000000000000000000011111111111',
    '1111111110000000000222000000011111111111',
    '1111111110000000000000000000011111111111',
    '1111111110000011000000000100011111111111',
    '1111111111110011000222000100011111111111',
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
    ],[2,22,0]]

class Map:
    def __init__(self,GAME,LEVEL):
        self.game = GAME
        self.levelMap = LEVEL[0]
        self.metadata = LEVEL[1]
        self.worldMap = {}
        self.createMap()
    
    def createMap(self):
        for i, row in enumerate(self.levelMap):
            for j, char in enumerate(row):
                if char != "0":
                    self.worldMap[(j,i)] = char
    
    def draw(self): # Test used to draw layout
        for pos in self.worldMap: pygame.draw.rect(self.game.screen,(100,100,100),(pos[0]*tilesize,pos[1]*tilesize,tilesize,tilesize),1)
