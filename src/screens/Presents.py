''' Skelly "Taffer presents..." screen class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame

from .Base import Base, ColorFade


class Presents(Base):
    def __init__(self, game):
        super().__init__(game)

        self.game.resources['fonts'] = {
            'default_serif': pygame.font.Font('graphics/A_Font_with_Serifs.ttf', 72),
            'default_mono': pygame.font.Font('graphics/LiberationMono-Bold.ttf', 16)
            }
        self.game.resources['images'] = {
            'pygame_logo': pygame.image.load('graphics/pygame-logo.png'),
            'taffer': pygame.image.load('graphics/taffer-ronos.png')
            }

        self.taffer_text = 'Taffer presents…'
        self.pygame_text = 'A game made with Pygame…'
        '''
        self:setNextScreen('Title')

        self.resources.text:setLanguage(gameState.settings:get('language'))

        self.resources.music.theme = love.audio.newSource('music/Heroic Demise (New).mp3',  'stream')
        love.audio.setVolume(gameState.settings:get('music_volume') * (gameState.settings:get('overall_volume')))
        love.audio.play(self.resources.music.theme) -- start playing ASAP

        local love_logo = self.resources.images.love_logo
        local logo_quad = love.graphics.newQuad(0, 0, love_logo:getWidth(), love_logo:getHeight(), love_logo)

        local taffer_logo = self.resources.images.taffer
        local taffer_quad = love.graphics.newQuad(0, 0, taffer_logo:getWidth(), taffer_logo:getHeight(), taffer_logo)

        self.ui = {
            Label:new(state.scr_width / 2, 16, self.taffer_text,
                self.resources.fonts.default_serif, {1, 1, 1, 1}, 'centre'),
            ImageButton:new((state.scr_width - taffer_logo:getWidth()) / 2, 120, taffer_logo, taffer_quad),
            ImageButton:new((state.scr_width - love_logo:getWidth()) / 2, 500, love_logo, logo_quad),
            Label:new(state.scr_width / 2, 640, self.love_text,
                self.resources.fonts.default_mono, {1, 1, 1, 1}, 'centre'),
        }
        '''
        self.fade = ColorFade((0, 0, 0, 255), (0, 0, 0, 0), 1)  # 1 second fade
        self.fade_out = False
        self.exit_countdown = 2 # Seconds after fade to auto-exit.

        self.taffer_logo = self.game.resources['images']['taffer']
        self.pygame_logo = self.game.resources['images']['pygame_logo']
        self.taffer_text_img = self.game.resources['fonts']['default_serif'].render(self.taffer_text, True, (255, 255, 255, 255))
        self.pygame_text_img = self.game.resources['fonts']['default_mono'].render(self.pygame_text, True, (255, 255, 255, 255))

    def draw(self):
        self.game.surface.fill((0, 0, 0, 255))

        # TODO: Store these in init(), since they don't change.
        taffer_text_rect = self.taffer_text_img.get_rect()
        taffer_text_rect.left = (self.game.screen_width - taffer_text_rect.width) / 2
        taffer_text_rect.top = 16
        self.game.surface.blit(self.taffer_text_img, taffer_text_rect)
        taffer_logo_rect = self.taffer_logo.get_rect()
        taffer_logo_rect.left = (self.game.screen_width - taffer_logo_rect.width) / 2
        taffer_logo_rect.top = 120
        self.game.surface.blit(self.taffer_logo, taffer_logo_rect)
        pygame_logo_rect = self.pygame_logo.get_rect()
        pygame_logo_rect.left = (self.game.screen_width - pygame_logo_rect.width) / 2
        pygame_logo_rect.top = 500
        self.game.surface.blit(self.pygame_logo, pygame_logo_rect)
        pygame_text_rect = self.pygame_text_img.get_rect()
        pygame_text_rect.left = (self.game.screen_width - pygame_text_rect.width) / 2
        pygame_text_rect.top = 640
        self.game.surface.blit(self.pygame_text_img, pygame_text_rect)

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
