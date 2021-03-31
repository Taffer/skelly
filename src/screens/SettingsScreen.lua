-- Skelly settings screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'

local ColorFade = require 'src/ColorFade'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'
local SettingsOverlay = require 'src/ui/SettingsOverlay'

local SettingsScreen = Class('SettingsScreen', ScreenBase)

function SettingsScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Journey')

    self.skelly_text = self.resources.text.skelly_title
    self.subtitle_text = self.resources.text.title.subtitle_text

    self.fade = ColorFade:new({0, 0, 0, 1}, {0, 0, 0, 0}, 1)

    local title_image = self.resources.images.skelly_title
    local title_quad = love.graphics.newQuad(0, 0, title_image:getWidth(), title_image:getHeight(), title_image)

    local font_mono = self.resources.fonts.default_mono
    local font_title = self.resources.fonts.skelly_title

    self.ui = {
        ImageButton:new(self, 0, 0, title_image, title_quad),
        Label:new(self, state.scr_width / 2, 40, self.skelly_text, font_title, {1, 1, 1, 1}, 'centre'),
        Label:new(self, state.scr_width / 2, 200, self.subtitle_text, font_mono, {1, 1, 1, 1}, 'centre'),
    }

    self.overlay = SettingsOverlay:new(resources, self, 300, 350, 680, 400)

    self.onMouseRelease = (function(self)
        self:setExit()
    end)

    self.onKeyRelease = (function(self)
        self:setExit()
    end)
end

-- Render this screen's contents.
function SettingsScreen:draw()
    love.graphics.clear(0, 0, 0, 1)

    -- UI parts
    for i in ipairs(self.ui) do
        self.ui[i]:draw()
    end

    -- Display the settings overlay.
    self.overlay:draw()

    if not self.fade:isDone() then
        love.graphics.setColor(unpack(self.fade:getColor()))
        love.graphics.rectangle('fill', 0, 0, gameState.scr_width, gameState.scr_height)
    end
end

-- Update the screen.
function SettingsScreen:update(dt)
    self.fade:update(dt)
end

return SettingsScreen
