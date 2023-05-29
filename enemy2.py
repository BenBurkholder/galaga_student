import os
import pygame as pg

# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the 
# rectangle x, y or centerx and centery to move the object.

class Enemy2(pg.sprite.Sprite):
    def __init__(self, position, enemies):
        super(Enemy2, self).__init__()
        self.size=(150,50)
        self.surf = pg.Surface(self.size)
        self.image = pg.image.load(os.path.join('assets', 'Dragon.png')).convert_alpha()
        self.image = pg.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect = self.surf.get_rect(center=(position))
        self.enemies = enemies
        self.health=2
        self.explosionSound = pg.mixer.Sound(os.path.join('assets', 'explosion.wav'))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.move_ip(0,0)
        if self.rect.x < 0:
            self.kill()
        collision = pg.sprite.spritecollideany(self, self.enemies)
        if collision:
            collision.damage()
            self.explosionSound.play()
            self.kill()

    def up(self, delta):
        self.rect.move_ip(0, -1)

    def down(self, delta):
        self.rect.move_ip(0, 1)

    def left(self,delta):
        self.rect.move_ip(-1,0)

    def right(self,delta):
        self.rect.move_ip(1,0)

    def damage(self):
        self.health -=1
        if self.health == 0:
            self.kill()