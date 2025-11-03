import time

from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        mouth = [43, 44, 50, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open = True):
        eyes = [17, 18, 21, 22, 26, 29]
        for pixel in eyes:
            if pixel not in [17, 18, 21, 22]:
                self.pixels[pixel] = self.BLANK if wide_open else self.complexion()
            else: self.pixels[pixel] = self.BLANK
    def blink(self, delay=0.25):
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
