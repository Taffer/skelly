''' Skelly title screen class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from . import Base
from .. import RESOURCE_LIST
from ..ui import ColorFade
from ..ui import Label

BLACK = pygame.Color('black')
BLACK_ALPHA = pygame.Color(BLACK.r, BLACK.g, BLACK.g, 0)  # BLACK, but fully transparent
WHITE = pygame.Color('white')


def loader(game: any, file_list: dict, done_text: str) -> str:
    ''' Load the files in the RESOURCE_LIST.
    '''
    yield ''

    resource = game.resources

    for k, v in file_list['font_paths'].items():
        try:
            game.manager.add_font_paths(k, v['regular'], v['bold'], v['italic'], v['bold_italic'])
        except Exception as ex:
            print('Unable to add font paths: {0} {1}'.format(k, ex))
        yield k

    for k, v in file_list['fonts'].items():
        try:
            game.manager.preload_fonts([v])
        except Exception as ex:
            print('Unable to load font: {0} {1}'.format(k, ex))
        yield v['name']

    for k, v in file_list['images'].items():
        try:
            resource['images'][k] = pygame.image.load(v).convert_alpha()
        except Exception as ex:
            print('Unable to load image: {0} {1}'.format(k, ex))
        yield v

    for k, v in file_list['music'].items():
        try:
            resource['music'][k] = pygame.mixer.Sound(v)
        except Exception as ex:
            print('Unable to load music: {0} {1}'.format(k, ex))
        yield v

    for k, v in file_list['sounds'].items():
        try:
            resource['sounds'][k] = pygame.mixer.Sound(v)
        except Exception as ex:
            print('Unable to load sound: {0} {1}'.format(k, ex))
        yield v

    for k, v in file_list['maps'].items():
        resource['maps'][k] = v  # Map class loads from paths.
        yield v

    yield done_text


class Title(Base):
    def __init__(self, game: any) -> None:
        super().__init__(game)

        self.next_screen = 'Journey'

        self.game.resources['fonts']['skelly_title'] = pygame.freetype.Font('graphics/Gypsy Curse.ttf', 144)
        self.game.resources['images']['skelly_title'] = pygame.image.load('graphics/Gersdorff_Feldbuch_skeleton.png').convert()

        self.loading_x = 16
        self.loading_y = self.game.screen_height - 16 - self.game.resources['fonts']['default_mono'].get_sized_height()

        title_text = self.game.text.get_text('title')
        self.loading_text = title_text['loading_text']
        self.done_text = title_text['loading_done']

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)  # 1 second fade
        self.fade_out = False

        self.loaded_resource = ""
        self.loading_finished = False
        self.loading_routine = loader(self.game, RESOURCE_LIST, self.done_text)

        self.add_title()

        self.ui = []
        self.loading_label = Label(self.loading_x, self.loading_y, self.loading_text, self.game.resources['fonts']['default_mono'],
                                   WHITE, 'left')
        self.ui.append(self.loading_label)

    def draw(self) -> None:
        self.game.surface.fill(BLACK)
        self.draw_title()

        for item in self.ui:
            item.draw()

        self.fade.draw()

    def update(self, dt: float) -> None:
        self.fade.update(dt)

        if self.fade_out:
            # If we're fading out...
            if self.fade.is_done():
                self.can_exit = True
        else:
            # If we're fading in...
            if self.fade.is_done():
                if self.loading_finished:
                    self.fade = ColorFade(BLACK_ALPHA, BLACK, 1)
                    self.fade_out = True

            if not self.loading_finished:
                try:
                    result = self.loading_routine.__next__()
                    self.loading_label.set_text('{0} {1}'.format(self.loading_text, result))
                except StopIteration:
                    self.loading_finished = True
