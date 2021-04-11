# Skelly text for internationalization.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

# Currently incomplete and therefore untranslated.
CREDITS = [  # Credits; the 'h1', 'h2', 'p' are styles to be applied.
    # Libraries
    ('h1', 'Additional coding'),

    ('h2', 'LÖVE'),
    ('p', 'LOVE Development Team'),

    ('h2', 'Lua libraries'),
    ('p', 'Enrique García Cota'),
    ('p', 'Jasmijn Wellner'),

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

    ('h2', 'Löve game icon'),
    ('p', 'Uploaded by Qubodup on the Löve wiki? rude on GitHub?'),

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
    'credits': CREDITS,
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
    'credits': CREDITS,
}
