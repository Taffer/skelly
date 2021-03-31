-- Skelly "Intro" screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIScreenBase = require 'src/screens/UIScreenBase'

local IntroScreen = Class('NewGameScreen', UIScreenBase)

function IntroScreen:initialize(resources, state)
    UIScreenBase.initialize(self, resources, state)
    self:setNextScreen('Game')

    -- Intro animated:
    --
    -- Scene: 1 - Farm, viewport bottom-left
    --  Enter: skeletons, walking along army_path_[1-4], exits
    --  Enter: necromancer, walking necro_path_[1-4]
    --  Animate: necromancer summons the skellies, RISE FROM YOUR GRAVE
    --  Animate: spawn_loc_[1-3] - ground disturbed, skellies spawn, walk to
    --      army_path_2 then follow army_path
    --  Animate: necromancer walks necro_path_[5-9], exits
    --
    -- Skeleton hoard continues for a bit. After they're all passed:
    --
    --  Enter: cute bunny, hops around for a bit, leaves
    --  Pan: viewport pans to top-left, more ambient nature/farm
    --  Animate: spawn_skelly - ground disturbed, Skelly spawns
    --  Animate: Skelly looks around, is confused?
    --
    -- Transition to Game
end

-- Check for input events.
function IntroScreen:checkInputs(keybord, mouse, gamepad)
    if keyboard['escape'] or mouse['1'] or gamepad['a'] then
        self:exit()
    end
end

return IntroScreen
