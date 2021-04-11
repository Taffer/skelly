#!/usr/bin/env python3
# Skelly, a story of the Skeleton War
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

import pygame
import pygame.freetype
import pygame.gfxdraw
import sys
import time

from Game import Game, PYGAME_VERSION, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH


def main():
    if PYGAME_VERSION > pygame.version.vernum:
        raise SystemExit('Pygame version too old: {0}'.format(pygame.version.ver))

    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    skelly = Game(window)

    ignore_events = [pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN,
                     pygame.VIDEORESIZE, pygame.VIDEOEXPOSE, pygame.AUDIODEVICEADDED, pygame.AUDIODEVICEREMOVED,
                     pygame.FINGERMOTION, pygame.FINGERDOWN, pygame.FINGERUP, pygame.MULTIGESTURE,
                     pygame.DROPBEGIN, pygame.DROPCOMPLETE, pygame.DROPFILE, pygame.DROPTEXT, pygame.MIDIIN, pygame.MIDIOUT,
                     pygame.CONTROLLERDEVICEADDED, pygame.JOYDEVICEADDED, pygame.CONTROLLERDEVICEREMOVED,
                     pygame.JOYDEVICEREMOVED, pygame.CONTROLLERDEVICEREMAPPED]
    pygame.event.set_blocked(ignore_events)

    prev_time = time.time()
    dt = 0
    while True:
        now = time.time()
        dt = now - prev_time
        prev_time = now

        skelly.update(dt)
        skelly.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            skelly.manager.process_events(event)

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                skelly.keypressed(event)
            elif event.type == pygame.KEYUP:
                skelly.keyreleased(event)
            elif event.type == pygame.MOUSEMOTION:
                skelly.mousemoved(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                skelly.mousedown(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                skelly.mouseup(event)
            elif event.type == pygame.USEREVENT:
                skelly.userevent(event)


if __name__ == '__main__':
    main()
