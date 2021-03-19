-- Skelly "Journey Onward" screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIScreenBase = require 'src/screens/UIScreenBase'

local Button = require 'src/ui/Button'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'

local JourneyScreen = Class('JourneyScreen', UIScreenBase)

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
    local ui_rpg = self.resources.images.ui_rpg
    local button_quad = love.graphics.newQuad(0, 282, 190, 49, ui_rpg)

    local x = (state.scr_width - 190) / 2

    local button_font = self.resources.fonts.button_font
    local button_color = {0, 0, 0, 1}
    self.journey_button  = Button:new(x, 350, ui_rpg, button_quad, self.journey_text, button_font, button_color)
    self.newgame_button  = Button:new(x, 410, ui_rpg, button_quad, self.newgame_text, button_font, button_color)
    self.settings_button = Button:new(x, 470, ui_rpg, button_quad, self.settings_text, button_font, button_color)

    self.credits_button  = Button:new(x, 550, ui_rpg, button_quad, self.credits_text, button_font, button_color)
    self.credits_button.onMousePress = function ()
        print('Credits clicked')
        self:setNextScreen('Credits')
        self.exit_screen = true
    end

    self.exit_button  = Button:new(x, 620, ui_rpg, button_quad, self.exit_text, button_font, button_color)
    self.exit_button.onMousePress = function ()
        print('Exit clicked')
        self.exit_screen = true
    end

    local title_image = self.resources.images.skelly_title
    local title_quad = love.graphics.newQuad(0, 0, title_image:getWidth(), title_image:getHeight(), title_image)

    local font_mono = self.resources.fonts.default_mono
    local font_title = self.resources.fonts.skelly_title

    self.ui = {
        ImageButton:new(0, 0, title_image, title_quad),
        Label:new(state.scr_width / 2, 40, self.skelly_text, font_title, {1, 1, 1, 1}, 'centre'),
        Label:new(state.scr_width / 2, 200, self.subtitle_text, font_mono, {1, 1, 1, 1}, 'centre'),

        self.journey_button,
        self.newgame_button,
        self.settings_button,
        self.credits_button,
        self.exit_button
    }
end

-- Render this screen's contents.
function JourneyScreen:draw()
    love.graphics.clear(0, 0, 0, 1)

    -- UI parts
    for i in ipairs(self.ui) do
        self.ui[i]:draw()
    end
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

return JourneyScreen
