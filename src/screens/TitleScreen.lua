-- Skelly title/loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'

local ColorFade = require 'src/ColorFade'
local ImageButton = require 'src/ui/ImageButton'
local Label = require 'src/ui/Label'

local rsrc_list = require 'src/rsrc_list'

local function loader(resource, file_list)
    local yield = coroutine.yield

    -- Load the files listed into the resource table.
    for k,v in pairs(file_list.fonts) do
        resource.fonts[k] = love.graphics.newFont(v.src, v.size)
        yield(v.src)
    end

    for k,v in pairs(file_list.images) do
        resource.images[k] = love.graphics.newImage(v)
        yield(v)
    end

    for k,v in pairs(file_list.music) do
        resource.music[k] = love.audio.newSource(v, 'stream')
        yield(v)
    end

    for k,v in pairs(file_list.sounds) do
        resource.sounds[k] = love.audio.newSource(v, 'static')
        yield(v)
    end

    for k, v in pairs(file_list.maps) do
        resource.maps[k] = dofile(v)
    end

    return resource.text.title.loading_done
end

local TitleScreen = Class('TitleScreen', ScreenBase)

function TitleScreen:initialize(resources, state)
    ScreenBase.initialize(self, resources, state)
    self:setNextScreen('Journey')

    self.resources.fonts.skelly_title = love.graphics.newFont('graphics/Gypsy Curse.ttf', 144)
    self.resources.images.skelly_title = love.graphics.newImage('graphics/Gersdorff_Feldbuch_skeleton.png')

    self.loading_x = 16
    self.loading_y = love.graphics.getHeight() - 16 - self.resources.fonts.default_mono:getHeight()

    self.skelly_text = self.resources.text.skelly_title
    self.subtitle_text = self.resources.text.title.subtitle_text
    self.loading_text = self.resources.text.title.loading_text

    self.fade = ColorFade:new({0, 0, 0, 1}, {0, 0, 0, 0}, 1)

    self.loaded_resource = ""
    self.loading_finished = false
    self.loading_routine = nil

    local title_image = self.resources.images.skelly_title
    local title_quad = love.graphics.newQuad(0, 0, title_image:getWidth(), title_image:getHeight(), title_image)

    local font_mono = self.resources.fonts.default_mono
    local font_title = self.resources.fonts.skelly_title

    self.loading_label = Label:new(self, self.loading_x, self.loading_y, self.loading_text, font_mono, {1, 1, 1, 1}, 'left')

    self.ui = {
        ImageButton:new(self, 0, 0, title_image, title_quad),
        Label:new(self, state.scr_width / 2, 40, self.skelly_text, font_title, {1, 1, 1, 1}, 'centre'),
        Label:new(self, state.scr_width / 2, 200, self.subtitle_text, font_mono, {1, 1, 1, 1}, 'centre'),
        self.loading_label,
    }

    self.onMouseRelease = (function(self)
        if self.loading_finished then
            self.exit_screen = true
        end
    end)

    self.onKeyRelease = (function(self)
        if self.loading_finished then
            self.exit_screen = true
        end
    end)
end

-- Render this screen's contents.
function TitleScreen:draw()
    love.graphics.clear(0, 0, 0, 1)

    self.loading_label:setText(self.loading_text .. ' ' .. (self.loaded_resource or ""))

    for i in ipairs(self.ui) do
        self.ui[i]:draw()
    end

    if not self.fade:isDone() then
        love.graphics.setColor(unpack(self.fade:getColor()))
        love.graphics.rectangle('fill', 0, 0, gameState.scr_width, gameState.scr_height)
    end
end

-- Update the screen.
function TitleScreen:update(dt)
    self.fade:update(dt)

    if self.loading_finished and self.fade:isDone() then
        self.exit_screen = true
    end

    -- Load resources.
    if self.loading_routine then
        local resume = coroutine.resume
        alive, self.loaded_resource = resume(self.loading_routine, self.resources, rsrc_list)
        if not alive then
            self.loading_finished = true
            self.loaded_resource = self.resources.text.title.loading_done
        end
    else
        self.loading_routine = coroutine.create(loader)
    end
end

return TitleScreen
