"""
Day 5: Hierarchical classes (inheritance)
Time goal: about 15–20 minutes

WHAT YOU'RE LEARNING
--------------------
A child class can inherit from a parent class:

  class Animal:
      def __init__(self, name):
          self.name = name
      def speak(self):
          return "..."

  class Dog(Animal):
      def speak(self):
          return "woof"

Dog is an Animal, but can replace (override) speak().

YOUR JOB
--------
Fill in where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 4 --day 5
"""


class Animal:
    def __init__(self, name):
        # >>> YOUR CODE HERE
        pass

    def speak(self):
        """
        Generic animals say: "..."
        Return exactly: ...
        """
        # >>> YOUR CODE HERE
        pass

    def label(self):
        """
        Return: "<name> the animal"
        Example: Animal("X").label() → "X the animal"
        """
        # >>> YOUR CODE HERE
        pass


class Dog(Animal):
    def speak(self):
        """
        Return exactly: woof
        """
        # >>> YOUR CODE HERE
        pass

    def label(self):
        """
        Return: "<name> the dog"
        """
        # >>> YOUR CODE HERE
        pass


class Cat(Animal):
    def speak(self):
        """
        Return exactly: meow
        """
        # >>> YOUR CODE HERE
        pass

    def label(self):
        """
        Return: "<name> the cat"
        """
        # >>> YOUR CODE HERE
        pass


def make_zoo():
    """
    Return a list with:
      - a Dog named "Buddy"
      - a Cat named "Misty"
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 5 playground (Week 4)")
    zoo = make_zoo()
    for animal in zoo:
        print(animal.label(), "→", animal.speak())
