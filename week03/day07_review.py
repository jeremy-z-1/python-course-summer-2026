"""
Day 7: Week 3 Review
Time goal: about 15 minutes

WHAT YOU'RE DOING
-----------------
Mix file types, reading files, and the Git habit words.

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run ALL of Week 3:
    python3 tests/run_acceptance.py 3
"""


def describe_extension(filename):
    """
    Return "python code" if extension is py,
    "notebook" if ipynb,
    otherwise "not python".

    Examples:
      describe_extension("a.py") → "python code"
      describe_extension("b.ipynb") → "notebook"
      describe_extension("c.txt") → "not python"
    """
    # >>> YOUR CODE HERE
    pass


def line_count_from_text(text):
    """
    text is a whole-file string.
    Return how many lines it has when split on newline.
    If text is empty, return 0.
    Hint: if text == "": return 0
          return len(text.splitlines())
    """
    # >>> YOUR CODE HERE
    pass


def git_habit():
    """
    Return the three everyday commands as a list:
      ["git add .", 'git commit -m "message"', "git push"]

    Use the exact commit message word: message
    so the middle item is: git commit -m "message"
    """
    # >>> YOUR CODE HERE
    pass


def pull_vs_push(action):
    """
    If action is "download", return "git pull"
    If action is "upload", return "git push"
    Otherwise return "unknown"
    """
    # >>> YOUR CODE HERE
    pass


def branch_sentence(name):
    """
    Return: Working on branch: NAME
    Example: branch_sentence("main") → "Working on branch: main"
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 7 playground (Week 3)")
    print(describe_extension("a.py"))
    print(line_count_from_text("a\\nb\\nc"))
    print(git_habit())
    print(pull_vs_push("download"), pull_vs_push("upload"))
    print(branch_sentence("main"))
