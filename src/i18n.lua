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
        presents = { -- 'presents' screen
            taffer_text = 'Taffer presents…',
            love_text = 'A game made with LÖVE…'
        },

        title = { -- 'title' screen
            subtitle_text = 'A tale of the Skeleton War',
            loading_text = 'Loading…',
            loading_done = 'Done.'
        }
    },

    -- Español translation attempted by Chris Herborth
    es = {
        -- DO NOT TRANSLATE
        skelly_title = 'Skelly',

        -- Translate these
        presents = { -- 'presents' screen
            taffer_text = 'Taffer presenta…',
            love_text = 'Un videojuego hecho con LÖVE…'
        },

        title = { -- 'title' screen
            subtitle_text = 'Una historia de la Guerra de los Esqueletos',
            loading_text = 'Cargando…',
            loading_done = 'Terminado.'
        }
    }
}

return internationalization
