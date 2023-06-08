#!/usr/bin/env python3

import pygame as pg
import pygame.freetype
import os
import random
import time
from enemy import Enemy
from player import Player
from projectile2 import Projectile2
from projectile3 import Projectile3
from projectile4 import Projectile4
from projectile5 import Projectile5
from background import Background
from projectile import Projectile
from pygame.locals import *
from enemy2 import Enemy2
from levelOne import LevelOne
from levelTwo import LevelTwo
from mainMenu import MainMenu
from upgradeMenu import UpgradeMenu




# def main():
# Startup pygame
pg.init()



# Get a screen object
screen = pg.display.set_mode([1024, 768])

# Create a background
background = Background()
#screen.blit(background.surf, background.rect)
background.draw(screen)

#add list of levels
levelList=[MainMenu, LevelOne, UpgradeMenu, LevelTwo]
levelListInt=0
#player.add(player)    

# Create a player - TODO
player = Player()
#screen.blit(player.surf, player.rect)
player.draw(screen)
players = pygame.sprite.Group()
players.add(player)

# Create enemy and projectile Groups - TODO
enemies = pygame.sprite.Group()
# for i in range(500, 1000, 75):
#     for j in range(100, 600, 50):
#         enemy = Enemy((i, j))
#         enemies.add(enemy)
projectiles = pygame.sprite.Group()

for entity in enemies:
    #screen.blit(entity.surf, entity.rect)
    entity.draw(screen)

# Start sound - Load background music and start it
# Open Space by | e s c p | https://escp-music.bandcamp.com
# Music promoted by https://www.free-stock-music.com
# Creative Commons Attribution 3.0 Unported License
# https://creativecommons.org/licenses/by/3.0/deed.en_US

pygame.mixer.music.load(os.path.join('assets', 'openSpace.wav'))
pygame.mixer.music.play(loops=-1)

# Get font setup
pg.freetype.init()
# font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets", "PermanentMarker-Regular.ttf")
font_size = 64
font = pg.freetype.Font(None)
# Make a tuple for FONTCOLOR - TODO
FONTCOLOR = (200, 20, 20)
# Startup the main game loop
running = True
# Frame limiting
fps = 60
clock = pg.time.Clock()
# Setup score variable
score = 0

mygame = levelList[levelListInt](player, screen, font, FONTCOLOR, fps)

keepGoing = "yes"
while (keepGoing == "yes"):
    keepGoing = mygame.main_game()
    if (keepGoing == "next"):
        levelListInt=levelListInt+1
        mygame = levelList[levelListInt](player, screen, font, FONTCOLOR, fps)
        keepGoing = "yes"
    if (keepGoing == "no"):
        # levelListInt=0
        # mygame = levelList[levelListInt](player, screen, font, FONTCOLOR, fps)
        # keepGoing = "yes"
        pg.QUIT
    if (keepGoing == "reset"):
        levelListInt=0
        mygame = levelList[levelListInt](player, screen, font, FONTCOLOR, fps)
        keepGoing = "yes"
    clock.tick(fps)


