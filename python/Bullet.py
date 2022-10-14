from pygame import *
from os.path import abspath, dirname

BASE_PATH  = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/../images/'

class Bullet(sprite.Sprite):
    def __init__(self, xpos, ypos, direction, speed, filename, side):
        sprite.Sprite.__init__(self)
        self.image = image.load(IMAGE_PATH + '{}.png'.format(filename)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.speed = speed
        self.direction = direction
        self.side = side
        self.filename = filename

    def update(self, spaceInvaders, keys, *args):
        spaceInvaders.screen.blit(self.image, self.rect)
        self.rect.y += self.speed * self.direction
        if self.rect.y < 15 or self.rect.y > 600:
            self.kill()