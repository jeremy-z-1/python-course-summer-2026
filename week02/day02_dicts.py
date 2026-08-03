"""
Day 2: Dicts (dictionaries)
Time goal: about 10–15 minutes

WHAT YOU'RE LEARNING
--------------------
A dict stores pairs of key → value inside curly braces:

  person = {"name": "Jeremy", "age": 13}

Useful ideas:
  person["name"]           → "Jeremy"
  person["age"] = 14       → change / set a value
  "name" in person         → True  (is this key there?)
  list(person.keys())      → ["name", "age"]  (order may vary in very old Python)

Think of a dict like a labeled box: you look things up by name, not by position.

YOUR JOB
--------
Fill in each function where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 2 --day 2
"""


def make_person():
    """
    Return a dict with exactly these keys and values:
      "name" → "Jeremy"
      "age"  → 13
    Example: {"name": "Jeremy", "age": 13}
    """
    # >>> YOUR CODE HERE
    return {"name": "Jeremy", "age": 13}


def get_value(data, key):
    """
    Return the value stored under key in the dict data.
    Example: get_value({"color": "blue"}, "color") → "blue"
    """
    # >>> YOUR CODE HERE
    return data[key]


def set_score(scores, name, points):
    """
    Put points into the scores dict under the key name.
    Then return the scores dict.

    Example:
      set_score({}, "Ada", 100) → {"Ada": 100}
    """
    # >>> YOUR CODE HERE
    scores[name] = points
    return scores


def has_key(data, key):
    """
    Return True if key is in data, otherwise False.
    Hint: return key in data
    Example: has_key({"a": 1}, "a") → True
             has_key({"a": 1}, "b") → False
    """
    # >>> YOUR CODE HERE
    return key in data


def favorite_color(person):
    """
    person is a dict that has a "color" key.
    Return that color.
    Example: favorite_color({"name": "Sam", "color": "green"}) → "green"
    """
    # >>> YOUR CODE HERE
    return person["color"]


def word_lengths(words):
    """
    words is a list of strings.
    Return a NEW dict where each word maps to its length.

    Example:
      word_lengths(["hi", "python"]) → {"hi": 2, "python": 6}

    Hint:
      result = {}
      for word in words:
          result[word] = len(word)
      return result
    """
    # >>> YOUR CODE HERE
    result = {}
    for word in words:
      result[word] = len(word)
    return result


if __name__ == "__main__":
    print("Day 2 playground (Week 2)")
    print(make_person())
    print(get_value({"color": "blue"}, "color"))
    print(set_score({}, "Ada", 100))
    print(has_key({"a": 1}, "b"))
    print(favorite_color({"name": "Sam", "color": "green"}))
    print(word_lengths(["hi", "python"]))
