-- Skelly, a story of the Skeleton War
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.


-- All the stuff we've loaded already.
gameResources = {
    fonts = {},
    images = {},
    screens = { -- Separate from state, we can be in Pause on top of a screen.
        loading = require 'src/screens/loading', -- place holder

        presents = require 'src/screens/presents' -- Splash screen
    },
    states = {}
}

-- Current state of the game.
gameState = {
    screen = nil, -- Currently displayed screen.
    next_screen = '' -- Which screen is next?
}

-- Love callbacks.
function love.load()
    math.randomseed(os.time())

    love.graphics.setDefaultFilter('nearest', 'nearest')

    -- Minimal loading screen.
    gameState.screen = gameResources.screens.presents:new(gameResources)
    gameState.next_screen = 'loading'
end

function love.draw()
    gameState.screen:draw()
end

function love.update(dt)
    gameState.screen:update(dt)

    if gameState.screen:exit() then
        if gameState.next_screen == 'loading' then
            gameState.screen = gameResources.screens.loading:new(gameResources)
            gameState.next_screen = 'there is no next screen'
        else
            love.event.quit()
        end
    end
end

-- Event generation.
function love.keyreleased(key)
    print('A key is released: ' .. key)
    if gameState.screen:handle(key) == false then
        print('Unhandled key.')
    end
end
