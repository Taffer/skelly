# Skelly actor (PC or NPC)
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame


class Actor:
    def __init__(self):
        self.controller = None

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def update(self, dt: float) -> None:
        pass


'''
Actor has a Controller
- PC controller is (usually) input from mouse/keyboard
- NPC controller is a Behaviour

Behaviours:
- follow a schedule
- wander(amount)
- hunt an Actor (usually the PC)

Schedule:
- target time: wander(small)
- target time: walk to location
- target time: wait
- target time: sleep
- ...
'''
