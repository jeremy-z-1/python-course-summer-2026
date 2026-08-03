"""
Day 1: 2-D Lists (lists inside lists)
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
A 2-D list is a list where each item is another list.
Think of it like a grid / table / spreadsheet:

  grid = [
      [1, 2, 3],   # row 0
      [4, 5, 6],   # row 1
  ]

Useful ideas:
  grid[0]       → [1, 2, 3]   (whole first row)
  grid[1][2]    → 6           (row 1, column 2)
  len(grid)     → 2           (number of rows)
  len(grid[0])  → 3           (number of columns in first row)

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 2 --day 1
"""


def make_tiny_grid():
    """
    Return this exact 2-D list:
      [[1, 2],
       [3, 4]]
    """
    # >>> YOUR CODE HERE
    return [[1, 2],
       [3, 4]]


def get_cell(grid, row, col):
    """
    Return the value at grid[row][col].
    Example:
      get_cell([[1, 2], [3, 4]], 1, 0) → 3
    """
    # >>> YOUR CODE HERE
    return grid[row][col]


def row_count(grid):
    """
    Return how many rows the grid has.
    Hint: len(grid)
    Example: row_count([[1, 2], [3, 4], [5, 6]]) → 3
    """
    # >>> YOUR CODE HERE
    return len(grid)


def column_count(grid):
    """
    Return how many columns the first row has.
    Assume the grid is not empty and every row has the same length.
    Hint: len(grid[0])
    Example: column_count([[1, 2, 3], [4, 5, 6]]) → 3
    """
    # >>> YOUR CODE HERE
    return len(grid[0])


def first_row(grid):
    """
    Return the first row (a normal 1-D list).
    Example: first_row([[10, 20], [30, 40]]) → [10, 20]
    """
    # >>> YOUR CODE HERE
    return grid[0]


def sum_row(grid, row):
    """
    Add up all numbers in the given row index and return the total.
    Hint: you can use sum(grid[row]) or a loop.
    Example: sum_row([[1, 2, 3], [4, 5, 6]], 0) → 6
    """
    # >>> YOUR CODE HERE
    return sum(grid[row])


if __name__ == "__main__":
    print("Day 1 playground (Week 2)")
    print(make_tiny_grid())
    g = [[1, 2, 3], [4, 5, 6]]
    print("cell:", get_cell(g, 1, 2))
    print("rows:", row_count(g), "cols:", column_count(g))
    print("first row:", first_row(g))
    print("sum row 1:", sum_row(g, 1))
