-- Skelly UI element: text label
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

-- Label class
local Label = Class('Label', UIBase)

function Label:initialize(x, y, text, font, colour, align)
    self.orig_x = x
    self.y = y
    self.text = text
    self.font = font
    self.colour = colour
    self.align = align

    self.width = font:getWidth(self.text)
    self.height = font:getHeight() * font:getLineHeight()

    -- Default is left-align, doesn't require any additional work.
    if align == 'right' then
        self.x = self.x - self.width
    elseif align == 'centre' then
        self.x = self.x - self.width / 2
    end
end

function Label:draw()
    love.graphics.setColor(unpack(self.colour))
    love.graphics.setFont(self.font)
    love.graphics.print(self.text, self.x, self.y)
end

function Label:setText(text)
    self.text = text
    self.width = self.font:getWidth(self.text)

    if align == 'right' then
        self.x = self.orig_x - self.width
    elseif align == 'centre' then
        self.x = self.orig_x - self.width / 2
    end
end
