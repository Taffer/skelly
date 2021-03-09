-- Skelly "Journey Onward" screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'
local Button = require 'src/ui/Button'

local JourneyScreen = Class('JourneyScreen', ScreenBase)

function JourneyScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)

    -- next_screen will be set when a button is chosen.

    self.skelly_text = self.resources.text.skelly_title
    self.subtitle_text = self.resources.text.title.subtitle_text
    self.journey_text = self.resources.text.journey.onward_text
    self.newgame_text = self.resources.text.journey.new_game_text
    self.settings_text = self.resources.text.journey.settings_text
    self.credits_text = self.resources.text.journey.credits_text
    self.exit_text = self.resources.text.journey.exit_text

    self.alpha = 0 -- Alpha level for the fade-in/out animation.
    self.ticks = 0
    self.pi_over_180 = math.pi / 180
    self.degrees_per_second = 45

    -- UI quads
    local ui = self.resources.images.ui_rpg
    self.quads = {
        --[[
    <SubTexture name="arrowBeige_left.png" x="303" y="486" width="22" height="21"/>
    <SubTexture name="arrowBeige_right.png" x="171" y="486" width="22" height="21"/>
        ]]
        arrow_left  = love.graphics.newQuad(303, 486,  22, 21, ui),
        arrow_right = love.graphics.newQuad(171, 486,  22, 21, ui),
    }

    local x = (love.graphics.getWidth() - 190) / 2

    local button_font = self.resources.fonts.button_font
    self.journey_button = Button:new(self.resources, button_font, self.journey_text, x, 380)
    self.newgame_button = Button:new(self.resources, button_font, self.newgame_text, x, 430)
    self.settings_button = Button:new(self.resources, button_font, self.settings_text, x, 480)

    self.credits_button = Button:new(self.resources, button_font, self.credits_text, x, 550)

    self.exit_button = Button:new(self.resources, button_font, self.exit_text, x, 620)
end

-- Render this screen's contents.
function JourneyScreen:draw()
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

    -- UI parts
    self.journey_button:draw()
    self.newgame_button:draw()
    self.settings_button:draw()

    self.credits_button:draw()

    self.exit_button:draw()
end

-- Update the screen.
function JourneyScreen:update(dt)
    self.ticks = self.ticks + dt

    local degrees = self.ticks * self.degrees_per_second -- 1 second = 90 degrees
    if degrees >= 90 then
        -- Pause the animation until loading is done.
        degrees = 90
    end

    self.alpha = math.sin(degrees * self.pi_over_180)

    if degrees > 180 then -- sin(180 degrees) is back to 0 alpha
        self.exit_screen = true
    end
end

-- Exit this screen?
function JourneyScreen:exit()
    return self.exit_screen
end

-- Handle events.
--
-- If you handled it, return true; false means the event continues on to the
-- next handler.
function JourneyScreen:handle(event)
    if event == 'escape' then
        -- Escape doesn't kick you out until loading is done, sorry.
        self.exit_screen = true
        return true
    end

    return ScreenBase.handle(self, event)
end

return JourneyScreen
