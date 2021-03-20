-- Skelly UI element base object
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

-- UI object base class
local UIBase = Class('UIBase')

function UIBase:initialize()
    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0

    self.onMousePress = nil -- I've been clicked!
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

function UIBase:handleMousePress(x, y, button, isTouch, presses)
    if self.onMousePress and self:intersects(x, y) then
        self:onMousePress(x, y, button, isTouch, presses)
    end
end

function UIBase:handleMousePressRelease(x, y, button, isTouch, presses)
    if self.onMousePress and self:intersects(x, y) then
        self:onMouseRelease(x, y, button, isTouch, presses)
    end
end

function UIBase:handleMouseMoved(x, y, dx, dy, isTouch)
    if self.onMouseMoved and self:intersects(x, y) then
        self:onMouseMoved(x, y, dx, dy, isTouch)
    end
end

function UIBase:handleKeyPress(key, scancode, isRepeat)
    if self.onKeyPress then
        self:onKeyPress(key, scancode, isRepeat)
    end
end

function UIBase:handleKeyRelease(key, scancode)
    if self.onKeyRelease then
        self:onKeyRelease(key, scancode)
    end
end

return UIBase
