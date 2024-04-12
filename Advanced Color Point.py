from colorpoint import ColoredPoint

class AdvancedColorPoint(ColoredPoint):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        if color in self.COLORS:
            self._color = color
        else:
            raise Exception(f"That is an invalid color. Accepted colors are {self.COLORS}")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        raise Exception("Dont try to hack my point!!")

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


p = AdvancedColorPoint(10, 10, "blue")
print(p)
#let me try to hack it
p.color = "bogdan"

print(p)