# Skelly "Journey Onward" screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame
import pygame.gfxdraw

from . import Base
from .. import Map
from .. import Viewport

BLACK = pygame.Color('black')
BLUE = pygame.Color('blue')
GREEN = pygame.Color('green')
RED = pygame.Color('red')


def draw_29x21(surface):
    ''' Prototype UI locations, not for human consumption.
    '''
    dx = 8
    dy = 8

    # Map area
    for y in range(21):
        for x in range(29):
            rect = pygame.Rect(dx + x * 32, dy + y * 32, 32, 32)
            pygame.gfxdraw.rectangle(surface, rect, GREEN)

    # Text? area
    rect = pygame.Rect(dx, dy + 21 * 32, 29 * 32, 32)
    pygame.gfxdraw.box(surface, rect, RED)

    # Stats/messages/etc. area
    surface_rect = surface.get_rect()
    rect = pygame.Rect(29 * 32 + dx * 2, dy, surface_rect.width - 29 * 32 - dx * 3, surface_rect.height - dy * 2)
    pygame.gfxdraw.box(surface, rect, BLUE)


'''
-- =============================================================================
-- Sloppy animation classes
-- =============================================================================
local PanViewport = Class('PanViewport')
function PanViewport:initialize(viewport)
    self.viewport = viewport
    self.ticks = 0
    self.done = false

    self.step = 0.2 -- Tick every 0.2 seconds
end

function PanViewport:update(dt, _)
    self.ticks = self.ticks + dt
    if self.ticks > self.step then
        self.ticks = self.ticks - self.step

        local x = self.viewport.x
        local y = self.viewport.y + 1
        self.viewport:setPosition(x, y)

        if self.viewport.y ~= y then
            self.done = true
        end
    end
end

function PanViewport:draw()
    -- Do nothing.
end

local WaitFor = Class('WaitFor')
function WaitFor:initialize(length)
    self.length = length
    self.ticks = 0
    self.done = false
end

function WaitFor:update(dt, _)
    self.ticks = self.ticks + dt
    if self.ticks > self.length then
        self.done = true
    end
end

function WaitFor:draw()
    love.graphics.setColor(1, 1, 1, 0)
    love.graphics.print(string.format('%d: %d', self.ticks, self.length))
end

local WalkTo = Class('WalkTo')
function WalkTo:initialize(sprite, sprite_locs, viewport)
    self.locs = sprite_locs
    self.x = self.locs[1][1] - viewport.x * 32
    self.y = self.locs[1][2] - viewport.y * 32
    self.target_idx = math.min(2, #self.locs)

    self.target_x = self.locs[self.target_idx][1] - viewport.x * 32
    self.target_y = self.locs[self.target_idx][2] - viewport.y * 32

    self.actor = SkeletonActor:new(sprite)
    self.actor.sprite:setFacing('right')
    self.actor.sprite:setAnimation('walk')

    self.step = 0.01
    self.ticks = 0

    self.on_screen = true
end

function WalkTo:update(dt, viewport)
    self.ticks = self.ticks + dt
    if self.ticks > self.step then
        self.ticks = self.ticks - self.step

        if self.x < self.target_x then
            self.x = self.x + 1
        end
        if self.x > self.target_x then
            self.x = self.x - 1
        end
        if self.y < self.target_y then
            self.y = self.y + 1
        end
        if self.y > self.target_y then
            self.y = self.y - 1
        end

        if self.x == self.target_x and self.y == self.target_y then
            self.target_idx = math.min(self.target_idx + 1, #self.locs)
            self.target_x = self.locs[self.target_idx][1] - viewport.x * 32
            self.target_y = self.locs[self.target_idx][2] - viewport.y * 32
        end
    end

    self.actor:update(dt)
end

function WalkTo:draw()
    if self.on_screen then
        self.actor:draw(self.x, self.y)
    end
end
'''


class NewGame(Base):
    def __init__(self, game):
        super().__init__(game)
        self.next_screen = 'Intro'  # TODO: This is sort of the intro...
        '''
        -- UI for creating a new character:
        --
        -- Name: [some reasonable length, default: Skelly]
        --
        -- Stats created (you don't get to pick):
        --
        -- Calcium: 25?
        -- Willpower: 25?

        TODO: What about a "Fortune Teller" type thing to tweak stats?
        '''

        self.map = Map(game.resources['maps']['scene1_farm'])
        rect = pygame.Rect(0, 0, 29, 21)
        self.viewport = Viewport(self.map.map_width, self.map.map_height, rect)

        '''
        self.skeleton_sprite = LPCSprite:new(gameResources.images.skeleton_sprite)
        self.sprite_locs = {
            {   5, 617},
            { 577, 610},
            { 913, 489},
            {1020, 480},
        }

        self.ani = {
            WaitFor:new(2), -- Wait for 2 seconds
            PanViewport:new(self.viewport), -- Pan to the bottom
            -- Walk a skeleton from army_path_1 to army_path_2. These will need to
            -- be converted from map co-ords to screen co-ords.
            WalkTo:new(self.skeleton_sprite, self.sprite_locs, self.viewport)
        }
        self.ani_idx = 1
        '''

    def draw(self):
        self.game.surface.fill(BLACK)
        draw_29x21(self.game.surface)

        self.map.render('Ground', self.game.surface, self.viewport, 8, 8)
        self.map.render('Buildings', self.game.surface, self.viewport, 8, 8)
        '''
        self.ani[self.ani_idx]:draw()
        '''

    def update(self, dt):
        pass
        '''
        if self.ani_idx <= #self.ani then
            self.ani[self.ani_idx]:update(dt, self.viewport)

            if self.ani[self.ani_idx].done then
                self.ani_idx = self.ani_idx + 1
            end
        end
        '''
