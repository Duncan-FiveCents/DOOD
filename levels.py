import pygame
from settings import *

# Note: Levels can be any size, but they need a 5 wall buffer on the bottom and an 8 wall buffer on the right
# This is to avoid a issue with the minimap code
level1 = [
    [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','4','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','0','0','0','0','0','2','2','0','0','0','2','2','2','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','0','0','0','0','0','2','2','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','0','0','0','0','0','2','2','0','0','0','0','0','0','0','0','0','2','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','2','2','2','2','2','2','2','2','2','0','0','2','2','0','0','0','2','2','2','0','0','0','2','0','0','0','1','1','1','1','1','2','2','2','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','2','1','2','0','0','2','2','0','0','0','0','0','0','0','0','0','2','0','0','0','2','2','2','2','2','0','0','0','2','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','2','1','2','0','0','2','2','0','0','0','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','2','1','2','0','0','2','2','2','2','2','2','3','2','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','0','0','0','2','1','2','0','0','2','1','1','1','1','2','0','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','0','0','0','2','2','2','0','0','2','1','1','1','1','2','0','2','1','1','1','2','0','0','0','2','2','2','2','2','0','0','0','2','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','2','2','2','2','0','2','2','2','2','2','0','0','0','2','1','1','1','2','0','0','0','2','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','2','0','0','0','0','0','0','0','2','2','0','0','0','2','1','1','2','0','0','0','0','0','2','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','2','0','0','0','0','0','0','0','2','2','0','0','0','2','1','2','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','0','0','0','2','2','2','0','0','2','1','2','0','0','0','0','0','0','0','2','2','0','0','0','2','1','2','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','0','0','0','2','1','2','0','0','2','1','2','0','0','0','0','0','0','0','2','2','0','0','0','2','1','2','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','2','1','2','0','0','2','1','1','1','1','1','1','1','1','1','1','2','0','0','0','2','2','2','2','2','2','2','2','2','2','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','2','1','2','0','0','2','1','1','1','1','1','1','1','1','1','1','2','0','0','0','2','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','2','1','2','0','0','2','1','1','1','1','1','1','2','2','2','2','2','0','0','0','2','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','2','2','2','2','2','2','2','2','2','0','0','2','2','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','6','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','2','2','2','2','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','2','2','2','2','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
    ],
    [1.5,21.5,0,100,0,10,10, # Player Start (X,Y,Angle (0 = right),Health,Shield,Shells,Slugs) Starting conditions for future levels will be saved in advance
    [["Skeleton",(10.5,9.5)],["Skeleton",(10.5,33.5)],["Skeleton",(23.5,7.5)],["Skeleton",(23.5,15.5)],["Skeleton",(30.5,17.5)],["Skeleton",(35.5,24.5)],
    ["Skeleton",(22.5,29.5)],["Skeleton",(24.5,36.5)],["Skeleton",(31.5,26.5)]], # Enemies (Type,(X,Y))
    [["Health",(6.5,29.5)],["Shield",(6.5,34.5)],["Shield",(19.5,24.5)],["Shield",(20.5,24.5)],["Shield",(21.5,24.5)],["Health",(33.5,21.5)],["Health",(37.5,21.5)],["Shield",(35.5,23.5)],["Health",(21.5,33.5)],["Shield",(33.5,37.5)],["Shield",(36.5,37.5)],
    ["Shell",(38.5,33.5)],["Slug",(38.5,31.5)],["Shell",(15.5,29.5)],["Slug",(15.5,34.5)]] # Health & Ammo Pickups (Type,(X,Y))
    ]]

level2 = [
    [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','6','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','2','2','2','2','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','4','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','2','2','2','2','0','0','0','0','0','0','2','2','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','2','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','0','0','0','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','2','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','0','0','0','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','2','2','1','1','1','1','1','1','2','0','2','2','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','2','2','1','1','1','1','1','1','1','1','1','2','0','2','2','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','2','2','0','0','2','2','1','1','1','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','0','0','0','0','0','0','0','0','1','1','2','0','0','0','0','0','2','2','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','0','0','0','0','0','0','0','0','1','1','2','0','0','0','0','0','2','2','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','2','0','0','0','0','0','3','0','0','0','0','0','2','2','0','0','2','1','1','1','1','1','1','1','1','2','2','2','2','2','1','1','1','2','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','2','0','0','0','0','0','2','2','0','0','0','0','2','2','0','0','2','2','2','2','1','1','1','1','2','0','0','0','0','0','2','1','1','2','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','2','4','2','2','2','0','0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','2','0','0','0','0','0','2','2','2','2','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','2','2','2','2','2','0','0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','2','0','0','0','0','0','2','1','2','2','2','2','2','2','2','2','2','2','2','2','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','2','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','1','1','2','0','0','2','2','2','2','2','2','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','0','2','2','1','1','1','1','1','1','1','1','1','1','1','2','0','0','0','0','2','1','2','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','2','0','0','0','0','2','2','2','0','0','2','2','2','2','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','0','2','2','2','2','2','2','2','2','2','2','2','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','2','0','0','0','2','2','2','2','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','0','2','2','0','0','2','2','0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','2','0','0','0','2','1','1','2','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','0','0','0','2','1','1','2','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','2','0','0','0','2','0','0','0','2','1','1','2','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','2','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1''1','1']
    ],
    [39.5,31.5,math.pi,100,0,10,10,
    [["Skeleton",(25.5,25.5)],["Skeleton",(26.5,28.5)],["Skeleton",(34.5,20.5)],["Skeleton",(46.5,6.5)],["Skeleton",(39.5,6.5)],
    ["Skeleton",(39.5,12.5)],["Skeleton",(17.5,31.5)],["Skeleton",(11.5,27.5)],["Skeleton",(4.5,26.5)],["Skeleton",(8.5,23.5)],
    ["Skeleton",(11.5,21.5)],["Skeleton",(8.5,15.5)],["Skeleton",(6.5,15.5)],["Skeleton",(1.5,19.5)],["Skeleton",(35.5,19.5)],
    ["Skeleton",(25.5,20.5)],["Skeleton",(14.5,9.5)],["Skeleton",(27.5,11.5)],["Skeleton",(25.5,5.5)],["Skeleton",(23.5,3.5)],["Skeleton",(16.5,5.5)]],
    [["Shield",(36.5,31.5)],["Shield",(37.5,31.5)],["Shield",(31.5,33.5)],["Shield",(27.5,24.5)],["Shield",(5.5,18.5)],["Shield",(14.5,21.5)],["Shield",(20.5,7.5)],["Shield",(21.5,7.5)],["Shield",(36.5,15.5)],
    ["Health",(25.5,33.5)],["Health",(43.5,19.5)],["Health",(47.5,11.5)],["Health",(25.5,13.5)],["Health",(16.5,13.5)],["Health",(9.5,29.5)],["Health",(12.5,29.5)],["Health",(4.5,19.5)],
    ["Shell",(20.5,27.5)],["Slug",(19.5,27.5)],["Shell",(7.5,22.5)],["Slug",(7.5,19.5)],["Shell",(13.5,7.5)],["Slug",(28.5,7.5)],["Shell",(42.5,7.5)],["Slug",(41.5,7.5)]]
    ]]

class Map:
    def __init__(self,GAME,LEVEL):
        self.game = GAME
        self.levelMap = LEVEL[0]
        self.metadata = LEVEL[1]
        self.worldMap = {}
        self.createMap()
    
    def createMap(self):
        for y, row in enumerate(self.levelMap):
            for x, column in enumerate(row):
                if column != "0":
                    self.worldMap[(x,y)] = column