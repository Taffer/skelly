-- Skelly title/loading screen.
--
-- By Chris Herborth (https://github.com/Taffer)
-- MIT license, see LICENSE.md for details.

local Class = require 'lib/middleclass/middleclass'
local ScreenBase = require 'src/screens/base'

local rsrc_list = require 'src/rsrc_list'

local function loader(resource, file_list)
    local yield = coroutine.yield

    -- Load the files listed into the resource table.
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

    return resource.text.title.loading_done
end

local TitleScreen = Class('TitleScreen', ScreenBase)

function TitleScreen:initialize(resources)
    ScreenBase.initialize(self, resources)

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
    self.degrees_per_second = 45

    self.loaded_resource = ""
    self.loading_finished = false
    self.loading_routine = nil
end

-- Render this screen's contents.
function TitleScreen:draw()
    -- Premature optimization:
    local rsrc = self.resources
    local font_mono = rsrc.fonts.default_mono
    local font_title = rsrc.fonts.skelly_title
    local image_title = rsrc.images.skelly_title

    love.graphics.clear(0, 0, 0, 1)

    love.graphics.setColor(1, 1, 1, self.alpha)
    love.graphics.draw(image_title, 0, 0)

    local screen_width = love.graphics.getWidth()
    local width = font_mono:getWidth(self.loading_text)
    local x = (screen_width - width) / 2
    love.graphics.setFont(font_mono)
    love.graphics.print(self.loading_text .. ' ' .. (self.loaded_resource or ""),
        self.loading_x, self.loading_y)

    width = font_mono:getWidth(self.subtitle_text)
    x = (screen_width - width) / 2
    love.graphics.print(self.subtitle_text, x, 200)

    width = font_title:getWidth(self.skelly_text)
    x = (screen_width - width) / 2
    love.graphics.setFont(font_title)
    love.graphics.print(self.skelly_text, x, 40)
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
        alive, self.loaded_resource = resume(self.loading_routine,self.resources, rsrc_list)
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
    if event == 'escape' then
        -- Escape doesn't kick you out until loading is done, sorry.
        if self.loading_finished then
            self.exit_screen = true
            return true
        end
    end

    return ScreenBase.handle(self, event)
end

return TitleScreen
