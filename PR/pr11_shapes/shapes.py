"""Shapes."""


class Shape:
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self._color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self._color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self._color

    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Constructor of the circle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        self.radius = radius
        self._color = color

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f'Circle (r: {self.radius}, color: {self._color})'

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return self.radius * self.radius * 3.14


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self._color = color
        self.side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f'Square (a: {self.side}, color: {self._color})'

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the circle is side * side.
        """
        return self.side * self.side


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""

    def __init__(self, color, a, b):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        :param color:
        :param a:
        :param b:
        """
        self._color = color
        self.a = a
        self.b = b

    def __repr__(self):
        """
        Return representation of the rectangle.

        For this exercise, this should return a string:
        Rectangle (l: {a}, w: {b}, color: {color})
        :return:
        """
        return f'Rectangle (l: {self.a}, w: {self.b}, color: {self._color})'

    def get_area(self):
        """
        Calculate the area of the square.

        Area of the circle is a * b.
        :return:
        """
        return self.a * self.b


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Constructor should create a list to store all the shapes."""
        self.paints = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.paints.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.paints

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total = 0
        for shape in self.get_shapes():
            total += shape.get_area()
        return total

    def get_circles(self) -> list:
        """Return only circles."""
        circles = []
        for shape in self.get_shapes():
            if type(shape) is Circle:
                circles.append(shape)
        return circles

    def get_squares(self) -> list:
        """Return only squares."""
        squares = []
        for shape in self.get_shapes():
            if type(shape) is Square:
                squares.append(shape)
        return squares

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangles = []
        for shape in self.get_shapes():
            if type(shape) is Rectangle:
                rectangles.append(shape)
        return rectangles


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(len(paint.get_circles()))
