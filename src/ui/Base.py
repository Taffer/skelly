''' Skelly UI element base class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame


class Base:
    def __init__(self):
        self.rect = pygame.Rect((0, 0, 0, 0))

    def intersects(self, x, y):
        return self.rect.collidepoint(x, y)
