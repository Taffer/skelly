-- Skelly Behaviour base class.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local ANIMATION = require 'src/LPCAnimations'
local FACING = require 'src/LPCFacings'

local BehaviourBase = Class('BehaviourBase')
function BehaviourBase:initialize(next_behaviour)
    self.next_behaviour = next_behaviour
    self.animation = ANIMATION.IDLE
    self.facing = FACING.FORWARD

    self.done = false
end

function ActorBase:getAnimation()
    return self.animation
end

function ActorBase:getFacing()
    return self.facing
end

function ActorBase:update(dt)
    if self.done then
        return self.next_behaviour
    end

    return self
end

return BehaviourBase
