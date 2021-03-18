-- Skelly, a story of the Skeleton War
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local bitser = require 'lib/bitser/bitser'
local UIEvent = require 'src/ui/UIEvent'

local settings_filename = 'settings.bin'

-- All the stuff we've loaded already.
gameResources = {
    fonts = {
        -- default_mono: LiberationMono-Bold 16-pixel (Presents)
        -- default_serif: A_Font_with_Serifs 72-pixel (Presents)
        -- skelly_title: Gypsy Curse 144-pixel (Title)
        --
        -- Everything else is loaded in Title by the loader.
    },
    images = {
        -- love_logo: love-game-0.10 (Presents)
        -- skelly_title: Gersdorff_Feldbuch_skeleton (Title)
        -- taffer: taffer-sketch (Title)
        --
        -- Everything else is loaded in Title by the loader.
    },
    music = {
        -- theme: Heroic Demise (New) (Presents)
        --
        -- Everything else is loaded in Title by the loader.
    },
    sounds = {
        -- Everything is loaded in Title by the loader.
    },
    text = {
        -- all translatable text (presents, see src/i18n)
    },

    maps = {
        -- all Tiled maps
    },

    screens = { -- Separate from state, we can be in Pause on top of a screen.
        placeholder = require 'src/screens/PlaceholderScreen', -- place holder

        journey = require 'src/screens/JourneyScreen', -- Journey Onward
        presents = require 'src/screens/PresentsScreen', -- Splash screen
        title_loading = require 'src/screens/TitleScreen', -- Title/loading
        credits = require 'src/screens/CreditsScreen', -- Credits
        settings = require 'src/screens/SettingsScreen', -- Settings
    },

    overlays = { -- UI overlays that can be drawn on "any" screen.
        settings = require 'src/ui/SettingsOverlay', -- Settings UI
    },

    states = {}
}

-- Current state of the game.
gameState = {
    screen = nil, -- Currently displayed screen.

    -- Player settings
    settings = {},

    -- Display screen dimensions
    scr_width = 0,
    scr_height = 0,
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

    gameState.scr_width = love.graphics.getWidth()
    gameState.scr_height = love.graphics.getHeight()

    -- Load settings if they exist. If not, create defaults.
    load_settings(settings_filename)

    -- Minimal loading screen.
    gameState.screen = gameResources.screens.presents:new(gameResources, gameState)
end

function love.draw()
    gameState.screen:draw()
end

-- Presents isn't in the lookup table because we never switch to it, it's
-- only a starting point.
local ScreenLookup = {
    Title = gameResources.screens.title_loading,
    Journey = gameResources.screens.journey,
    Credits = gameResources.screens.credits,

    Placeholder = gameResources.screens.placeholder -- not a real screen
}

function love.update(dt)
    gameState.screen:update(dt)

    -- Screen state machine:
    --
    -- Presents -> Title -> Journey -> exit
    --                             \-> Newgame -> Intro -> Game
    --                             \-------------------/
    --
    local lookup = ScreenLookup
    if gameState.screen:exit() then
        local next_screen = gameState.screen:getNextScreen()
        if next_screen then
            gameState.screen = lookup[next_screen]:new(gameResources, gameState)
        else
            save_settings(settings_filename, gameState.settings)
            love.audio.stop()
            love.event.quit()
        end
    end
end

-- Event generation.
function love.keypressed(key)
    local event = UIEvent:new({keydown = key})

    if gameState.screen:handle(event) == false then
        print('Unhandled key press event.')
    end
end

function love.keyreleased(key)
    local event = UIEvent:new({keyup = key})

    if gameState.screen:handle(event) == false then
        print('Unhandled key release event.')
    end
end

function love.mousereleased(x, y, button, is_touch, presses)
    local event = UIEvent:new({mouseup = button, x = x, y = y, touch = is_touch, presses = presses})

    if gameState.screen:handle(event) == false then
        print('Unhandled mouse release event.')
    end
end
