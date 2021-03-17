-- Skelly settings overlay.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local OverlayBase = require 'src/ui/OverlayBase'

local Button = require 'src/ui/Button'
local ImageButton = require 'src/ui/ImageButton'
local Spinner = require 'src/ui/Spinner'

local SettingsOverlay = Class('SettingsOverlay', OverlayBase)

function SettingsOverlay:initialize(resources, owner, x, y, width, height)
    OverlayBase.initialize(self, owner, x, y, width, height)

    -- Add components.
    --
    -- Current settings include:
    --
    -- * Language: English or Español.
    -- * Volume: 0 - 100
    --
    -- Both need a spin box:  <| text |>
    self.texture = resources.images.ui_rpg
    self.background_quad = love.graphics.newQuad(190, 100, 100, 100, self.texture)
    self.background_image = ImageButton:new(x, y, self.texture, self.background_quad)
    self:addInterface(self.background_image)

    self.language_label = Label:new(x, y, 'Language', font, colour, 'right')
    self.language_spinner = Spnner:new(x, y, {'English', 'Español'}, 1, font, colour, texture, quads)

    local one_hundred = {0} -- very inefficient...
    for i = 1, 100 do
        table.insert(one_hundred, i)
    end
    self.volume_label = Label:new(x, y, 'Volume', font, colour, 'right')
    self.volume_spinner = Spnner:new(x, y, one_hundred, #one_hundred, font, colour, texture, quads)
end

return SettingsOverlay
