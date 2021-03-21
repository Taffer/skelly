-- Skelly overlay base class.
--
-- Overlays are bits of UI than can be drawn on top of "any" screen, such
-- as the settings, inventory, etc.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local OverlayBase = Class('OverlayBase')

function OverlayBase:initialize(parent, x, y, width, height)
    self.parent = parent -- A Screen object.
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.overlay = {} -- UI elements in the overlay.
end

function OverlayBase:addInterface(ui_part)
    table.insert(self.overlay, ui_part)
end

function OverlayBase:draw()
    for i in ipairs(self.overlay) do
        self.overlay[i]:draw()
    end
end

function OverlayBase:onMouseMove(x, y)
    if not self:intersects(x, y) then
        return false
    end

    -- Did one of my UI elements handle the event?
    for i in ipairs(self.overlay) do
        local handled = self.overlay[i]:onMouseMove(event.mouse_x, event.mouse_y)
        if handled then
            return handled
        end
    end

    return false
end

function OverlayBase:onMousePress(x, y)
    if not self:intersects(x, y) then
        return false
    end

    -- Did one of my UI elements handle the event?
    for i in ipairs(self.overlay) do
        local handled = self.overlay[i]:onMousePress(event.mouse_x, event.mouse_y)
        if handled then
            return handled
        end
    end

    return false
end

function OverlayBase:onMouseRelease(x, y)
    if not self:intersects(x, y) then
        return false
    end

    -- Did one of my UI elements handle the event?
    for i in ipairs(self.overlay) do
        local handled = self.overlay[i]:onMouseRelease(event.mouse_x, event.mouse_y)
        if handled then
            return handled
        end
    end

    return false
end

function OverlayBase:intersects(x, y)
    -- Does x,y intersect with the overlay?
    if x < self.x or y < self.y then
        return false
    end

    if x > self.x + self.width or y > self.y + self.height then
        return false
    end

    return true
end

return OverlayBase
