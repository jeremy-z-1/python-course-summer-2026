"""
Day 6: Version control — branches
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
A branch is a separate line of work in Git.

  main (or master)  → the main line of the project
  feature branches  → safe places to try changes

Useful commands (learn the words; you may not need them every day yet):

  git branch                 → list branches
  git branch my-idea         → create a branch named my-idea
  git checkout my-idea       → switch to that branch
  git checkout -b my-idea    → create AND switch in one step
  git checkout main          → go back to main

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 3 --day 6
"""


def default_branch_name():
    """
    In this course / on modern GitHub, the usual main branch name is:
    Return exactly: main
    """
    # >>> YOUR CODE HERE
    pass


def create_branch_command(name):
    """
    Return the command that creates a branch with the given name
    (without switching yet).
    Example: create_branch_command("practice") → git branch practice
    """
    # >>> YOUR CODE HERE
    pass


def switch_branch_command(name):
    """
    Return the command that switches to an existing branch.
    Example: switch_branch_command("practice") → git checkout practice
    """
    # >>> YOUR CODE HERE
    pass


def create_and_switch_command(name):
    """
    Return the create-and-switch command.
    Example: create_and_switch_command("practice") → git checkout -b practice
    """
    # >>> YOUR CODE HERE
    pass


def why_branches():
    """
    Return exactly: try changes safely
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 6 playground (Week 3)")
    print(default_branch_name())
    print(create_branch_command("practice"))
    print(switch_branch_command("practice"))
    print(create_and_switch_command("practice"))
    print(why_branches())
