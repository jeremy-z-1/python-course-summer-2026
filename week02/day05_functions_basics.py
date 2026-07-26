"""
Day 5: Functions 1 — Basics and main
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
A function is a reusable chunk of code with a name.

  def say_hi():
      return "hi"

  def add(a, b):
      return a + b

The special block at the bottom:

  if __name__ == "__main__":
      ...

runs only when you start THIS file directly (not when tests import it).
People often put a main() function there as the "starting point."

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 2 --day 5
"""


def say_hello():
    """
    Return the exact string: Hello!
    """
    # >>> YOUR CODE HERE
    pass


def add_two(a, b):
    """
    Return a + b.
    Example: add_two(2, 5) → 7
    """
    # >>> YOUR CODE HERE
    pass


def square(n):
    """
    Return n times n.
    Example: square(4) → 16
    """
    # >>> YOUR CODE HERE
    pass


def describe_today():
    """
    Return the exact string: Learning functions
    """
    # >>> YOUR CODE HERE
    pass


def main():
    """
    This is your program's starting helper.
    Return a short status string by calling describe_today().
    Exact return value: "Ready: Learning functions"

    Hint:
      return "Ready: " + describe_today()
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 5 playground (Week 2)")
    print(say_hello())
    print(add_two(2, 5))
    print(square(4))
    print(main())
