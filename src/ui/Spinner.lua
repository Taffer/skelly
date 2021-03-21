-- Skelly UI element: Value spinner
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIBase = require 'src/ui/UIBase'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'

-- Spinner class
local Spinner = Class('Label', UIBase)

function Spinner:initialize(parent, x, y, values, start_at, font, colour, texture, quads)
    UIBase.initialize(self, parent)

    self.x = x
    self.y = y
    self.values = values
    self.text = values[start_at] or values[1]
    self.font = font
    self.colour = colour
    self.texture = texture
    self.left_quad = quads[1] -- "Decrease" button
    self.right_quad = quads[2] -- "Increase" button
    self.label_quad = quads[3] -- Background for the label.

    if self.text == values[1] then
        self.index = 1
    else
        self.index = start_at
    end

    local vp_left = self.left_quad:getViewport() -- x, y, w, h
    local vp_right = self.right_quad:getViewport()
    local vp_label = self.label_quad:getViewport()

    -- We assume the text is small enough to fit into the label's area.
    self.width = vp_left[3] + vp_right[3] + vp_label[3]
    self.height = math.max(vp_left[4], vp_right[4], vp_label[4])

    local text_height = font:getHeight() * font:getLineheight()

    self.left_button = ImageButton:new(x, y, texture, self.left_quad)
    self.label = ImageButton:new(x + self.left_button.width, y, texture, self.label_quad)
    self.label_text = Label:new(label.x + label.width / 2, y + (self.label.height - text_height) / 2,
        self.text, self.font, self.colour, 'centre')
    self.right_button = ImageButton(self.label.x + self.label.width, y, texture, self.right_quad)

    -- Callbacks
    self.left_button.onClick = (function()
        self.index = self.index - 1
        if self.index < 1 then
            self.index = #self.values
        end

        self.text = self.values[self.index]
        self.label_text:setText(self.text)
    end)

    self.right_button.onClick = (function()
        self.index = self.index + 1
        if self.index > #self.values then
            self.index = 1
        end

        self.text = self.values[self.index]
        self.label_text:setText(self.text)
    end)
end

function Spinner:draw()
    self.left_button:draw()
    self.label:draw()
    self.label_text:draw()
    self.right_button:draw()
end

function Spinner:getIndex()
    return self.index
end

function Spinner:getValue()
    return self.text
end

return Spinner
