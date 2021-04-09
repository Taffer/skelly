''' Skelly title screen class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from . import Base
from . import ColorFade
from .. import RESOURCE_LIST
from ..ui import ImageButton
from ..ui import Label

BLACK = pygame.colordict.THECOLORS['black']
BLACK_ALPHA = (BLACK[0], BLACK[1], BLACK[2], 0)  # BLACK, but fully transparent
WHITE = pygame.colordict.THECOLORS['white']


def loader(resource, file_list, done_text):
    ''' Load the files in the RESOURCE_LIST.
    '''
    yield ''

    for k, v in file_list['fonts'].items():
        try:
            resource['fonts'][k] = pygame.font.Font(v['src'], v['size'])
        except Exception as ex:
            print('Unable to load font: {0} {1}'.format(k, ex))
        yield v['src']

    for k, v in file_list['images'].items():
        try:
            resource['images'][k] = pygame.image.load(v)
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
        try:
            with open(v) as fp:
                resource['maps'][k] = fp.read()  # Load directly into Tiled obj?
        except Exception as ex:
            print('Unable to load map: {0} {1}'.format(k, ex))
        yield v

    yield done_text


class Title(Base):
    def __init__(self, game):
        super().__init__(game)

        self.next_screen = 'Journey'

        self.game.resources['fonts']['skelly_title'] = pygame.font.Font('graphics/Gypsy Curse.ttf', 144)
        self.game.resources['images']['skelly_title'] = pygame.image.load('graphics/Gersdorff_Feldbuch_skeleton.png')

        self.loading_x = 16
        self.loading_y = self.game.screen_height - 16 - self.game.resources['fonts']['default_mono'].get_height()

        title_text = self.game.text.getText('title')
        self.skelly_text = self.game.text.getText('skelly_title')
        self.subtitle_text = title_text['subtitle_text']
        self.loading_text = title_text['loading_text']
        self.done_text = title_text['loading_done']

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)  # 1 second fade
        self.fade_out = False

        self.loaded_resource = ""
        self.loading_finished = False
        self.loading_routine = loader(self.game.resources, RESOURCE_LIST, self.done_text)

        self.ui = [
            ImageButton(0, 0, self.game.resources['images']['skelly_title']),
            Label(self.game.screen_width / 2, 40, self.skelly_text, self.game.resources['fonts']['skelly_title'],
                  WHITE, 'centre'),
            Label(self.game.screen_width / 2, 220, self.subtitle_text, self.game.resources['fonts']['default_mono'],
                  WHITE, 'centre'),
        ]

        self.loading_label = Label(self.loading_x, self.loading_y, self.loading_text, self.game.resources['fonts']['default_mono'],
                                   WHITE, 'left')
        self.ui.append(self.loading_label)

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
                if self.loading_finished:
                    self.fade = ColorFade(BLACK_ALPHA, BLACK, 1)
                    self.fade_out = True

            if not self.loading_finished:
                try:
                    result = self.loading_routine.__next__()
                    self.loading_label.setText('{0} {1}'.format(self.loading_text, result))
                except StopIteration:
                    self.loading_finished = True
