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
--
-- If you handled it, return true; false means the event continues on to the
-- next handler.
function ScreenBase:handle(event)
    if event == 'escape' then
        self.exit_screen = true

        return true
    end

    return false -- I didn't handle the event.
end

-- Screen state machine.
function ScreenBase:getNextScreen()
    return self.next_screen
end

function ScreenBase:setNextScreen(screen)
    self.next_screen = screen
end

return ScreenBase
