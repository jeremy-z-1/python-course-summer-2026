"""
Day 3: Nested Loops
Time goal: about 10–20 minutes

WHAT YOU'RE LEARNING
--------------------
A nested loop is a loop inside another loop.

  for row in range(2):
      for col in range(3):
          print(row, col)

That prints every (row, col) pair:
  0 0, 0 1, 0 2, then 1 0, 1 1, 1 2

This is perfect for walking through a 2-D grid.

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 2 --day 3
"""


def count_cells(grid):
    """
    Count how many total cells are in the grid.
    Hint: nested loops, or rows * cols if every row is the same length.
    Example: count_cells([[1, 2], [3, 4], [5, 6]]) → 6
    """
    # >>> YOUR CODE HERE
    pass


def sum_all(grid):
    """
    Add up EVERY number in the 2-D grid.
    Hint:
      total = 0
      for row in grid:
          for value in row:
              total = total + value
      return total
    Example: sum_all([[1, 2], [3, 4]]) → 10
    """
    # >>> YOUR CODE HERE
    pass


def make_grid(rows, cols, fill):
    """
    Build a 2-D list with `rows` rows and `cols` columns.
    Every cell should be the value `fill`.

    Example: make_grid(2, 3, 0) → [[0, 0, 0], [0, 0, 0]]

    Hint:
      grid = []
      for r in range(rows):
          row = []
          for c in range(cols):
              row.append(fill)
          grid.append(row)
      return grid
    """
    # >>> YOUR CODE HERE
    pass


def flatten(grid):
    """
    Turn a 2-D list into a 1-D list (all values in order, row by row).
    Example: flatten([[1, 2], [3, 4]]) → [1, 2, 3, 4]
    """
    # >>> YOUR CODE HERE
    pass


def multiplication_row(n, times):
    """
    Return a list: [n*1, n*2, ..., n*times]
    Example: multiplication_row(3, 4) → [3, 6, 9, 12]

    Hint: build a list with a loop over range(1, times + 1).
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 3 playground (Week 2)")
    g = [[1, 2], [3, 4], [5, 6]]
    print("cells:", count_cells(g))
    print("sum:", sum_all([[1, 2], [3, 4]]))
    print("grid:", make_grid(2, 3, 0))
    print("flat:", flatten([[1, 2], [3, 4]]))
    print("row:", multiplication_row(3, 4))
