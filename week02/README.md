# Week 2: Fundamentals 2

Welcome back! This week builds on Week 1 — bigger data shapes, smarter loops, and real functions.

## Daily plan (~10–20 minutes each)

| Day | File | Topic |
|-----|------|--------|
| 1 | `day01_2d_lists.py` | 2-D lists (lists inside lists) |
| 2 | `day02_dicts.py` | Dicts (dictionaries — key → value) |
| 3 | `day03_nested_loops.py` | Nested loops (a loop inside a loop) |
| 4 | `day04_basic_algorithms.py` | Basic algorithms (search, count, reverse) |
| 5 | `day05_functions_basics.py` | Functions 1 (basics and `main`) |
| 6 | `day06_functions_params.py` | Functions 2 (parameters and arguments) |
| 7 | `day07_review.py` | Review — mix it all |

## How to do each day

1. Open that day's `.py` file in Cursor.
2. Read the comments at the top (they teach you the idea).
3. Find every line that says `# >>> YOUR CODE HERE` and write code there.
4. Save the file.
5. Check your work (from the project root folder):

```bash
python3 tests/run_acceptance.py 2
```

Or test just one day:

```bash
python3 tests/run_acceptance.py 2 --day 1
```

6. When you're happy, commit and push to GitHub so your brother can check it.

## Tips

- Do **one day at a time**.
- 2-D lists use **two** indexes: `grid[row][col]`.
- Dicts use **keys**, not positions: `person["name"]`.
- If a test fails, read the error — it usually names the function to fix.
