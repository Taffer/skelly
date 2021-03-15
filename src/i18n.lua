-- Skelly title/loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

-- Currently incomplete and therefore untranslated.
local credits = { -- Credits; the 'h1', 'h2', 'p' are styles to be applied.
    -- Libraries
    {'h1', 'Additional coding'},

    {'h2', 'LÖVE'},
    {'p', 'LOVE Development Team'},

    {'h2', 'Lua libraries'},
    {'p', 'Enrique García Cota'},
    {'p', 'Jasmijn Wellner'},

    -- Graphics
    {'h1', 'Graphics'},

    {'h2', "OpenGameArt.org's Liberated Pixel Cup"},
    {'p', 'Anamaris and Krusmira (aka? Emilio J Sanchez)'},
    {'p', 'Barbara Rivera'},
    {'p', 'Casper Nilsson'},
    {'p', 'Charles Sanchez (AKA CharlesGabriel)'},
    {'p', 'Chris Phillips'},
    {'p', 'Daniel Armstrong (AKA HughSpectrum)'},
    {'p', 'Daniel Eddeland'},
    {'p', 'Johann CHARLOT'},
    {'p', 'Jonas Klinger'},
    {'p', 'Joshua Taylor'},
    {'p', 'Lanea Zimmerman (AKA Sharm)'},
    {'p', 'Leo Villeveygoux'},
    {'p', 'Manuel Riecke (AKA MrBeast)'},
    {'p', 'Mark Weyer'},
    {'p', 'Matthew Nash'},
    {'p', 'Skyler Robert Colladay'},
    {'p', 'Stephen Challener (AKA Redshrike)'},

    {'h2', 'Fancy skeleton'},
    {'p', 'Hans von Gersdorff'},

    {'h2', 'Title screen skeleton'},
    {'p', 'goo30 (OpenGameArt)'},

    {'h2', 'Löve game icon'},
    {'p', 'Uploaded by Qubodup on the Löve wiki? rude on GitHub?'},

    {'h2', 'Taffer logo'},
    {'p', 'ronos_art (Fiverr)'},

    {'h2', 'UI elements'},
    {'p', 'Kenney.nl'},

    -- Music
    {'h1', 'Music and Sounds'},
    {'p', 'Kenney.nl'},
    {'p', 'Matthew Pablo'},

    -- Leftovers
    {'h1', 'Everything else'},
    {'h2', 'Design, Coding, Writing'},
    {'p', 'Taffer (Chris Herborth)'},

    {'h1', 'Special thanks'},
    {'p', 'Lynette and Alex'},
    {'p', 'Molly and Maisey and those who came before'},
    {'p', 'My online nerd buddies'},

    -- Blank line for some space.
    {'h1', ''}
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

        ui = { -- UI parts
            ui_language = 'Language',
            ui_languages = {'English', 'Español'},
            ui_volume = 'Volume',
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
        },

        ui = { -- UI parts
            ui_language = 'Idioma',
            ui_languages = {'English', 'Español'},
            ui_volume = 'Volumen',
        },

        -- Not translated yet.
        credits = credits,
    }
}

return internationalization
