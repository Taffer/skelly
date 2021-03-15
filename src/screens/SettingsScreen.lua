-- Skelly settings screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'
local Button = require 'src/ui/Button'
local SettingsOverlay = require 'src/ui/SettingsOverlay'

local SettingsScreen = Class('SettingsScreen', ScreenBase)

function SettingsScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Journey')

    self.skelly_text = self.resources.text.skelly_title
    self.subtitle_text = self.resources.text.title.subtitle_text

    self.alpha = 0 -- Alpha level for the fade-in/out animation.
    self.ticks = 0
    self.pi_over_180 = math.pi / 180
    self.degrees_per_second = 45

    self.overlay = SettingsOverlay:new(resources, self, 300, 350, 680, 400)
end

-- Render this screen's contents.
function SettingsScreen:draw()
    -- Premature optimization:
    local rsrc = self.resources
    local font_mono = rsrc.fonts.default_mono
    local font_title = rsrc.fonts.skelly_title
    local image_title = rsrc.images.skelly_title

    love.graphics.clear(0, 0, 0, 1)

    love.graphics.setColor(1, 1, 1, self.alpha)
    love.graphics.draw(image_title, 0, 0)

    local screen_width = love.graphics.getWidth()
    local width = font_mono:getWidth(self.subtitle_text)
    local x = (screen_width - width) / 2
    love.graphics.setFont(font_mono)
    love.graphics.print(self.subtitle_text, x, 200)

    width = font_title:getWidth(self.skelly_text)
    x = (screen_width - width) / 2
    love.graphics.setFont(font_title)
    love.graphics.print(self.skelly_text, x, 40)

    -- Display the settings overlay.
    self.overlay:draw()
end

-- Update the screen.
function SettingsScreen:fadeInAnimation()
    local degrees = self.ticks * self.degrees_per_second
    if degrees > 90 then
        degrees = 90
    end

    self.alpha = math.sin(degrees * self.pi_over_180)
end

function SettingsScreen:update(dt)
    self.ticks = self.ticks + dt

    self:fadeInAnimation()
end

-- Exit this screen?
function SettingsScreen:exit()
    return self.exit_screen
end

-- Handle events.
--
-- If you handled it, return true; false means the event continues on to the
-- next handler.
function SettingsScreen:handle(event)
    if event.keys['escape'] then
        self.exit_screen = true
        return true
    end

    if event.button then
        -- Mouse click.
        self.overlay:onMousePress(event.mouse_x, event.mouse_y)
    end

    return ScreenBase.handle(self, event)
end

return SettingsScreen
