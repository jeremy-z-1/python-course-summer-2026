# Week 3: Organization

This week connects coding with files and GitHub habits (pull, commit, push, branches).

## Daily plan (~10–20 minutes each)

| Day | File | Topic |
|-----|------|--------|
| 1 | `day01_files_and_folders.py` | Files & folders (`.py` vs `.ipynb`, csv, txt) |
| 2 | `day02_reading_files.py` | Reading from a file |
| 3 | `day03_pull.py` | Git pull (download updates) |
| 4 | `day04_commit.py` | Git commit (save a snapshot) |
| 5 | `day05_push.py` | Git push (upload to GitHub) |
| 6 | `day06_branches.py` | Version control — branches |
| 7 | `day07_review.py` | Review |

Sample files for Day 2 live in `week03/data/`.

## How to do each day

1. Open that day's `.py` file in Cursor.
2. Read the comments. Fill in `# >>> YOUR CODE HERE`.
3. Save, then test from the project root:

```bash
python3 tests/run_acceptance.py 3
```

One day only:

```bash
python3 tests/run_acceptance.py 3 --day 2
```

4. Commit and push when you're done so your brother can review.

## Tips

- Days 3–6 are partly **quiz-style**: return the exact command / word the comments ask for.
- Day 2 needs the files in `week03/data/` — don't delete them.
- Real Git practice: after Day 5, try the three-command habit on your own work (`add` → `commit` → `push`).
