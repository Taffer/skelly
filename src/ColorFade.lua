-- Skelly Colour Fader object
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

-- =============================================================================
local ColorFade = Class("ColorFade")
function ColorFade:initialize(rgba1, rgba2, duration)
    self.r, self.g, self.b, self.a = unpack(rgba1)
    self.start_r, self.start_g, self.start_b, self.start_a = unpack(rgba1)
    self.end_r, self.end_g, self.end_b, self.end_a = unpack(rgba2)
    self.duration = duration
    self.dt = 0

    self.done = false
end

function ColorFade:update(dt)
    if self.done then
        return
    end

    self.dt = self.dt + dt
    if self.dt > self.duration then
        self.r = self.end_r
        self.g = self.end_g
        self.b = self.end_b
        self.a = self.end_a

        self.done = true

        return
    end

    local diff = self.dt / self.duration
    self.r = self.start_r + (self.end_r - self.start_r) * diff
    self.g = self.start_g + (self.end_g - self.start_g) * diff
    self.b = self.start_b + (self.end_b - self.start_b) * diff
    self.a = self.start_a + (self.end_a - self.start_a) * diff
end

function ColorFade:getColor()
    return {self.r, self.g, self.b, self.a}
end

function ColorFade:isDone()
    return self.done
end

return ColorFade
