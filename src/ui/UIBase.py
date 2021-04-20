''' Skelly UI element base class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame


class UIBase:
    def __init__(self) -> None:
        self.rect = pygame.Rect((0, 0, 0, 0))

    def intersects(self, x: int, y: int) -> bool:
        return self.rect.collidepoint(x, y)
