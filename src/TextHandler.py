# Skelly text handler for internationalization.
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

from typing import Union


class TextHandler:
    def __init__(self):
        self.default = None
        self.current = None
        self.lang = {}

    def addLanguage(self, code: str, dictionary: dict):
        ''' Add language strings. The first one is the default.
        '''
        self.lang[code] = dictionary
        if self.default is None:
            self.default = code

    def setLanguage(self, code: str):
        self.current = code

    def getText(self, tag: str) -> Union[str, dict, list]:
        return self.lang[self.current].get(tag, self.lang[self.default].get(tag, f'~~{tag} not found~~'))

    def code_for(self, language: str) -> str:
        ''' Return the two-character language code for the named language.
        '''
        if language in ('English', 'Ingles'):
            return 'en'
        elif language in ('Spanish', 'Español'):
            return 'es'

        return 'en'  # Default is the development language, sorry.
