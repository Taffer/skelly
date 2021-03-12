-- Skelly credits screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'
local Button = require 'src/ui/Button'

local CreditsScreen = Class('CreditsScreen', ScreenBase)

local function next_credit(credits)
    local yield = coroutine.yield

    -- Top level of credits.
    for k, v in credits do
        yield(k)

        if type(v) == 'string' then
            yield(v)
        elseif type(v) == 'table' then
            for a, b in v do
                yield(a)

                if type(b) == 'string' then
                    yield(b)
                elseif type(b) == 'table' then
                    yield('<table>')
                end
            end
        end
    end
end

function CreditsScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Journey')

    self.skelly_text = self.resources.text.skelly_title
    self.subtitle_text = self.resources.text.title.subtitle_text
    self.credits = self.resources.text.journey.credits_table

    self.alpha = 0 -- Alpha level for the fade-in/out animation.
    self.ticks = 0
    self.pi_over_180 = math.pi / 180
    self.degrees_per_second = 45

    self.credits_area = {200, 250, 880, 450}

    self.font = self.resources.fonts.default_mono
    self.font_em = self.font:getWidth('M')
    self.font_lh = self.font:getHeight()

    -- One drawback to this is if you leave the credits running forever, it'll
    -- consume all RAM.
    self.buffer = {}
    self.buffer_idx = 1 -- draw buffer from here
    self.max_columns = math.floor(880 / self.font_em)
    self.max_lines = math.floor(450 / self.font_lh)
    self.lines_to_add = 0
    self.credits_routine = nil
end

-- Render this screen's contents.
function CreditsScreen:draw()
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

        while self.lines_to_add > 0.1 do
            local alive
            local credit
            if self.credits_routine then
                local resume = coroutine.resume
                alive, credit = resume(self.credits_routine, self.credits)
            else
                self.credits_routine = coroutine.create(next_credit)
            end

            if alive then
                table.insert(self.buffer, credit or 'nil')
            end
            self.lines_to_add = self.lines_to_add - 0.1
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
