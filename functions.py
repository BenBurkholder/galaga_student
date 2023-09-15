import os
import pygame as pg
#functions.py

def spawnEnemy(enemyType, Xpos, Ypos, player, movement):
    self.enemy = enemyType(Xpos,Ypos, player, movement)
    self.enemies.add(player)