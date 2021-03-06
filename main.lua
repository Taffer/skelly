-- Skelly, a story of the Skeleton War
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local settings_filename = 'settings.bin'

local bitser = require 'lib/bitser/bitser'

-- All the stuff we've loaded already.
gameResources = {
    fonts = {
        -- default_mono: LiberationMono-Bold 16-pixel (presents)
        -- default_serif: A_Font_with_Serifs 72-pixel (presents)
        -- skelly_title: Gypsy Curse 144-pixel (title)
    },
    images = {
        -- love_logo: love-game-0.10 (presents)
        -- skelly_title: Gersdorff_Feldbuch_skeleton (title)
        -- taffer: taffer-sketch (title)
    },
    music = {
        -- theme: Heroic Demise (New) (presents)
    },
    sounds = {},
    text = {
        -- all translatable text (presents)
    },

    screens = { -- Separate from state, we can be in Pause on top of a screen.
        placeholder = require 'src/screens/PlaceholderScreen', -- place holder

        presents = require 'src/screens/PresentsScreen', -- Splash screen
        title_loading = require 'src/screens/TitleScreen' -- Title/loading
    },

    states = {}
}

-- Current state of the game.
gameState = {
    screen = nil, -- Currently displayed screen.
    next_screen = '', -- Which screen is next?

    -- Player settings
    settings = {}
}

-- Serialize/deserialize settings.
local function load_settings(name)
    local binary_data, size = love.filesystem.read(name)
    if binary_data then
        gameState.settings = bitser.loads(binary_data)
    else
        print('Error reading settings file: ' .. size)

        gameState.settings = {
            -- Default settings.
            music_volume = 1.0,

            language = 'en'
        }
    end
end

local function save_settings(name, table)
    local binary_data = bitser.dumps(table)
    local success, message = love.filesystem.write(name, binary_data)
    if not success then
        print('Error writing settings file: ' .. message)
    end
end

-- Love callbacks.
function love.load()
    math.randomseed(os.time())

    love.graphics.setDefaultFilter('nearest', 'nearest')

    io.stdout:setvbuf("no") -- Don't buffer console output.

    -- Load settings if they exist. If not, create defaults.
    load_settings(settings_filename)

    -- Minimal loading screen.
    gameState.screen = gameResources.screens.presents:new(gameResources)
    gameState.next_screen = 'title'
end

function love.draw()
    gameState.screen:draw()
end

function love.update(dt)
    gameState.screen:update(dt)

    -- Screen state machine:
    --
    -- presents -> title -> journey -> exit
    --                             \-> newgame -> intro -> game
    --                             \-------------------/
    if gameState.screen:exit() then
        if gameState.next_screen == 'title' then
            gameState.screen = gameResources.screens.title_loading:new(gameResources)
            gameState.next_screen = 'placeholder'
        elseif gameState.next_screen == 'placeholder' then
            gameState.screen = gameResources.screens.placeholder:new(gameResources)
            gameState.next_screen = 'there is no next screen'
        else
            save_settings(settings_filename, gameState.settings)
            love.audio.stop()
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
