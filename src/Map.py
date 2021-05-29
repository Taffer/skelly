# Skelly Map for Tiled maps.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import base64
import os
import struct
import pygame
import zlib

from . import Actor
from . import Trigger
from typing import Tuple, Union
from xml.etree import ElementTree


class Map:
    def __init__(self: 'Map', map_path: str) -> None:
        self.map_triggers = []  # Triggers to call when someone enters/exits this map.
        self.triggers = {}  # Tile triggers, indexed by (x,y).

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
                for c in data_contents.split(','):
                    if c != '':
                        this_data.append(int(c))
            elif data.attrib['encoding'] == 'base64' and data.attrib.get('compression', 'none') == 'zlib':
                the_data = base64.b64decode(data_contents)

                # CSV data is organized into rows, so we make this one big row.
                this_data = [x[0] for x in struct.iter_unpack('<I', zlib.decompress(the_data))]
            else:
                raise RuntimeError('Unsupported encoding/compression.')

            self.layer_data[layer.attrib['name']] = this_data

    def get_index(self: 'Map', x: int, y: int) -> int:
        return x + y * self.map_width

    def get_tile(self: 'Map', layer: str, x: int, y: int) -> int:
        return self.layer_data[layer][self.get_index(x, y)]

    def get_tile_texture(self: 'Map', idx: int) -> pygame.Surface:
        return self.tiles[idx]

    def find_point(self: 'Map', layer_name: str, object_name: str) -> Union[None, Tuple[int, int]]:
        ''' Returns a Point object's location, in map pixel co-ordinates.

        TODO: Should this return tile co-ordinates?
        '''
        groups = self.root.findall('.//objectgroup[@name="{0}"]'.format(layer_name))
        if len(groups) == 1:
            objects = groups[0].findall('.//object[@name="{0}"'.format(object_name))

            if len(objects) == 1:
                if 'width' not in objects[0].attrib and 'height' not in objects[0].attrib:
                    # Then this is a point.
                    return (int(objects[0].attrib['x']), int(objects[0].attrib['y']))

        return None

    def find_rect(self: 'Map', layer_name: str, object_name: str) -> Union[None, pygame.Rect]:
        ''' Returns a Rect object's location, in map pixel co-ordinates.

        TODO: Should this return tile co-ordinates?
        '''
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

    def add_map_trigger(self: 'Map', map_trigger: Trigger) -> None:
        ''' Add an On Enter/On Exit trigger to the map.

        On Enter/On Exit functions are called with (x, y, actor) when an actor
        enters the map. (x, y) will be their spawn point in *tile* co-ordinates.

        Note that you can't remove these triggers.
        '''
        self.map_triggers.append(map_trigger)

    def add_trigger(self: 'Map', x: int, y: int, trigger: Trigger) -> None:
        ''' Add a trigger at (x,y).
        '''
        self.triggers[(x, y)] = trigger

    def enter_map(self: 'Map', x: int, y: int, actor: Actor) -> None:
        for trigger in self.map_triggers:
            trigger.on_enter(x, y, actor)

    def exit_map(self: 'Map', x: int, y: int, actor: Actor) -> None:
        for trigger in self.map_triggers:
            trigger.on_exit(x, y, actor)

    def enter_tile(self: 'Map', x: int, y: int, actor: Actor) -> None:
        ''' *actor* has entered the tile at (x, y), activate any triggers.
        '''
        if (x, y) in self.triggers:
            self.triggers[(x, y)].on_enter(x, y, actor)

    def exit_tile(self: 'Map', x: int, y: int, actor: Actor) -> None:
        ''' *actor* is exiting the tile at (x, y), activate any triggers.
        '''
        if (x, y) in self.triggers:
            self.triggers[(x, y)].on_exit(x, y, actor)
