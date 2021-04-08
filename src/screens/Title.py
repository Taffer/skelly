''' Skelly title screen class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from .Base import Base, ColorFade
from ..ui.ImageButton import ImageButton


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

        self.fade = ColorFade((0, 0, 0, 255), (0, 0, 0, 0), 1)  # 1 second fade

        self.loaded_resource = ""
        self.loading_finished = False
        '''
        self.loading_routine = nil
        '''

        self.title_image = ImageButton(0, 0, self.game.resources['images']['skelly_title'])

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

        self.title_image.draw()
        self.game.surface.blit(self.skelly_text_img, self.skelly_text_rect)
        self.game.surface.blit(self.subtitle_text_img, self.subtitle_text_rect)
        self.game.surface.blit(self.loading_label, self.loading_label_rect)

        self.fade.draw()

    def update(self, dt):
        self.fade.update(dt)

        if self.fade.isDone():
            self.can_exit = True

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
