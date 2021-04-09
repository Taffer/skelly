''' Skelly src package.

By Chris Herborth (https://github.com/Taffer)
MIT license, see LICENSE.md for details.
'''

from .GameSettings import GameSettings
from .I18n import I18N_EN, I18N_ES
from .Resources import RESOURCE_LIST
from .TextHandler import TextHandler

__all__ = [
    'GameSettings',
    'I18N_EN',
    'I18N_ES',
    'RESOURCE_LIST',
    'TextHandler',
]
