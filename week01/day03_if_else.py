"""
Day 3: If-Else (making decisions)
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
Programs often need to choose what to do.

  if score >= 90:
      print("Great job!")
  else:
      print("Keep practicing!")

Important comparison signs:
  ==   equal to
  !=   not equal to
  >    greater than
  <    less than
  >=   greater than or equal to
  <=   less than or equal to

True and False are called booleans (yes/no values).

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 1 --day 3
"""


def is_even(number):
    """
    Return True if number is even, otherwise return False.
    Hint: even numbers have no remainder when divided by 2.
          Use: number % 2 == 0
    Example: is_even(4) → True
             is_even(5) → False
    """
    # >>> YOUR CODE HERE
    if number % 2 == 0:
        return True
    else:
        return False


def is_positive(number):
    """
    Return True if number is greater than 0, otherwise False.
    Example: is_positive(3) → True
             is_positive(-1) → False
             is_positive(0) → False
    """
    # >>> YOUR CODE HERE
    if number > 0:
        return True
    else:
        return False

def bigger(a, b):
    """
    Return whichever number is bigger.
    If they are equal, return either one (they're the same).
    Example: bigger(3, 10) → 10
    """
    # >>> YOUR CODE HERE
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a


def can_ride(height_inches):
    """
    A ride needs you to be at least 48 inches tall.
    If height_inches >= 48, return "Yes"
    Otherwise return "No"
    Example: can_ride(50) → "Yes"
             can_ride(40) → "No"
    """
    # >>> YOUR CODE HERE
    if height_inches >= 48:
        return "Yes"
    else:
        return "No"

def letter_grade(score):
    """
    Return a letter grade:
      score >= 90 → "A"
      score >= 80 → "B"
      score >= 70 → "C"
      anything else → "Keep practicing"

    Hint: check the highest scores first with if / elif / else.
    Example:
      letter_grade(95) → "A"
      letter_grade(82) → "B"
      letter_grade(70) → "C"
      letter_grade(50) → "Keep practicing"
    """
    # >>> YOUR CODE HERE
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "Keep practicing"

if __name__ == "__main__":
    print("Day 3 playground")
    print("is_even(4):", is_even(4))
    print("is_positive(-2):", is_positive(-2))
    print("bigger(3, 10):", bigger(3, 10))
    print("can_ride(50):", can_ride(50))
    print("letter_grade(95):", letter_grade(95))
