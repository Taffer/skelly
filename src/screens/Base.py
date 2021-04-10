''' Skelly screen base class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from ..ui import ImageButton
from ..ui import Label

WHITE = pygame.Color('white')


class Base:
    def __init__(self, game):
        ''' Initialize.

        @param game Game global state.
        '''
        self.game = game

        self.can_exit = False  # Time for this screen to exit?
        self.next_screen = None  # Next screen to display.

        self.has_title = False
        self.title_ui = []  # For Title elements.

    def draw(self):
        ''' Draw the screen's contents.
        '''
        pass

    def update(self, dt):
        ''' Update the screen's contents.
        '''
        pass

    def keypressed(self, event):
        pass

    def keyreleased(self, event):
        pass

    def mousemoved(self, event):
        pass

    def mousedown(self, event):
        pass

    def mouseup(self, event):
        pass

    def userevent(self, event):
        pass

    def addTitle(self):
        title_text = self.game.text.getText('title')
        skelly_text = self.game.text.getText('skelly_title')
        subtitle_text = title_text['subtitle_text']

        self.title_ui = [
            ImageButton(0, 0, self.game.resources['images']['skelly_title']),
            Label(self.game.screen_width / 2, 40, skelly_text, self.game.resources['fonts']['skelly_title'],
                  WHITE, 'centre'),
            Label(self.game.screen_width / 2, 220, subtitle_text, self.game.resources['fonts']['default_mono'],
                  WHITE, 'centre'),
        ]

        self.has_title = True

    def drawTitle(self):
        if self.has_title:
            for item in self.title_ui:
                item.draw()
