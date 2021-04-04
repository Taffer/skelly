-- Skelly LPC Sprite for animation.
--
-- This sets up a set of sprites, quads, etc. using the standard Liberated
-- Pixel Cup sprite format:
--
-- https://lpc.opengameart.org/static/lpc-style-guide/styleguide.html
--
-- Specifically:
-- * Each row is a complete animation cycle.
-- * Rows are mostly in groups of four based on facing = away, left, forward,
--   right.
-- * Animation rows are: Spellcast, Thrust, Walk, Slash, Shoot, Hurt (only one
--   facing for Hurt). We fake an Idle animation by cloning the first frame of
--   Walk.
-- * Are 64x64 on the sprite sheet.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local ANIMATION = require 'src/LPCAnimations'
local FACING = require 'src/LPCFacings'

-- Quads singleton, hopefully.
--
-- quads[animation][facing][frame] is an actual quad.
local lpcSpriteQuads = nil -- Quads singleton

local LPCSprite = Class('LPCSprite')
function LPCSprite:initialize(texture, framerate)
    self.facings = {}
    self.facings[FACING.AWAY]    = 1
    self.facings[FACING.LEFT]    = 2,
    self.facings[FACING.FORWARD] = 3,
    self.facings[FACING.RIGHT]   = 4
    self.facing_order = {FACing.away, Facing.left, Facing.forward, Facing.right}

    self.animations = {}
    self.animations[ANIMATION.SPELLCAST] = 1
    self.animations[ANIMATION.THRUST]    = 2
    self.animations[ANIMATION.WALK]      = 3
    self.animations[ANIMATION.SLASH]     = 4
    self.animations[ANIMATION.SHOOT]     = 5
    self.animations[ANIMATION.HURT]      = 6
    self.animations[ANIMATION.IDLE]      = 7
    self.animation_order = {ANIMATION.SPELLCAST, ANIMATION.THRUST, ANIMATION.WALK, ANIMATION.SLASH, ANIMATION.SHOOT, ANIMATION.HURT,
        ANIMATION.IDLE}

    self.frames = {}
    self.frames[ANIMATION.SPELLCAST] =  7
    self.frames[ANIMATION.THRUST]    =  8
    self.frames[ANIMATION.WALK]      =  9
    self.frames[ANIMATION.SLASH]     =  6
    self.frames[ANIMATION.SHOOT]     = 13
    self.frames[ANIMATION.HURT]      =  6
    self.frames[ANIMATION.IDLE]      =  1

    self.width = 64 -- Standard for LPC sprite sheets.
    self.height = 64

    self.feet_x = self.width / 2 -- Where are the feet relative to 0,0?
    self.feet_y = self.height - 2

    self.framerate = framerate or 0.1 -- Too slow for default?
    self.ticks = 0

    self.facing = FACING.FORWARD -- Default facing and animation.
    self.animation = ANIMATION.WALK
    self.frame = 1

    self.texture = texture
    if lpcSpriteQuads == nil then
        self:generateQuads()
    end
    self.quads = lpcSpriteQuads
end

function LPCSprite:generateQuads()
    lpcSpriteQuads = {}

    local y = 0
    for _, av in ipairs(self.animation_order) do
        lpcSpriteQuads[av] = {}

        if av ~= ANIMATION.HURT and av ~= ANIMATION.IDLE then
            for _, fv in ipairs(self.facing_order) do
                lpcSpriteQuads[av][fv] = {}

                for i = 1, self.frames[av] do
                    local x = (i - 1) * self.width
                    table.insert(lpcSpriteQuads[av][fv], love.graphics.newQuad(x, y, self.width, self.height, self.texture))
                end

                y = y + self.height
            end
        end
    end

    -- 'hurt' has to be special-cased because it only has one facing.
    y = self.texture:getHeight() - self.height
    for _, fv in ipairs(self.facing_order) do
        -- We'll lie and re-use these for all four facings.
        lpcSpriteQuads[ANIMATION.HURT][fv] = {}
    end
    for i = 1, self.frames[ANIMATION.HURT] do
        local x = (i - 1) * self.width
        local quad = love.graphics.newQuad(x, y, self.width, self.height, self.texture)
        for _, fv in ipairs(self.facing_order) do
            table.insert(lpcSpriteQuads[ANIMATION.HURT][fv], quad)
        end
    end

    -- 'idle' is a fake state that's just the first 'walk' frame.
    for _, fv in ipairs(self.facing_order) do
        lpcSpriteQuads[ANIMATION.IDLE][fv] = lpcSpriteQuads[ANIMATION.WALK][fv]
    end
end

function LPCSprite:checkFrame()
    if self.frame > self.frames[self.animation] then
        self.frame = 1
    end
end

function LPCSprite:nextFrame()
    self.frame = self.frame + 1
    self:checkFrame()
end

function LPCSprite:setFacing(facing)
    self.facing = facing
    self:checkFrame()
end

function LPCSprite:setAnimation(animation)
    self.animation = animation
    self:checkFrame()
end

function LPCSprite:getQuad()
    return self.quads[self.animation][self.facing][self.frame]
end

function LPCSprite:update(dt)
    self.ticks = self.ticks + dt
    if self.ticks > self.framerate then
        self:nextFrame()
        self.ticks = self.ticks - self.framerate
    end
end

function LPCSprite:draw(x, y)
    love.graphics.setColor(1, 1, 1, 1)
    love.graphics.draw(self.texture, self:getQuad(), x, y)
end

return LPCSprite
