# Skelly map trigger.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

from . import Actor


class Trigger:
    def __init__(self: 'Trigger'):
        ''' Trigger on a tile, calls on_enter/on_exit functions when moving.
        '''
        pass

    def on_enter(self: 'Trigger', x: int, y: int, actor: Actor):
        ''' Triggered when an actor enters this tile.
        '''
        pass

    def on_exit(self: 'Trigger', x: int, y: int, actor: Actor):
        ''' Triggered when an actor exits this tile.
        '''
        pass
