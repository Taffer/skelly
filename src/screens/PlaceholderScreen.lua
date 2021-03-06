-- Skelly initial loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'

local PlaceholderScreen = Class('PlaceholderScreen', ScreenBase)

function PlaceholderScreen:initialize(resources)
    ScreenBase.initialize(self, resources)

    self.resources.fonts.default = love.graphics.newFont('graphics/A_Font_with_Serifs.ttf', 32)
    self.resources.images.loading = love.graphics.newImage('graphics/youre-being-a-dick.png')

    self.text = 'Insert game here.'
end

-- Render this screen's contents.
function PlaceholderScreen:draw()
    love.graphics.setColor(1, 1, 1, 1)
    love.graphics.draw(self.resources.images.loading)
    love.graphics.setFont(self.resources.fonts.default)
    love.graphics.setColor(0, 1, 0, 1)
    love.graphics.print(self.text, 5, 5)
end

-- Handle events.
--
-- If you handled it, return true; false means the event continues on to the
-- next handler.
function PlaceholderScreen:handle(event)
    if not event then
        print('No event.')
        return true
    end

    if event ~= 'escape' then
        if string.len(self.text) > 20 then
            self.text = string.sub(self.text, 20)
        end
        self.text = self.text .. event
    end

    return ScreenBase.handle(self, event)
end

return PlaceholderScreen
