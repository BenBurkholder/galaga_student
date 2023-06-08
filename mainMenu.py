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
from menuBackground import Background
from projectile import Projectile
from pygame.locals import *
from enemy2 import Enemy2
from optionNewGame import OptionNewGame

class MainMenu():
    def __init__(self, player, screen, font, fontcolor, fps):
        self.state = 'main_game'
        self.timer = 0
        self.delta = 0
        self.dead = False
        self.shotDelta = 250
        self.enemyShotDelta = 250
        self.score = 0
        self.selectedWeapon = 1
        self.enemy = Enemy2((5000,5000), player)
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.screen = screen
        self.background = Background()
        self.font = font
        self.FONTCOLOR = fontcolor
        self.delta = 0
        self.fps = fps
        self.player = player
        self.clock = clock = pg.time.Clock()
        self.players = pygame.sprite.Group()
        self.players.add(self.player)

    def main_game(self):
        #  increment timer
        self.timer += 1

        # First thing we need to clear the events.
        if self.dead:
            time.sleep(5)
            return "no"
        pg.key.set_repeat(200,200)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.background.youLose(self.delta)
                self.background.draw(self.screen)
                self.dead = True
            if event.type == pg.USEREVENT + 1:
                self.score += 100
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_UP) | (event.key == pg.K_w):
                    self.player.menuMoveUp(self.delta)
                elif (event.key == pg.K_DOWN) | (event.key == pg.K_s):
                    self.player.menuMoveDown(self.delta)
                if (event.key == pg.K_SPACE) | (event.key == pg.K_RETURN):
                    if self.player.menuSelect() == "levelOne":
                        return "next"
                    elif self.player.menuSelect() == "exitProgram":
                        return "no"
        
        # keys = pg.key.get_pressed()

        # if keys[K_s] | keys[K_DOWN]:
        #     self.player.menuMoveDown(self.delta)
        # if keys[K_w] | keys[K_UP]:
        #     self.player.menuMoveUp(self.delta)
        # if keys[K_a] | keys[K_LEFT]:
        #     self.player.left(self.delta)
        # if keys[K_d] | keys[K_RIGHT]:
        #     self.player.right(self.delta)
        # if keys[K_SPACE]:
        #     if self.selectedWeapon !=3:
        #         if self.shotDelta >= .3:
        #             if self.selectedWeapon == 1:
        #                 projectile = Projectile(self.player.rect, self.enemies)
        #                 self.projectiles.add(projectile)
        #             if self.selectedWeapon == 2:
        #                 projectile = Projectile3(self.player.rect, self.enemies)
        #                 self.projectiles.add(projectile) 
        #                 projectile2 = Projectile4(self.player.rect, self.enemies)
        #                 self.projectiles.add(projectile2)
        #             self.shotDelta = 0
        #     elif self.shotDelta >=.05:
        #         projectile = Projectile5(self.player.rect, self.enemies)
        #         self.projectiles.add(projectile)
        #         self.shotDelta = 0
        # if keys[K_TAB]:
        #     pygame.key.set_repeat(8)
        #     if self.selectedWeapon == 3:
        #         self.selectedWeapon = 1
        #     else:
        #         self.selectedWeapon = self.selectedWeapon + 1
        # if keys[K_1]:
        #     self.selectedWeapon = 1
        # if keys[K_2]:
        #     self.selectedWeapon = 2
        # if keys[K_3]:
        #     self.selectedWeapon = 3

        # add menu items 

        # if self.timer == 1:
        #     self.enemy = OptionNewGame((150, 450), self.players)
        #     self.enemies.add(self.enemy)
        # #add new mobile enemies
        # if self.timer % 100 == 0:
        #     self.enemy = Enemy2((1024,random.randint(1, 720)), self.players)
        #     self.enemies.add(self.enemy)

        # #new enemy movement
        # if self.enemy:
        #     for enemy in self.enemies:
        #         enemy.left(self.delta)

        # # enemy firing        
        # if self.enemy:
        #     for enemy in self.enemies:
        #         if self.enemyShotDelta >= 1 and random.randint(1, 20) == 10:
        #             projectile = Projectile2(enemy.rect, self.players)
        #             self.projectiles.add(projectile)
        #             self.enemyShotDelta = 0

        # Ok, events are handled, let's update objects!
        self.player.update(self.delta)
        for enemy in self.enemies:
            enemy.update(self.delta)
        for projectile in self.projectiles:
            projectile.update(self.delta)

        # Objects are updated, now let's draw!
        self.screen.fill((0, 0, 0))
        self.background.draw(self.screen)
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)
        self.projectiles.draw(self.screen)
        self.font.render_to(self.screen, (10, 10), "Score: " + str(self.score), self.FONTCOLOR, None, size=64)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        # How much time has passed this loop?
        self.delta = self.clock.tick(self.fps) / 1000.0
        self.shotDelta += self.delta
        self.enemyShotDelta += self.delta
        
        # #did you win?
        # if len(self.enemies) == 1:
        #     print(self.enemies[0])
        # #     running = False

        # if self.timer > 500 :
        #     print("times up")
        #     return "next"
        if self.player.isDead() == True:
            return "reset"
        return "yes"