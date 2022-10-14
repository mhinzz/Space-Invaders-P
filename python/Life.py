from pygame import *
from os.path import abspath, dirname

BASE_PATH  = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/../images/'

class Life(sprite.Sprite):
    def __init__(self, xpos, ypos):
        sprite.Sprite.__init__(self)
        self.image = image.load(IMAGE_PATH + '{}.png'.format('ship')).convert_alpha()
        self.image = transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, spaceInvaders, *args):
        spaceInvaders.screen.blit(self.image, self.rect)