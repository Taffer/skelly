''' Skelly "Taffer presents..." screen class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from . import Base, ColorFade
from ..ui import ImageButton, Label

BLACK = pygame.colordict.THECOLORS['black']
BLACK_ALPHA = (BLACK[0], BLACK[1], BLACK[2], 0)  # BLACK, but fully transparent
WHITE = pygame.colordict.THECOLORS['white']


class Presents(Base):
    def __init__(self, game):
        super().__init__(game)

        self.next_screen = 'Title'
        '''
        self.resources.text:setLanguage(gameState.settings:get('language'))
        '''

        self.game.resources['fonts'] = {
            'default_serif': pygame.font.Font('graphics/A_Font_with_Serifs.ttf', 72),
            'default_mono': pygame.font.Font('graphics/LiberationMono-Bold.ttf', 16)
            }
        self.game.resources['images'] = {
            'pygame_logo': pygame.image.load('graphics/pygame-logo.png'),
            'taffer': pygame.image.load('graphics/taffer-ronos.png')
            }
        self.game.resources['music'] = {
            'theme': pygame.mixer.music.load('music/Heroic Demise (New).ogg')
        }

        pygame.mixer.music.set_volume(self.game.settings.get('music_volume') * self.game.settings.get('overall_volume'))
        pygame.mixer.music.play()

        presents_text = self.game.text.getText('presents')
        self.taffer_text = presents_text['taffer_text']
        self.pygame_text = presents_text['pygame_text']

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)  # 1 second fade
        self.fade_out = False
        self.exit_countdown = 2  # Seconds after fade to auto-exit.

        self.ui = []
        rect = self.game.resources['images']['taffer'].get_rect()
        self.ui.append(ImageButton((self.game.screen_width - rect.width) / 2, 120, self.game.resources['images']['taffer']))

        rect = self.game.resources['images']['pygame_logo'].get_rect()
        self.ui.append(ImageButton((self.game.screen_width - rect.width) / 2, 580, self.game.resources['images']['pygame_logo']))

        self.ui.append(Label(self.game.screen_width / 2, 16, self.taffer_text, self.game.resources['fonts']['default_serif'],
                       WHITE, 'centre'))

        self.ui.append(Label(self.game.screen_width / 2, 640, self.pygame_text, self.game.resources['fonts']['default_mono'],
                       WHITE, 'centre'))

    def draw(self):
        self.game.surface.fill(BLACK)

        for item in self.ui:
            item.draw()

        self.fade.draw()

    def update(self, dt):
        self.fade.update(dt)

        if self.fade_out:
            # If we're fading out...
            if self.fade.isDone():
                self.can_exit = True
        else:
            # If we're fading in...
            if self.fade.isDone():
                self.exit_countdown = self.exit_countdown - dt
                if self.exit_countdown < 0:
                    self.fade = ColorFade(BLACK_ALPHA, BLACK, 1)
                    self.fade_out = True
