from pygame import *
from os.path import abspath, dirname

BASE_PATH  = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/../images/'

SCREEN = display.set_mode((800, 600))

class Ship(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(IMAGE_PATH + '{}.png'.format('ship')).convert_alpha()
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.speed = 5

    def update(self, spaceInvaders, keys, *args):
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
        spaceInvaders.screen.blit(self.image, self.rect)