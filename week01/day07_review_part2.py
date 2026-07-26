"""
Day 7: Review Part 2 (lists + loops mini challenge)
Time goal: about 10–20 minutes

WHAT YOU'RE DOING
-----------------
Put lists and loops together. This is your Week 1 "boss level" —
still short, just a little more practice.

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run ALL of Week 1:
    python3 tests/run_acceptance.py 1

When everything passes, commit and push so your brother can review!
"""


def shopping_total(prices):
    """
    prices is a list of numbers, like [2.50, 1.25, 3.00]
    Return the total cost (add them all up).
    Example: shopping_total([2.5, 1.25, 3.0]) → 6.75
    """
    # >>> YOUR CODE HERE
    pass


def only_long_words(words):
    """
    words is a list of strings.
    Return a NEW list with only the words that have more than 3 letters.

    Example:
      only_long_words(["cat", "lion", "dog", "tiger"])
      → ["lion", "tiger"]

    Hint:
      result = []
      for word in words:
          if len(word) > 3:
              result.append(word)
      return result
    """
    # >>> YOUR CODE HERE
    pass


def countdown(n):
    """
    Return a list counting down from n to 1.
    Example: countdown(3) → [3, 2, 1]

    Hint: return list(range(n, 0, -1))
    or build it with a loop.
    """
    # >>> YOUR CODE HERE
    pass


def average(numbers):
    """
    Return the average (mean) of the numbers.
    Assume the list is not empty.
    Hint: total / len(numbers)
    Example: average([2, 4, 6]) → 4.0
    """
    # >>> YOUR CODE HERE
    pass


def fizz_label(n):
    """
    A tiny classic puzzle:
      - if n is divisible by 3 AND 5, return "FizzBuzz"
      - if n is divisible by 3 only, return "Fizz"
      - if n is divisible by 5 only, return "Buzz"
      - otherwise return the number as a string (use str(n))

    Hint: check 3 AND 5 first!
    Examples:
      fizz_label(15) → "FizzBuzz"
      fizz_label(9)  → "Fizz"
      fizz_label(10) → "Buzz"
      fizz_label(7)  → "7"
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 7 playground")
    print(shopping_total([2.5, 1.25, 3.0]))
    print(only_long_words(["cat", "lion", "dog", "tiger"]))
    print(countdown(5))
    print(average([2, 4, 6]))
    print(fizz_label(15), fizz_label(9), fizz_label(10), fizz_label(7))
