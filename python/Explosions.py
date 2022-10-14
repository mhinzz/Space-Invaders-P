from pygame import *
from os.path import abspath, dirname

from Text import Text

BASE_PATH  = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/../images/'
FONT_PATH  = BASE_PATH + '/../fonts/'
FONT = FONT_PATH + 'space-invaders-p.ttf'
IMG_NAMES = ['ship', 'explosionblue', 'explosiongreen', 'explosionpurple']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}

WHITE  = (255, 255, 255)

class EnemyExplosion(sprite.Sprite):
    def __init__(self, enemy, *groups):
        super(EnemyExplosion, self).__init__(*groups)
        self.image = transform.scale(self.get_image(enemy.row), (40, 35))
        self.image2 = transform.scale(self.get_image(enemy.row), (50, 45))
        self.rect = self.image.get_rect(topleft=(enemy.rect.x, enemy.rect.y))
        self.timer = time.get_ticks()

    @staticmethod
    def get_image(row):
        img_colors = ['purple', 'blue', 'blue', 'green', 'green']
        return IMAGES['explosion{}'.format(img_colors[row])]

    def update(self, spaceInvaders, keys, current_time, *args):
        passed = current_time - self.timer
        if passed <= 100:
            spaceInvaders.screen.blit(self.image, self.rect)
        elif passed <= 200:
            spaceInvaders.screen.blit(self.image2, (self.rect.x - 6, self.rect.y - 6))
        elif 400 < passed:
            self.kill()


class MysteryExplosion(sprite.Sprite):
    def __init__(self, mystery, score, *groups):
        super(MysteryExplosion, self).__init__(*groups)
        self.text = Text(FONT, 20, str(score), WHITE,
                         mystery.rect.x + 20, mystery.rect.y + 6)
        self.timer = time.get_ticks()

    def update(self, spaceInvaders, keys, current_time, *args):
        passed = current_time - self.timer
        if passed <= 200 or 400 < passed <= 600:
            self.text.draw(spaceInvaders.screen)
        elif 600 < passed:
            self.kill()


class ShipExplosion(sprite.Sprite):
    def __init__(self, ship, *groups):
        super(ShipExplosion, self).__init__(*groups)
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(ship.rect.x, ship.rect.y))
        self.timer = time.get_ticks()

    def update(self, spaceInvaders, keys, current_time, *args):
        passed = current_time - self.timer
        if 300 < passed <= 600:
            spaceInvaders.screen.blit(self.image, self.rect)
        elif 900 < passed:
            self.kill()