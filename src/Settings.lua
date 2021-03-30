-- Skelly settings object
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local IniFile = require 'lib/ini'

local GameSettings = Class('GameSettings')

function GameSettings:initialize(filename, defaults)
    self.filename = filename
    self.ini = IniFile.load(filename)['skelly'] or nil

    if self.ini == nil then
        print(string.format('Settings file %s not found, using defaults.', filename))
        self.ini = defaults
        self:save()
    else
        print(string.format('Loaded settings file %s.', filename))
        for k, v in defaults do
            -- Update settings with defaults; this will apply any new settings
            -- to their default values.
            self.ini[k] = self.ini[k] or v
        end
    end
end

function GameSettings:save()
    IniFile.save({ skelly = self.ini }, self.filename)
end

function GameSettings:get(x)
    return self.ini[x]
end

function GameSettings:set(x, value)
    self.ini[x] = value
end

return GameSettings
