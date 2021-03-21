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
    end
end

function GameSettings:save()
    print('Attempting to save settings...')
    local result = IniFile.save({ skelly = self.ini }, self.filename)
    print('... result was:', result)
end

function GameSettings:get(x, default)
    return self.ini[x] or default
end

function GameSettings:set(x, value)
    self.ini[x] = value
end

return GameSettings
