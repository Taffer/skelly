-- Skelly UI element: image button
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass'
local UIBase = require 'src/ui/UIBase'

-- ImageButton class
local ImageButton = Class('ImageButton', UIBase)

function ImageButton:initialize(x, y, texture, quad)
    self.x = x
    self.y = y
    self.texture = texture
    self.quad = quad

    local _, _, w, h = self.quad:getViewport()
    self.width = w
    self.height = h
end

function ImageButton:draw()
    love.graphics.setColor(1, 1, 1, 1)
    love.graphics.draw(self.texture, self.quad, self.x, self.y)
end
