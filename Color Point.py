import random

from point import Point


class ColoredPoint(Point): # this class inherits from point
    COLORS = ["red", "blue", "green", "yellow", "purple", "pink", "beige", "bordeaux",
              "marsala", "peach", "turquoise", "saffron", "magenta"]
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"That is an invalid color. Accepted colors are {self.COLORS}")

    def __str__(self):
        return f"{self.color}({self.x}, {self.y})"

    @classmethod
    def add_extra_color(cls, color):
        cls.COLORS.append(color)

    @property
    def distance_origin(self):
        result = (self.x**2 + self.y**2)**0.5
        if result == int(result):
            return int(result)
        else:
            return result


# lets create a list of random 5 colored points
colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.choice(ColoredPoint.COLORS)
                     )
    )

if __name__ == "__main__":
    print(colored_points)
    # lets add orange as an extra color
    ColoredPoint.add_extra_color("orange")
    p2 = ColoredPoint(3, 4, "orange")
    p2.x = 77 # this feels wrong, lets fix it in the child class
    print(p2)
    print(f"p2={p2} and has distance to origin={p2.distance_origin}")