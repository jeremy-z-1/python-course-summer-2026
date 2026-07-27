"""
Day 2: Strings
Time goal: about 5–10 minutes

WHAT YOU'RE LEARNING
--------------------
A string is text. In Python you wrap text in quotes:

  name = "Jeremy"
  greeting = 'hi'     # single quotes also work

You can join strings with + :
  "Hello, " + "Jeremy"  →  "Hello, Jeremy"

Useful tools:
  len("cat")        → 3          (how many characters)
  "hi".upper()      → "HI"
  "HI".lower()      → "hi"

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 1 --day 2
"""


def make_greeting():
    """
    Return the exact string: Hello, Python!
    (Include the comma and the exclamation mark.)
    """
    # >>> YOUR CODE HERE
    return "Hello, Python!"


def greet(name):
    """
    Return a greeting using the name you are given.
    Example: greet("Jeremy") should return "Hello, Jeremy!"
    Hint: return "Hello, " + name + "!"
    """
    # >>> YOUR CODE HERE
    return "Hello, " + name + "!"


def full_name(first, last):
    """
    Put first and last together with a space in the middle.
    Example: full_name("Ada", "Lovelace") → "Ada Lovelace"
    """
    # >>> YOUR CODE HERE
    return first + " " + last


def shout(text):
    """
    Return the text in ALL CAPS.
    Hint: use text.upper()
    Example: shout("hi") → "HI"
    """
    # >>> YOUR CODE HERE
    return text.upper()


def whisper(text):
    """
    Return the text in all lowercase.
    Hint: use text.lower()
    Example: whisper("HI") → "hi"
    """
    # >>> YOUR CODE HERE
    return text.lower()


def count_characters(text):
    """
    Return how many characters are in the text.
    Hint: use len(text)
    Example: count_characters("cat") → 3
    """
    # >>> YOUR CODE HERE
    return len(text)


if __name__ == "__main__":
    print("Day 2 playground")
    print(make_greeting())
    print(greet("Jeremy"))
    print(full_name("Ada", "Lovelace"))
    print(shout("hello"))
    print(whisper("HELLO"))
    print("letters in 'python':", count_characters("python"))
