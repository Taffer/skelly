# Skelly "New Game" screen.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame
import pygame.gfxdraw
import pygame_gui
import random

from . import Base
from .. import Map
from .. import Viewport
from ..ui import ColorFade
from ..ui import ImageButton

BLACK = pygame.Color('black')
BLACK_ALPHA = pygame.Color(BLACK.r, BLACK.g, BLACK.g, 0)  # BLACK, but fully transparent
BLUE = pygame.Color('blue')
GREEN = pygame.Color('green')
RED = pygame.Color('red')


def draw_29x21(surface: pygame.Surface):
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
        self.viewport:set_position(x, y)

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


class StateBase:  # New Game screen state base class
    def __init__(self, game: any, screen: any):
        self.game = game
        self.screen = screen
        self.done = False

    def update(self, dt: float):
        pass

    def draw(self):
        pass

    def is_done(self):
        return self.done

    def next_state(self):
        raise NotImplementedError

    def userevent(self, event: pygame.event.Event):
        pass


class Fortune1(StateBase):
    # "You are at peace..."
    def __init__(self, game: any, screen: any):
        super().__init__(game, screen)
        self.text = screen.fortune1_text

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)

        self.textbox = None
        self.next_button = None

    def update(self, dt: float):
        self.fade.update(dt)

    def draw(self):
        if self.textbox is not None:
            self.game.manager.draw_ui(self.game.surface)
        else:
            rect = pygame.Rect(550, 110, 650, 100)
            self.textbox = pygame_gui.elements.UITextBox(self.text, rect, self.game.manager, object_id='#fortuneteller')

            rect = pygame.Rect(1000, 300, 190, 49)
            self.next_button = pygame_gui.elements.UIButton(rect, 'Next', self.game.manager, object_id='#menubutton')

        self.fade.draw()

    def next_state(self):
        return Fortune2(self.game, self.screen)

    def userevent(self, event: pygame.event.Event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_button:
                self.done = True


class Fortune2(StateBase):
    # "In the distance..."
    def __init__(self, game: any, screen: any):
        super().__init__(game, screen)
        self.text = screen.fortune2_text

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 1)

        self.textbox = None
        self.next_button = None

    def update(self, dt: float):
        self.fade.update(dt)

    def draw(self):
        if self.textbox is not None:
            self.game.manager.draw_ui(self.game.surface)
        else:
            rect = pygame.Rect(550, 110, 650, 100)
            self.textbox = pygame_gui.elements.UITextBox(self.text, rect, self.game.manager, object_id='#fortuneteller')

            rect = pygame.Rect(1000, 300, 190, 49)
            self.next_button = pygame_gui.elements.UIButton(rect, 'Next', self.game.manager, object_id='#menubutton')

        self.fade.draw()

    def next_state(self):
        return Fortune3(self.game, self.screen)

    def userevent(self, event: pygame.event.Event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_button:
                self.done = True


class Fortune3(StateBase):
    # Death fades in
    def __init__(self, game: any, screen: any):
        super().__init__(game, screen)
        self.image = self.game.resources['images']['reaper']

        self.fade = ColorFade(BLACK, BLACK_ALPHA, 3)

        self.reaper = None

    def update(self, dt: float):
        self.fade.update(dt)
        if self.fade.is_done():
            self.done = True

    def draw(self):
        if self.reaper is not None:
            self.game.manager.draw_ui(self.game.surface)
        else:
            rect = pygame.Rect(0, 0, self.game.screen_width, self.game.screen_height)
            self.reaper = pygame_gui.elements.UIImage(rect, self.image, self.game.manager)

        self.fade.draw()

    def next_state(self):
        return Fortune4(self.game, self.screen)


class Fortune4(StateBase):
    # "What was your name..."
    def __init__(self, game: any, screen: any):
        super().__init__(game, screen)
        self.text = screen.fortune4_text
        self.image = self.game.resources['images']['reaper']

        self.reaper = None
        self.textbox = None
        self.name_entry = None
        self.label = None
        self.next_button = None

    def draw(self):
        if self.reaper is not None:
            self.game.manager.draw_ui(self.game.surface)
        else:
            rect = pygame.Rect(0, 0, self.game.screen_width, self.game.screen_height)
            self.reaper = pygame_gui.elements.UIImage(rect, self.image, self.game.manager)

            rect = pygame.Rect(550, 110, 650, 100)
            self.textbox = pygame_gui.elements.UITextBox(self.text, rect, self.game.manager, object_id='#fortuneteller')

            rect = pygame.Rect(700, 250, 450, 50)
            self.name_entry = pygame_gui.elements.UITextEntryLine(rect, self.game.manager, object_id='#fortuneteller')
            self.name_entry.set_text(self.screen.player_name)

            rect = pygame.Rect(600, 250, 100, self.name_entry.relative_rect.height)
            self.label = pygame_gui.elements.UILabel(rect, 'Name:', self.game.manager, object_id='#fortuneteller')

            rect = pygame.Rect(1000, 300, 190, 49)
            self.next_button = pygame_gui.elements.UIButton(rect, 'Next', self.game.manager, object_id='#menubutton')

    def next_state(self):
        return Fortune5(self.game, self.screen)

    def userevent(self, event: pygame.event.Event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_button:
                self.screen.player_name = self.name_entry.get_text()
                self.done = True


class Fortune5(StateBase):
    # "There are things I must know..."
    def __init__(self, game: any, screen: any):
        super().__init__(game, screen)
        self.text = screen.fortune5_text
        self.image = self.game.resources['images']['reaper']

        self.reaper = None
        self.textbox = None
        self.next_button = None

        self.answers = []
        self.question_idx = 0

    def draw(self):
        if self.reaper is not None:
            self.game.manager.draw_ui(self.game.surface)
        else:
            rect = pygame.Rect(0, 0, self.game.screen_width, self.game.screen_height)
            self.reaper = pygame_gui.elements.UIImage(rect, self.image, self.game.manager)

            rect = pygame.Rect(550, 110, 650, 100)
            self.textbox = pygame_gui.elements.UITextBox(self.text, rect, self.game.manager, object_id='#fortuneteller')

            rect = pygame.Rect(1000, 300, 190, 49)
            self.next_button = pygame_gui.elements.UIButton(rect, 'Next', self.game.manager, object_id='#menubutton')

    def next_state(self):
        return Fortune5a(self.game, self.screen, 0)

    def userevent(self, event: pygame.event.Event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_button:
                self.done = True


class Fortune5a(StateBase):
    # A question
    def __init__(self, game: any, screen: any, question_idx: int):
        super().__init__(game, screen)
        self.text = screen.fortune5_text
        self.image = self.game.resources['images']['reaper']

        self.reaper = None
        self.textbox = None
        self.left_button = None
        self.right_button = None

        self.question_text = screen.questions[question_idx][0]
        self.answers = screen.questions[question_idx][1]
        random.shuffle(self.answers)

        self.next_question = question_idx + 1

    def draw(self):
        if self.reaper is not None:
            self.game.manager.draw_ui(self.game.surface)
        else:
            rect = pygame.Rect(0, 0, self.game.screen_width, self.game.screen_height)
            self.reaper = pygame_gui.elements.UIImage(rect, self.image, self.game.manager)

            rect = pygame.Rect(550, 110, 650, 100)
            self.textbox = pygame_gui.elements.UITextBox(self.question_text, rect, self.game.manager, object_id='#fortuneteller')

            rect = pygame.Rect(800, 300, 190, 49)
            self.left_button = pygame_gui.elements.UIButton(rect, self.answers[0][1], self.game.manager, object_id='#menubutton')

            rect = pygame.Rect(1000, 300, 190, 49)
            self.right_button = pygame_gui.elements.UIButton(rect, self.answers[1][1], self.game.manager, object_id='#menubutton')

    def next_state(self):
        if self.next_question >= len(self.screen.questions):
            return Fortune6(self.game, self.screen)
        else:
            return Fortune5a(self.game, self.screen, self.next_question)

    def userevent(self, event: pygame.event.Event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.left_button:
                self.screen.answers.append(self.answers[0][0])
                self.done = True
            elif event.ui_element == self.right_button:
                self.screen.answers.append(self.answers[1][0])
                self.done = True


class Fortune6(StateBase):
    # "In the distance..."
    def __init__(self, game: any, screen: any):
        super().__init__(game, screen)
        self.text = screen.fortune6_text
        self.image = self.game.resources['images']['reaper']

        self.fade = ColorFade(BLACK_ALPHA, BLACK, 1)

        self.reaper = None
        self.textbox = None
        self.next_button = None
        self.clicked_next = False

    def update(self, dt: float):
        if self.clicked_next:
            self.fade.update(dt)

    def draw(self):
        if self.reaper is not None:
            self.game.manager.draw_ui(self.game.surface)
        else:
            rect = pygame.Rect(0, 0, self.game.screen_width, self.game.screen_height)
            self.reaper = pygame_gui.elements.UIImage(rect, self.image, self.game.manager)

            rect = pygame.Rect(550, 110, 650, 100)
            self.textbox = pygame_gui.elements.UITextBox(self.text, rect, self.game.manager, object_id='#fortuneteller')

            rect = pygame.Rect(1000, 300, 190, 49)
            self.next_button = pygame_gui.elements.UIButton(rect, 'Next', self.game.manager, object_id='#menubutton')

        if self.clicked_next:
            self.fade.draw()
            if self.fade.is_done():
                self.done = True

    def next_state(self):
        return Fortune8(self.game, self.screen)

    def userevent(self, event: pygame.event.Event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_button:
                self.clicked_next = True


class Fortune8(StateBase):
    def __init__(self, game: any, screen: any):
        super().__init__(game, screen)

    def draw(self):
        draw_29x21(self.game.surface)

        self.screen.map.render('Ground', self.game.surface, self.screen.viewport, 8, 8)
        self.screen.map.render('Buildings', self.game.surface, self.screen.viewport, 8, 8)

        for item in self.screen.ui:
            item.draw()


class NewGame(Base):
    def __init__(self, game: any):
        super().__init__(game)
        self.next_screen = 'Journey'  # TODO: Should be 'Game'
        '''
        Character creation:

            "Fortune Teller" type scene featuring Death

        Intro animated:

        Scene: 1 - Farm, viewport bottom-left
            Enter: skeletons, walking along army_path_[1-4], exits
            Enter: necromancer, walking necro_path_[1-4]
            Animate: necromancer summons the skellies, RISE FROM YOUR GRAVE
            Animate: spawn_loc_[1-3] - ground disturbed, skellies spawn, walk to
                     army_path_2 then follow army_path
            Animate: necromancer walks necro_path_[5-9], exits

            Skeleton hoard continues for a bit. After they're all passed:

            Enter: cute bunny, hops around for a bit, leaves
            Pan: viewport pans to top-left, more ambient nature/farm
            Animate: spawn_skelly - ground disturbed, Skelly spawns
            Animate: Skelly looks around, is confused?

        Transition to Game
        '''

        fortune_text = self.game.text.get_text('newgame')
        self.fortune1_text = fortune_text['fortune1']
        self.fortune2_text = fortune_text['fortune2']
        self.fortune4_text = fortune_text['fortune4']
        self.fortune5_text = fortune_text['fortune5']
        self.fortune6_text = fortune_text['fortune6']

        str_vs_fin = [
            fortune_text['q1'],
            fortune_text['q2'],
            fortune_text['q3'],
        ]
        cal_vs_wil = [
            fortune_text['q4'],
            fortune_text['q5'],
            fortune_text['q6'],
        ]

        random.shuffle(str_vs_fin)  # Randomnly choose 4 questions out of 6.
        random.shuffle(cal_vs_wil)
        self.questions = str_vs_fin[:2] + cal_vs_wil[:2]
        random.shuffle(self.questions)

        self.player_name = 'Skelly'
        self.answers = []

        self.map = Map(game.resources['maps']['scene1_farm'])
        rect = pygame.Rect(0, 0, 29, 21)
        self.viewport = Viewport(self.map.map_width, self.map.map_height, rect)

        x = 16
        y = game.screen_height - 40
        dx = 48

        self.icon_attack = ImageButton(x, y, game.resources['images']['icon-attack'])
        x += dx
        self.icon_cast = ImageButton(x, y, game.resources['images']['icon-cast'])
        x += dx
        self.icon_talk = ImageButton(x, y, game.resources['images']['icon-talk'])
        x += dx
        self.icon_look = ImageButton(x, y, game.resources['images']['icon-look'])
        x += dx
        self.icon_get = ImageButton(x, y, game.resources['images']['icon-get'])
        x += dx
        self.icon_drop = ImageButton(x, y, game.resources['images']['icon-drop'])
        x += dx
        self.icon_move = ImageButton(x, y, game.resources['images']['icon-move'])
        x += dx
        self.icon_use = ImageButton(x, y, game.resources['images']['icon-use'])
        x += dx
        self.icon_rest = ImageButton(x, y, game.resources['images']['icon-rest'])
        x += dx
        self.icon_combat_on = ImageButton(x, y, game.resources['images']['icon-combat-on'])
        x += dx
        self.icon_combat_off = ImageButton(x, y, game.resources['images']['icon-combat-off'])
        self.ui = [
            self.icon_attack,
            self.icon_cast,
            self.icon_talk,
            self.icon_look,
            self.icon_get,
            self.icon_drop,
            self.icon_move,
            self.icon_use,
            self.icon_rest,
            self.icon_combat_on,
            self.icon_combat_off,
        ]

        self.state = Fortune1(game, self)

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

        self.state.draw()
        '''
        self.ani[self.ani_idx]:draw()
        '''

    def update(self, dt: float):
        self.state.update(dt)

        if self.state.is_done():
            try:
                self.game.manager.clear_and_reset()
                self.state = self.state.next_state()
            except NotImplementedError:
                self.can_exit = True
        '''
        if self.ani_idx <= #self.ani then
            self.ani[self.ani_idx]:update(dt, self.viewport)

            if self.ani[self.ani_idx].done then
                self.ani_idx = self.ani_idx + 1
            end
        end
        '''

    def userevent(self, event: pygame.event.Event):
        self.state.userevent(event)
