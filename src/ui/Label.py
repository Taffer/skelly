# Skelly UI element: text label
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame
import pygame.freetype

from .UIBase import UIBase


class Label(UIBase):
    def __init__(self, x: int, y: int, text: str, font: pygame.freetype.Font, color: pygame.Color, align: str) -> None:
        super().__init__()

        self.orig_x = x
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.align = align

        self.texture = None
        self.rect = None

        self.set_text(text)

    def draw(self) -> None:
        pygame.display.get_surface().blit(self.texture, self.rect)

    def set_text(self, text: str) -> None:
        self.texture, self.rect = self.font.render(text, self.color)

        if self.align == 'right':
            self.x = self.orig_x - self.rect.width
        elif self.align == 'centre' or self.align == 'center':
            self.x = self.orig_x - self.rect.width / 2

        self.rect.left = self.x
        self.rect.top = self.y
