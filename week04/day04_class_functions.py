"""
Day 4: Class functions (instance methods vs static)
Time goal: about 10–20 minutes

WHAT YOU'RE LEARNING
--------------------
Instance method: needs an object (uses self).

  def bark(self):
      return self.name + " says woof"

Static-style helper: does not need self / a particular object.
In Python you can mark it with @staticmethod:

  @staticmethod
  def species():
      return "Canis familiaris"

YOUR JOB
--------
Fill in where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 4 --day 4
"""


class Dog:
    def __init__(self, name, energy=5):
        self.name = name
        self.energy = energy

    def bark(self):
        """
        Return: "<name> says woof"
        Example: Dog("Buddy").bark() → "Buddy says woof"
        """
        # >>> YOUR CODE HERE
        pass

    def play(self):
        """
        If energy > 0: subtract 1 from energy and return "fun"
        Else: return "tired"
        """
        # >>> YOUR CODE HERE
        pass

    @staticmethod
    def species():
        """
        Return exactly: dog
        """
        # >>> YOUR CODE HERE
        pass

    @staticmethod
    def describe_age(years):
        """
        Return: "Age: <years>"
        Example: Dog.describe_age(3) → "Age: 3"
        Hint: return "Age: " + str(years)
        """
        # >>> YOUR CODE HERE
        pass


def make_dog(name, energy=5):
    """
    Return a Dog with the given name and energy.
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 4 playground (Week 4)")
    d = make_dog("Buddy", energy=1)
    print(d.bark())
    print(d.play(), d.play())
    print(Dog.species())
    print(Dog.describe_age(3))
