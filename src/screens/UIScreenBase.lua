-- Skelly UI screen base class.
--
-- This kind of screen has a UI collection, and passes events down to the
-- collection's members.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'

local UIScreenBase = Class('UIScreenBase', ScreenBase)

-- Constructor
function UIScreenBase:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)

    self.ui = {}
end

-- Handle events.
function UIScreenBase:handleKeyPress(key, scancode, isRepeat)
    for i in ipairs(self.ui) do
        if self.ui[i].onKeyPress then
            self.ui[i]:onKeyPress(key, scancode, isRepeat)
        end
    end
end

function ScreenBase:handleKeyRelease(key, scancode)
    for i in ipairs(self.ui) do
        if self.ui[i].onKeyRelease then
            self.ui[i]:onKeyRelease(key, scancode)
        end
    end
end

function ScreenBase:handleMousePress(x, y, button, isTouch, presses)
    for i in ipairs(self.ui) do
        if self.ui[i].onMousePress then
            self.ui[i]:onMousePress(x, y, button, isTouch, presses)
        end
    end
end

function ScreenBase:handleMouseRelease(x, y, button, isTouch, presses)
    for i in ipairs(self.ui) do
        if self.ui[i].onMouseRelease then
            self.ui[i]:onMouseRelease(x, y, button, isTouch, presses)
        end
    end
end

function ScreenBase:handleMouseMoved(x, y, dx, dy, isTouch)
    for i in ipairs(self.ui) do
        if self.ui[i].onMouseMoved then
            self.ui[i]:onMouseMoved(x, y, dx, dy, isTouch)
        end
    end
end

return ScreenBase
