"""
Day 7: Week 2 Review
Time goal: about 15–20 minutes

WHAT YOU'RE DOING
-----------------
Mix 2-D lists, dicts, nested loops, tiny algorithms, and functions.
Still short — just enough to feel confident.

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run ALL of Week 2:
    python3 tests/run_acceptance.py 2

When everything passes, commit and push so your brother can review!
"""


def grid_trace(grid):
    """
    Return a list of all values from the grid, left-to-right, top-to-bottom.
    Same idea as flatten.
    Example: grid_trace([[1, 2], [3, 4]]) → [1, 2, 3, 4]
    """
    # >>> YOUR CODE HERE
    list = []
    for row in grid:
        for value in row:
            list.append(value)
    return list


def tallest(people):
    """
    people is a dict of name → height (number).
    Return the name of the tallest person.
    Assume there is at least one person, and no ties.

    Example: tallest({"Ada": 64, "Grace": 66}) → "Grace"
    """
    # >>> YOUR CODE HERE
    tallest = None
    tallest_height = 0
    for name, height in people.items():
        if height > tallest_height:
            tallest_height = height
            tallest = name
    return tallest


def count_above(grid, limit):
    """
    Count how many numbers in the 2-D grid are greater than limit.
    Example: count_above([[1, 5], [3, 9]], 4) → 2
    """
    # >>> YOUR CODE HERE
    count = 0
    for row in grid:
        for value in row:
            if value > limit:
                count += 1
    return count


def first_even(numbers):
    """
    Return the first even number in the list.
    If there is no even number, return None.
    Example: first_even([1, 3, 4, 6]) → 4
             first_even([1, 3, 5]) → None
    """
    # >>> YOUR CODE HERE
    for number in numbers:
        if number % 2 == 0:
            return number
    return None


def build_report(name, score):
    """
    Return a dict with keys "name" and "score".
    Example: build_report("Jeremy", 95) → {"name": "Jeremy", "score": 95}
    """
    # >>> YOUR CODE HERE
    return {"name": name, "score": score}


if __name__ == "__main__":
    print("Day 7 playground (Week 2)")
    print(grid_trace([[1, 2], [3, 4]]))
    print(tallest({"Ada": 64, "Grace": 66}))
    print(count_above([[1, 5], [3, 9]], 4))
    print(first_even([1, 3, 4, 6]))
    print(build_report("Jeremy", 95))
