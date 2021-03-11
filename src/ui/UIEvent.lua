-- Skelly UI events
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local UIEvent = Class('UIEvent')

function UIEvent:initialize()
    self.keys = {} -- keypress

    self.click = nil -- mouse click
    self.mouse_x = 0
    self.mouse_y = 0
end

function UIEvent:keyPressed(key)
    self.keys[key] = true
end

function UIEvent:keyReleased(key)
    self.keys[key] = nil
end

function UIEvent:mouseClicked(button, x, y)
    self.click = button
    self.x = x
    self.y = y
end

return UIEvent
