# Skelly UI - Button
#
# By Chris Herborth (https://github.com/Taffer)
# MIT license, see LICENSE.md for details.

from . import Base
from . import ImageButton
from . import Label


class Button(Base):
    def __init__(self, x, y, texture, text, font, color):
        super().__init__()

        self.x = x
        self.y = y

        self.imageButton = ImageButton.ImageButton(x, y, texture)
        rect = texture.get_rect()
        rect.left = x
        rect.top = y

        label_x = x + rect.width / 2
        label_y = y + (rect.height - font.get_height()) / 2
        self.labelButton = Label.Label(label_x, label_y, text, font, color, 'centre')

    def draw(self):
        self.imageButton.draw()
        self.labelButton.draw()
