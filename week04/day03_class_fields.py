"""
Day 3: Changing class fields (instance vs shared)
Time goal: about 10–20 minutes

WHAT YOU'RE LEARNING
--------------------
Instance field: belongs to ONE object (usually set with self.something).

  self.lives = 3

Shared (class) field: belongs to the class; all objects can see the same value.
In other languages people sometimes say "static" for this idea.

  class Player:
      team_name = "Tigers"   # shared
      def __init__(self, name):
          self.name = name   # instance

YOUR JOB
--------
Fill in where you see:
    # >>> YOUR CODE HERE

Then run:
    python3 tests/run_acceptance.py 4 --day 3
"""


class Player:
    team_name = "Tigers"  # shared by all Player objects
    player_count = 0      # shared counter

    def __init__(self, name, lives=3):
        """
        Set self.name and self.lives.
        Also increase Player.player_count by 1.
        """
        # >>> YOUR CODE HERE
        pass


def make_player(name, lives=3):
    """
    Return a new Player.
    """
    # >>> YOUR CODE HERE
    pass


def get_lives(player):
    """
    Return player.lives
    """
    # >>> YOUR CODE HERE
    pass


def lose_life(player):
    """
    Subtract 1 from player.lives (do not go below 0), then return player.lives.
    """
    # >>> YOUR CODE HERE
    pass


def get_team_name():
    """
    Return the shared team name from the Player class.
    Hint: return Player.team_name
    """
    # >>> YOUR CODE HERE
    pass


def set_team_name(new_name):
    """
    Change the shared Player.team_name to new_name.
    Then return Player.team_name.
    """
    # >>> YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Day 3 playground (Week 4)")
    Player.player_count = 0
    Player.team_name = "Tigers"
    a = make_player("Ada")
    b = make_player("Grace", lives=2)
    print(a.name, get_lives(a), Player.player_count)
    print(lose_life(a))
    print(get_team_name())
    print(set_team_name("Lions"))
