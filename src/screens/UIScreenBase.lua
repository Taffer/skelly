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

function UIScreenBase:addElement(tag, uiElement)
    self.ui[tag] = uiElement
end

-- Check for input events.
function UIScreenBase:checkInputs(keybord, mouse, gamepad)
    for _, ui in pairs(self.ui) do
        ui:checkInputs(keyboard, mouse, gamepad)
    end
end

return UIScreenBase
