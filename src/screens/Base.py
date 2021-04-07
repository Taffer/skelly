''' Skelly screen base class.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame


class Base:
    def __init__(self, game):
        ''' Initialize.

        @param game Game global state.
        '''
        self.game = game

        self.can_exit = False  # Time for this screen to exit?
        self.next_screen = None  # Next screen to display.

    def draw(self):
        ''' Draw the screen's contents.
        '''
        pass

    def update(self, dt):
        ''' Update the screen's contents.
        '''
        pass


class ColorFade:
    def __init__(self, rgba1, rgba2, duration):
        self.rgba = tuple(rgba1)
        self.start_rgba = rgba1
        self.end_rgba = rgba2
        self.duration = duration

        self.dt = 0
        self.done = False

        info = pygame.display.Info()
        self.screen_rect = pygame.Rect(0, 0, info.current_w, info.current_h)
        self.texture = pygame.Surface((self.screen_rect.width, self.screen_rect.height))
        self.texture.fill(self.rgba)
        self.texture.set_alpha(self.rgba[-1])

    def getColor(self):
        ''' Return the current colour.
        '''
        return self.rgba

    def isDone(self):
        return self.done

    def update(self, dt):
        if self.done:
            return

        self.dt = self.dt + dt
        if self.dt > self.duration:
            self.rgba = tuple(self.end_rgba)

            self.done = True
            return

        diff = self.dt / self.duration
        self.rgba = tuple(map(lambda a, b: a + (b - a) * diff, self.start_rgba, self.end_rgba))
        self.texture.fill(self.rgba)
        self.texture.set_alpha(self.rgba[-1])

    def draw(self):
        pygame.display.get_surface().blit(self.texture, self.screen_rect)
