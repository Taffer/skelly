# Skelly UI element: text label
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from . import Base


class Label(Base):
    def __init__(self, x, y, text, font, color, align):
        super().__init__()

        self.orig_x = x
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.align = align

        self.setText(text)

    def draw(self):
        pygame.display.get_surface().blit(self.texture, self.rect)

    def setText(self, text):
        self.texture = self.font.render(text, True, self.color)
        self.rect = self.texture.get_rect()

        if self.align == 'right':
            self.x = self.orig_x - self.rect.width
        elif self.align == 'centre' or self.align == 'center':
            self.x = self.orig_x - self.rect.width / 2

        self.rect.left = self.x
        self.rect.top = self.y
