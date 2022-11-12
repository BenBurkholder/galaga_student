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

class GameState():
    def __init__(self):
        self.state = 'main_game'
        self.timer = 0
        self.delta = 0
        self.dead = False
        self.shotDelta = 250
        self.enemyShotDelta = 250
        self.score = 0
        self.selectedWeapon = 1
        self.enemy = Enemy2((5000,5000), players)

    def main_game(self):
        #  increment timer
        self.timer += 1

        # First thing we need to clear the events.
        if self.dead:
            time.sleep(5)
            return False
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                background.youLose(self.delta)
                background.draw(screen)
                self.dead = True
            if event.type == pg.USEREVENT + 1:
                self.score += 100

        

        keys = pg.key.get_pressed()

        if keys[K_s] | keys[K_DOWN]:
            player.down(self.delta)
        if keys[K_w] | keys[K_UP]:
            player.up(self.delta)
        if keys[K_a] | keys[K_LEFT]:
            player.left(self.delta)
        if keys[K_d] | keys[K_RIGHT]:
            player.right(self.delta)
        if keys[K_SPACE]:
            if self.selectedWeapon !=3:
                if self.shotDelta >= .10:
                    if self.selectedWeapon == 1:
                        projectile = Projectile(player.rect, enemies)
                        projectiles.add(projectile)
                    if self.selectedWeapon == 2:
                        projectile = Projectile3(player.rect, enemies)
                        projectiles.add(projectile) 
                        projectile2 = Projectile4(player.rect, enemies)
                        projectiles.add(projectile2)
                    self.shotDelta = 0
            elif self.shotDelta >=.01:
                projectile = Projectile5(player.rect, enemies)
                projectiles.add(projectile)
                self.shotDelta = 0
        if keys[K_TAB]:
            pygame.key.set_repeat(8)
            if self.selectedWeapon == 3:
                self.selectedWeapon = 1
            else:
                self.selectedWeapon = self.selectedWeapon + 1
        if keys[K_1]:
            self.selectedWeapon = 1
        if keys[K_2]:
            self.selectedWeapon = 2
        if keys[K_3]:
            self.selectedWeapon = 3
  
        #add new mobile enemies
        if self.timer % 100 == 0:
            self.enemy = Enemy2((1024,random.randint(1, 720)), players)
            enemies.add(self.enemy)

        #new enemy movement
        if self.enemy:
            for enemy in enemies:
                enemy.left(self.delta)

        # enemy firing        
        if self.enemy:
            for enemy in enemies:
                if self.enemyShotDelta >= 1 and random.randint(1, 20) == 10:
                    projectile = Projectile2(enemy.rect, players)
                    projectiles.add(projectile)
                    self.enemyShotDelta = 0

        # Ok, events are handled, let's update objects!
        player.update(self.delta)
        for enemy in enemies:
            enemy.update(self.delta)
        for projectile in projectiles:
            projectile.update(self.delta)

        # Objects are updated, now let's draw!
        screen.fill((0, 0, 0))
        background.draw(screen)
        player.draw(screen)
        enemies.draw(screen)
        projectiles.draw(screen)
        font.render_to(screen, (10, 10), "Score: " + str(score), FONTCOLOR, None, size=64)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        # How much time has passed this loop?
        self.delta = clock.tick(fps) / 1000.0
        self.shotDelta += self.delta
        self.enemyShotDelta += self.delta
        
        #did you win?
        # if len(enemies) == 0:
        #     print("Congratulations! You win.")
        #     running = False

        if self.timer > 2500 :
            print("times up")
            return False
        return True


# def main():
# Startup pygame
pg.init()



# Get a screen object
screen = pg.display.set_mode([1024, 768])

# Create a background
background = Background()
#screen.blit(background.surf, background.rect)
background.draw(screen)


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
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets", "PermanentMarker-Regular.ttf")
font_size = 64
font = pg.freetype.Font(font_path, font_size)
# Make a tuple for FONTCOLOR - TODO
FONTCOLOR = (200, 20, 20)
# Startup the main game loop
running = True
# Frame limiting
fps = 180
clock = pg.time.Clock()
# Setup score variable
score = 0

mygame = GameState()
keepGoing = True
while keepGoing:
    keepGoing = mygame.main_game()
    clock.tick(fps)


