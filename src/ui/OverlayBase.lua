-- Skelly overlay base class.
--
-- Overlays are bits of UI than can be drawn on top of "any" screen, such
-- as the settings, inventory, etc.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

-- =============================================================================
local OverlayBase = Class('OverlayBase')
function OverlayBase:initialize(x, y, width, height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.overlay = {} -- UI elements in the overlay.
end

function OverlayBase:addElement(tag, uiElement)
    self.overlay[tag] = uiElement
end

function OverlayBase:draw()
    love.graphics.setColor(1, 1, 1, 1/3) -- This might not be dark enough.
    love.graphics.rectangle('fill', 0, 0, love.graphics.getWidth(), love.graphics.getHeight())

    for k, v in pairs(self.overlay) do
        self.overlay[k]:draw()
    end
end

-- Check for input events.
function OverlayBase:checkInputs(keyboard, mouse, gamepad)
    for _, ui in pairs(self.overlay) do
        ui:checkInputs(keyboard, mouse, gamepad)
    end
end

return OverlayBase
