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

-- =============================================================================
-- Global variables
-- =============================================================================

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

    -- -------------------------------------------------------------------------
    -- Input device states
    -- -------------------------------------------------------------------------
    input_ticks = 0,
    keyboard = {
        -- Dict of key:state.
    },
    gamepad = {
        id = nil,
        -- Dict of axis:value.
        -- Dict of button:state.
    },
    mouse = {
        current_x = 0,
        current_y = 0,
        last_x = 0,
        last_y = 0,

        -- Dict of button:state
    },

    -- -------------------------------------------------------------------------
    -- Character
    -- -------------------------------------------------------------------------
    character = {
        name = 'Skelly',
        sex = 'Unknown',
        sex_pref = 'None',
        calcium = 25, -- = 0, you are dead
        willpower = 25, -- spend to come back to life
    }
}

-- =============================================================================
-- Game settings
-- =============================================================================

-- Serialize/deserialize settings.
local function load_settings(name)
    local defaults = {
        -- Default settings.
        music_volume = 1.0,
        sfx_volume = 1.0,
        voice_volume = 1.0,
        overall_volume = 1.0,

        input_frequency = 200, -- in milliseconds

        language = 'en'
    }

    gameState.settings = GameSettings(name, defaults)
end

local function save_settings()
    gameState.settings:save()
end

-- =============================================================================
-- Love callbacks.
-- =============================================================================

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

    local gameState = gameState
    local input_freq = gameState.settings:get('input_frequency')
    gameState.input_ticks = gameState.input_ticks + dt
    if gameState.input_ticks > input_freq then
        -- Generate input events.
        -- TODO: input events

        gameState.input_ticks = gameState.input_ticks - input_freq
    end

    gameState.screen:update(dt)

    -- Screen state machine:
    --
    -- Presents -> Title -> Journey -> exit
    --                             \-> Newgame -> Intro -> Game
    --                             \-------------------/
    --
    local lookup = ScreenLookup
    if gameState.screen:canExit() then
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

-- =============================================================================
-- Keyboard events
-- =============================================================================

function love.keypressed(_, scancode, _)
    -- Use scancode instead of key as it'll handle shift, etc. properly.
    -- Ignore isRepeat as we'll generate events ourselves.
    local keyboard = gameState.keyboard

    keyboard[scancode] = true
end

function love.keyreleased(_, scancode)
    local keyboard = gameState.keyboard

    keyboard[scancode] = false
end

-- =============================================================================
-- Mouse events
-- =============================================================================

function love.mousemoved(x, y, _, _, _)
    -- Ignore dx, dy for now, not sure if anything will need them (maybe pie
    -- menus?). Ignore isTouch because we don't care.
    local mouse = gameState.mouse

    mouse.last_x = mouse.current_x
    mouse.last_y = mouse.current_y
    mouse.current_x = x
    mouse.current_y = y
end

function love.mousepressed(x, y, button, _, _)
    -- Ignore isTouch and presses.
    --
    -- Not sure if you get mousemoved before this or not.
    love.mousemoved(x, y)

    local mouse = gameState.mouse
    mouse[button] = true
end

function love.mousereleased(x, y, button, _, _)
    -- Not sure if you get mousemoved before this or not.
    love.mousemoved(x, y)

    local mouse = gameState.mouse
    mouse[button] = false
end

function love.wheelmoved(x, y)
    love.mousemoved(x, y)
end

-- =============================================================================
-- Gamepad events
--
-- Gamepads other than the first one are ignored.
-- =============================================================================

function love.gamepadaxis(joystick, axis, value)
    local gamepad = gameState.gamepad

    if gamepad.id == nil then
        gamepad.id = joystick:getID()[1]
    end

    local this_id = joystick:getID()[1]
    if this_id == gamepad.id then
        gamepad[axis] = value
    end
end

function love.gamepadpressed(joystick, button)
    local gamepad = gameState.gamepad

    if gamepad.id == nil then
        gamepad.id = joystick:getID()[1]
    end

    local this_id = joystick:getID()[1]
    if this_id == gamepad.id then
        gamepad[button] = true
    end
end

function love.gamepadreleased(joystick, button)
    local gamepad = gameState.gamepad

    if gamepad.id == nil then
        gamepad.id = joystick:getID()[1]
    end

    local this_id = joystick:getID()[1]
    if this_id == gamepad.id then
        gamepad[button] = false
    end
end
