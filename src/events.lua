-- Skelly events.
--
-- These are game events, not UI events. Input comes in via keyboard, mouse,
-- joystick, buttons, etc. and is converted into events by the game's UI.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local Event = Class('Event')

-- Constructor
function Event:initialize(action, source, target)
    if not Event.Action[action] then
        action = Event.Action.__INVALID__
    end

    self.action = action -- One of the Event.Actions
    self.source = source -- The entity who caused this Event.
    self.target = target -- The entity the Event targeted (or nil).
end

-- Defined actions.
Event.static.Action = {
    ATTACK = 'attack', -- Attack an Entity.
    LOOK = 'look',     -- Look at at Entity.
    USE = 'use',       -- Interact with an Entity. Talk, Board, etc.
    WALK = 'walk',     -- Walk; the Entity will be a direction? Or the tile in the specified direction?

    -- Special value used to indicate an invalid Event.
    __INVALID__ = 'invalid'
}

return Event
