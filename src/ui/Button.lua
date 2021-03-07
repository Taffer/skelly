-- Skelly UI - Button
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local Button = Class('Button')

function Button:initialize(resources, font, text, x, y)
    self.resources = resources

    self.ui = self.resources.images.ui_rpg
    self.font = font
    self.text = text
    self.x = x
    self.y = y

    -- All these magic numbers are gross.
    self.quad_up   = love.graphics.newQuad(  0, 282, 190, 49, self.ui)
    self.quad_down = love.graphics.newQuad(  0, 237, 190, 45, self.ui)

    -- These are relative to x,y, not absolute.
    self.text_x = (190 - self.font:getWidth(self.text)) / 2
    self.text_y = (45 - self.font:getHeight()) / 2

    self.selected = false
end

function Button:draw()
    love.graphics.setFont(self.font)

    if self.selected then
        love.graphics.setColor(1, 1, 1, 1) -- white
        love.graphics.draw(self.ui, self.quad_down, self.x, self.y + 4)
        love.graphics.setColor(0, 0, 0, 1) -- black
        love.graphics.print(self.text, self.x + self.text_x, self.y + 4 + self.text_y)
    else
        love.graphics.setColor(1, 1, 1, 1) -- white
        love.graphics.draw(self.ui, self.quad_up, self.x, self.y)
        love.graphics.setColor(0, 0, 0, 1) -- black
        love.graphics.print(self.text, self.x + self.text_x, self.y + self.text_y)
    end
end

return Button
