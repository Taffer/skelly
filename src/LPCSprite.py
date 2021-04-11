# Skelly LPC Sprite for animation.
#
# This sets up a set of sprites, quads, etc. using the standard Liberated
# Pixel Cup sprite format:
#
# https://lpc.opengameart.org/static/lpc-style-guide/styleguide.html
#
# Specifically:
# * Each row is a complete animation cycle.
# * Rows are mostly in groups of four based on facing = away, left, forward,
#   right.
# * Animation rows are: Spellcast, Thrust, Walk, Slash, Shoot, Hurt (only one
#   facing for Hurt). We fake an Idle animation by cloning the first frame of
#   Walk.
# * Are 64x64 on the sprite sheet.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame

# Note that this includes a non-standard animation, 'idle', made up of the
# first 'walk' frame.
LPC_ANIMATION = [
    'spellcast',
    'thrust',
    'walk',
    'slash',
    'shoot',
    'hurt',
    'idle'
]

LPC_FACING = [
    'away',
    'left',
    'forward',
    'right'
]

FRAMES = {
    LPC_ANIMATION[0]: 7,  # spellcast
    LPC_ANIMATION[1]: 8,  # thrust
    LPC_ANIMATION[2]: 9,  # walk
    LPC_ANIMATION[3]: 6,  # slash
    LPC_ANIMATION[4]: 13,  # shoot
    LPC_ANIMATION[5]: 6,  # hurt
    LPC_ANIMATION[6]: 1,  # idle
}


class LPCSprite:  # TODO: Should this be a pygame.Sprite subclass?
    def __init__(self, texture: pygame.Surface):
        self.width = 64
        self.height = 64

        self.feet_x = self.width / 2  # Where are the feet relative to 0,0?
        self.feet_y = self.height - 2

        self.facing = LPC_FACING[2]  # Default facing and animation.
        self.animation = LPC_ANIMATION[2]
        self.frame = 1

        self.texture = texture

        # Generate subsurfaces.
        self.frames = {}
        y = 0
        for av in LPC_ANIMATION[:-2]:  # "hurt" and "idle" are special cases
            self.frames[av] = {}

            for fv in LPC_FACING:
                self.frames[av][fv] = []
                for i in range(FRAMES[av]):
                    x = i * self.width
                    rect = pygame.Rect(x, y, self.width, self.height)
                    self.frames[av][fv].append(texture.subsurface(rect))

                y += self.height

        # "hurt" has to be special-cased because it only has one facing.
        y = texture.get_height() - self.height
        for fv in LPC_FACING:
            # We'll use this animation for all four facings.
            self.frames['hurt'][fv] = []
        for i in range(FRAMES['hurt']):
            x = i * self.width
            rect = pygame.Rect(x, y, self.width, self.height)
            for fv in LPC_FACING:
                self.frames['hurt'][fv].append(texture.subsurface(rect))

        # "idle" is fake, just the first frame from "walk"
        for fv in LPC_FACING:
            self.frames['idle'][fv] = [self.frames['walk'][fv][0]]

    def check_frame(self):
        if self.frame >= FRAMES[self.animation]:
            self.frame = 0

    def next_frame(self):
        self.frame += 1
        self.check_frame()

    def set_facing(self, facing: str):
        self.facing = facing
        self.check_frame()

    def set_animation(self, animation: str):
        self.animation = animation
        self.check_frame()

    def get_texture(self):
        self.frames[self.animation][self.facing][self.frame]
