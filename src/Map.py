# Skelly Map for Tiled maps.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import os
import pygame

from xml.etree import ElementTree


class Map:
    def __init__(self, map_path):
        tree = ElementTree.parse(map_path)
        self.root = tree.getroot()
        layers = self.root.findall('layer')
        if len(layers) > 1:
            raise SystemExit('Map has multiple layers, this experiment only deals with one.')

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
            tileset_tree = ElementTree.parse(tileset_path)
            tileset_root = tileset_tree.getroot()

            image = tileset_root.find('image')
            image_path = os.path.join(prefix, image.attrib['source'])
            texture = pygame.image.load(image_path).convert_alpha()  # TODO: Do I need to keep a ref to these?
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
            data = layer.find('data').text

            this_data = []
            lines = data.split()
            for line in lines:
                for c in line.split(','):
                    if c != '':
                        this_data.append(int(c))
            self.layer_data[layer.attrib['name']] = this_data

    def render(self, layer, surface, viewport):
        # TODO: How to batch this so it's faster?
        view_rect = viewport.rect
        for y in range(view_rect.height):
            for x in range(view_rect.width):
                tile = self.tiles[self.layer_data[layer][self.getIndex(x, y)]]
                target = pygame.Rect(x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height)
                if tile is not None:
                    surface.blit(tile, target)

    def getIndex(self, x, y):
        return x + y * self.map_width + 1

    def pointToScreen(self, viewport, offset_x, offset_y, x, y):
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

    def findPoint(self, layer_name, object_name):
        groups = self.root.findall('.//objectgroup[@name="{0}"]'.format(layer_name))
        if len(groups) == 1:
            objects = groups[0].findall('.//object[@name="{0}"'.format(object_name))

            if len(objects) == 1:
                if 'width' not in objects[0].attrib and 'height' not in objects[0].attrib:
                    # Then this is a point.
                    return (int(objects[0].attrib['x']), int(objects[0].attrib['y']))

        return None

    def findRect(self, layer_name, object_name):
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
