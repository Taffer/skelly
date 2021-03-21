-- Skelly screen base class.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local ScreenBase = Class('ScreenBase')

-- Constructor
function ScreenBase:initialize(resources, state)
    self.resources = resources
    self.state = state

    self.exit_screen = false -- Time to exit this screen?
    self.next_screen = nil   -- No next screen means Exit the game.

    -- Event handlers.
    self.onKeyPress = nil -- (key)
    self.onKeyRelease = nil -- (key)
    self.onMousePress = nil
    self.onMouseRelease = nil
    self.onMouseMoved = nil
end

-- Render this screen's contents.
function ScreenBase:draw()
end

-- Update this screen's contents.
function ScreenBase:update(dt)
end

-- Exit this screen?
function ScreenBase:exit()
    return self.exit_screen
end

-- Handle events.
function ScreenBase:handleKeyPress(key, scancode, isRepeat)
    if self.onKeyPress then
        self:onKeyPress(key, scancode, isRepeat)
    end
end

function ScreenBase:handleKeyRelease(key, scancode)
    if self.onKeyRelease then
        self:onKeyRelease(key, scancode)
    end
end

function ScreenBase:handleMousePress(x, y, button, isTouch, presses)
    if self.onMousePress then
        self:onMousePress(x, y, button, isTouch, presses)
    end
end

function ScreenBase:handleMouseRelease(x, y, button, isTouch, presses)
    if self.onMouseRelease then
        self:onMouseRelease(x, y, button, isTouch, presses)
    end
end

function ScreenBase:handleMouseMoved(x, y, dx, dy, isTouch)
    if self.onMouseMoved then
        self:onMouseMoved(x, y, dx, dy, isTouch)
    end
end

-- Screen state machine.
function ScreenBase:getNextScreen()
    return self.next_screen
end

function ScreenBase:setNextScreen(screen)
    self.next_screen = screen
end

return ScreenBase
