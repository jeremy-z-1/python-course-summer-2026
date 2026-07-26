"""
Day 6: Functions 2 — Parameters and arguments
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
Parameters are the names in the function definition.
Arguments are the real values you pass in when you call it.

  def greet(name):          # name is a parameter
      return "Hi, " + name

  greet("Jeremy")           # "Jeremy" is an argument

Default values:
  def greet(name, title="Friend"):
      return title + " " + name

  greet("Ada")                 → "Friend Ada"
  greet("Ada", title="Dr.")    → "Dr. Ada"

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 2 --day 6
"""


def greet(name, title="Friend"):
    """
    Return: title + " " + name
    Examples:
      greet("Ada") → "Friend Ada"
      greet("Ada", "Dr.") → "Dr. Ada"
    """
    # >>> YOUR CODE HERE
    pass


def power(base, exponent=2):
    """
    Return base raised to exponent.
    Hint: base ** exponent
    Examples:
      power(3) → 9
      power(2, 3) → 8
    """
    # >>> YOUR CODE HERE
    pass


def full_label(first, last, age):
    """
    Return: "first last (age)"
    Example: full_label("Ada", "Lovelace", 36) → "Ada Lovelace (36)"
    Hint: use str(age)
    """
    # >>> YOUR CODE HERE
    pass


def apply_discount(price, percent):
    """
    price is the original price.
    percent is how much to take off (example: 10 means 10% off).
    Return the new price after the discount.

    Example: apply_discount(100, 10) → 90.0
    Hint: price * (1 - percent / 100)
    """
    # >>> YOUR CODE HERE
    pass


def average_of_three(a, b, c):
    """
    Return the average of a, b, and c as a float-friendly number.
    Example: average_of_three(2, 4, 6) → 4.0
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 6 playground (Week 2)")
    print(greet("Ada"))
    print(greet("Ada", "Dr."))
    print(power(3), power(2, 3))
    print(full_label("Ada", "Lovelace", 36))
    print(apply_discount(100, 10))
    print(average_of_three(2, 4, 6))
