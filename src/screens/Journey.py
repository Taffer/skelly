# Skelly "Journey Onward" screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame
import pygame_gui

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

        self.create_buttons()

    def draw(self):
        self.game.surface.fill(BLACK)
        self.draw_title()

        self.game.manager.draw_ui(self.game.surface)

        if not self.fade.is_done():
            self.fade.draw()

    def update(self, dt: float):
        self.fade.update(dt)

    def keyreleased(self, event: pygame.event.Event):
        if event.key == pygame.K_j:  # Journey onward!
            pass
        elif event.key == pygame.K_n:  # New game
            self.switch_to('NewGame')
        elif event.key == pygame.K_s:  # Settings
            self.switch_to('Settings')
        elif event.key == pygame.K_c:  # Credits
            self.switch_to('Credits')
        elif event.key == pygame.K_ESCAPE:  # Exit
            self.switch_to('Exit')

    def userevent(self, event: pygame.event.Event):
        if event.user_type == pygame_gui.UI_WINDOW_CLOSE:
            if event.ui_element == self.window:
                self.overlay_closed = True
                self.game.manager.clear_and_reset()
                self.create_buttons()  # Recreate the page's buttons.
        elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.journey_button:
                pass
            elif event.ui_element == self.newgame_button:
                self.switch_to('NewGame')
            elif event.ui_element == self.settings_button:
                self.switch_to('Settings')
            elif event.ui_element == self.credits_button:
                self.switch_to('Credits')
            elif event.ui_element == self.exit_button:
                self.switch_to('Exit')

    def create_buttons(self):
        x = (self.game.screen_width - 190) / 2  # Buttons are 190 pixels wide.

        self.journey_button = pygame_gui.elements.UIButton(pygame.Rect(x, 350, 190, 49), self.journey_text, self.game.manager,
                                                           object_id='#menubutton')
        self.newgame_button = pygame_gui.elements.UIButton(pygame.Rect(x, 410, 190, 49), self.newgame_text, self.game.manager,
                                                           object_id='#menubutton')
        self.settings_button = pygame_gui.elements.UIButton(pygame.Rect(x, 470, 190, 49), self.settings_text, self.game.manager,
                                                            object_id='#menubutton')
        self.credits_button = pygame_gui.elements.UIButton(pygame.Rect(x, 550, 190, 49), self.credits_text, self.game.manager,
                                                           object_id='#menubutton')
        self.exit_button = pygame_gui.elements.UIButton(pygame.Rect(x, 620, 190, 49), self.exit_text, self.game.manager,
                                                        object_id='#menubutton')

    def switch_to(self, screen_name):
        self.next_screen = screen_name
        self.can_exit = True
        self.game.manager.clear_and_reset()  # Kill our UI buttons.
