-- Skelly title/loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local internationalization = {
    -- Original English by Chris Herborth.
    en = {
        -- DO NOT TRANSLATE
        skelly_title = 'Skelly',

        -- Translate these
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
        }
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
    }
}

return internationalization
