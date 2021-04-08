''' Skelly title screen class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from . import Base, ColorFade
from ..ui import ImageButton, Label

BLACK = pygame.colordict.THECOLORS['black']
BLACK_ALPHA = (BLACK[0], BLACK[1], BLACK[2], 0)  # BLACK, but fully transparent
WHITE = pygame.colordict.THECOLORS['white']


'''
local function loader(resource, file_list)
    local yield = coroutine.yield

    -- Load the files listed into the resource table.
    for k,v in pairs(file_list.fonts) do
        resource.fonts[k] = love.graphics.newFont(v.src, v.size)
        if resource.fonts[k] == nil then
            print('Unable to load font:', k)
        end

        yield(v.src)
    end

    for k,v in pairs(file_list.images) do
        resource.images[k] = love.graphics.newImage(v)
        if resource.images[k] == nil then
            print('Unable to load image:', k)
        end

        yield(v)
    end

    for k,v in pairs(file_list.music) do
        resource.music[k] = love.audio.newSource(v, 'stream')
        if resource.music[k] == nil then
            print('Unable to load music:', k)
        end

        yield(v)
    end

    for k,v in pairs(file_list.sounds) do
        resource.sounds[k] = love.audio.newSource(v, 'static')
        if resource.sounds[k] == nil then
            print('Unable to load sound:', k)
        end

        yield(v)
    end

    for k, v in pairs(file_list.maps) do
        resource.maps[k] = require(v)
        if resource.maps[k] == nil then
            print('Unable to load map:', k)
        end

        yield(v)
    end

    local title_text = resource.text:getText('title')
    return title_text.loading_done
end
'''


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

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)  # 1 second fade
        self.fade_out = False

        self.loaded_resource = ""
        self.loading_finished = True
        '''
        self.loading_routine = nil
        '''

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
        '''
        -- Load resources.
        if self.loading_routine then
            local resume = coroutine.resume
            alive, self.loaded_resource = resume(self.loading_routine, self.resources, rsrc_list)
            if not alive then
                self.loading_finished = true
                local title_text = self.resources.text:getText('title')
                self.loaded_resource = title_text.loading_done
            end
        else
            self.loading_routine = coroutine.create(loader)
        end
        '''
