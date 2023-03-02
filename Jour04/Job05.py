import math
from Job04 import *


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return (self.radius * self.radius) * math.pi


Rect1 = Rectangle(7, 4)
Cercle1 = Cercle(5)
print(Rect1.aire())
print(Cercle1.aire())
