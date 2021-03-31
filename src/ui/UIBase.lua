-- Skelly UI element base object
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

-- =============================================================================
local UIBase = Class('UIBase')
function UIBase:initialize()
    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0

    self.color = {1, 1, 1, 1}

    -- Event tracking.
    self.cursor_x = 0
    self.cursor_y = 0
    self.selected = false
    self.highlight = false
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
function UIBase:checkInputs(keyboard, mouse, gamepad)
    if self:intersects(mouse.current_x, mouse.current_y) then
        if mouse[1] and not self.selected then
            self.selected = true
            self:selectOn()
        elseif not mouse[1] and self.selected then
            self.selected = false
            self:selectOff()
        end

        if not self.highlight then
            self.highlight = true
            self:cursorEnter()
        end
    else
        if self.highlight then
            self.highlight = false
            self:cursorExit()
        end
    end

    self.cursor_x = mouse.current_x
    self.cursor_y = mouse.current_y
end

function UIBase:selectOn()
    -- Called when mouse clicked, or gamepad button A pressed.
end

function UIBase:selectOff()
    -- Called when mouse/gamepad button released.
end

function UIBase:cursorEnter()
    -- Called when the cursor enters its rectangle.
end

function UIBase:cursorExit()
    -- Called when the cursor exits its rectangle.
end

return UIBase
