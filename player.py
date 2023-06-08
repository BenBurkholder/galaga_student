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
        self.size=(75,40)
        self.surf = pg.Surface(self.size)
        self.image = pg.image.load(os.path.join('assets', 'NewShip3.png')).convert_alpha()
        # self.defaultImageSize=(75,400)
        self.image = pg.transform.scale(self.image, self.size)
        self.rect = self.surf.get_rect()
        self.rect = self.surf.get_rect(topleft=(60,425))
        self.health = 2
        self.endGame =  pg.QUIT
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
    
    def damage(self):
        self.health -= 1
        # if self.health == 0:
        #     pg.event.post(pg.event.Event(self.endGame))

    def isDead(self):
        if self.health < 1:
            self.rect.y=425
            self.rect.x=60
            self.health = 2
            return True
        else:
            return False

#Movement for Menus
    def menuMoveUp(self, delta):
        if self.rect.y==425:
            self.rect.y=525
        elif self.rect.y==475:
            self.rect.y=425
        elif self.rect.y==525:
            self.rect.y=475

    def menuMoveDown(self, delta):
        if self.rect.y==525:
            self.rect.y=425
        elif self.rect.y==475:
            self.rect.y=525
        elif self.rect.y==425:
            self.rect.y=475

    def menuSelect(self):
        if self.rect.y==425:
            return "levelOne"
        elif self.rect.y==475:
            return "levelTwo"
        elif self.rect.y==525:
            return "exitProgram"
            