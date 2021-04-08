# Skelly UI element: image button
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from .Base import Base


class ImageButton(Base):
    def __init__(self, x, y, texture):
        super().__init__()

        self.texture = texture
        self.rect = self.texture.get_rect()
        self.rect.left = x
        self.rect.top = y

    def draw(self):
        pygame.display.get_surface().blit(self.texture, self.rect)
