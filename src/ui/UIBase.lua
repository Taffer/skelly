-- Skelly UI element base object
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

-- UI object base class
local UIBase = Class('UIBase')

function UIBase:initialize(parent)
    self.parent = parent -- "Owner" of this UI object, for callbacks.

    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0

    self.color = {1, 1, 1, 1}
end

function UIBase:setColor(color)
    self.color = color
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

-- Check for input events.
function UIBase:checkInputs(keybord, mouse, gamepad)
end

return UIBase
