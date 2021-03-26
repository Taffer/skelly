-- Skelly "New Game" screen.
--
-- This handles the "Create a character" UI, then passes you off to the Intro.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local UIScreenBase = require 'src/screens/UIScreenBase'

local NewGameScreen = Class('NewGameScreen', UIScreenBase)

function NewGameScreen:initialize(resources, state)
    UIScreenBase.initialize(self, resources, state)
    self:setNextScreen('Intro')

    -- UI for creating a new character:
    --
    -- Name: [some reasonable length, default: Skelly]
    -- Sex: {choose: Male, Female, Unknown, Fluid, default: Unknown}
    -- Preference: {choose: Men, Women, None, Any, default: None}
    -- 3rd Person Pronoun: [some short length, default: It]
    -- Object Pronoun: [some short length, default: It]
    --
    -- Stats created (you don't get to pick):
    --
    -- Calcium: 25?
    -- Willpower: 25?
end

return NewGameScreen
