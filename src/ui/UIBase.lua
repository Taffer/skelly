-- Skelly UI element base object
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass'

-- UI object base class
local UIBase = Class('UIBase')

function UIBase:initialize()
    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0

    self.onClick = nil -- I've been clicked!
end

function UIBase:intersects(x, y)
    -- Does x,y intersect with the button?
    if x < self.x or y < self.y then
        return false
    end

    if x > self.x + self.width or y > self.y + self.height then
        return false
    end

    return true
end

function UIBase:onMousePress(x, y, button)
    if not self:intersects(x, y) then
        return
    end

    -- We're ignoring the button, click with anything.
    if self.onClick then
        self:onClick(button)
    end
end
