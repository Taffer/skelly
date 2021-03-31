-- Skelly settings overlay.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local OverlayBase = require 'src/ui/OverlayBase'

local Button = require 'src/ui/Button'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'
local Spinner = require 'src/ui/Spinner'

-- =============================================================================
local SettingsOverlay = Class('SettingsOverlay', OverlayBase)
function SettingsOverlay:initialize(resources, x, y, width, height)
    OverlayBase.initialize(self, x, y, width, height)

    -- Add components.
    --
    -- Current settings include:
    --
    -- * Language: English or Español.
    -- * Volume: 0 - 100
    -- * Effects Volume: 0 - 100
    -- * Music Volume: 0 - 100
    -- * Voice Volume: 0 - 100
    -- * [Cancel] [Apply]
    --
    -- All need a spin box:  <| text |>
    -- With more localizations, we'll need a pop-up menu or radio buttons.
    self.texture = resources.images.ui_rpg

    local spinner_quads = {
        love.graphics.newQuad(303, 486, 22, 21, self.texture), -- "Decrease"
        love.graphics.newQuad(171, 486, 22, 21, self.texture), -- "Increase"
        love.graphics.newQuad(0, 237, 190, 45, self.texture), -- Background
    }

    self.language_label = Label:new(x, y + 5, 'Language:', resources.fonts.button_font, {1, 1, 1, 1}, 'right')
    self.language_spinner = Spinner:new(x, y + 5, {'English', 'Español'}, 1, resources.fonts.button_font, {1, 1, 1, 1},
        self.texture, spinner_quads)
    self:addElement('language_label', self.language_label)
    self:addElement('language_spinner', self.language_spinner)

    local one_hundred = {0} -- very inefficient...
    for i = 1, 100 do
        table.insert(one_hundred, i)
    end
    self.volume_label = Label:new(x, y + 50, 'Overall Volume:', resources.fonts.button_font, {1, 1, 1, 1}, 'right')
    self.volume_spinner = Spinner:new(x, y + 50, one_hundred, #one_hundred, resources.fonts.button_font, {1, 1, 1, 1},
        self.texture, spinner_quads)
    self:addElement('volume_label', self.volume_label)
    self:addElement('volume_spinner', self.volume_spinner)

    self.effects_volume_label = Label:new(x, y + 100, 'Effects Volume:', resources.fonts.button_font, {1, 1, 1, 1}, 'right')
    self.effects_volume_spinner = Spinner:new(x, y + 100, one_hundred, #one_hundred, resources.fonts.button_font,
        {1, 1, 1, 1}, self.texture, spinner_quads)
    self:addElement('fx_volume_label', self.effects_volume_label)
    self:addElement('fx_volume_spinner', self.effects_volume_spinner)

    self.music_volume_label = Label:new(x, y + 150, 'Music Volume:', resources.fonts.button_font, {1, 1, 1, 1}, 'right')
    self.music_volume_spinner = Spinner:new(x, y + 150, one_hundred, #one_hundred, resources.fonts.button_font,
        {1, 1, 1, 1}, self.texture, spinner_quads)
    self:addElement('music_volume_label', self.music_volume_label)
    self:addElement('music_volume_spinner', self.music_volume_spinner)

    self.voice_volume_label = Label:new(x, y + 200, 'Voice Volume:', resources.fonts.button_font, {1, 1, 1, 1}, 'right')
    self.voice_volume_spinner = Spinner:new(x, y + 200, one_hundred, #one_hundred, resources.fonts.button_font,
        {1, 1, 1, 1}, self.texture, spinner_quads)
    self:addElement('vox_volume_label', self.voice_volume_label)
    self:addElement('vox_volume_spinner', self.voice_volume_spinner)
end

return SettingsOverlay
