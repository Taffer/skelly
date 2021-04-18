# Skelly text for internationalization.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

# Currently incomplete and therefore untranslated.
CREDITS_EN = [  # Credits; the 'h1', 'h2', 'p' are styles to be applied.
    # Libraries
    ('h1', 'Additional coding'),

    ('h2', 'Pygame'),
    ('p', 'Pygame Development Team'),
    ('p', 'Especially the folks on the Pygame Discord'),

    ('h2', 'Pygame GUI'),
    ('p', 'Dan Lawrence'),

    # Graphics
    ('h1', 'Graphics'),

    ('h2', "OpenGameArt.org's Liberated Pixel Cup"),
    ('p', 'Anamaris and Krusmira (aka? Emilio J Sanchez)'),
    ('p', 'Barbara Rivera'),
    ('p', 'Casper Nilsson'),
    ('p', 'Charles Sanchez (AKA CharlesGabriel)'),
    ('p', 'Chris Phillips'),
    ('p', 'Daniel Armstrong (AKA HughSpectrum)'),
    ('p', 'Daniel Eddeland'),
    ('p', 'Johann CHARLOT'),
    ('p', 'Jonas Klinger'),
    ('p', 'Joshua Taylor'),
    ('p', 'Lanea Zimmerman (AKA Sharm)'),
    ('p', 'Leo Villeveygoux'),
    ('p', 'Manuel Riecke (AKA MrBeast)'),
    ('p', 'Mark Weyer'),
    ('p', 'Matthew Nash'),
    ('p', 'Skyler Robert Colladay'),
    ('p', 'Stephen Challener (AKA Redshrike)'),

    ('h2', 'Fancy skeleton'),
    ('p', 'Hans von Gersdorff'),

    ('h2', 'Title screen skeleton'),
    ('p', 'goo30 (OpenGameArt)'),

    ('h2', 'Pygame game icon'),
    ('p', 'TheCorruptor'),

    ('h2', 'Taffer logo'),
    ('p', 'ronos_art (Fiverr)'),

    ('h2', 'UI elements'),
    ('p', 'Kenney.nl'),

    # Music
    ('h1', 'Music and Sounds'),
    ('p', 'Kenney.nl'),
    ('p', 'Matthew Pablo'),

    # Leftovers
    ('h1', 'Everything else'),
    ('h2', 'Design, Coding, Writing'),
    ('p', 'Taffer (Chris Herborth)'),

    ('h1', 'Special thanks'),
    ('p', 'Lynette and Alex'),
    ('p', 'Molly and Maisey and those who came before'),
    ('p', 'My online nerd buddies'),

    # Blank line for some space.
    ('h1', '')
]

# "Complete" text that's been translated.
I18N_EN = {
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
            '<i>Strength vs. Finesse?</i>',
            [
                ('STR', 'Strength'),
                ('DEX', 'Finesse')
            ]
        ),
        'q4': (
            '<i>Physical toughness vs. Mental toughness?</i>',
            [
                ('CAL', 'Physical'),
                ('WIL', 'Mental')
            ]
        ),
        'q5': (
            '<i>Physical toughness vs. Mental toughness?</i>',
            [
                ('CAL', 'Physical'),
                ('WIL', 'Mental')
            ]
        ),
        'q6': (
            '<i>Physical toughness vs. Mental toughness?</i>',
            [
                ('CAL', 'Physical'),
                ('WIL', 'Mental')
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

    # Not translated yet.
    'credits': CREDITS_EN,
}

I18N_ES = {
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

    # Not translated yet.
    'credits': CREDITS_EN,
}
