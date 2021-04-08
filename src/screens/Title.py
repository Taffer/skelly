''' Skelly title screen class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from .Base import Base, ColorFade


class Title(Base):
    def __init__(self, game):
        super().__init__(game)

        self.next_screen = 'Journey'
        # self.next_screen = 'NewGame'

        self.game.resources['fonts']['skelly_title'] = pygame.font.Font('graphics/Gypsy Curse.ttf', 144)
        self.game.resources['images']['skelly_title'] = pygame.image.load('graphics/Gersdorff_Feldbuch_skeleton.png')

        self.loading_x = 16
        self.loading_y = self.game.screen_height - 16 - self.game.resources['fonts']['default_mono'].get_height()

        self.skelly_text = 'Skelly'
        self.subtitle_text = 'A tale of the Skeleton War'
        self.loading_text = 'Loading…'

        self.fade = ColorFade((0, 0, 0, 255), (0, 0, 0, 0), 1)  # 1 second fade

        self.loaded_resource = ""
        self.loading_finished = False
        '''
        self.loading_routine = nil
        '''

        self.title_image = self.game.resources['images']['skelly_title']
        self.title_rect = self.title_image.get_rect()

        self.skelly_text_img = self.game.resources['fonts']['skelly_title'].render(self.skelly_text, True, (255, 255, 255, 255))
        self.skelly_text_rect = self.skelly_text_img.get_rect()
        self.skelly_text_rect.left = (self.game.screen_width - self.skelly_text_rect.width) / 2
        self.skelly_text_rect.top = 40

        self.subtitle_text_img = self.game.resources['fonts']['default_mono'].render(self.subtitle_text, True, (255, 255, 255, 255))
        self.subtitle_text_rect = self.subtitle_text_img.get_rect()
        self.subtitle_text_rect.left = (self.game.screen_width - self.subtitle_text_rect.width) / 2
        self.subtitle_text_rect.top = self.skelly_text_rect.top + self.skelly_text_rect.height + 10

        self.loading_label = self.game.resources['fonts']['default_mono'].render(self.loading_text, True, (255, 255, 255, 255))
        self.loading_label_rect = self.loading_label.get_rect()
        self.loading_label_rect.left = self.loading_x
        self.loading_label_rect.top = self.loading_y

    def draw(self):
        self.game.surface.fill((0, 0, 0, 255))

        self.game.surface.blit(self.title_image, self.title_rect)
        self.game.surface.blit(self.skelly_text_img, self.skelly_text_rect)
        self.game.surface.blit(self.subtitle_text_img, self.subtitle_text_rect)
        self.game.surface.blit(self.loading_label, self.loading_label_rect)

        self.fade.draw()

    def update(self, dt):
        self.fade.update(dt)
