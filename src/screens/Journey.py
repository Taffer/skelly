# Skelly "Journey Onward" screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from . import Base
from . import ColorFade
from ..ui import Button
from ..ui import ImageButton
from ..ui import Label

BLACK = pygame.colordict.THECOLORS['black']
BLACK_ALPHA = (BLACK[0], BLACK[1], BLACK[2], 0)  # BLACK, but fully transparent
WHITE = pygame.colordict.THECOLORS['white']


class Journey(Base):
    def __init__(self, game):
        super().__init__(game)

        # next_screen is set when a button is clicked.

        title_text = game.text.getText('title')
        journey_text = game.text.getText('journey')
        self.skelly_text = game.text.getText('skelly_title')
        self.subtitle_text = title_text['subtitle_text']
        self.journey_text = journey_text['onward_text']
        self.newgame_text = journey_text['new_game_text']
        self.settings_text = journey_text['settings_text']
        self.credits_text = journey_text['credits_text']
        self.exit_text = journey_text['exit_text']

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)

        ui_rpg = game.resources['images']['ui_rpg']
        button_rect = pygame.Rect(0, 282, 190, 49)
        button_texture = ui_rpg.subsurface(button_rect)

        x = (game.screen_width - 190) / 2  # Buttons are 190 pixels wide.

        button_font = game.resources['fonts']['button_font']
        button_color = BLACK
        self.journey_button = Button(x, 350, button_texture, self.journey_text, button_font, button_color)
        self.newgame_button = Button(x, 410, button_texture, self.newgame_text, button_font, button_color)
        self.settings_button = Button(x, 470, button_texture, self.settings_text, button_font, button_color)
        self.credits_button = Button(x, 550, button_texture, self.credits_text, button_font, button_color)
        self.exit_button = Button(x, 620, button_texture, self.exit_text, button_font, button_color)

        title_image = game.resources['images']['skelly_title']
        font_mono = game.resources['fonts']['default_mono']
        font_title = game.resources['fonts']['skelly_title']

        self.ui = [
            ImageButton(0, 0, title_image),
            Label(game.screen_width / 2, 40, self.skelly_text, font_title, WHITE, 'centre'),
            Label(game.screen_width / 2, 220, self.subtitle_text, font_mono, WHITE, 'centre'),

            self.journey_button,
            self.newgame_button,
            self.settings_button,
            self.credits_button,
            self.exit_button,
        ]

    def draw(self):
        for item in self.ui:
            item.draw()

        if not self.fade.isDone():
            self.fade.draw()

    def update(self, dt):
        self.fade.update(dt)
