# Skelly Camera for Tiled maps.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from .Map import Map


class Camera:
    ''' Camera/viewport for a tile-based map.
    '''
    def __init__(self: 'Camera', screen: pygame.Surface, the_map: Map) -> None:
        self.screen = screen
        self.map = the_map

        # Co-ordinates are in *tiles*, not pixels.
        self.x = 0
        self.y = 0
        self.tile_width = 0
        self.tile_height = 0

        # Co-ordinates are in *pixels*, not tiles.
        self.viewport = None

        # Tile to use for out-of-bounds tiles.
        self.edge_tile = 0

    def set_viewport(self: 'Camera', viewport: pygame.Rect) -> None:
        ''' Set the camera's on-screen viewport.
        '''
        self.viewport = viewport

        self.tile_width = viewport.width // self.map.tile_width
        self.tile_height = viewport.height // self.map.tile_height

    def set_position(self: 'Camera', x: int, y: int) -> None:
        self.x = x
        self.y = y

    def set_edge(self: 'Camera', edge: int) -> None:
        self.edge_tile = edge

    def get_rect(self: 'Camera') -> pygame.Rect:
        ''' Get the rectangle representing the camera position in screen pixels.
        '''
        return pygame.Rect(self.tile_width // 2 * self.map.tile_width, self.tile_height // 2 * self.map.tile_height,
                           self.map.tile_width, self.map.tile_height)

    def draw(self: 'Camera', layer: str) -> None:
        tile_x = self.x - self.tile_width // 2
        tile_y = self.y - self.tile_height // 2

        for y in range(self.tile_height):
            for x in range(self.tile_width):
                dx = tile_x + x
                dy = tile_y + y
                if dx < 0 or dx >= self.map.map_width or dy < 0 or dy >= self.map.map_height:
                    tile_idx = self.edge_tile
                else:
                    tile_idx = self.map.get_tile(layer, tile_x + x, tile_y + y)
                if tile_idx is not None and tile_idx != 0:
                    tile = self.map.get_tile_texture(tile_idx)
                    target = pygame.Rect(self.viewport.x + x * self.map.tile_width, self.viewport.y + y * self.map.tile_height,
                                         self.map.tile_width, self.map.tile_height)
                    self.screen.blit(tile, target)
