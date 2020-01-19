-- Skelly, a story of the Skeleton War
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

gameState = {
    fonts = {}
}

-- Love callbacks.
function love.load()
    math.randomseed(os.time())

    love.graphics.setDefaultFilter('nearest', 'nearest')

    -- Load the minimum required to provide some sort of loading screen,
    -- where we'll do the actual loading.
    gameState.fonts.default = love.graphics.newFont('graphics/A_Font_with_Serifs.ttf', 32)
end

function love.draw()
    love.graphics.setFont(gameState.fonts.default)
    love.graphics.setColor(0, 1, 0, 1)
    love.graphics.print('Insert game here.', 5, 5)
end
