-- Skelly, a story of the Skeleton War
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local DEBUG = false

local lovebird = nil
if DEBUG then
    lovebird = require 'lib/lovebird'
end

local GameSettings = require 'src/Settings'

local settings_filename = 'settings.ini'

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
        new_game = require 'src/screens/NewGameScreen', -- New Game
        intro = require 'src/screens/IntroScreen', -- Intro
    },

    overlays = { -- UI overlays that can be drawn on "any" screen.
        settings = require 'src/ui/SettingsOverlay', -- Settings UI
    },

    states = {}
}

-- Current state of the game.
gameState = {
    screen = 'nil', -- Currently displayed screen.

    -- Player settings
    settings = nil,

    -- Display screen dimensions
    scr_width = 0,
    scr_height = 0,

    -- Character
    character = {
        name = 'Skelly',
        sex = 'Unknown',
        sex_pref = 'None',
        calcium = 25, -- = 0, you are dead
        willpower = 25, -- spend to come back to life
    }
}

-- Serialize/deserialize settings.
local function load_settings(name)
    local defaults = {
        -- Default settings.
        music_volume = 1.0,
        sfx_volume = 1.0,
        voice_volume = 1.0,
        overall_volume = 1.0,

        language = 'en'
    }

    gameState.settings = GameSettings(name, defaults)
end

local function save_settings()
    gameState.settings:save()
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
    Settings = gameResources.screens.settings,
    NewGame = gameResources.screens.new_game,
    Intro = gameResources.screens.intro,

    Placeholder = gameResources.screens.placeholder, -- not a real screen
    Game = gameResources.screens.placeholder, -- not a real screen
}

function love.update(dt)
    if lovebird then
        lovebird.update()
    end

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
            save_settings()
            love.audio.stop()
            love.event.quit()
        end
    end
end

-- Event generation.
function love.keypressed(key, scancode, isRepeat)
    gameState.screen:handleKeyPress(key, scancode, isRepeat)
end

function love.keyreleased(key, scancode)
    gameState.screen:handleKeyRelease(key, scancode)
end

function love.mousemoved(x, y, dx, dy, isTouch)
    gameState.screen:handleMouseMoved(x, y, dx, dy, isTouch)
end

function love.mousepressed(x, y, button, isTouch, presses)
    gameState.screen:handleMousePress(x, y, button, isTouch, presses)
end

function love.mousereleased(x, y, button, isTouch, presses)
    gameState.screen:handleMouseRelease(x, y, button, isTouch, presses)
end
