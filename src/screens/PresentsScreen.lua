-- Skelly splash screen, "Taffer presents".
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'

local text = require 'src/i18n'

local PresentsScreen = Class('PresentsScreen', ScreenBase)

function PresentsScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Title')

    -- Default English.
    self.resources.text = text[gameState.settings.language] or text.en

    self.resources.fonts.default_serif = love.graphics.newFont('graphics/A_Font_with_Serifs.ttf', 72)
    self.resources.fonts.default_mono = love.graphics.newFont('graphics/LiberationMono-Bold.ttf', 16)
    self.resources.images.love_logo = love.graphics.newImage('graphics/love-game-0.10.png')
    self.resources.images.taffer = love.graphics.newImage('graphics/taffer-ronos-512x512.png')
    self.resources.music.theme = love.audio.newSource('music/Heroic Demise (New).mp3',  'stream')
    love.audio.setVolume(gameState.settings.music_volume)
    love.audio.play(self.resources.music.theme) -- start playing ASAP

    self.taffer_text = self.resources.text.presents.taffer_text
    self.love_text = self.resources.text.presents.love_text

    self.alpha = 0 -- Alpha level for the fade-in/out animation.
    self.ticks = 0
    self.pi_over_180 = math.pi / 180
    self.degrees_per_second = 45 / 2 -- Fade in/out takes ~2 seconds for each.
end

-- Render this screen's contents.
function PresentsScreen:draw()
    -- Premature optimization:
    local rsrc = self.resources
    local font_default = rsrc.fonts.default_serif
    local font_mono = rsrc.fonts.default_mono
    local image_love = rsrc.images.love_logo
    local image_taffer = rsrc.images.taffer

    love.graphics.clear(0, 0, 0, 1)

    local screen_width = love.graphics.getWidth()
    local width = font_default:getWidth(self.taffer_text)
    local x = (screen_width - width) / 2
    love.graphics.setColor(1, 1, 1, self.alpha)
    love.graphics.setFont(font_default)
    love.graphics.print(self.taffer_text, x, 16)

    local love_scale = 0.125
    width = image_love:getWidth() * love_scale
    x = (screen_width - width) / 2
    love.graphics.draw(image_love, x, 500, 0, love_scale, love_scale)

    local taffer_scale = 0.65
    width = image_taffer:getWidth() * taffer_scale
    x = (screen_width - width) / 2
    love.graphics.draw(image_taffer, x, 150, 0, taffer_scale, taffer_scale)

    width = font_mono:getWidth(self.love_text)
    x = (screen_width - width) / 2
    love.graphics.setFont(font_mono)
    love.graphics.print(self.love_text, x, 640)
end

-- Update the screen.
function PresentsScreen:update(dt)
    self.ticks = self.ticks + dt

    local degrees = self.ticks * self.degrees_per_second -- 1 second = 90 degrees

    self.alpha = math.sin(degrees * self.pi_over_180)

    if degrees > 180 then -- sin(180 degrees) is back to 0 alpha
        self.exit_screen = true
    end
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
