# Skelly text for internationalization.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

from typing import Final

# "Complete" text that's been translated.
I18N_EN: Final = {
    # Original English by Chris Herborth.

    # DO NOT TRANSLATE:
    'skelly_title': 'Skelly',

    # Translate these:
    'journey': {  # 'Journey' screen
        'credits_text': 'Credits',
        'exit_text': 'Exit',
        'new_game_text': 'New Game',
        'onward_text': 'Journey Onward',
        'settings_text': 'Settings',
    },

    'newgame': {  # 'NewGame' screen
        'fortune1': 'You are at peace, drifting in the <i>Void</i>. '
                    'You have no sense of time, or location, but you '
                    'have no worries and feel content.',

        'fortune2': 'In the distance, a light appears, growing steadily as '
                    'it approaches you. <i>Death</i> is coming.',

        'fortune4': '<i>What was your name in life?</i>',

        'fortune5': '<i>You are being called back. Before I release you, '
                    'there are things I must know.</i>',

        'fortune6': '<i>So be it.</i> Everything goes dark…',

        'q1': (
            '<i>You have a locked box with something important inside. '
            "You've lost the key. Do you smash it open or pick the lock?</i>",
            [
                ('STR', 'Smash it open'),
                ('DEX', 'Pick the lock')
            ]
        ),
        'q2': (
            '<i>An angry wasp is flying around your head. '
            'Do you slap it when it lands, or brush it off until it leaves?</i>',
            [
                ('STR', 'Slap it'),
                ('DEX', 'Brush it off')
            ]
        ),
        'q3': (
            '<i>Are you a dog person or a cat person?</i>',
            [
                ('STR', 'Dog'),
                ('DEX', 'Cat')
            ]
        ),
        'q4': (
            '<i>Would you open a banana at the top or bottom?</i>',
            [
                ('CAL', 'Top'),
                ('WIL', 'Bottom')
            ]
        ),
        'q5': (
            '<i>Do you prefer winter or summer?</i>',
            [
                ('CAL', 'Winter'),
                ('WIL', 'Summer')
            ]
        ),
        'q6': (
            '<i>Would you rather do ten push-ups or remember five things?</i>',
            [
                ('CAL', 'Push-ups'),
                ('WIL', 'Remember')
            ]
        ),

        'rockpaperscissors': (
            '<i>Rock, paper, or scissors?</i>',
            [
                ('R', 'Rock'),
                ('P', 'Paper'),
                ('S', 'Scissors')
            ]
        ),
    },

    'presents': {  # 'Presents' screen
        'pygame_text': 'A game made with Pygame…',
        'taffer_text': 'Taffer presents…',
    },

    'settings': {  # 'Settings' overlay
        'effects_volume': 'Effects Volume:',
        'language': 'Language:',
        'master_volume': 'Master Volume:',
        'music_volume': 'Music Volume:',
        'title': 'Skelly Settings',
        'translations': ['English', 'Español'],
        'voice_volume': 'Voice Volume:',
    },

    'title': {  # 'Title' screen
        'loading_done': 'Done.',
        'loading_text': 'Loading…',
        'subtitle_text': 'A tale of the Skeleton War',
    },

    'ui': {  # UI parts
        'ui_language': 'Language',
        'ui_languages': {'English', 'Español'},
        'ui_volume': 'Volume',
    },
}

I18N_ES: Final = {
    # Español translation attempted by Chris Herborth. These are likely to be
    # hilariously bad!

    # DO NOT TRANSLATE
    'skelly_title': 'Skelly',

    # Translate these
    'journey': {  # 'Journey' screen
        'credits_text': 'Créditos',
        'exit_text': 'Salir De Videojuego',
        'new_game_text': 'Videojuego Nuevo',
        'onward_text': 'Viaja Hacia Delante',
        'settings_text': 'Los Entornos',
    },

    'presents': {  # 'Presents' screen
        'pygame_text': 'Un videojuego hecho con Pygame…',
        'taffer_text': 'Taffer presenta…',
    },

    'settings': {  # 'Settings' overlay
        'effects_volume': 'Volumen de efectos:',
        'language': 'Idioma:',
        'master_volume': 'Volumen general:',
        'music_volume': 'Volumen de la música:',
        'title': 'Configuración de Skelly',
        'translations': ['English', 'Español'],
        'voice_volume': 'Volumen de voz:',
    },

    'title': {  # 'Title' screen
        'loading_done': 'Terminado.',
        'loading_text': 'Cargando…',
        'subtitle_text': 'Una historia de la Guerra de los Esqueletos',
    },

    'ui': {  # UI parts
        'ui_language': 'Idioma',
        'ui_languages': {'English', 'Español'},
        'ui_volume': 'Volumen',
    },
}
