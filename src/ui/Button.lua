-- Skelly UI - Button
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIBase = require 'src/ui/UIBase'

local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'

-- From Experiment 9:

local Button = Class('Button', UIBase)

function Button:initialize(parent, x, y, texture, quad, text, font, color)
    UIBase.initialize(self, parent)

    self.x = x
    self.y = y

    self.imageButton = ImageButton:new(self, x, y, texture, quad)

    self.width = self.imageButton.width
    self.height = self.imageButton.height

    local label_x = x + self.imageButton.width / 2
    local label_y = y + (self.imageButton.height - font:getHeight() * font:getLineHeight()) / 2
    self.labelButton = Label:new(self, label_x, label_y, text, font, color, 'centre')
end

function Button:draw(color)
    self.imageButton:draw()
    self.labelButton:draw()

    if self.intersected then
        love.graphics.setColor(0, 1, 0, 1) -- green
        love.graphics.rectangle('line', self.x - 1, self.y - 1, self.width + 2, self.height + 2)
    end
end

return Button
