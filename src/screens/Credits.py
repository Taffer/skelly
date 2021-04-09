# Skelly credits screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

from . import Base
from ..ui import ColorFade
from ..ui import ImageButton
from ..ui import Label

local CreditsScreen = Class('CreditsScreen', ScreenBase)
function CreditsScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Journey')

    local title_text = self.resources.text:getText('title')
    self.skelly_text = self.resources.text:getText('skelly_title')
    self.subtitle_text = title_text.subtitle_text
    self.credits = self.resources.text:getText('credits')

    self.fade = ColorFade:new({0, 0, 0, 1}, {0, 0, 0, 0}, 1)

    self.ticks = 0
    self.credits_area = {200, 250, 880, 450}

    self.font = self.resources.fonts.default_mono
    self.font:setLineHeight(1.1) -- little extra space
    self.font_em = self.font:getWidth('M')
    self.font_lh = self.font:getHeight() * self.font:getLineHeight()

    -- One drawback to this is if you leave the credits running forever, it'll
    -- consume all RAM.
    self.buffer = {}
    self.buffer_idx = 1 -- draw buffer from here
    self.max_columns = math.floor(880 / self.font_em)
    self.max_lines = math.floor(450 / self.font_lh)
    self.lines_to_add = 0
    self.credits_idx = 1

    -- UI pieces
    local title_image = self.resources.images.skelly_title
    local title_quad = love.graphics.newQuad(0, 0, title_image:getWidth(), title_image:getHeight(), title_image)

    local font_mono = self.resources.fonts.default_mono
    local font_title = self.resources.fonts.skelly_title

    self.ui = {
        ImageButton:new(0, 0, title_image, title_quad),
        Label:new(state.scr_width / 2, 40, self.skelly_text, font_title, {1, 1, 1, 1}, 'centre'),
        Label:new(state.scr_width / 2, 200, self.subtitle_text, font_mono, {1, 1, 1, 1}, 'centre'),
    }
end

-- Render this screen's contents.
function CreditsScreen:draw()
    -- Premature optimization:
    local rsrc = self.resources
    local font_mono = rsrc.fonts.default_mono

    love.graphics.clear(0, 0, 0, 1)

    for i in ipairs(self.ui) do
        self.ui[i]:draw()
    end

    -- Display the credits.
    local x, y, w, h = unpack(self.credits_area)
    love.graphics.setColor(0, 0, 0, 0.75)
    love.graphics.rectangle('fill', x, y, w, h)
    love.graphics.setFont(self.font)

    local delta = 0
    local buff_start = 1
    local buff_end = #self.buffer
    if #self.buffer > self.max_lines then
        buff_start = buff_end - self.max_lines + 1
    end

    love.graphics.setColor(1, 1, 1, 1)
    for idx = buff_start, buff_end do
        love.graphics.print(self.buffer[idx], x, y + delta)
        delta = delta + self.font_lh
    end

    if not self.fade:isDone() then
        love.graphics.setColor(unpack(self.fade:getColor()))
        love.graphics.rectangle('fill', 0, 0, gameState.scr_width, gameState.scr_height)
    end
end

-- Update the screen.
function CreditsScreen:update(dt)
    self.fade:update(dt)

    self.ticks = self.ticks + dt
    if self.ticks > 1 then
        self.lines_to_add = self.lines_to_add + dt

        while self.lines_to_add > 0.25 do
            table.insert(self.buffer, self.credits[self.credits_idx][2])
            self.credits_idx = self.credits_idx + 1
            if self.credits_idx > #self.credits then
                self.credits_idx = 1
            end

            self.lines_to_add = self.lines_to_add - 0.25
        end
    end
end

-- Check for input events.
function CreditsScreen:checkInputs(keyboard, mouse, gamepad)
    if keyboard['escape'] or mouse[1] or gamepad['a'] then
        self:setExit()
    end
end

return CreditsScreen
