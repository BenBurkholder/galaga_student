import os
import pygame as pg

# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the 
# rectangle x, y or centerx and centery to move the object.

class Background(pg.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.surf = pg.Surface((1024, 768))
        # image from https://www.10wallpaper.com/view/2019_Fractal_Nebula_Glow_Space_HD_Universe.html
        # no artist credited 
        self.image = pg.image.load(os.path.join('assets', 'space.png')).convert_alpha()
        self.rect = self.image.get_rect()
        #self.rect = self.surf.get_rect(center=(0,0))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.move_ip(0,0)

    def up(self, delta):
        self.rect.move_ip(0, -1)

    def down(self, delta):
        self.rect.move_ip(0, 1)

    def youLose(self, delta):
        self.image = pg.image.load(os.path.join('assets', 'youLose.png')).convert_alpha()
        self.rect = self.image.get_rect()
        # self.update(delta)
