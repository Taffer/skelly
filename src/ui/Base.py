''' Skelly UI element base class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame


class Base:
    def __init__(self):
        self.rect = pygame.Rect((0, 0, 0, 0))

    def intersects(self, x, y):
        if x < self.rect.left or y < self.rect.top:
            return False

        if x > (self.rect.left + self.rect.width) or y > (self.rect.top + self.rect.height):
            return False

        return True
