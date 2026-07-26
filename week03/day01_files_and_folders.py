"""
Day 1: Files and folders (.py vs .ipynb) & (csv, txt)
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
Programs and notes live in files. Common types in this course:

  .py     → Python code file (what you've been editing)
  .ipynb  → Jupyter notebook (code + text cells in a browser-like app)
  .txt    → plain text
  .csv    → "comma-separated values" (spreadsheet-like data as text)

A file's type is usually in its name after the last dot — the extension.

  "notes.txt"     → extension "txt"
  "day01.py"      → extension "py"
  "lab.ipynb"     → extension "ipynb"
  "scores.csv"    → extension "csv"

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 3 --day 1
"""


def get_extension(filename):
    """
    Return the part after the last dot, without the dot.
    If there is no dot, return "".

    Examples:
      get_extension("notes.txt") → "txt"
      get_extension("day01.py") → "py"
      get_extension("README") → ""

    Hint: if "." not in filename: return ""
          return filename.split(".")[-1]
    """
    # >>> YOUR CODE HERE
    pass


def is_python_file(filename):
    """
    Return True if the file ends with .py (extension is "py").
    Example: is_python_file("day01.py") → True
             is_python_file("notes.txt") → False
    """
    # >>> YOUR CODE HERE
    pass


def is_notebook_file(filename):
    """
    Return True if the extension is "ipynb".
    Example: is_notebook_file("lab.ipynb") → True
    """
    # >>> YOUR CODE HERE
    pass


def file_kind(filename):
    """
    Return one of these exact strings based on extension:
      "py"    → "python"
      "ipynb" → "notebook"
      "txt"   → "text"
      "csv"   → "csv"
      anything else → "other"

    Examples:
      file_kind("app.py") → "python"
      file_kind("lab.ipynb") → "notebook"
      file_kind("notes.txt") → "text"
      file_kind("data.csv") → "csv"
      file_kind("photo.png") → "other"
    """
    # >>> YOUR CODE HERE
    pass


def is_data_file(filename):
    """
    Return True if the file is txt OR csv (common simple data files).
    Example: is_data_file("a.txt") → True
             is_data_file("b.csv") → True
             is_data_file("c.py") → False
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 1 playground (Week 3)")
    for name in ["day01.py", "lab.ipynb", "notes.txt", "data.csv", "photo.png", "README"]:
        print(name, "→", get_extension(name), file_kind(name))
