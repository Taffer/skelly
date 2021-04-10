#!/usr/bin/env python3
''' Skelly, a story of the Skeleton War

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import os
import platform
import pygame
import pygame.freetype
import pygame.gfxdraw
import pygame_gui
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
        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

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
        self.manager.draw_ui(self.surface)

    def update(self, dt):
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
                print('Switch to NewGame')
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

    def userevent(self, event):
        self.screen.userevent(event)


def main():
    if PYGAME_VERSION > pygame.version.vernum:
        raise SystemExit('Pygame version too old: {0}'.format(pygame.version.ver))

    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    skelly = Game(window)

    ignore_events = [pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN,
                     pygame.VIDEORESIZE, pygame.VIDEOEXPOSE, pygame.AUDIODEVICEADDED, pygame.AUDIODEVICEREMOVED,
                     pygame.FINGERMOTION, pygame.FINGERDOWN, pygame.FINGERUP, pygame.MULTIGESTURE,
                     pygame.DROPBEGIN, pygame.DROPCOMPLETE, pygame.DROPFILE, pygame.DROPTEXT, pygame.MIDIIN, pygame.MIDIOUT,
                     pygame.CONTROLLERDEVICEADDED, pygame.JOYDEVICEADDED, pygame.CONTROLLERDEVICEREMOVED,
                     pygame.JOYDEVICEREMOVED, pygame.CONTROLLERDEVICEREMAPPED]
    pygame.event.set_blocked(ignore_events)

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
            skelly.manager.process_events(event)

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
            elif event.type == pygame.USEREVENT:
                skelly.userevent(event)


if __name__ == '__main__':
    main()
