-- Skelly credits screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'

local CreditsScreen = Class('CreditsScreen', ScreenBase)

function CreditsScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Journey')

    self.skelly_text = self.resources.text.skelly_title
    self.subtitle_text = self.resources.text.title.subtitle_text
    self.credits = self.resources.text.credits

    self.alpha = 0 -- Alpha level for the fade-in/out animation.
    self.ticks = 0
    self.pi_over_180 = math.pi / 180
    self.degrees_per_second = 45

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
        self.ui[i]:setColor({1, 1, 1, self.alpha})
        self.ui[i]:draw()
    end

    -- Display the credits.
    local x, y, w, h = unpack(self.credits_area)
    love.graphics.setColor(0, 0, 0, 0.75)
    love.graphics.rectangle('fill', x, y, w, h)
    love.graphics.setColor(1, 1, 1, 1)
    love.graphics.setFont(self.font)

    local delta = 0
    local buff_start = 1
    local buff_end = #self.buffer
    if #self.buffer > self.max_lines then
        buff_start = buff_end - self.max_lines + 1
    end

    for idx = buff_start, buff_end do
        love.graphics.print(self.buffer[idx], x, y + delta)
        delta = delta + self.font_lh
    end
end

-- Update the screen.
function CreditsScreen:fadeInAnimation()
    local degrees = self.ticks * self.degrees_per_second
    if degrees > 90 then
        degrees = 90
    end

    self.alpha = math.sin(degrees * self.pi_over_180)
end

function CreditsScreen:update(dt)
    self.ticks = self.ticks + dt

    self:fadeInAnimation()

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

-- Exit this screen?
function CreditsScreen:exit()
    return self.exit_screen
end

-- Handle events.
--
-- If you handled it, return true; false means the event continues on to the
-- next handler.
function CreditsScreen:handle(event)
    if event.keys['escape'] or event.button then
        self.exit_screen = true
        return true
    end

    return ScreenBase.handle(self, event)
end

return CreditsScreen
