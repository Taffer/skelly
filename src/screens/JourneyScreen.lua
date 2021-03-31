-- Skelly "Journey Onward" screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIScreenBase = require 'src/screens/UIScreenBase'

local ColorFade = require 'src/ColorFade'
local Button = require 'src/ui/Button'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'

local JourneyButton = Class('JourneyButton', Button)
function JourneyButton:initialize(parent, x, y, texture, quad, text, font, color)
    Button.initialize(self, x, y, texture, quad, text, font, color)
    self.parent = parent
end

local JourneyScreen = Class('JourneyScreen', UIScreenBase)

function JourneyScreen:initialize(resources, state)
    UIScreenBase.initialize(self, resources, state)
    -- next_screen will be set when a button is chosen.

    local title_text = self.resources.text:getText('title')
    local journey_text = self.resources.text:getText('journey')
    self.skelly_text = self.resources.text:getText('skelly_title')
    self.subtitle_text = title_text.subtitle_text
    self.journey_text = journey_text.onward_text
    self.newgame_text = journey_text.new_game_text
    self.settings_text = journey_text.settings_text
    self.credits_text = journey_text.credits_text
    self.exit_text = journey_text.exit_text

    self.fade = ColorFade:new({0, 0, 0, 1}, {0, 0, 0, 0}, 1)

    -- UI quads
    local ui_rpg = self.resources.images.ui_rpg
    local button_quad = love.graphics.newQuad(0, 282, 190, 49, ui_rpg)

    local x = (state.scr_width - 190) / 2

    local button_font = self.resources.fonts.button_font
    local button_color = {0, 0, 0, 1}
    self.journey_button = JourneyButton:new(self, x, 350, ui_rpg, button_quad, self.journey_text, button_font, button_color)
    self.journey_button.selectOff = function(self)
        self.parent:setNextScreen('Game')
        self.parent:setExit()
    end

    self.newgame_button = JourneyButton:new(self, x, 410, ui_rpg, button_quad, self.newgame_text, button_font, button_color)
    self.newgame_button.selectOff = function(self)
        self.parent:setNextScreen('NewGame')
        self.parent:setExit()
    end

    self.settings_button = JourneyButton:new(self, x, 470, ui_rpg, button_quad, self.settings_text, button_font, button_color)
    self.settings_button.selectOff = function(self)
        self.parent:setNextScreen('Settings')
        self.parent:setExit()
    end

    self.credits_button = JourneyButton:new(self, x, 550, ui_rpg, button_quad, self.credits_text, button_font, button_color)
    self.credits_button.selectOff = function(self)
        self.parent:setNextScreen('Credits')
        self.parent:setExit()
    end

    self.exit_button = JourneyButton:new(self, x, 620, ui_rpg, button_quad, self.exit_text, button_font, button_color)
    self.exit_button.selectOff = function(self)
        self.parent:setNextScreen(nil)
        self.parent:setExit()
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

    if not self.fade:isDone() then
        love.graphics.setColor(unpack(self.fade:getColor()))
        love.graphics.rectangle('fill', 0, 0, gameState.scr_width, gameState.scr_height)
    end
end

-- Update the screen.
function JourneyScreen:update(dt)
    self.fade:update(dt)
end

return JourneyScreen
