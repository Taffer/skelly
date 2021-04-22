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
    def __init__(self, game) -> None:
        self.manager = game.manager
        self.settings = game.settings
        self.text = game.text

        self.overlay_closed = False

        settings_text = self.text.get_text('settings')

        self.window = pygame_gui.elements.UIWindow(pygame.Rect(100, 250, 1080, 420), self.manager, settings_text['title'])

        rect = pygame.Rect(10, 10, 150, 25)
        self.master_vol_label = UILabel(rect, settings_text['master_volume'], self.manager, self.window)
        rect.y += 50
        self.music_vol_label = UILabel(rect, settings_text['music_volume'], self.manager, self.window)
        rect.y += 50
        self.effects_vol_label = UILabel(rect, settings_text['effects_volume'], self.manager, self.window)
        rect.y += 50
        self.voice_vol_label = UILabel(rect, settings_text['voice_volume'], self.manager, self.window)

        rect = pygame.Rect(150, 10, 250, 25)
        self.master_slider = UIHorizontalSlider(rect, self.settings.get('overall_volume'), (0.0, 1.0), self.manager, self.window)
        rect.y += 50
        self.music_slider = UIHorizontalSlider(rect, self.settings.get('music_volume'), (0.0, 1.0), self.manager, self.window)
        rect.y += 50
        self.effects_slider = UIHorizontalSlider(rect, self.settings.get('sfx_volume'), (0.0, 1.0), self.manager, self.window)
        rect.y += 50
        self.voice_slider = UIHorizontalSlider(rect, self.settings.get('voice_volume'), (0.0, 1.0), self.manager, self.window)

        rect = pygame.Rect(10, 250, 100, 23)
        self.language_label = UILabel(rect, settings_text['language'], self.manager, self.window)
        rect = pygame.Rect(150, 250, 250, 25)
        self.language_menu = UIDropDownMenu(settings_text['translations'], 'English', rect, self.manager, self.window)

    def userevent(self, event: pygame.event.Event) -> None:
        if event.user_type == pygame_gui.UI_WINDOW_CLOSE:
            if event.ui_element == self.window:
                self.overlay_closed = True
        elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.language_menu:
                self.settings.set('language', self.text.code_for(event.value))
        elif event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == self.master_slider:
                self.settings.set('overall_volume', event.value)
            elif event.ui_element == self.music_slider:
                self.settings.set('music_volume', event.value)
            elif event.ui_element == self.effects_slider:
                self.settings.set('sfx_volume', event.value)
            elif event.ui_element == self.voice_slider:
                self.settings.set('voice_volume', event.value)
