import os
import pygame as pg

# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the 
# rectangle x, y or centerx and centery to move the object.

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((75,40))
        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = self.surf.get_rect(center=(100,300))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):

        self.rect.move_ip(0,0)

    def up(self, delta):
        if self.rect.y > 0:
            self.rect.move_ip(0, -5)

    def down(self, delta):
        if self.rect.y < 700:
            self.rect.move_ip(0, 5)
    
    def left(self, delta):
        if self.rect.x > 5:
            self.rect.move_ip(-5, 0)
    
    def right(self, delta):
        if self.rect.x < 1020:
            self.rect.move_ip(5, 0)