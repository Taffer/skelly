-- Skelly "New Game" screen.
--
-- This handles the "Create a character" UI, then passes you off to the Intro.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIScreenBase = require 'src/screens/UIScreenBase'

local Map = require 'src/Map'
local Viewport = require 'src/Viewport'

local function draw_29x21(screen_width, screen_height)
    love.graphics.setColor(0, 1, 0, 1)
    dx = 8
    dy = 8
    for y = 0, 20 do
        for x = 0, 28 do
            love.graphics.rectangle('line', dx + x * 32, dy + y * 32, 32, 32)
        end
    end

    love.graphics.setColor(1, 0, 0, 1)
    love.graphics.rectangle('fill', dx, dy + 21 * 32, 29 * 32, screen_height - 21 * 32 - dy * 2)

    love.graphics.setColor(0, 0, 1, 1)
    love.graphics.rectangle('fill', 29 * 32 + dx * 2, dy, screen_width - 29 * 32 - dx * 3, screen_height - dy * 2)
end

local NewGameScreen = Class('NewGameScreen', UIScreenBase)

function NewGameScreen:initialize(resources, state)
    UIScreenBase.initialize(self, resources, state)
    self:setNextScreen('Intro')

    -- UI for creating a new character:
    --
    -- Name: [some reasonable length, default: Skelly]
    --
    -- Stats created (you don't get to pick):
    --
    -- Calcium: 25?
    -- Willpower: 25?

    print('Yo, got any of them maps?')
    for k, v in pairs(gameResources.maps) do
        print('MAP:', k, v)
    end

    self.map = Map:new(gameResources, gameResources.maps.scene1_farm)
    self.viewport = Viewport:new(self.map.width, self.map.height, 0, 0, 29, 21)
end

function NewGameScreen:draw()
    local gameState = gameState

    love.graphics.clear(0, 0, 0, 1)
    draw_29x21(gameState.scr_width, gameState.scr_height)

    self.map:render(self.viewport, self.map.tile_layers[1], 8, 8)
    self.map:render(self.viewport, self.map.tile_layers[2], 8, 8)
end

-- Check for input events.
function NewGameScreen:checkInputs(keybord, mouse, gamepad)
    if keyboard['escape'] or mouse['1'] or gamepad['a'] then
        self:setExit()
    end
end

return NewGameScreen
