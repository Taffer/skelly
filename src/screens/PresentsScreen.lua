-- Skelly splash screen, "Taffer presents".
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'

local ColorFade = require 'src/ColorFade'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'
local UIBase = require 'src/ui/UIBase'

local FADE_TIME = 0.5 -- Set to 2.0 for production.

local PresentsScreen = Class('PresentsScreen', ScreenBase)
function PresentsScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Title')

    self.resources.text:setLanguage(gameState.settings:get('language'))

    self.resources.fonts.default_serif = love.graphics.newFont('graphics/A_Font_with_Serifs.ttf', 72)
    self.resources.fonts.default_mono = love.graphics.newFont('graphics/LiberationMono-Bold.ttf', 16)
    self.resources.images.love_logo = love.graphics.newImage('graphics/love-game-0.10.png')
    self.resources.images.taffer = love.graphics.newImage('graphics/taffer-ronos.png')
    self.resources.music.theme = love.audio.newSource('music/Heroic Demise (New).mp3',  'stream')
    love.audio.setVolume(gameState.settings:get('music_volume') * (gameState.settings:get('overall_volume')))
    love.audio.play(self.resources.music.theme) -- start playing ASAP

    local presents_text = self.resources.text:getText('presents')
    self.taffer_text = presents_text.taffer_text
    self.love_text = presents_text.love_text

    self.fade = ColorFade:new({0, 0, 0, 1}, {0, 0, 0, 0}, FADE_TIME)
    self.fade_out = false -- fade in first...
    self.exit_countdown = FADE_TIME * 2 -- seconds after fade to automatically exit

    local love_logo = self.resources.images.love_logo
    local logo_quad = love.graphics.newQuad(0, 0, love_logo:getWidth(), love_logo:getHeight(), love_logo)

    local taffer_logo = self.resources.images.taffer
    local taffer_quad = love.graphics.newQuad(0, 0, taffer_logo:getWidth(), taffer_logo:getHeight(), taffer_logo)

    self.ui = {
        Label:new(state.scr_width / 2, 16, self.taffer_text,
            self.resources.fonts.default_serif, {1, 1, 1, 1}, 'centre'),
        ImageButton:new((state.scr_width - taffer_logo:getWidth()) / 2, 120, taffer_logo, taffer_quad),
        ImageButton:new((state.scr_width - love_logo:getWidth()) / 2, 500, love_logo, logo_quad),
        Label:new(state.scr_width / 2, 640, self.love_text,
            self.resources.fonts.default_mono, {1, 1, 1, 1}, 'centre'),
    }
end

-- Render this screen's contents.
function PresentsScreen:draw()
    love.graphics.clear(0, 0, 0, 1)

    for i in ipairs(self.ui) do
        self.ui[i]:draw()
    end

    love.graphics.setColor(unpack(self.fade:getColor()))
    love.graphics.rectangle('fill', 0, 0, gameState.scr_width, gameState.scr_height)
end

-- Update the screen.
function PresentsScreen:update(dt)
    self.fade:update(dt)

    if self.fade_out then
        -- If we're fading out...
        if self.fade:isDone() then
            self:setExit()
        end
    else
        -- If we're fading in...
        if self.fade:isDone() then
            self.exit_countdown = self.exit_countdown - dt
            if self.exit_countdown < 0 then
                self.fade = ColorFade:new({0, 0, 0, 0}, {0, 0, 0, 1}, FADE_TIME)
                self.fade_out = true
            end
        end
    end
end

-- Check for input events.
function PresentsScreen:checkInputs(keyboard, mouse, gamepad)
    if keyboard['escape'] or mouse[1] or gamepad['a'] then
        self:setExit()
    end
end

return PresentsScreen
