-- Skelly initial loading screen, "Taffer presents".
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/base'

local PresentsScreen = Class('PresentsScreen', ScreenBase)

function PresentsScreen:initialize(resources)
    ScreenBase.initialize(self, resources)

    self.resources.fonts.default_serif = love.graphics.newFont('graphics/A_Font_with_Serifs.ttf', 72)
    self.resources.fonts.default_mono = love.graphics.newFont('graphics/LiberationMono-Bold.ttf', 16)
    self.resources.images.love_logo = love.graphics.newImage('graphics/love-game-0.10.png')

    self.taffer_text = "Taffer presents…"
    self.love_text = "A game made with LÖVE…"
end

-- Render this screen's contents.
function PresentsScreen:draw()
    -- Premature optimization:
    local rsrc = self.resources
    local font_default = rsrc.fonts.default_serif
    local font_mono = rsrc.fonts.default_mono
    local image_love = rsrc.images.love_logo

    love.graphics.clear(0, 0, 0, 1)

    local screen_width = love.graphics.getWidth()
    local width = font_default:getWidth(self.taffer_text)
    local x = (screen_width - width) / 2

    love.graphics.setColor(1, 1, 1, 1)
    love.graphics.setFont(font_default)
    love.graphics.print(self.taffer_text, x, 16)

    local scale = 0.25
    width = image_love:getWidth() * scale
    x = (screen_width - width) / 2

    love.graphics.draw(image_love, x, 360, 0, scale, scale)

    width = font_mono:getWidth(self.love_text)
    x = (screen_width - width) / 2

    love.graphics.setFont(font_mono)
    love.graphics.print(self.love_text, x, 640)
end

-- Update the screen.
function PresentsScreen:update(dt)
end

-- Exit this screen?
function PresentsScreen:exit()
    return self.exit_screen
end

-- Handle events.
--
-- If you handled it, return true; false means the event continues on to the
-- next handler.
function PresentsScreen:handle(event)
    if event == 'escape' then
        self.exit_screen = true
        return true
    end

    return ScreenBase.handle(self, event)
end

return PresentsScreen
