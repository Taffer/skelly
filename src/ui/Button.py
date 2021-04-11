# Skelly UI - Button
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame
import pygame.freetype

from . import Base
from . import ImageButton
from . import Label


class Button(Base):
    def __init__(self, x: int, y: int, texture: pygame.Surface, text: str, font: pygame.freetype.Font, color: pygame.Color):
        super().__init__()

        self.x = x
        self.y = y

        self.imageButton = ImageButton.ImageButton(x, y, texture)
        self.rect = texture.get_rect()
        self.rect.left = x
        self.rect.top = y

        label_x = x + self.rect.width / 2
        label_y = y + (self.rect.height - font.get_sized_height()) / 2
        self.labelButton = Label.Label(label_x, label_y, text, font, color, 'centre')

    def draw(self):
        self.imageButton.draw()
        self.labelButton.draw()
