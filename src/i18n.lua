-- Skelly title/loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

-- Currently incomplete and therefore untranslated.
local credits = { -- Credits; the keys also need to be translated.
    -- Libraries
    ['Additional coding'] = {
        ['LÖVE'] = 'LOVE Development Team',

        ['Lua libraries'] = {
            'Enrique García Cota',
            'Jasmijn Wellner',
        },
    },

    -- Graphics
    ['Graphics'] = {
        ["OpenGameArt.org's Liberated Pixel Cup"] = {
            'Anamaris and Krusmira (aka? Emilio J Sanchez)',
            'Barbara Rivera',
            'Casper Nilsson',
            'Charles Sanchez (AKA CharlesGabriel)',
            'Chris Phillips',
            'Daniel Armstrong (AKA HughSpectrum)',
            'Daniel Eddeland',
            'Johann CHARLOT',
            'Jonas Klinger',
            'Joshua Taylor',
            'Lanea Zimmerman (AKA Sharm)',
            'Leo Villeveygoux',
            'Manuel Riecke (AKA MrBeast)',
            'Mark Weyer',
            'Matthew Nash',
            'Skyler Robert Colladay',
            'Stephen Challener (AKA Redshrike)',
        },

        ['Fancy skeleton'] = 'Hans von Gersdorff',
        ['Title screen skeleton'] = 'goo30 (OpenGameArt)',
        ['Löve game icon'] = 'Uploaded by Qubodup on the Löve wiki? rude on GitHub?',
        ['Taffer logo'] = 'ronos_art (Fiverr)',
        ['UI elements'] = 'Kenney.nl',
    }

    -- Music
    ['Music and Sounds'] = {
        'Kenney.nl',
        'Matthew Pablo',
    },

    -- Leftovers
    ['Everything else'] = {
        ['Design, Coding, Writing'] = 'Taffer (Chris Herborth)'
    }
}

-- "Complete" text that's been translated.
local internationalization = {
    -- Original English by Chris Herborth.
    en = {
        -- DO NOT TRANSLATE:
        skelly_title = 'Skelly',

        -- Translate these:
        journey = { -- 'Journey' screen
            credits_text = 'Credits',
            exit_text = 'Exit',
            new_game_text = 'New Game',
            onward_text = 'Journey Onward',
            settings_text = 'Settings',
        },

        presents = { -- 'Presents' screen
            love_text = 'A game made with LÖVE…',
            taffer_text = 'Taffer presents…',
        },

        title = { -- 'Title' screen
            loading_done = 'Done.',
            loading_text = 'Loading…',
            subtitle_text = 'A tale of the Skeleton War',
        },

        -- Not translated yet.
        credits = credits,
    },

    -- Español translation attempted by Chris Herborth. These are likely to be
    -- hilariously bad!
    es = {
        -- DO NOT TRANSLATE
        skelly_title = 'Skelly',

        -- Translate these
        journey = { -- 'Journey' screen
            credits_text = 'Créditos',
            exit_text = 'Salir De Videojuego',
            new_game_text = 'Videojuego Nuevo',
            onward_text = 'Viaja Hacia Delante',
            settings_text = 'Los Entornos',
        },

        presents = { -- 'Presents' screen
            love_text = 'Un videojuego hecho con LÖVE…',
            taffer_text = 'Taffer presenta…',
        },

        title = { -- 'Title' screen
            loading_done = 'Terminado.',
            loading_text = 'Cargando…',
            subtitle_text = 'Una historia de la Guerra de los Esqueletos',
        }

        -- Not translated yet.
        credits = credits,
    }
}

return internationalization
