# Skelly "Journey Onward" screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from . import Base
from ..ui import Button
from ..ui import ColorFade

BLACK = pygame.Color('black')
BLACK_ALPHA = pygame.Color(BLACK.r, BLACK.g, BLACK.g, 0)  # BLACK, but fully transparent
WHITE = pygame.Color('white')


class Journey(Base):
    def __init__(self, game: any):
        super().__init__(game)

        # next_screen is set when a button is clicked.

        self.add_title()

        journey_text = game.text.get_text('journey')
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

        self.click_button = None  # Mouse-down on which button?

        self.ui = [
            self.journey_button,
            self.newgame_button,
            self.settings_button,
            self.credits_button,
            self.exit_button,
        ]

    def draw(self):
        self.game.surface.fill(BLACK)
        self.draw_title()

        for item in self.ui:
            item.draw()

        if not self.fade.is_done():
            self.fade.draw()

    def update(self, dt: float):
        self.fade.update(dt)

    def keyreleased(self, event: pygame.event.Event):
        if event.key == pygame.K_j:  # Journey onward!
            pass
        elif event.key == pygame.K_n:  # New game
            self.next_screen = 'NewGame'
            self.can_exit = True
        elif event.key == pygame.K_s:  # Settings
            self.next_screen = 'Settings'
            self.can_exit = True
        elif event.key == pygame.K_c:  # Credits
            self.next_screen = 'Credits'
            self.can_exit = True
        elif event.key == pygame.K_ESCAPE:  # Exit
            self.next_screen = 'Exit'
            self.can_exit = True

    def mousedown(self, event: pygame.event.Event):
        x = event.pos[0]
        y = event.pos[1]

        self.click_button = None
        for button in self.ui:
            if button.intersects(x, y):
                self.click_button = button

    def mouseup(self, event: pygame.event.Event):
        x = event.pos[0]
        y = event.pos[1]

        if self.click_button is not None and self.click_button.intersects(x, y):
            if self.click_button == self.journey_button:
                pass
            elif self.click_button == self.newgame_button:
                self.next_screen = 'NewGame'
                self.can_exit = True
            elif self.click_button == self.settings_button:
                self.next_screen = 'Settings'
                self.can_exit = True
            elif self.click_button == self.credits_button:
                self.next_screen = 'Credits'
                self.can_exit = True
            elif self.click_button == self.exit_button:
                self.next_screen = 'Exit'
                self.can_exit = True

        self.click_button = None
