-- Skelly title/loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/ScreenBase'
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

    self.alpha = 0 -- Alpha level for the fade-in/out animation.
    self.ticks = 0
    self.pi_over_180 = math.pi / 180
    self.degrees_per_second = 90

    self.loaded_resource = ""
    self.loading_finished = false
    self.loading_routine = nil

    local title_image = self.resources.images.skelly_title
    local title_quad = love.graphics.newQuad(0, 0, title_image:getWidth(), title_image:getHeight(), title_image)

    local font_mono = self.resources.fonts.default_mono
    local font_title = self.resources.fonts.skelly_title

    self.loading_label = Label:new(self.loading_x, self.loading_y, self.loading_text, font_mono, {1, 1, 1, 1}, 'left')

    self.ui = {
        ImageButton:new(0, 0, title_image, title_quad),
        Label:new(state.scr_width / 2, 40, self.skelly_text, font_title, {1, 1, 1, 1}, 'centre'),
        Label:new(state.scr_width / 2, 200, self.subtitle_text, font_mono, {1, 1, 1, 1}, 'centre'),
        self.loading_label,
    }
end

-- Render this screen's contents.
function TitleScreen:draw()
    love.graphics.clear(0, 0, 0, 1)

    self.loading_label:setText(self.loading_text .. ' ' .. (self.loaded_resource or ""))

    for i in ipairs(self.ui) do
        self.ui[i]:setColor({1, 1, 1, self.alpha})
        self.ui[i]:draw()
    end
end

-- Update the screen.
function TitleScreen:update(dt)
    self.ticks = self.ticks + dt

    local degrees = self.ticks * self.degrees_per_second -- 1 second = 90 degrees

    if degrees >= 90 and not self.loading_finished then
        -- Pause the animation until loading is done.
        degrees = 90
    end

    self.alpha = math.sin(degrees * self.pi_over_180)

    if degrees > 180 then -- sin(180 degrees) is back to 0 alpha
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

-- Exit this screen?
function TitleScreen:exit()
    return self.exit_screen
end

-- Handle events.
--
-- If you handled it, return true; false means the event continues on to the
-- next handler.
function TitleScreen:handle(event)
    if event.keys['escape'] or event.button then
        -- Escape doesn't kick you out until loading is done, sorry.
        if self.loading_finished then
            self.exit_screen = true
            return true
        end
    end

    return ScreenBase.handle(self, event)
end

return TitleScreen
