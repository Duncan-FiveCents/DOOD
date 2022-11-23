# player.py

'''
title: The Dood Man Guy
author: Duncan Nickel
date-created: 22/11/2022
'''

import pygame
from math import pi

class Player:
    def __init__(self,STARTPOS):
        self.pos = STARTPOS # Player position within the world
        self.angle = pi