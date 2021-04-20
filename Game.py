# Skelly, a story of the Skeleton War
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import os
import platform
import pygame
import pygame.freetype
import pygame.gfxdraw
import pygame_gui
import sys

import src
import src.screens

from typing import Final

WINDOW_TITLE: Final = 'Skelly'
WINDOW_WIDTH: Final = 1280
WINDOW_HEIGHT: Final = 720
GAME_IDENTITY: Final = 'ca.taffer.skelly'
PYGAME_VERSION: Final = (2, 0, 1)  # Expected minimum Pygame version.

SETTINGS_FILENAME: Final = 'settings.ini'


class Game:
    def __init__(self, surface: pygame.Surface) -> None:
        self.surface = surface
        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT), 'graphics/ui-theme.json')

        self.state = {}
        self.resources = {  # Loaded by loader() in the Title screen.
            'fonts': {},
            'images': {},
            'music': {},
            'sounds': {},
            'maps': {},
        }

        self.screen_width = WINDOW_WIDTH
        self.screen_height = WINDOW_HEIGHT

        self.settings = self.load_settings(SETTINGS_FILENAME)

        self.text = src.TextHandler()
        self.text.addLanguage('en', src.I18N_EN)
        self.text.addLanguage('es', src.I18N_ES)
        self.text.setLanguage('en')

        self.screen = src.screens.Presents(self)

    def find_config_dir(self) -> str:
        ''' Based on the OS, find the configuration directory.
        '''
        system = platform.system()
        if system == 'Linux':
            return os.path.join(os.getenv('HOME'), '.config', GAME_IDENTITY)
        else:
            raise RuntimeError(f'Unsupported system: {system}')

    def load_settings(self, filename: str) -> src.GameSettings:
        defaults = {
            # Default settings.
            'music_volume': 1.0,
            'sfx_volume': 1.0,
            'voice_volume': 1.0,
            'overall_volume': 1.0,

            'language': 'en'
        }

        dir = self.find_config_dir()
        path = os.path.join(dir, filename)

        return src.GameSettings(path, defaults)

    def save_settings(self) -> None:
        self.settings.save()
        self.manager.draw_ui(self.surface)

    def update(self, dt: float) -> None:
        self.screen.update(dt)
        self.manager.update(dt)

        # Screen state machine:
        if self.screen.can_exit:
            next_screen = self.screen.next_screen
            if next_screen == 'Credits':  # Credits screen
                self.screen = src.screens.Credits(self)
            elif next_screen == 'Journey':  # "Journey Onwards" screen
                self.screen = src.screens.Journey(self)
            elif next_screen == 'NewGame':  # New Game/Intro screen
                self.screen = src.screens.NewGame(self)
            elif next_screen == 'Presents':  # "Taffer presents" screen
                self.screen = src.screens.Presents(self)
            elif next_screen == 'Settings':  # Blank with Settings overlay
                self.screen = src.screens.Settings(self)
            elif next_screen == 'Title':  # Title screen
                self.screen = src.screens.Title(self)
            else:
                self.save_settings()
                pygame.mixer.music.stop()
                sys.exit()

    def draw(self) -> None:
        self.screen.draw()

    def keypressed(self, event: pygame.event.Event) -> None:
        self.screen.keypressed(event)

    def keyreleased(self, event: pygame.event.Event) -> None:
        self.screen.keyreleased(event)

    def mousemoved(self, event: pygame.event.Event) -> None:
        self.screen.mousemoved(event)

    def mousedown(self, event: pygame.event.Event) -> None:
        self.screen.mousedown(event)

    def mouseup(self, event: pygame.event.Event) -> None:
        self.screen.mouseup(event)

    def userevent(self, event: pygame.event.Event) -> None:
        self.screen.userevent(event)
