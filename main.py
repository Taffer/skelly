#!/usr/bin/env python3
''' Skelly, a story of the Skeleton War

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame
import sys
import time

import src.screens.Presents


WINDOW_TITLE = 'Skelly'
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_IDENTITY = 'ca.taffer.skelly'
PYGAME_VERSION = (2, 0, 1)  # Expected minimum Pygame version.


class Game:
    def __init__(self, surface):
        self.surface = surface

        self.state = {}
        self.resources = {}

        self.screen_width = WINDOW_WIDTH
        self.screen_height = WINDOW_HEIGHT
        '''
        -- Load settings if they exist. If not, create defaults.
        load_settings(settings_filename)

        -- Load strings.
        gameResources.text:addLanguage('en', I18n['en'])
        gameResources.text:addLanguage('es', I18n['es'])

        -- Minimal loading screen.
        gameState.screen = gameResources.screens.presents:new(gameResources, gameState)
        '''
        self.screen = src.screens.Presents.Presents(self)

    def update(self, dt):
        self.screen.update(dt)
        '''
        local input_freq = gameState.settings:get('input_frequency') / 10000
        gameState.input_ticks = gameState.input_ticks + dt
        if gameState.input_ticks > input_freq then
            -- Generate input events.
            gameState.screen:checkInputs(gameState.keyboard, gameState.mouse, gameState.gamepad)

            gameState.input_ticks = gameState.input_ticks - input_freq
        end

        gameState.screen:update(dt)

        -- Screen state machine:
        --
        -- Presents -> Title -> Journey -> exit
        --                             \-> Newgame -> Intro -> Game
        --                             \-------------------/
        --
        local lookup = ScreenLookup
        if gameState.screen:getExit() then
            local next_screen = gameState.screen:getNextScreen()
            if next_screen then
                gameState.screen = lookup[next_screen]:new(gameResources, gameState)
            else
                save_settings()
                love.audio.stop()
                love.event.quit()
            end
        end
        '''

    def draw(self):
        self.screen.draw()

    def keypressed(self, event):
        pass

    def keyreleased(self, event):
        pass


def main():
    if PYGAME_VERSION > pygame.version.vernum:
        raise SystemExit('Pygame version too old:'.format(pygame.version.ver))

    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    skelly = Game(window)

    prev_time = time.time()
    dt = 0
    while True:
        now = time.time()
        dt = now - prev_time
        prev_time = now

        skelly.update(dt)
        skelly.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                skelly.keypressed(event)
            elif event.type == pygame.KEYUP:
                skelly.keyreleased(event)

if __name__ == '__main__':
    main()
