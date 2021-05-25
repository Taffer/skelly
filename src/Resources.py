# Skelly title/loading screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

from typing import Final

# List of all resources to load during the Loading... screen.
RESOURCE_LIST: Final = {
    'font_paths': {
        'LiberationSerif': {
            'regular': 'graphics/LiberationSerif-Regular.ttf',
            'bold': 'graphics/LiberationSerif-Bold.ttf',
            'bold_italic': 'graphics/LiberationSerif-BoldItalic.ttf',
            'italic': 'graphics/LiberationSerif-Italic.ttf'
        },
        'LiberationSerif-Bold': {
            'regular': 'graphics/LiberationMono-Bold.ttf',
            'bold': 'graphics/LiberationMono-Bold.ttf',
            'bold_italic': 'graphics/LiberationMono-Bold.ttf',
            'italic': 'graphics/LiberationMono-Bold.ttf',
        }
    },
    'fonts': {
        # Note that the "regular" flavour of each font specified in the
        # theme JSON is preloaded automatically. Doing it again here will
        # give you a warning.
        'serif-bold': {
            'name': 'LiberationSerif',
            'point_size': 16,
            'style': 'bold'
        },
        'serif-bolditalic': {
            'name': 'LiberationSerif',
            'point_size': 16,
            'style': 'bold_italic'
        },
        'serif-italic': {
            'name': 'LiberationSerif',
            'point_size': 16,
            'style': 'italic'
        },
    },

    'images': {
        # I don't need all of these, but I haven't decided yet.
        'ui_blue': 'graphics/kenney.nl/uipack/Spritesheet/blueSheet.png',
        'ui_green': 'graphics/kenney.nl/uipack/Spritesheet/greenSheet.png',
        'ui_grey': 'graphics/kenney.nl/uipack/Spritesheet/greySheet.png',
        'ui_red': 'graphics/kenney.nl/uipack/Spritesheet/redSheet.png',
        'ui_yellow': 'graphics/kenney.nl/uipack/Spritesheet/yellowSheet.png',

        'ui_rpg': 'graphics/kenney.nl/uipack-rpg/Spritesheet/uipack_rpg_sheet.png',

        # I should turn these into a sprite sheet.
        'icon-attack': 'graphics/game-icons.net/sword-wound.png',
        'icon-cast': 'graphics/game-icons.net/magic-swirl.png',
        'icon-combat-off': 'graphics/game-icons.net/guards-with-minus.png',
        'icon-combat-on': 'graphics/game-icons.net/guards.png',
        'icon-drop': 'graphics/game-icons.net/fall-down.png',
        'icon-get': 'graphics/game-icons.net/card-pickup.png',
        'icon-look': 'graphics/game-icons.net/look-at.png',
        'icon-move': 'graphics/game-icons.net/move.png',
        'icon-rest': 'graphics/game-icons.net/camping-tent.png',
        'icon-talk': 'graphics/game-icons.net/talk.png',
        'icon-use': 'graphics/game-icons.net/button-finger.png',

        # I might not need both of these.
        'map_terrain': 'graphics/lpc-terrains/terrain-map-v7-repacked.png',
        'map_sheet': 'graphics/lpc-terrains/terrain-v7.png',

        # I should turn these into a sprite sheet.
        'skelly_bone': 'graphics/skeleton/bone.png',
        'skelly_die_left': 'graphics/skeleton/die_left.png',
        'skelly_die_right': 'graphics/skeleton/die_right.png',
        'skelly_idle_left': 'graphics/skeleton/idle_left.png',
        'skelly_idle_right': 'graphics/skeleton/idle_right.png',
        'skelly_throw_left': 'graphics/skeleton/throw_left.png',
        'skelly_throw_right': 'graphics/skeleton/throw_right.png',
        'skelly_walk_left': 'graphics/skeleton/walk_left.png',
        'skelly_walk_right': 'graphics/skeleton/walk_right.png',

        'skeleton_sprite': 'graphics/lpc-skeleton/skeleton.png',

        'zombie_bleeding_eye': 'graphics/lpc-zombie/Bleeding Eye.png',
        'zombie_bloody_arm': 'graphics/lpc-zombie/Bloody Arm.png',
        'zombie_bloody_mouth': 'graphics/lpc-zombie/Bloody Mouth.png',
        'zombie_brain': 'graphics/lpc-zombie/Brain.png',
        'zombie_ribs': 'graphics/lpc-zombie/Ribs.png',
        'zombie_zombie': 'graphics/lpc-zombie/Zombie.png',

        # Tile atlases used with Tiled.
        'tiles_base_out_atlas': 'graphics/lpc-atlas/base_out_atlas.png',
        'tiles_build_atlas': 'graphics/lpc-atlas/build_atlas.png',
        'tiles_obj_misk_atlas': 'graphics/lpc-atlas/obj_misk_atlas.png',
        'tiles_terrain_atlas': 'graphics/lpc-atlas/terrain_atlas.png',

        'tiles_cottage': 'graphics/lpc-thatched-roof-cottage/cottage.png',
        'tiles_thatched_roof': 'graphics/lpc-thatched-roof-cottage/thatched-roof.png',

        # Intro screens
        'reaper': 'graphics/reaper.png',
    },

    'music': {
    },

    'sounds': {
        # Yes, I know these are in the wrong spot in the filesystem, I wanted
        # to keep Kenney's UI Pack resources together.
        'ui_click1': 'graphics/kenney.nl/uipack/Bonus/click1.ogg',
        'ui_click2': 'graphics/kenney.nl/uipack/Bonus/click2.ogg',
        'ui_rollover1': 'graphics/kenney.nl/uipack/Bonus/rollover1.ogg',
        'ui_rollover2': 'graphics/kenney.nl/uipack/Bonus/rollover2.ogg',
        'ui_switch2': 'graphics/kenney.nl/uipack/Bonus/switch2.ogg',
        'ui_switch3': 'graphics/kenney.nl/uipack/Bonus/switch3.ogg',
    },

    'maps': {
        'scene1_farm': 'maps/scene1-farm.tmx',
    }
}
