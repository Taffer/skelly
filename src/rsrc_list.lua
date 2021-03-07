-- Skelly title/loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

-- List of all resources to load during the Loading... screen.
local resource_list = {
    fonts = {
        button_font = {size = 16, src = 'graphics/LiberationSerif-Bold.ttf'},
    },

    images = {
        -- I don't need all of these, but I haven't decided yet.
        ui_blue = 'graphics/kenney.nl/uipack/Spritesheet/blueSheet.png',
        ui_green = 'graphics/kenney.nl/uipack/Spritesheet/greenSheet.png',
        ui_grey = 'graphics/kenney.nl/uipack/Spritesheet/greySheet.png',
        ui_red = 'graphics/kenney.nl/uipack/Spritesheet/redSheet.png',
        ui_yellow = 'graphics/kenney.nl/uipack/Spritesheet/yellowSheet.png',

        ui_rpg = 'graphics/kenney.nl/uipack-rpg/Spritesheet/uipack_rpg_sheet.png',

        -- I might not need both of these.
        map_terrain = 'graphics/lpc-terrains/terrain-map-v7.png',
        map_sheet = 'graphics/lpc-terrains/terrain-v7.png',

        -- I should turn these into a sprite sheet.
        skelly_bone = 'graphics/skeleton/bone.png',
        skelly_die_left = 'graphics/skeleton/die_left.png',
        skelly_die_right = 'graphics/skeleton/die_right.png',
        skelly_idle_left = 'graphics/skeleton/idle_left.png',
        skelly_idle_right = 'graphics/skeleton/idle_right.png',
        skelly_throw_left = 'graphics/skeleton/throw_left.png',
        skelly_throw_right = 'graphics/skeleton/throw_right.png',
        skelly_walk_left = 'graphics/skeleton/walk_left.png',
        skelly_walk_right = 'graphics/skeleton/walk_right.png',
    },

    music = {
    },

    sounds = {
        -- Yes, I know these are in the wrong spot, I wanted to keep Kenney's
        -- UI Pack resources in one spot.
        ui_click1 = 'graphics/kenney.nl/uipack/Bonus/click1.ogg',
        ui_click2 = 'graphics/kenney.nl/uipack/Bonus/click2.ogg',
        ui_rollover1 = 'graphics/kenney.nl/uipack/Bonus/rollover1.ogg',
        ui_rollover2 = 'graphics/kenney.nl/uipack/Bonus/rollover2.ogg',
        ui_switch1 = 'graphics/kenney.nl/uipack/Bonus/switch1.ogg',
        ui_switch2 = 'graphics/kenney.nl/uipack/Bonus/switch2.ogg',
    }
}

return resource_list
