-- Skelly UI events
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local UIEvent = Class('UIEvent')

local keys = {} -- keys that are pressed

function UIEvent:initialize(event)
    self.keys = keys

    self.button = nil
    self.mouse_x = 0
    self.mouse_y = 0

    if event.keydown then
        self.keys[event.keydown] = true
    elseif event.keyup then
        self.keys[event.keyup] = false
    elseif event.mousedown then
        self.button = event.mousedown
        self.mouse_x = event.x
        self.mouse_y = event.y
    elseif event.mouseup then
        self.button = event.mouseup
        self.mouse_x = event.x
        self.mouse_y = event.y
    else
        print('UNKNOWN EVENT')
        for k,v in pairs(event) do
            print('-->', k, '=', v)
        end
    end
end

return UIEvent
