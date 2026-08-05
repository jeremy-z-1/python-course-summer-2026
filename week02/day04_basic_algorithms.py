"""
Day 4: Basic Algorithms
Time goal: about 10–20 minutes

WHAT YOU'RE LEARNING
--------------------
An algorithm is a clear step-by-step plan to solve a problem.

Today you'll practice tiny classic plans:
  - search: is a value in the list?
  - count: how many times does something appear?
  - reverse: flip the order
  - sorted check: are the numbers in order?

You can use loops you already know. Built-ins like `in` / `count` are ok too,
but trying a loop helps you understand the idea.

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 2 --day 4
"""


def contains(items, target):
    """
    Return True if target is in items, otherwise False.
    Example: contains([1, 2, 3], 2) → True
             contains([1, 2, 3], 9) → False
    """
    # >>> YOUR CODE HERE
    for number in items:
        if number == target:
            return True
    return False


def count_occurrences(items, target):
    """
    How many times does target appear in items?
    Example: count_occurrences([1, 2, 1, 1], 1) → 3
    """
    # >>> YOUR CODE HERE
    count = 0
    for number in items:
        if number == target:
            count += 1
    return count


def find_index(items, target):
    """
    Return the index (position) of the first time target appears.
    If it is not found, return -1.

    Example:
      find_index(["a", "b", "c"], "b") → 1
      find_index(["a", "b", "c"], "z") → -1

    Hint:
      for i in range(len(items)):
          if items[i] == target:
              return i
      return -1
    """
    # >>> YOUR CODE HERE
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def reverse_list(items):
    """
    Return a NEW list with the items in reverse order.
    Do not worry about changing the original.
    Example: reverse_list([1, 2, 3]) → [3, 2, 1]

    Hint: return items[::-1]  or build a new list in a loop.
    """
    # >>> YOUR CODE HERE
    reversed_list = []
    for i in range(len(items) - 1, -1, -1):
        reversed_list.append(items[i])
    return reversed_list


def is_sorted_ascending(numbers):
    """
    Return True if the list is sorted from small to big (or equal).
    Empty lists and 1-item lists count as sorted.

    Example:
      is_sorted_ascending([1, 2, 2, 5]) → True
      is_sorted_ascending([3, 1, 2]) → False

    Hint: compare each number to the next one.
    """
    # >>> YOUR CODE HERE
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print("Day 4 playground (Week 2)")
    print(contains([1, 2, 3], 2))
    print(count_occurrences([1, 2, 1, 1], 1))
    print(find_index(["a", "b", "c"], "b"))
    print(reverse_list([1, 2, 3]))
    print(is_sorted_ascending([1, 2, 2, 5]))
