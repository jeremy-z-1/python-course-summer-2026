"""
Day 1: Integers vs Floats
Time goal: about 5–10 minutes

WHAT YOU'RE LEARNING
--------------------
In Python we mostly use two kinds of numbers:

  - int   (integer)  → whole numbers like 0, 1, 42, -7
  - float (floating) → numbers with a decimal like 3.5, 0.25, -2.0

In some other languages people say "double" for decimal numbers.
In Python, that idea is just called a float.

EXAMPLES (already done for you — read these!)
---------------------------------------------
age = 13          # int
height = 5.4      # float
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>

YOUR JOB
--------
Fill in each function below where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 1 --day 1
"""


def make_integer():
    """
    Return any whole number (int).
    Example: return 10
    """
    # >>> YOUR CODE HERE
    pass


def make_float():
    """
    Return any number with a decimal (float).
    Example: return 3.5
    """
    # >>> YOUR CODE HERE
    pass


def add_numbers(a, b):
    """
    Return a + b.
    Hint: use the + sign.
    """
    # >>> YOUR CODE HERE
    pass


def subtract_numbers(a, b):
    """
    Return a - b.
    """
    # >>> YOUR CODE HERE
    pass


def multiply_numbers(a, b):
    """
    Return a * b.
    Hint: * means multiply in Python.
    """
    # >>> YOUR CODE HERE
    pass


def divide_numbers(a, b):
    """
    Return a / b.
    Hint: / usually gives a float in Python (example: 5 / 2 is 2.5).
    """
    # >>> YOUR CODE HERE
    pass


# ------------------------------------------------------------
# Optional: run this file by itself to play around.
# In Cursor's terminal:  python3 week01/day01_numbers.py
# ------------------------------------------------------------
if __name__ == "__main__":
    print("Day 1 playground")
    print("make_integer() ->", make_integer())
    print("make_float()   ->", make_float())
    print("2 + 3 =", add_numbers(2, 3))
    print("10 - 4 =", subtract_numbers(10, 4))
    print("3 * 5 =", multiply_numbers(3, 5))
    print("10 / 4 =", divide_numbers(10, 4))
