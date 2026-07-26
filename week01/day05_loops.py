"""
Day 5: Loops
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
A loop repeats code.

For loop over a list:
  for fruit in ["apple", "banana"]:
      print(fruit)

For loop over a range of numbers:
  for i in range(3):
      print(i)     # prints 0, then 1, then 2

  for i in range(1, 4):
      print(i)     # prints 1, then 2, then 3

While loop (careful — needs a stopping condition):
  count = 0
  while count < 3:
      print(count)
      count = count + 1

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 1 --day 5
"""


def count_to(n):
    """
    Return a list of numbers from 1 to n (including n).
    Hint: return list(range(1, n + 1))
    Example: count_to(3) → [1, 2, 3]
    """
    # >>> YOUR CODE HERE
    pass


def sum_list(numbers):
    """
    Add up all numbers in the list and return the total.
    Hint: start with total = 0, then loop and add each number.
    Example: sum_list([1, 2, 3]) → 6

    You may write it with a loop like this:
      total = 0
      for number in numbers:
          total = total + number
      return total
    """
    # >>> YOUR CODE HERE
    pass


def repeat_word(word, times):
    """
    Return a list that has the same word repeated `times` times.
    Example: repeat_word("hi", 3) → ["hi", "hi", "hi"]

    Hint:
      result = []
      for i in range(times):
          result.append(word)
      return result
    """
    # >>> YOUR CODE HERE
    pass


def count_evens(numbers):
    """
    Count how many even numbers are in the list.
    Hint: use a loop + if number % 2 == 0
    Example: count_evens([1, 2, 3, 4]) → 2
    """
    # >>> YOUR CODE HERE
    pass


def find_max(numbers):
    """
    Return the biggest number in the list.
    Assume the list is not empty.
    Hint: keep a variable called biggest, update it in a loop.
    Example: find_max([3, 10, 2]) → 10

    You can use max(numbers) if you want — both are fine for now.
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 5 playground")
    print(count_to(5))
    print(sum_list([1, 2, 3, 4]))
    print(repeat_word("hi", 3))
    print(count_evens([1, 2, 3, 4, 5, 6]))
    print(find_max([3, 10, 2]))
