# Skelly settings screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from . import Base
from ..ui import SettingsOverlay
from ..ui import ColorFade

BLACK = pygame.Color('black')
BLACK_ALPHA = pygame.Color(BLACK.r, BLACK.g, BLACK.g, 0)  # BLACK, but fully transparent
WHITE = pygame.Color('white')


class Settings(Base):
    def __init__(self, game):
        super().__init__(game)

        self.next_screen = 'Journey'

        self.addTitle()

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)

        # self.overlay = SettingsOverlay:new(resources, 300, 350, 680, 400)

    def draw(self):
        self.game.surface.fill(BLACK)
        self.drawTitle()

    def update(self, dt):
        self.fade.update(dt)
