-- Skelly Viewport for tiled maps.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local Viewport = Class('Viewport')

function Viewport:initialize(map_width, map_height, x, y, width, height)
    self.map_width = map_width
    self.map_height = map_height

    self.x = x -- These are specified in tiles, not pixels.
    self.y = y
    self.width = width or 29 -- Viewport is 29x21 in Skelly.
    self.height = height or 21
end

function Viewport:setPosition(x, y)
    if x + self.width > self.map_width then
        self.x = self.map_width - self.width
    else
        self.x = x
    end
    if y + self.height > self.map_height then
        self.y = self.map_height - self.height
    else
        self.y = y
    end
end

return Viewport
