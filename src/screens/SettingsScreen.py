# Skelly settings screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from .ScreenBase import ScreenBase
from ..ui import SettingsOverlay
from ..ui import ColorFade

BLACK = pygame.Color('black')
BLACK_ALPHA = pygame.Color(BLACK.r, BLACK.g, BLACK.g, 0)  # BLACK, but fully transparent
WHITE = pygame.Color('white')


class SettingsScreen(ScreenBase):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.next_screen = 'Journey'

        self.add_title()
        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)
        self.overlay = SettingsOverlay(game)

    def draw(self) -> None:
        self.game.surface.fill(BLACK)
        self.draw_title()

        self.game.manager.draw_ui(self.game.surface)

    def update(self, dt: float) -> None:
        self.fade.update(dt)

        if self.overlay.overlay_closed:
            self.can_exit = True

    def userevent(self, event: pygame.event.Event) -> None:
        self.overlay.userevent(event)
