-- Skelly "New Game" screen.
--
-- This handles the "Create a character" UI, then passes you off to the Intro.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIScreenBase = require 'src/screens/UIScreenBase'

local LPCSprite = require 'src/LPCSprite'
local Map = require 'src/Map'
local SkeletonActor = require 'src/SkeletonActor'
local Viewport = require 'src/Viewport'

-- =============================================================================
-- Prototype UI locations, not for human consumption.
-- =============================================================================
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

-- =============================================================================
-- Sloppy animation classes
-- =============================================================================
local PanViewport = Class('PanViewport')
function PanViewport:initialize(viewport)
    self.viewport = viewport
    self.ticks = 0
    self.done = false

    self.step = 0.2 -- Tick every 0.2 seconds
end

function PanViewport:update(dt, _)
    self.ticks = self.ticks + dt
    if self.ticks > self.step then
        self.ticks = self.ticks - self.step

        local x = self.viewport.x
        local y = self.viewport.y + 1
        self.viewport:setPosition(x, y)

        if self.viewport.y ~= y then
            self.done = true
        end
    end
end

function PanViewport:draw()
    -- Do nothing.
end

local WaitFor = Class('WaitFor')
function WaitFor:initialize(length)
    self.length = length
    self.ticks = 0
    self.done = false
end

function WaitFor:update(dt, _)
    self.ticks = self.ticks + dt
    if self.ticks > self.length then
        self.done = true
    end
end

function WaitFor:draw()
    love.graphics.setColor(1, 1, 1, 0)
    love.graphics.print(string.format('%d: %d', self.ticks, self.length))
end

local WalkTo = Class('WalkTo')
function WalkTo:initialize(sprite, sprite_locs, viewport)
    self.locs = sprite_locs
    self.x = self.locs[1][1] - viewport.x * 32
    self.y = self.locs[1][2] - viewport.y * 32
    self.target_idx = math.min(2, #self.locs)

    self.target_x = self.locs[self.target_idx][1] - viewport.x * 32
    self.target_y = self.locs[self.target_idx][2] - viewport.y * 32

    self.actor = SkeletonActor:new(sprite)
    self.actor.sprite:setFacing('right')
    self.actor.sprite:setAnimation('walk')

    self.step = 0.01
    self.ticks = 0

    self.on_screen = true
end

function WalkTo:update(dt, viewport)
    self.ticks = self.ticks + dt
    if self.ticks > self.step then
        self.ticks = self.ticks - self.step

        if self.x < self.target_x then
            self.x = self.x + 1
        end
        if self.x > self.target_x then
            self.x = self.x - 1
        end
        if self.y < self.target_y then
            self.y = self.y + 1
        end
        if self.y > self.target_y then
            self.y = self.y - 1
        end

        if self.x == self.target_x and self.y == self.target_y then
            self.target_idx = math.min(self.target_idx + 1, #self.locs)
            self.target_x = self.locs[self.target_idx][1] - viewport.x * 32
            self.target_y = self.locs[self.target_idx][2] - viewport.y * 32
        end
    end

    self.actor:update(dt)
end

function WalkTo:draw()
    if self.on_screen then
        self.actor:draw(self.x, self.y)
    end
end

-- =============================================================================
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

    self.map = Map:new(gameResources, gameResources.maps.scene1_farm)
    self.viewport = Viewport:new(self.map.width, self.map.height, 0, 0, 29, 21)

    self.skeleton_sprite = LPCSprite:new(gameResources.images.skeleton_sprite)
    self.sprite_locs = {
        {   5, 617},
        { 577, 610},
        { 913, 489},
        {1020, 480},
    }

    self.ani = {
        WaitFor:new(2), -- Wait for 2 seconds
        PanViewport:new(self.viewport), -- Pan to the bottom
        -- Walk a skeleton from army_path_1 to army_path_2. These will need to
        -- be converted from map co-ords to screen co-ords.
        WalkTo:new(self.skeleton_sprite, self.sprite_locs, self.viewport)
    }
    self.ani_idx = 1
end

function NewGameScreen:draw()
    local gameState = gameState

    love.graphics.clear(0, 0, 0, 1)
    draw_29x21(gameState.scr_width, gameState.scr_height)

    self.map:render(self.viewport, self.map.tile_layers[1], 8, 8)
    self.map:render(self.viewport, self.map.tile_layers[2], 8, 8)

    self.ani[self.ani_idx]:draw()
end

function NewGameScreen:update(dt)
    if self.ani_idx <= #self.ani then
        self.ani[self.ani_idx]:update(dt, self.viewport)

        if self.ani[self.ani_idx].done then
            self.ani_idx = self.ani_idx + 1
        end
    end
end

-- Check for input events.
function NewGameScreen:checkInputs(keyboard, mouse, gamepad)
    if keyboard['escape'] or mouse[1] or gamepad['a'] then
        self:setExit()
    end
end

return NewGameScreen
