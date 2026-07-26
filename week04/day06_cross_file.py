"""
Day 6: Cross-file programming
Time goal: about 10–20 minutes

WHAT YOU'RE LEARNING
--------------------
Big programs split code into multiple files.

This folder has toolbox.py with helper functions.
You can import them like this:

  from week04.toolbox import double, shout, add_exclaim

Or, when running from this folder in some setups:
  from toolbox import double

For this course / tests, use:
  from week04.toolbox import double, shout, add_exclaim

YOUR JOB
--------
1) Fill in week04/toolbox.py
2) Fill in the functions below using those imports

Then run:
    python3 tests/run_acceptance.py 4 --day 6
"""

from week04.toolbox import add_exclaim, double, shout


def double_list(numbers):
    """
    Return a new list where every number is doubled using toolbox.double.
    Example: double_list([1, 2, 3]) → [2, 4, 6]
    """
    # >>> YOUR CODE HERE
    pass


def loud_greeting(name):
    """
    Build a greeting using toolbox helpers:
      shout("hello " + name) then add_exclaim(...)
    Example: loud_greeting("Jeremy") → "HELLO JEREMY!"
    """
    # >>> YOUR CODE HERE
    pass


def scoreboard(points):
    """
    points is a list of numbers.
    Return a dict:
      {
        "raw": points,
        "doubled": double_list(points),
      }
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 6 playground (Week 4)")
    print(double_list([1, 2, 3]))
    print(loud_greeting("Jeremy"))
    print(scoreboard([1, 2, 3]))
