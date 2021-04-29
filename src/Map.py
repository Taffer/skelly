# Skelly Map for Tiled maps.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import base64
import os
import struct
import pygame
import zlib

from typing import Tuple, Union
from xml.etree import ElementTree
from . import Viewport


class Map:
    def __init__(self, map_path: str) -> None:
        tree = ElementTree.parse(map_path)
        self.root = tree.getroot()
        layers = self.root.findall('layer')

        # Map size in tiles.
        self.map_width = int(self.root.attrib['width'])
        self.map_height = int(self.root.attrib['height'])

        # Tile size in pixels.
        self.tile_width = int(self.root.attrib['tilewidth'])
        self.tile_height = int(self.root.attrib['tileheight'])

        # Tileset and image atlas paths are relative to the map file.
        prefix = os.path.split(map_path)[0]

        tilesets = self.root.findall('tileset')
        self.tiles = [None]  # Index 0 means "don't draw a tile" in Tiled.
        for tileset in tilesets:
            tileset_path = os.path.join(prefix, tileset.attrib['source'])
            tileset_prefix = os.path.split(tileset_path)[0]
            tileset_tree = ElementTree.parse(tileset_path)
            tileset_root = tileset_tree.getroot()

            image = tileset_root.find('image')
            image_path = os.path.join(tileset_prefix, image.attrib['source'])
            texture = pygame.image.load(image_path).convert_alpha()
            texture_rect = texture.get_rect()

            # Create subsurfaces for the tiles in the atlas.
            for y in range(texture_rect.height // self.tile_height):
                for x in range(texture_rect.width // self.tile_width):
                    tile_rect = pygame.Rect(x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height)
                    self.tiles.append(texture.subsurface(tile_rect))

        self.layer_data = {}
        for layer in layers:
            # Decode the layer data. This map is using CSV, which is easy; for
            # help decoding other formats, check out my tileset crusher's code:
            # https://github.com/Taffer/crushtileset/
            data = layer.find('data')
            data_contents = data.text

            this_data = []
            if data.attrib['encoding'] == 'csv':
                lines = data_contents.split()
                for line in lines:
                    for c in line.split(','):
                        if c != '':
                            this_data.append(int(c))
            elif data.attrib['encoding'] == 'base64' and data.attrib.get('compression', 'none') == 'zlib':
                the_data = base64.b64decode(data_contents)

                # CSV data is organized into rows, so we make this one big row.
                this_data = [x[0] for x in struct.iter_unpack('<I', zlib.decompress(the_data))]
            else:
                raise RuntimeError('Unsupported encoding/compression.')

            self.layer_data[layer.attrib['name']] = this_data

    def render(self, layer: str, surface: pygame.Surface, viewport: Viewport, offset_x: int, offset_y: int) -> None:
        # This use case seems to be faster than using blits(); the overhead of
        # creating a list of tuples is probably what kills it.
        view_rect = viewport.rect
        for y in range(view_rect.height):
            for x in range(view_rect.width):
                tile = self.tiles[self.layer_data[layer][self.get_index(x + view_rect.x, y + view_rect.y)]]
                target = pygame.Rect(offset_x + x * self.tile_width, offset_y + y * self.tile_height,
                                     self.tile_width, self.tile_height)
                if tile is not None:
                    surface.blit(tile, target)

    def get_index(self, x: int, y: int) -> int:
        return x + y * self.map_width

    def get_tile(self, layer: str, x: int, y: int) -> int:
        return self.layer_data[layer][self.get_index(x, y)]

    def point_to_screen(self, viewport: Viewport, offset_x: int, offset_y: int, x: int, y: int) -> Tuple[int, int]:
        # Convert a map point location to an on-screen location. Returns None if
        # the point is outside the viewport.
        #
        # offset_x, offset_y are where the map gets drawn (8,8 in our case.)
        viewport_x = viewport.x * self.tile_width
        viewport_y = viewport.y * self.tile_height
        viewport_width = viewport.width * self.tile_width
        viewport_height = viewport.height * self.tile_height

        if x < viewport_x or x > (viewport_x + viewport_width):
            return None
        if y < viewport_y or y > (viewport_y + viewport_height):
            return None

        screen_x = x + offset_x - viewport_x
        screen_y = y + offset_y - viewport_y

        return (screen_x, screen_y)

    def find_point(self, layer_name: str, object_name: str) -> Union[None, Tuple[int, int]]:
        groups = self.root.findall('.//objectgroup[@name="{0}"]'.format(layer_name))
        if len(groups) == 1:
            objects = groups[0].findall('.//object[@name="{0}"'.format(object_name))

            if len(objects) == 1:
                if 'width' not in objects[0].attrib and 'height' not in objects[0].attrib:
                    # Then this is a point.
                    return (int(objects[0].attrib['x']), int(objects[0].attrib['y']))

        return None

    def find_rect(self, layer_name: str, object_name: str) -> Union[None, pygame.Rect]:
        groups = self.root.findall('.//objectgroup[@name="{0}"]'.format(layer_name))
        if len(groups) == 1:
            objects = groups[0].findall('.//object[@name="{0}"'.format(object_name))

            if len(objects) == 1:
                if 'width' in objects[0].attrib and 'height' in objects[0].attrib:
                    # Then this is a rect.
                    rect = pygame.Rect(int(objects[0].attrib['x']), int(objects[0].attrib['y']),
                                       int(objects[0].attrib['width']), int(objects[0].attrib['height']))
                    return rect

        return None
