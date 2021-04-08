''' Skelly "Taffer presents..." screen class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from .Base import Base, ColorFade
from ..ui.ImageButton import ImageButton


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

        self.taffer_text = 'Taffer presents…'
        self.pygame_text = 'A game made with Pygame…'

        self.fade = ColorFade((0, 0, 0, 255), (0, 0, 0, 0), 1)  # 1 second fade
        self.fade_out = False
        self.exit_countdown = 2  # Seconds after fade to auto-exit.

        rect = self.game.resources['images']['taffer'].get_rect()
        self.taffer_logo = ImageButton((self.game.screen_width - rect.width) / 2, 120, self.game.resources['images']['taffer'])

        rect = self.game.resources['images']['pygame_logo'].get_rect()
        self.pygame_logo = ImageButton((self.game.screen_width - rect.width) / 2, 580,
                                       self.game.resources['images']['pygame_logo'])

        self.taffer_text_img = self.game.resources['fonts']['default_serif'].render(self.taffer_text, True, (255, 255, 255, 255))
        self.taffer_text_rect = self.taffer_text_img.get_rect()
        self.taffer_text_rect.left = (self.game.screen_width - self.taffer_text_rect.width) / 2
        self.taffer_text_rect.top = 16

        self.pygame_text_img = self.game.resources['fonts']['default_mono'].render(self.pygame_text, True, (255, 255, 255, 255))
        self.pygame_text_rect = self.pygame_text_img.get_rect()
        self.pygame_text_rect.left = (self.game.screen_width - self.pygame_text_rect.width) / 2
        self.pygame_text_rect.top = 640

    def draw(self):
        self.game.surface.fill((0, 0, 0, 255))

        self.game.surface.blit(self.taffer_text_img, self.taffer_text_rect)
        self.taffer_logo.draw()
        self.pygame_logo.draw()
        self.game.surface.blit(self.pygame_text_img, self.pygame_text_rect)

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
                    self.fade = ColorFade((0, 0, 0, 0), (0, 0, 0, 255), 1)
                    self.fade_out = True
