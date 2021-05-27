# Skelly title/loading screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

from typing import Final

# List of all resources to load during the Loading... screen.
RESOURCE_LIST: Final = {
    # These fonts are used in-game, see below for Pygame GUI fonts.
    'fonts': {
        'germania-h1': ('fonts/GermaniaOne-Bold.ttf', 32),
        'germania-h2': ('fonts/GermaniaOne-BoldItalic.ttf', 28),
        'germania-h3': ('fonts/GermaniaOne-Italic.ttf', 24),
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
    },

    # These fonts are for Pygame GUI.
    'ui_font_paths': {
        'Germania': {
            'regular': 'fonts/GermaniaOne-Regular.ttf',
            'bold': 'fonts/GermaniaOne-Bold.ttf',
            'bold_italic': 'fonts/GermaniaOne-BoldItalic.ttf',
            'italic': 'fonts/GermaniaOne-Italic.ttf'
        },
        'LiberationSerif': {
            'regular': 'fonts/LiberationSerif-Regular.ttf',
            'bold': 'fonts/LiberationSerif-Bold.ttf',
            'bold_italic': 'fonts/LiberationSerif-BoldItalic.ttf',
            'italic': 'fonts/LiberationSerif-Italic.ttf'
        },
        'LiberationSerif-Bold': {
            'regular': 'fonts/LiberationMono-Bold.ttf',
            'bold': 'fonts/LiberationMono-Bold.ttf',
            'bold_italic': 'fonts/LiberationMono-Bold.ttf',
            'italic': 'fonts/LiberationMono-Bold.ttf',
        }
    },
    'ui_fonts': {
        # Note that the "regular" flavour of each font specified in the
        # theme JSON is preloaded automatically. Doing it again here will
        # give you a warning.
        'serif-bold': {
            'name': 'Germania',
            'point_size': 18,
            'style': 'bold'
        },
        'serif-bolditalic': {
            'name': 'Germania',
            'point_size': 18,
            'style': 'bold_italic'
        },
        'serif-italic': {
            'name': 'Germania',
            'point_size': 18,
            'style': 'italic'
        },
    },
}
