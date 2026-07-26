"""
Day 2: Creating a class and object
Time goal: about 10–20 minutes

WHAT YOU'RE LEARNING
--------------------
A class is a blueprint. An object is one thing built from that blueprint.

  class Dog:
      def __init__(self, name):
          self.name = name

  buddy = Dog("Buddy")   # create an object
  print(buddy.name)      # "Buddy"

__init__ runs when you create the object.
self means "this object."

YOUR JOB
--------
Fill in the class / functions where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 4 --day 2
"""


class Dog:
    def __init__(self, name):
        """
        Save the name on the object as self.name
        """
        # >>> YOUR CODE HERE
        pass


def make_dog(name):
    """
    Create and return a Dog object with the given name.
    Example: make_dog("Buddy") → a Dog whose .name is "Buddy"
    """
    # >>> YOUR CODE HERE
    pass


def dog_name(dog):
    """
    Return the dog's name (dog.name).
    """
    # >>> YOUR CODE HERE
    pass


def rename_dog(dog, new_name):
    """
    Change dog.name to new_name, then return the dog.
    """
    # >>> YOUR CODE HERE
    pass


class Point:
    def __init__(self, x, y):
        """
        Save x and y as self.x and self.y
        """
        # >>> YOUR CODE HERE
        pass


def make_point(x, y):
    """
    Return a Point with the given x and y.
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 2 playground (Week 4)")
    d = make_dog("Buddy")
    print(dog_name(d))
    rename_dog(d, "Max")
    print(dog_name(d))
    p = make_point(2, 3)
    print(p.x, p.y)
