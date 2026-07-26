"""
Day 7: Week 4 Review
Time goal: about 15–20 minutes

WHAT YOU'RE DOING
-----------------
Mix libraries, classes, inheritance, and a tiny bit of design.

YOUR JOB
--------
Fill in where you see:
    # >>> YOUR CODE HERE

Then run ALL of Week 4:
    python3 tests/run_acceptance.py 4
"""

import math


class Rectangle:
    def __init__(self, width, height):
        """
        Save width and height on the object.
        """
        # >>> YOUR CODE HERE
        pass

    def area(self):
        """
        Return width * height.
        """
        # >>> YOUR CODE HERE
        pass

    def perimeter(self):
        """
        Return 2 * (width + height).
        """
        # >>> YOUR CODE HERE
        pass


class Square(Rectangle):
    def __init__(self, side):
        """
        A square is a rectangle with width == height == side.
        Hint: call Rectangle's setup: Rectangle.__init__(self, side, side)
        or: super().__init__(side, side)
        """
        # >>> YOUR CODE HERE
        pass


def circle_circumference(radius):
    """
    Return 2 * math.pi * radius
    """
    # >>> YOUR CODE HERE
    pass


def describe_shape(shape):
    """
    shape has .area()
    Return: "area=<value>"
    Example: describe_shape(Rectangle(2, 3)) → "area=6"
    Hint: return "area=" + str(shape.area())
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 7 playground (Week 4)")
    r = Rectangle(2, 3)
    print(r.area(), r.perimeter())
    s = Square(4)
    print(s.area(), s.perimeter())
    print(circle_circumference(1))
    print(describe_shape(r))
