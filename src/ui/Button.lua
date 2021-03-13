-- Skelly UI - Button
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

-- From Experiment 9:

local Button = Class('Button')

function Button:initialize(x, y, text, resources, font)
    self.x = x
    self.y = y
    self.text = text
    self.font = font

    -- All these magic numbers are gross. Should pass texture/quad instead.
    self.ui_texture = resources.images.ui_rpg
    self.button_normal   = love.graphics.newQuad(  0, 282, 190, 49, self.ui_texture)
    self.button_selected = love.graphics.newQuad(  0, 237, 190, 45, self.ui_texture)

    local _, _, w, h = self.button_normal:getViewport()
    self.width = w
    self.height = h

    self.text_width = self.font:getWidth(self.text)
    self.text_height = self.font:getHeight()
    self.text_x = (self.width - self.text_width) / 2 -- offset by x,y to draw
    self.text_y = (self.height - self.text_height) / 2

    self.selected = false
    self.intersected = false

    -- Event handlers
    self.onClick = nil
end

function Button:draw()
    love.graphics.setColor(1, 1, 1, 1)
    love.graphics.setFont(self.font)

    if self.selected then
        love.graphics.draw(self.ui_texture, self.button_selected, self.x, self.y)
    else
        love.graphics.draw(self.ui_texture, self.button_normal, self.x, self.y)
    end

    love.graphics.setColor(0, 0, 0, 1)
    love.graphics.print(self.text, self.x + self.text_x, self.y + self.text_y)

    if self.intersected then
        love.graphics.setColor(0, 1, 0, 1) -- green
        love.graphics.rectangle('line', self.x - 1, self.y - 1, self.width + 2, self.height + 2)
    end
end

function Button:intersects(x, y)
    -- Does x,y intersect with the button?
    if x < self.x or y < self.y then
        return false
    end

    if x > self.x + self.width or y > self.y + self.height then
        return false
    end

    return true
end

function Button:onMouseMove(x, y)
    if not self:intersects(x, y) then
        self.intersected = false
        return
    end

    self.intersected = true
end

function Button:onMousePress(x, y)
    if not self:intersects(x, y) then
        return
    end

    -- We're ignoring the button, click with anything.
    self.selected = true

    if self.onClick then
        self:onClick()
    end
end

function Button:onMouseRelease(x, y)
    if not self:intersects(x, y) then
        return
    end

    -- We're ignoring the button, click with anything.
    self.selected = false
end

return Button
