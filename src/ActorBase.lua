-- Skelly Actor base class.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local ActorBase = Class('ActorBase')
function ActorBase:initialize(sprite, default_behaviour, map, x, y)
    self.sprite = sprite
    self.default_behaviour = default_behaviour
    self.current_behaviour = default_behaviour
    self.map = map
    self.x = x
    self.y = y
end

function ActorBase:update(dt)
    local animation = nil
    local facing = nil
    if self.current_behaviour then
        self.current_behaviour = self.current_behaviour:update(dt)
        animation = self.current_behaviour:getAnimation()
        facing = self.current_behaviour:getFacing()
    else
        self.default_behaviour:update(dt)
        animation = self.default_behaviour:getAnimation()
        facing = self.default_behaviour:getFacing()
    end

    self.sprite:setAnimation(animation)
    self.sprite:update(dt)
end

function ActorBase:draw(x, y)
    self.sprite:draw(x, y)
end

return ActorBase
