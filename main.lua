-- Skelly, a story of the Skeleton War
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

-- All the stuff we've loaded already.
gameResources = {
    fonts = {},
    images = {},
    screens = { -- Separate from state, we can be in Pause on top of a screen.
        base = require 'src/screens/base',
        loading = require 'src/screens/loading'
    },
    states = {}
}

-- Current state of the game.
gameState = {
    screen = nil, -- Currently displayed screen.
    tick = 0
}

-- Love callbacks.
function love.load()
    math.randomseed(os.time())

    love.graphics.setDefaultFilter('nearest', 'nearest')

    -- Minimal loading screen.
    gameState.screen = gameResources.screens.loading:new(gameResources)
end

function love.draw()
    gameState.screen:draw()
end

-- Event generation.
function love.keypressed(key)
    print('A key is pressed: ' .. key)
    if gameState.screen:handle(key) == false then
        print('Unhandled key press.')
    end
end
