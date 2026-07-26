"""
Day 2: Reading from a file
Time goal: about 10–20 minutes

WHAT YOU'RE LEARNING
--------------------
Python can open a file and read its text:

  with open(path) as f:
      text = f.read()

  with open(path) as f:
      lines = f.readlines()

There are sample files in week03/data/:
  hello.txt
  scores.csv

The tests will pass you the full path — you just open that path.

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 3 --day 2
"""


def read_whole_file(path):
    """
    Open the file at path and return its full text as one string.
    Hint:
      with open(path) as f:
          return f.read()
    """
    # >>> YOUR CODE HERE
    pass


def count_lines(path):
    """
    Return how many lines are in the file.
    Hint: read the lines and use len(...).
    Empty final newlines can vary by editor — for our sample files
    this matches the number of newline-separated lines.
    """
    # >>> YOUR CODE HERE
    pass


def read_first_line(path):
    """
    Return the first line of the file, without a trailing newline.
    Hint:
      with open(path) as f:
          return f.readline().rstrip("\n")
    """
    # >>> YOUR CODE HERE
    pass


def list_lines(path):
    """
    Return a list of all lines with newline characters removed.
    Hint:
      with open(path) as f:
          return [line.rstrip("\n") for line in f]
    """
    # >>> YOUR CODE HERE
    pass


def csv_names(path):
    """
    Read a simple CSV that looks like:

      name,score
      Ada,95
      Grace,88

    Skip the header row. Return a list of the names only.
    Example result: ["Ada", "Grace", "Alan"]

    Hint:
      lines = list_lines(path)
      names = []
      for line in lines[1:]:
          parts = line.split(",")
          names.append(parts[0])
      return names
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    import os

    here = os.path.dirname(os.path.abspath(__file__))
    hello = os.path.join(here, "data", "hello.txt")
    scores = os.path.join(here, "data", "scores.csv")
    print("Day 2 playground (Week 3)")
    print(read_whole_file(hello))
    print("lines:", count_lines(hello))
    print("first:", read_first_line(hello))
    print("all:", list_lines(hello))
    print("names:", csv_names(scores))
