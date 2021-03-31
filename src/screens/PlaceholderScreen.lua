-- Skelly initial loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'

local PlaceholderScreen = Class('PlaceholderScreen', ScreenBase)

function PlaceholderScreen:initialize(resources)
    ScreenBase.initialize(self, resources)
    self:setNextScreen('Journey')

    self.resources.fonts.default = love.graphics.newFont('graphics/A_Font_with_Serifs.ttf', 32)
    self.resources.images.loading = love.graphics.newImage('graphics/youre-being-a-dick.png')

    self.text = 'Insert game here.'

    self.onMouseRelease = (function(self)
        self.exit_screen = true
    end)

    self.onKeyRelease = (function(self)
        self.exit_screen = true
    end)
end

-- Render this screen's contents.
function PlaceholderScreen:draw()
    love.graphics.setColor(1, 1, 1, 1)
    love.graphics.draw(self.resources.images.loading)
    love.graphics.setFont(self.resources.fonts.default)
    love.graphics.setColor(0, 1, 0, 1)
    love.graphics.print(self.text, 5, 5)
end

-- Check for input events.
function PlaceholderScreen:checkInputs(keybord, mouse, gamepad)
    if keyboard['escape'] or mouse['1'] or gamepad['a'] then
        self:setExit()
    end
end

return PlaceholderScreen
