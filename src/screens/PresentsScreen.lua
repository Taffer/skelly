-- Skelly splash screen, "Taffer presents".
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'

local ColorFade = require 'src/ColorFade'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'

local text = require 'src/i18n'

local PresentsScreen = Class('PresentsScreen', ScreenBase)

function PresentsScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Title')

    -- Default English.
    self.resources.text = text[gameState.settings:get('language', 'en')]

    self.resources.fonts.default_serif = love.graphics.newFont('graphics/A_Font_with_Serifs.ttf', 72)
    self.resources.fonts.default_mono = love.graphics.newFont('graphics/LiberationMono-Bold.ttf', 16)
    self.resources.images.love_logo = love.graphics.newImage('graphics/love-game-0.10.png')
    self.resources.images.taffer = love.graphics.newImage('graphics/taffer-ronos.png')
    self.resources.music.theme = love.audio.newSource('music/Heroic Demise (New).mp3',  'stream')
    love.audio.setVolume(gameState.settings:get('music_volume', 1.0) * (gameState.settings:get('overall_volume', 1.0)))
    love.audio.play(self.resources.music.theme) -- start playing ASAP

    self.taffer_text = self.resources.text.presents.taffer_text
    self.love_text = self.resources.text.presents.love_text

    self.fade = ColorFade:new({1, 1, 1, 0}, {1, 1, 1, 1}, 2)
    self.exit_countdown = 2 -- seconds after fade to automatically exit

    local love_logo = self.resources.images.love_logo
    local logo_quad = love.graphics.newQuad(0, 0, love_logo:getWidth(), love_logo:getHeight(), love_logo)

    local taffer_logo = self.resources.images.taffer
    local taffer_quad = love.graphics.newQuad(0, 0, taffer_logo:getWidth(), taffer_logo:getHeight(), taffer_logo)

    self.ui = {
        Label:new(self, state.scr_width / 2, 16, self.taffer_text,
            self.resources.fonts.default_serif, {1, 1, 1, 1}, 'centre'),
        ImageButton:new(self, (state.scr_width - taffer_logo:getWidth()) / 2, 120, taffer_logo, taffer_quad),
        ImageButton:new(self, (state.scr_width - love_logo:getWidth()) / 2, 500, love_logo, logo_quad),
        Label:new(self, state.scr_width / 2, 640, self.love_text,
            self.resources.fonts.default_mono, {1, 1, 1, 1}, 'centre'),
    }

    self.onMouseRelease = (function(self)
        if self.fade:isDone() then
            self.exit_screen = true
        end
    end)

    self.onKeyRelease = (function(self)
        if self.fade:isDone() then
            self.exit_screen = true
        end
    end)
end

-- Render this screen's contents.
function PresentsScreen:draw()
    love.graphics.clear(0, 0, 0, 1)

    for i in ipairs(self.ui) do
        self.ui[i]:setColor(self.fade:getColor())
        self.ui[i]:draw()
    end
end

-- Update the screen.
function PresentsScreen:update(dt)
    self.fade:update(dt)

    if self.fade:isDone() then
        self.exit_countdown = self.exit_countdown - dt
        if self.exit_countdown < 0 then
            self.exit_screen = true
        end
    end
end

-- Exit this screen?
function PresentsScreen:exit()
    return self.exit_screen
end

return PresentsScreen
