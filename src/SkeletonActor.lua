-- Skelly Skeleton actor for animation.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local ActorBase = require 'src/ActorBase'
local ANIMATION = require 'src/LPCAnimations'
local FACING = require 'src/LPCFacings'

local SkeletonActor = Class('SkeletonActor', ActorBase)
function SkeletonActor:initialize(sprite, behaviour, map, x, y)
    ActorBase.initialize(self, sprite, behaviour, map, x, y)
    self.sprite = sprite

    self.behaviour = behaviour
    self.map = map
    self.map_x = x
    self.map_y = y

    self.sprite:setAnimation(ANIMATION.IDLE)
    self.sprite:setFacing(FACING.FORWARD)
end

function SkeletonActor:update(dt)
    self.behaviour:update(dt)
    self.sprite:update(dt)
end

function SkeletonActor:draw(x, y)
    self.sprite:draw(x, y)
end

return SkeletonActor
