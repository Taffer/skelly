# Skelly settings overlay.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.
#
# Drawn on top of the game screen (or Settings screen) to handle settings
# changes.
#
# Widgets needed:
#
# Master volume: slider 0.0 to 1.0
# Music volume: slider 0.0 to 1.0
# Effects volume: slider 0.0 to 1.0
# Voice volume: slider 0.0 to 1.0
#
# Language: drop-down ['en', 'es']

import pygame
import pygame_gui

from pygame_gui.elements import UIDropDownMenu, UIHorizontalSlider, UILabel


class SettingsOverlay:
    def __init__(self, manager):
        self.manager = manager

        self.window = pygame_gui.elements.UIWindow(pygame.Rect(100, 250, 1080, 420))

        rect = pygame.Rect(10, 10, 100, 25)
        self.master_vol_label = UILabel(rect, 'Master Volume:', manager, self.window)
        self.music_vol_label = UILabel(rect, 'Music Volume:', manager, self.window)
        self.effects_vol_label = UILabel(rect, 'Effects Volume:', manager, self.window)
        self.voice_vol_label = UILabel(rect, 'Voice Volume:', manager, self.window)

        self.master_slider = UIHorizontalSlider(rect, 1.0, (0.0, 1.0), manager, self.window)
        self.music_slider = UIHorizontalSlider(rect, 1.0, (0.0, 1.0), manager, self.window)
        self.effects_slider = UIHorizontalSlider(rect, 1.0, (0.0, 1.0), manager, self.window)
        self.voice_slider = UIHorizontalSlider(rect, 1.0, (0.0, 1.0), manager, self.window)

        self.language_label = UILabel(rect, 'Language:', manager, self.window)
        self.language_menu = UIDropDownMenu(['English', 'Espanol'], 'English', rect, manager, self.window)

    def userevent(self, event):
        pass
