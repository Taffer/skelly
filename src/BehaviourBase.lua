-- Skelly Behaviour base class.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local BehaviourBase = Class('BehaviourBase')
function BehaviourBase:initialize(next_behaviour)
    self.next_behaviour = next_behaviour
    self.animation = 'idle'
    self.facing = 'forward'

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
