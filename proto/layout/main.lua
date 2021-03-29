-- Experiment with UI layout options

local function draw_29x21(screen_width, screen_height)
    love.graphics.setColor(0, 1, 0, 1)
    dx = 8
    dy = 8
    for y = 0, 20 do
        for x = 0, 28 do
            love.graphics.rectangle('line', dx + x * 32, dy + y * 32, 32, 32)
        end
    end

    love.graphics.setColor(1, 0, 0, 1)
    love.graphics.rectangle('fill', dx, dy + 21 * 32, 29 * 32, screen_height - 21 * 32 - dy * 2)

    love.graphics.setColor(0, 0, 1, 1)
    love.graphics.rectangle('fill', 29 * 32 + dx * 2, dy, screen_width - 29 * 32 - dx * 3, screen_height - dy * 2)
end

local function draw_21x21(screen_width, screen_height)
    love.graphics.setColor(0, 1, 0, 1)
    for dx = 0, 20 do
        for dy = 0, 20 do
            love.graphics.rectangle('line', dx * 32, dy * 32, 32, 32)
        end
    end

    love.graphics.setColor(1, 0, 0, 1)
    love.graphics.rectangle('fill', 0, 21 * 32, 21 * 32, 48)

    love.graphics.setColor(0, 0, 1, 1)
    love.graphics.rectangle('fill', 21 * 32, 0, screen_width - (21 * 32), screen_height)
end

local function draw_39x22(screen_width, screen_height)
    love.graphics.setColor(0, 1, 0, 1)
    for dx = 0, 39 do
        for dy = 0, 21 do
            love.graphics.rectangle('line', dx * 32, dy * 32, 32, 32)
        end
    end

    love.graphics.setColor(1, 0, 0, 1)
    love.graphics.rectangle('fill', 0, 22 * 32, screen_width, screen_height - (22 * 32))
end

function love.draw()
    love.graphics.clear(0, 0, 0, 1)

    local screen_width = love.graphics.getWidth()
    local screen_height = love.graphics.getHeight()

    draw_29x21(screen_width, screen_height)
    -- draw_21x21(screen_width, screen_height)
    -- draw_39x22(screen_width, screen_height)
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    end
end
