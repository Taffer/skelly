# Skelly Viewport for tiled maps.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame


class Viewport:
    ''' View into the map in tile co-ords.
    '''
    def __init__(self, map_width: int, map_height: int, rect: pygame.Rect) -> None:
        self.map_tile_width = map_width
        self.map_tile_height = map_height

        self.rect = rect

    def set_position(self, x: int, y: int) -> None:
        if x + self.rect.width > self.map_tile_width:
            self.rect.x = self.map_tile_width - self.rect.width
        else:
            self.rect.x = x

        if y + self.rect.height > self.map_tile_height:
            self.rect.y = self.map_tile_height - self.rect.height
        else:
            self.rect.y = y
