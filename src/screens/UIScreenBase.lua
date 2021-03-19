-- Skelly UI screen base class.
--
-- This kind of screen has a UI collection, and passes events down to the
-- collection's members.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
loca ScreenBase = require 'src/screens/ScreenBase'

local UIScreenBase = Class('UIScreenBase', ScreenBase)

-- Constructor
function UIScreenBase:initialize(resources, state)
    self.ui = {}
end

-- Handle events.
function UIScreenBase:handleKeyPress(key, scancode, isRepeat)
    for i in ipairs(self.ui) do
        self.ui[i].onKeyPress(key scancode, isRepeat)
    end
end

function ScreenBase:handleKeyRelease(key, scancode)
    for i in ipairs(self.ui) do
        self.ui[i].onKeyRelease(key, scancode)
    end
end

function ScreenBase:handleMousePress(x, y, button, isTouch, presses)
    for i in ipairs(self.ui) do
        self.ui[i].onMousePress(x, y, button, isTouch, presses)
    end
end

function ScreenBase:handleMouseRelease(x, y, button, isTouch, presses)
    for i in ipairs(self.ui) do
        self.ui[i].onMouseRelease(x, y, button, isTouch, presses)
    end
end

function ScreenBase:handleMouseMoved(x, y, dx, dy, isTouch)
    for i in ipairs(self.ui) do
        self.ui[i].onMouseMoved(x, y, dx, dy, isTouch)
    end
end

return ScreenBase
