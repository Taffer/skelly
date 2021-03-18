-- Skelly UI element: image button
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIBase = require 'src/ui/UIBase'

-- ImageButton class
local ImageButton = Class('ImageButton', UIBase)

function ImageButton:initialize(x, y, texture, quad)
    UIBase.initialize(self)

    self.x = x
    self.y = y
    self.texture = texture
    self.quad = quad

    self.color = {1, 1, 1, 1} -- Default is draw it normally.

    local _, _, w, h = self.quad:getViewport()
    self.width = w
    self.height = h
end

function ImageButton:draw()
    love.graphics.setColor(unpack(self.color))
    love.graphics.draw(self.texture, self.quad, self.x, self.y)
end

function ImageButton:setColor(color)
    self.color = color
end

return ImageButton
