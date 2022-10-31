#!/usr/bin/env python3

import pygame as pg
import pygame.freetype
import os
import random
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

def main():
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
    selectedWeapon = 1


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
    # Keep track of time
    delta = 0
    # Make sure we can't fire more than once every 250ms
    shotDelta = 250
    # Make sure enemies can't fire more than once every 1000ms
    enemyShotDelta = 250
    # Frame limiting
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    # Setup score variable
    score = 0
    # Setup movement variable
    move = 0
    timer = 0
    enemy = Enemy2((5000,5000), players)
    while running:
        #increment timer
        timer += 1

        # First thing we need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 100

        keys = pg.key.get_pressed()

        if keys[K_s] | keys[K_DOWN]:
            player.down(delta)
        if keys[K_w] | keys[K_UP]:
            player.up(delta)
        if keys[K_a] | keys[K_LEFT]:
            player.left(delta)
        if keys[K_d] | keys[K_RIGHT]:
            player.right(delta)
        if keys[K_SPACE]:
            if selectedWeapon !=3:
                if shotDelta >= .25:
                    if selectedWeapon == 1:
                        projectile = Projectile(player.rect, enemies)
                        projectiles.add(projectile)
                    if selectedWeapon == 2:
                        projectile = Projectile3(player.rect, enemies)
                        projectiles.add(projectile) 
                        projectile2 = Projectile4(player.rect, enemies)
                        projectiles.add(projectile2)
                    shotDelta = 0
            elif shotDelta >=.05:
                projectile = Projectile5(player.rect, enemies)
                projectiles.add(projectile)
                shotDelta = 0
        if keys[K_TAB]:
            pygame.key.set_repeat(8)
            if selectedWeapon == 3:
                selectedWeapon = 1
            else:
                selectedWeapon = selectedWeapon + 1
        if keys[K_1]:
            selectedWeapon = 1
        if keys[K_2]:
            selectedWeapon = 2
        if keys[K_3]:
            selectedWeapon = 3
  
        #add new mobile enemies
        if timer % 100 == 0:
            enemy = Enemy2((1024,random.randint(1, 720)), players)
            enemies.add(enemy)
        
        # enemy movement
        # enemyMove = move % 100
        # if enemyMove < 50:
        #     for enemy in enemies:
        #         enemy.down(delta)
        # if enemyMove > 49:
        #     for enemy in enemies:
        #         enemy.up(delta)
        # move = move + 1

        #new enemy movement
        if enemy:
            for enemy in enemies:
                enemy.left(delta)



        # enemy firing        
        if enemy:
            for enemy in enemies:
                if enemyShotDelta >= 1 and random.randint(1, 20) == 10:
                    projectile = Projectile2(enemy.rect, players)
                    projectiles.add(projectile)
                    enemyShotDelta = 0

        # Ok, events are handled, let's update objects!
        player.update(delta)
        for enemy in enemies:
            enemy.update(delta)
        for projectile in projectiles:
            projectile.update(delta)

        # Objects are updated, now let's draw!
        screen.fill((0, 0, 0))
        background.draw(screen)
        player.draw(screen)
        enemy.draw(screen)
        enemies.draw(screen)
        projectiles.draw(screen)
        font.render_to(screen, (10, 10), "Score: " + str(score), FONTCOLOR, None, size=64)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        # How much time has passed this loop?
        delta = clock.tick(fps) / 1000.0
        shotDelta += delta
        enemyShotDelta += delta
        
        #did you win?
        # if len(enemies) == 0:
        #     print("Congratulations! You win.")
        #     running = False

        if timer > 2500 :
            print("times up")
            running = False

# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()
