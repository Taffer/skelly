# Skelly UI element: image button
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from . import Base


class ImageButton(Base):
    def __init__(self, x: int, y: int, texture: pygame.Surface) -> None:
        super().__init__()

        self.texture = texture
        self.rect = self.texture.get_rect()
        self.rect.left = x
        self.rect.top = y

    def draw(self) -> None:
        pygame.display.get_surface().blit(self.texture, self.rect)
