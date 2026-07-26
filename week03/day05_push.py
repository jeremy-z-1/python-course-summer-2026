"""
Day 5: Push (upload to GitHub)
Time goal: about 10 minutes

WHAT YOU'RE LEARNING
--------------------
After you commit on your computer, GitHub still doesn't have it until you push:

  git push

The everyday habit becomes:

  git add .
  git commit -m "your message"
  git push

Pull = download updates
Push = upload your commits

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 3 --day 5
"""


def push_command():
    """
    Return exactly: git push
    """
    # >>> YOUR CODE HERE
    pass


def push_purpose():
    """
    Return exactly: upload commits to GitHub
    """
    # >>> YOUR CODE HERE
    pass


def habit_three_steps(message):
    """
    Return the classic three commands as a list, in order,
    using the given commit message.

    Example:
      habit_three_steps("Done")
      → [
          'git add .',
          'git commit -m "Done"',
          'git push',
        ]
    """
    # >>> YOUR CODE HERE
    pass


def push_before_or_after_commit():
    """
    Do you push before or after you commit?
    Return exactly: after
    """
    # >>> YOUR CODE HERE
    pass


def brother_can_see_after_push():
    """
    After a successful push, can your brother usually see the new work on GitHub?
    Return True.
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 5 playground (Week 3)")
    print(push_command())
    print(push_purpose())
    print(habit_three_steps("Done"))
    print(push_before_or_after_commit())
    print(brother_can_see_after_push())
