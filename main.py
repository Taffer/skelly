#!/usr/bin/env python3
''' Skelly, a story of the Skeleton War

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import os
import platform
import pygame
import sys
import time

import src
import src.screens


WINDOW_TITLE = 'Skelly'
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_IDENTITY = 'ca.taffer.skelly'
PYGAME_VERSION = (2, 0, 1)  # Expected minimum Pygame version.

SETTINGS_FILENAME = 'settings.ini'


class Game:
    def __init__(self, surface):
        self.surface = surface

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

    def save_settings(self):
        self.settings.save()

    def update(self, dt):
        self.screen.update(dt)

        # Screen state machine:
        if self.screen.can_exit:
            next_screen = self.screen.next_screen
            if next_screen == 'Journey':  # "Journey Onwards" screen
                self.screen = src.screens.Journey(self)
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

    def draw(self):
        self.screen.draw()

    def keypressed(self, event):
        self.screen.keypressed(event)

    def keyreleased(self, event):
        self.screen.keyreleased(event)

    def mousemoved(self, event):
        self.screen.mousemoved(event)

    def mousedown(self, event):
        self.screen.mousedown(event)

    def mouseup(self, event):
        self.screen.mouseup(event)


def main():
    if PYGAME_VERSION > pygame.version.vernum:
        raise SystemExit('Pygame version too old: {0}'.format(pygame.version.ver))

    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    skelly = Game(window)

    prev_time = time.time()
    dt = 0
    while True:
        now = time.time()
        dt = now - prev_time
        prev_time = now

        skelly.update(dt)
        skelly.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                skelly.keypressed(event)
            elif event.type == pygame.KEYUP:
                skelly.keyreleased(event)
            elif event.type == pygame.MOUSEMOTION:
                skelly.mousemoved(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                skelly.mousedown(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                skelly.mouseup(event)


if __name__ == '__main__':
    main()
