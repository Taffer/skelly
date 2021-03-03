-- Default configuration for Skelly.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

function love.conf(t)
    -- "Native" window size matches the Switch. Some day, I'd like to port
    -- there.
    --
    -- To work on the GameShell (320x240) the layout/UI/etc. will need
    -- reworking.
    t.window.title = "Skelly"
    t.window.width = 1280
    t.window.height = 720

    t.identity = t.window.title
    t.version = 11.3 -- Made with Love 11.3.
    t.console = true
end
