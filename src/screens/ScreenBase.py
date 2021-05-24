''' Skelly screen base class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from ..ui import ImageButton
from ..ui import Label

WHITE = pygame.Color('white')


class ScreenBase:
    def __init__(self, game) -> None:
        ''' Initialize.

        @param game Game global state.
        '''
        self.game = game

        self.can_exit = False  # Time for this screen to exit?
        self.next_screen = None  # Next screen to display.

        self.has_title = False
        self.title_ui = []  # For Title elements.

    def draw(self) -> None:
        ''' Draw the screen's contents.
        '''
        pass

    def update(self, dt: float) -> None:
        ''' Update the screen's contents.
        '''
        pass

    def keypressed(self, event: pygame.event.Event) -> None:
        pass

    def keyreleased(self, event: pygame.event.Event) -> None:
        pass

    def mousemoved(self, event: pygame.event.Event) -> None:
        pass

    def mousedown(self, event: pygame.event.Event) -> None:
        pass

    def mouseup(self, event: pygame.event.Event) -> None:
        pass

    def userevent(self, event: pygame.event.Event) -> None:
        pass

    def add_title(self) -> None:
        title_text = self.game.text.get_text('title')
        skelly_text = self.game.text.get_text('skelly_title')
        subtitle_text = title_text['subtitle_text']

        self.title_ui = [
            ImageButton(0, 0, self.game.resources['images']['skelly_title']),
            Label(self.game.screen_width / 2, 40, skelly_text, self.game.resources['fonts']['skelly_title'],
                  WHITE, 'centre'),
            Label(self.game.screen_width / 2, 220, subtitle_text, self.game.resources['fonts']['germania'],
                  WHITE, 'centre'),
        ]

        self.has_title = True

    def draw_title(self) -> None:
        if self.has_title:
            for item in self.title_ui:
                item.draw()
