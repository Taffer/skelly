-- Skelly screen base class.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local ScreenBase = Class('ScreenBase')

-- Constructor
function ScreenBase:initialize(resources)
    self.resources = resources
end

-- Render this screen's contents.
function ScreenBase:draw()
end

-- Handle events.
--
-- If you handled it, return true; false means the event continues on to the
-- next handler.
function ScreenBase:handle(event)
    if event == 'escape' then
        love.event.quit()
        return true
    end

    return false -- I didn't handle the event.
end

return ScreenBase
