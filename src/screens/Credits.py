#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from .ScreenBase import ScreenBase
from ..ui import ColorFade

BLACK = pygame.Color('black')
BLACK_ALPHA = pygame.Color(BLACK.r, BLACK.g, BLACK.g, 0)  # BLACK, but fully transparent
CREDITS_BLACK = pygame.Color(BLACK.r, BLACK.g, BLACK.g, 3 * 255 // 4)  # BLACK, but slightly transparent
WHITE = pygame.Color('white')


class Credits(ScreenBase):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.next_screen = 'Journey'

        self.credits = game.text.get_text('credits')

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)

        self.ticks = 0
        self.credits_area = pygame.Rect(200, 250, 880, 450)

        self.font = game.resources['fonts']['default_mono']
        rect = self.font.get_rect('M')
        self.font_em = rect.width
        self.font_lh = self.font.get_sized_height()

        self.buffer = []
        self.buffer_idx = 0  # Draw from here.
        self.max_columns = self.credits_area.width // self.font_em
        self.max_lines = self.credits_area.height // self.font_lh
        self.lines_to_add = 0
        self.credits_idx = 0

        self.add_title()

    def draw(self) -> None:
        self.game.surface.fill(BLACK)
        self.draw_title()

        pygame.gfxdraw.box(self.game.surface, self.credits_area, CREDITS_BLACK)

        delta = 0
        buff_start = 0
        buff_end = len(self.buffer)
        if len(self.buffer) > self.max_lines:
            buff_start = buff_end - self.max_lines + 1

        for i in range(buff_start, buff_end):
            self.font.render_to(self.game.surface, (self.credits_area.x, self.credits_area.y + delta), self.buffer[i], WHITE)
            delta += self.font_lh

        if not self.fade.is_done():
            self.fade.draw()

    def update(self, dt: float) -> None:
        self.fade.update(dt)

        self.ticks += dt
        if self.ticks > 1:  # Every second we add a credit
            self.lines_to_add += dt

            while self.lines_to_add > 0.25:
                self.buffer.append(self.credits[self.credits_idx][1])
                self.credits_idx += 1
                if self.credits_idx >= len(self.credits):
                    self.credits_idx = 0

                self.lines_to_add -= 0.25

    def keyreleased(self, event: pygame.event.Event) -> None:
        self.can_exit = True

    def mouseup(self, event: pygame.event.Event) -> None:
        self.can_exit = True
