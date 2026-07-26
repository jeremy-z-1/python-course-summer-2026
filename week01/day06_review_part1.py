"""
Day 6: Review Part 1 (numbers + strings + if-else)
Time goal: about 10–15 minutes

WHAT YOU'RE DOING
-----------------
No brand-new big idea today. Practice mixing what you already learned.

Remember:
  - ints and floats are numbers
  - strings are text
  - if / else helps you make decisions

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 1 --day 6
"""


def double_number(n):
    """
    Return n times 2.
    Example: double_number(7) → 14
    """
    # >>> YOUR CODE HERE
    pass


def describe_number(n):
    """
    Return a string describing the number:
      - if n > 0: return "positive"
      - if n < 0: return "negative"
      - if n == 0: return "zero"
    """
    # >>> YOUR CODE HERE
    pass


def make_label(name, age):
    """
    Return a label like: "Name: Jeremy, Age: 13"
    Example: make_label("Jeremy", 13) → "Name: Jeremy, Age: 13"

    Hint: you may need str(age) to turn the number into text:
      return "Name: " + name + ", Age: " + str(age)
    """
    # >>> YOUR CODE HERE
    pass


def password_ok(password):
    """
    A password is ok if it has at least 6 characters.
    Return True if len(password) >= 6, otherwise False.
    Example: password_ok("abcdef") → True
             password_ok("hi") → False
    """
    # >>> YOUR CODE HERE
    pass


def choose_snack(hungry):
    """
    hungry will be True or False.
    If hungry is True, return "Get a snack"
    If hungry is False, return "Maybe later"
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 6 playground")
    print(double_number(7))
    print(describe_number(-3))
    print(make_label("Jeremy", 13))
    print(password_ok("secret"))
    print(choose_snack(True))
