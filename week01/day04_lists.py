"""
Day 4: Lists (Python's arrays)
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
A list holds many values in order, inside square brackets:

  fruits = ["apple", "banana", "cherry"]
  numbers = [10, 20, 30]

Useful ideas:
  fruits[0]        → "apple"     (first item; counting starts at 0!)
  fruits[-1]       → "cherry"    (last item)
  len(fruits)      → 3
  fruits.append("date")          (add to the end)

In some languages this is called an "array."
In Python, beginners usually use lists.

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 1 --day 4
"""


def make_number_list():
    """
    Return a list with these exact numbers: 1, 2, 3, 4, 5
    Example: return [1, 2, 3, 4, 5]
    """
    # >>> YOUR CODE HERE
    pass


def first_item(items):
    """
    Return the first item in the list.
    Hint: items[0]
    Example: first_item(["a", "b", "c"]) → "a"
    """
    # >>> YOUR CODE HERE
    pass


def last_item(items):
    """
    Return the last item in the list.
    Hint: items[-1]
    Example: last_item(["a", "b", "c"]) → "c"
    """
    # >>> YOUR CODE HERE
    pass


def list_length(items):
    """
    Return how many items are in the list.
    Hint: len(items)
    """
    # >>> YOUR CODE HERE
    pass


def add_favorite(items, new_item):
    """
    Make a NEW list that has everything from items,
    plus new_item at the end. Then return that new list.

    Hint (easy way):
      return items + [new_item]

    Example: add_favorite(["pizza"], "tacos") → ["pizza", "tacos"]
    """
    # >>> YOUR CODE HERE
    pass


def second_item(items):
    """
    Return the second item in the list.
    Hint: items[1]  (remember: 0 is first, so 1 is second)
    Example: second_item(["red", "green", "blue"]) → "green"
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 4 playground")
    print(make_number_list())
    colors = ["red", "green", "blue"]
    print("first:", first_item(colors))
    print("second:", second_item(colors))
    print("last:", last_item(colors))
    print("length:", list_length(colors))
    print("add:", add_favorite(["pizza"], "tacos"))
