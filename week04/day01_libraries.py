"""
Day 1: Libraries
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
A library (module) is code someone else wrote that you can import.

  import math
  math.sqrt(9)      → 3.0
  math.ceil(3.2)    → 4
  math.floor(3.8)   → 3
  math.pi           → 3.14159...

You can also import one name:
  from math import sqrt

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 4 --day 1
"""

import math


def square_root(n):
    """
    Return the square root of n using math.sqrt.
    Example: square_root(9) → 3.0
    """
    # >>> YOUR CODE HERE
    pass


def round_up(n):
    """
    Return n rounded UP to the next whole number (math.ceil).
    Example: round_up(3.2) → 4
    """
    # >>> YOUR CODE HERE
    pass


def round_down(n):
    """
    Return n rounded DOWN (math.floor).
    Example: round_down(3.8) → 3
    """
    # >>> YOUR CODE HERE
    pass


def circle_area(radius):
    """
    Return the area of a circle: pi * radius * radius
    Use math.pi
    Example: circle_area(1) → math.pi  (about 3.14159...)
    """
    # >>> YOUR CODE HERE
    pass


def hypotenuse(a, b):
    """
    For a right triangle with legs a and b, return the hypotenuse.
    Hint: math.sqrt(a*a + b*b)  or  math.hypot(a, b)
    Example: hypotenuse(3, 4) → 5.0
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 1 playground (Week 4)")
    print(square_root(9))
    print(round_up(3.2), round_down(3.8))
    print(circle_area(1))
    print(hypotenuse(3, 4))
