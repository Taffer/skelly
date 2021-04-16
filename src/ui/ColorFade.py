''' Skelly colour fade the screen.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

import pygame


class ColorFade:
    def __init__(self, rgba1: pygame.Color, rgba2: pygame.Color, duration: float):
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

    def get_color(self):
        ''' Return the current colour.
        '''
        return self.rgba

    def is_done(self):
        return self.done

    def update(self, dt: float):
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
