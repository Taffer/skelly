-- Skelly text handler for internationalization.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'

local TextHandler = Class("TextHandler")

function TextHandler:initialize()
    self.default = nil
    self.current = nil
    self.lang = {}
end

function TextHandler:addLanguage(code, dictionary)
    -- Add a language specified by code, with the specified string dictionary.
    self.lang[code] = dictionary
    if self.default == nil then
        self.default = code
    end
end

function TextHandler:setLanguage(code)
    self.current = code
end

function TextHandler:getText(tag)
    return self.lang[self.current][tag] or self.lang[self.default][tag]
end

return TextHandler
