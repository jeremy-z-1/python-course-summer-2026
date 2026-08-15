"""
Day 4: Commit (save a snapshot)
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
A commit is a saved snapshot of your project with a short message.

Usual two steps:
  1. git add .              ← stage (choose) what to include
  2. git commit -m "msg"    ← save the snapshot with message msg

Good messages are short and clear, like:
  Finish day 2 file reading

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 3 --day 4
"""


def stage_all_command():
    """
    Return the command that stages all changes in this folder.
    Exact answer: git add .
    """
    # >>> YOUR CODE HERE
    return "git add ."


def commit_command(message):
    """
    Return the full commit command for the given message.
    Example:
      commit_command("Finish day 1")
      → git commit -m "Finish day 1"

    Hint: return 'git commit -m "' + message + '"'
    """
    # >>> YOUR CODE HERE
    return 'git commit -m "' + message + '"'


def commit_purpose():
    """
    Return exactly: save a snapshot
    """
    # >>> YOUR CODE HERE
    return "save a snapshot"


def is_good_message(message):
    """
    A message is "good enough" for this course if:
      - it is not empty
      - it has at least 3 characters
    Return True/False.
    """
    # >>> YOUR CODE HERE
    if len(message) >= 3:
      return True
    else:
      return False


def two_step_commit(message):
    """
    Return a list of the two commands, in order:
      1) stage all
      2) commit with message

    Example:
      two_step_commit("Hi")
      → ['git add .', 'git commit -m "Hi"']
    """
    # >>> YOUR CODE HERE
    return ['git add .', 'git commit -m "' + message + '"']


if __name__ == "__main__":
    print("Day 4 playground (Week 3)")
    print(stage_all_command())
    print(commit_command("Finish day 1"))
    print(commit_purpose())
    print(is_good_message("ok!"))
    print(two_step_commit("Hi"))
