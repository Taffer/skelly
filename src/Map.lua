-- Skelly Map for Tiled maps.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local Viewport = require 'src/Viewport'

-- =============================================================================
local Map = Class('Map')
function Map:initialize(resources, map_data)
    -- Maps are assumed to be "orthogonal" and "right-down", using 32x32 tiles.
    -- Map sizes will vary.
    --
    -- @param resources Loaded Skelly resources.
    -- @param map_data  Loaded Tiled map data, in Lua format.
    print('gameResources -', gameResources)
    print('Map -', resources)
    print('    -', map_data)

    self.width = map_data.width -- In tiles.
    self.height = map_data.height

    self.tile_width = map_data.tilewidth
    self.tile_height = map_data.tileheight

    -- Tiled 1.5 seems to have stopped including the texture atlas info in
    -- the exported map, so we're going to have to cheat.
    self.atlases = {
        ['base_out_atlas']          = resources.images.tiles_base_out_atlas,
        ['build_atlas']             = resources.images.tiles_build_atlas,
        ['obj_misk_atlas']          = resources.images.tiles_obj_misk_atlas,
        ['terrain-map-v7-repacked'] = resources.images.map_terrain,
        ['terrain_atlas']           = resources.images.tiles_terrain_atlas,
    }

    self.batches = {} -- One per tile atlas.
    for k, v in pairs(self.atlases) do
        self.batches[v] = love.graphics.newSpriteBatch(v, self.width * self.height)
    end

    -- Build quads from the tilesets. We need to keep the {atlas, quad} for
    -- each one so we can draw them later.
    self.quads = {
        [0] = {nil, nil}, -- Don't render me, I'm not a tile.
    }
    for i, tileset in pairs(map_data.tilesets) do
        local atlas = self.atlases[tileset.name]
        if atlas == nil then
            print('Unknown tileset: ' .. tileset.name)
        end

        local gid = tileset.firstgid

        local columns = atlas:getWidth() / self.tile_width
        local rows = atlas:getHeight() / self.tile_height

        local r = 0
        while r < rows do
            local c = 0
            while c < columns do
                self.quads[gid] = {
                    atlas,
                    love.graphics.newQuad(c * self.tile_width, r * self.tile_height, self.tile_width, self.tile_height, atlas)
                }
                gid = gid + 1
                c = c + 1
            end
            r = r + 1
        end
    end

    self.tile_layers = {}
    self.obj_layers = {}
    for i, layer in ipairs(map_data.layers) do
        if layer.type == 'tilelayer' then
            table.insert(self.tile_layers, layer)
        elseif layer.type == 'objectgroup' then
            table.insert(self.obj_layers, layer)
        else
            print('Unknown layer type: ' .. layer.type)
        end
    end
end

function Map:getIndex(x, y)
    -- Return the index of the tile at x, y.
    local i = y * self.width + x + 1
    return i
end

function Map:render(viewport, layer, x, y)
    -- Render one layer of the map.
    --
    -- @param viewport  A Viewport indicating which tiles to draw.
    -- @param layer     Which layer to draw. Tile layers only!
    -- @param x         Draw at x, y.
    -- @param y         Draw at x, y.
    if layer.type ~= 'tilelayer' then
        print('Tried to render invalid layer type: ' .. layer.type)
        return
    end

    -- TODO: If the viewport hasn't changed since last time, we can skip the
    --       batch:clear() and batch:add() steps and just draw.
    for _, batch in pairs(self.batches) do
        batch:clear()
    end

    for r = viewport.y, (viewport.y + viewport.height - 1) do
        for c = viewport.x, (viewport.x + viewport.width - 1) do
            local this_quad = layer.data[self:getIndex(c, r)]
            local atlas, quad = unpack(self.quads[this_quad])
            if atlas ~= nil then
                self.batches[atlas]:add(quad, x + c * self.tile_width, y + r * self.tile_height)
            end
        end
    end

    love.graphics.setColor(1, 1, 1, 1)
    for _, batch in pairs(self.batches) do
        love.graphics.draw(batch)
    end
end

return Map
