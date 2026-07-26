"""
Acceptance tests for this Python course.

How to use (from the project root folder):

  python3 tests/run_acceptance.py 1           # all Week 1 days
  python3 tests/run_acceptance.py 2 --day 3   # Week 2, only Day 3
  python3 tests/run_acceptance.py 3
  python3 tests/run_acceptance.py 4
  python3 tests/run_acceptance.py             # same as week 1

Your older brother can run the same commands after you push to GitHub.
"""

from __future__ import print_function

import argparse
import importlib
import math
import os
import sys
import traceback


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

WEEK03_DATA = os.path.join(ROOT, "week03", "data")


class TestFailure(Exception):
    pass


def check_equal(actual, expected, label):
    if actual != expected:
        raise TestFailure(
            "{label}: expected {expected!r}, got {actual!r}".format(
                label=label, expected=expected, actual=actual
            )
        )


def check_true(condition, label):
    if not condition:
        raise TestFailure(label)


def check_almost_equal(actual, expected, label, places=7):
    if round(abs(actual - expected), places) != 0:
        raise TestFailure(
            "{label}: expected about {expected!r}, got {actual!r}".format(
                label=label, expected=expected, actual=actual
            )
        )


# ---------------------------------------------------------------------------
# Week 1
# ---------------------------------------------------------------------------

def run_week1_day01():
    m = importlib.import_module("week01.day01_numbers")
    value = m.make_integer()
    check_true(isinstance(value, int) and not isinstance(value, bool), "make_integer() must return an int")
    value = m.make_float()
    check_true(isinstance(value, float), "make_float() must return a float")
    check_equal(m.add_numbers(2, 3), 5, "add_numbers(2, 3)")
    check_equal(m.add_numbers(-1, 4), 3, "add_numbers(-1, 4)")
    check_equal(m.subtract_numbers(10, 4), 6, "subtract_numbers(10, 4)")
    check_equal(m.multiply_numbers(3, 5), 15, "multiply_numbers(3, 5)")
    check_equal(m.divide_numbers(10, 4), 2.5, "divide_numbers(10, 4)")


def run_week1_day02():
    m = importlib.import_module("week01.day02_strings")
    check_equal(m.make_greeting(), "Hello, Python!", "make_greeting()")
    check_equal(m.greet("Jeremy"), "Hello, Jeremy!", "greet('Jeremy')")
    check_equal(m.greet("Ada"), "Hello, Ada!", "greet('Ada')")
    check_equal(m.full_name("Ada", "Lovelace"), "Ada Lovelace", "full_name()")
    check_equal(m.shout("hello"), "HELLO", "shout('hello')")
    check_equal(m.whisper("HELLO"), "hello", "whisper('HELLO')")
    check_equal(m.count_characters("python"), 6, "count_characters('python')")
    check_equal(m.count_characters(""), 0, "count_characters('')")


def run_week1_day03():
    m = importlib.import_module("week01.day03_if_else")
    check_equal(m.is_even(4), True, "is_even(4)")
    check_equal(m.is_even(5), False, "is_even(5)")
    check_equal(m.is_even(0), True, "is_even(0)")
    check_equal(m.is_positive(3), True, "is_positive(3)")
    check_equal(m.is_positive(-1), False, "is_positive(-1)")
    check_equal(m.is_positive(0), False, "is_positive(0)")
    check_equal(m.bigger(3, 10), 10, "bigger(3, 10)")
    check_equal(m.bigger(9, 2), 9, "bigger(9, 2)")
    check_equal(m.bigger(5, 5), 5, "bigger(5, 5)")
    check_equal(m.can_ride(50), "Yes", "can_ride(50)")
    check_equal(m.can_ride(48), "Yes", "can_ride(48)")
    check_equal(m.can_ride(47), "No", "can_ride(47)")
    check_equal(m.letter_grade(95), "A", "letter_grade(95)")
    check_equal(m.letter_grade(90), "A", "letter_grade(90)")
    check_equal(m.letter_grade(82), "B", "letter_grade(82)")
    check_equal(m.letter_grade(70), "C", "letter_grade(70)")
    check_equal(m.letter_grade(50), "Keep practicing", "letter_grade(50)")


def run_week1_day04():
    m = importlib.import_module("week01.day04_lists")
    check_equal(m.make_number_list(), [1, 2, 3, 4, 5], "make_number_list()")
    check_equal(m.first_item(["a", "b", "c"]), "a", "first_item()")
    check_equal(m.last_item(["a", "b", "c"]), "c", "last_item()")
    check_equal(m.list_length(["a", "b", "c"]), 3, "list_length()")
    check_equal(m.add_favorite(["pizza"], "tacos"), ["pizza", "tacos"], "add_favorite()")
    check_equal(m.second_item(["red", "green", "blue"]), "green", "second_item()")


def run_week1_day05():
    m = importlib.import_module("week01.day05_loops")
    check_equal(m.count_to(3), [1, 2, 3], "count_to(3)")
    check_equal(m.count_to(1), [1], "count_to(1)")
    check_equal(m.sum_list([1, 2, 3]), 6, "sum_list([1, 2, 3])")
    check_equal(m.sum_list([]), 0, "sum_list([])")
    check_equal(m.repeat_word("hi", 3), ["hi", "hi", "hi"], "repeat_word()")
    check_equal(m.repeat_word("x", 0), [], "repeat_word(..., 0)")
    check_equal(m.count_evens([1, 2, 3, 4]), 2, "count_evens()")
    check_equal(m.count_evens([1, 3, 5]), 0, "count_evens(odds)")
    check_equal(m.find_max([3, 10, 2]), 10, "find_max()")
    check_equal(m.find_max([-5, -1, -9]), -1, "find_max(negatives)")


def run_week1_day06():
    m = importlib.import_module("week01.day06_review_part1")
    check_equal(m.double_number(7), 14, "double_number(7)")
    check_equal(m.describe_number(3), "positive", "describe_number(3)")
    check_equal(m.describe_number(-2), "negative", "describe_number(-2)")
    check_equal(m.describe_number(0), "zero", "describe_number(0)")
    check_equal(m.make_label("Jeremy", 13), "Name: Jeremy, Age: 13", "make_label()")
    check_equal(m.password_ok("abcdef"), True, "password_ok('abcdef')")
    check_equal(m.password_ok("hi"), False, "password_ok('hi')")
    check_equal(m.choose_snack(True), "Get a snack", "choose_snack(True)")
    check_equal(m.choose_snack(False), "Maybe later", "choose_snack(False)")


def run_week1_day07():
    m = importlib.import_module("week01.day07_review_part2")
    check_equal(m.shopping_total([2.5, 1.25, 3.0]), 6.75, "shopping_total()")
    check_equal(m.shopping_total([]), 0, "shopping_total([])")
    check_equal(
        m.only_long_words(["cat", "lion", "dog", "tiger"]),
        ["lion", "tiger"],
        "only_long_words()",
    )
    check_equal(m.countdown(3), [3, 2, 1], "countdown(3)")
    check_equal(m.countdown(1), [1], "countdown(1)")
    check_equal(m.average([2, 4, 6]), 4.0, "average([2, 4, 6])")
    check_equal(m.fizz_label(15), "FizzBuzz", "fizz_label(15)")
    check_equal(m.fizz_label(9), "Fizz", "fizz_label(9)")
    check_equal(m.fizz_label(10), "Buzz", "fizz_label(10)")
    check_equal(m.fizz_label(7), "7", "fizz_label(7)")


# ---------------------------------------------------------------------------
# Week 2
# ---------------------------------------------------------------------------

def run_week2_day01():
    m = importlib.import_module("week02.day01_2d_lists")
    check_equal(m.make_tiny_grid(), [[1, 2], [3, 4]], "make_tiny_grid()")
    check_equal(m.get_cell([[1, 2], [3, 4]], 1, 0), 3, "get_cell()")
    check_equal(m.row_count([[1, 2], [3, 4], [5, 6]]), 3, "row_count()")
    check_equal(m.column_count([[1, 2, 3], [4, 5, 6]]), 3, "column_count()")
    check_equal(m.first_row([[10, 20], [30, 40]]), [10, 20], "first_row()")
    check_equal(m.sum_row([[1, 2, 3], [4, 5, 6]], 0), 6, "sum_row()")
    check_equal(m.sum_row([[1, 2, 3], [4, 5, 6]], 1), 15, "sum_row(row 1)")


def run_week2_day02():
    m = importlib.import_module("week02.day02_dicts")
    check_equal(m.make_person(), {"name": "Jeremy", "age": 13}, "make_person()")
    check_equal(m.get_value({"color": "blue"}, "color"), "blue", "get_value()")
    check_equal(m.set_score({}, "Ada", 100), {"Ada": 100}, "set_score()")
    scores = {"Ada": 90}
    check_equal(m.set_score(scores, "Grace", 88), {"Ada": 90, "Grace": 88}, "set_score(existing)")
    check_equal(m.has_key({"a": 1}, "a"), True, "has_key(True)")
    check_equal(m.has_key({"a": 1}, "b"), False, "has_key(False)")
    check_equal(m.favorite_color({"name": "Sam", "color": "green"}), "green", "favorite_color()")
    check_equal(m.word_lengths(["hi", "python"]), {"hi": 2, "python": 6}, "word_lengths()")


def run_week2_day03():
    m = importlib.import_module("week02.day03_nested_loops")
    check_equal(m.count_cells([[1, 2], [3, 4], [5, 6]]), 6, "count_cells()")
    check_equal(m.sum_all([[1, 2], [3, 4]]), 10, "sum_all()")
    check_equal(m.make_grid(2, 3, 0), [[0, 0, 0], [0, 0, 0]], "make_grid()")
    check_equal(m.make_grid(1, 1, 7), [[7]], "make_grid(1x1)")
    check_equal(m.flatten([[1, 2], [3, 4]]), [1, 2, 3, 4], "flatten()")
    check_equal(m.multiplication_row(3, 4), [3, 6, 9, 12], "multiplication_row()")


def run_week2_day04():
    m = importlib.import_module("week02.day04_basic_algorithms")
    check_equal(m.contains([1, 2, 3], 2), True, "contains(True)")
    check_equal(m.contains([1, 2, 3], 9), False, "contains(False)")
    check_equal(m.count_occurrences([1, 2, 1, 1], 1), 3, "count_occurrences()")
    check_equal(m.count_occurrences([1, 2, 3], 9), 0, "count_occurrences(0)")
    check_equal(m.find_index(["a", "b", "c"], "b"), 1, "find_index()")
    check_equal(m.find_index(["a", "b", "c"], "z"), -1, "find_index(missing)")
    check_equal(m.reverse_list([1, 2, 3]), [3, 2, 1], "reverse_list()")
    check_equal(m.is_sorted_ascending([1, 2, 2, 5]), True, "is_sorted_ascending(True)")
    check_equal(m.is_sorted_ascending([3, 1, 2]), False, "is_sorted_ascending(False)")
    check_equal(m.is_sorted_ascending([]), True, "is_sorted_ascending([])")
    check_equal(m.is_sorted_ascending([7]), True, "is_sorted_ascending([7])")


def run_week2_day05():
    m = importlib.import_module("week02.day05_functions_basics")
    check_equal(m.say_hello(), "Hello!", "say_hello()")
    check_equal(m.add_two(2, 5), 7, "add_two()")
    check_equal(m.square(4), 16, "square()")
    check_equal(m.describe_today(), "Learning functions", "describe_today()")
    check_equal(m.main(), "Ready: Learning functions", "main()")


def run_week2_day06():
    m = importlib.import_module("week02.day06_functions_params")
    check_equal(m.greet("Ada"), "Friend Ada", "greet(default)")
    check_equal(m.greet("Ada", "Dr."), "Dr. Ada", "greet(title)")
    check_equal(m.power(3), 9, "power(default)")
    check_equal(m.power(2, 3), 8, "power(3)")
    check_equal(m.full_label("Ada", "Lovelace", 36), "Ada Lovelace (36)", "full_label()")
    check_equal(m.apply_discount(100, 10), 90.0, "apply_discount()")
    check_equal(m.average_of_three(2, 4, 6), 4.0, "average_of_three()")


def run_week2_day07():
    m = importlib.import_module("week02.day07_review")
    check_equal(m.grid_trace([[1, 2], [3, 4]]), [1, 2, 3, 4], "grid_trace()")
    check_equal(m.tallest({"Ada": 64, "Grace": 66}), "Grace", "tallest()")
    check_equal(m.count_above([[1, 5], [3, 9]], 4), 2, "count_above()")
    check_equal(m.first_even([1, 3, 4, 6]), 4, "first_even()")
    check_equal(m.first_even([1, 3, 5]), None, "first_even(None)")
    check_equal(m.build_report("Jeremy", 95), {"name": "Jeremy", "score": 95}, "build_report()")


# ---------------------------------------------------------------------------
# Week 3
# ---------------------------------------------------------------------------

def run_week3_day01():
    m = importlib.import_module("week03.day01_files_and_folders")
    check_equal(m.get_extension("notes.txt"), "txt", "get_extension(txt)")
    check_equal(m.get_extension("day01.py"), "py", "get_extension(py)")
    check_equal(m.get_extension("README"), "", "get_extension(none)")
    check_equal(m.is_python_file("day01.py"), True, "is_python_file(True)")
    check_equal(m.is_python_file("notes.txt"), False, "is_python_file(False)")
    check_equal(m.is_notebook_file("lab.ipynb"), True, "is_notebook_file(True)")
    check_equal(m.is_notebook_file("lab.py"), False, "is_notebook_file(False)")
    check_equal(m.file_kind("app.py"), "python", "file_kind(python)")
    check_equal(m.file_kind("lab.ipynb"), "notebook", "file_kind(notebook)")
    check_equal(m.file_kind("notes.txt"), "text", "file_kind(text)")
    check_equal(m.file_kind("data.csv"), "csv", "file_kind(csv)")
    check_equal(m.file_kind("photo.png"), "other", "file_kind(other)")
    check_equal(m.is_data_file("a.txt"), True, "is_data_file(txt)")
    check_equal(m.is_data_file("b.csv"), True, "is_data_file(csv)")
    check_equal(m.is_data_file("c.py"), False, "is_data_file(py)")


def run_week3_day02():
    m = importlib.import_module("week03.day02_reading_files")
    hello = os.path.join(WEEK03_DATA, "hello.txt")
    scores = os.path.join(WEEK03_DATA, "scores.csv")
    text = m.read_whole_file(hello)
    check_true("Hello from a text file!" in text, "read_whole_file() should include the first line")
    check_true("Line three is last." in text, "read_whole_file() should include the last line")
    check_equal(m.count_lines(hello), 3, "count_lines(hello.txt)")
    check_equal(m.read_first_line(hello), "Hello from a text file!", "read_first_line()")
    check_equal(
        m.list_lines(hello),
        ["Hello from a text file!", "This is line two.", "Line three is last."],
        "list_lines()",
    )
    check_equal(m.csv_names(scores), ["Ada", "Grace", "Alan"], "csv_names()")


def run_week3_day03():
    m = importlib.import_module("week03.day03_pull")
    check_equal(m.pull_command(), "git pull", "pull_command()")
    check_equal(m.pull_purpose(), "download updates from GitHub", "pull_purpose()")
    check_equal(m.when_to_pull(), "before you start coding", "when_to_pull()")
    check_equal(m.pull_needs_internet(), True, "pull_needs_internet()")
    check_equal(m.safer_order(), "pull then code", "safer_order()")


def run_week3_day04():
    m = importlib.import_module("week03.day04_commit")
    check_equal(m.stage_all_command(), "git add .", "stage_all_command()")
    check_equal(m.commit_command("Finish day 1"), 'git commit -m "Finish day 1"', "commit_command()")
    check_equal(m.commit_purpose(), "save a snapshot", "commit_purpose()")
    check_equal(m.is_good_message("ok!"), True, "is_good_message(True)")
    check_equal(m.is_good_message("hey"), True, "is_good_message(3 chars)")
    check_equal(m.is_good_message("ab"), False, "is_good_message(too short)")
    check_equal(m.is_good_message(""), False, "is_good_message(empty)")
    check_equal(
        m.two_step_commit("Hi"),
        ["git add .", 'git commit -m "Hi"'],
        "two_step_commit()",
    )


def run_week3_day05():
    m = importlib.import_module("week03.day05_push")
    check_equal(m.push_command(), "git push", "push_command()")
    check_equal(m.push_purpose(), "upload commits to GitHub", "push_purpose()")
    check_equal(
        m.habit_three_steps("Done"),
        ["git add .", 'git commit -m "Done"', "git push"],
        "habit_three_steps()",
    )
    check_equal(m.push_before_or_after_commit(), "after", "push_before_or_after_commit()")
    check_equal(m.brother_can_see_after_push(), True, "brother_can_see_after_push()")


def run_week3_day06():
    m = importlib.import_module("week03.day06_branches")
    check_equal(m.default_branch_name(), "main", "default_branch_name()")
    check_equal(m.create_branch_command("practice"), "git branch practice", "create_branch_command()")
    check_equal(m.switch_branch_command("practice"), "git checkout practice", "switch_branch_command()")
    check_equal(
        m.create_and_switch_command("practice"),
        "git checkout -b practice",
        "create_and_switch_command()",
    )
    check_equal(m.why_branches(), "try changes safely", "why_branches()")


def run_week3_day07():
    m = importlib.import_module("week03.day07_review")
    check_equal(m.describe_extension("a.py"), "python code", "describe_extension(py)")
    check_equal(m.describe_extension("b.ipynb"), "notebook", "describe_extension(ipynb)")
    check_equal(m.describe_extension("c.txt"), "not python", "describe_extension(txt)")
    check_equal(m.line_count_from_text("a\nb\nc"), 3, "line_count_from_text()")
    check_equal(m.line_count_from_text(""), 0, "line_count_from_text(empty)")
    check_equal(
        m.git_habit(),
        ["git add .", 'git commit -m "message"', "git push"],
        "git_habit()",
    )
    check_equal(m.pull_vs_push("download"), "git pull", "pull_vs_push(download)")
    check_equal(m.pull_vs_push("upload"), "git push", "pull_vs_push(upload)")
    check_equal(m.pull_vs_push("dance"), "unknown", "pull_vs_push(unknown)")
    check_equal(m.branch_sentence("main"), "Working on branch: main", "branch_sentence()")


# ---------------------------------------------------------------------------
# Week 4
# ---------------------------------------------------------------------------

def run_week4_day01():
    m = importlib.import_module("week04.day01_libraries")
    check_equal(m.square_root(9), 3.0, "square_root(9)")
    check_equal(m.round_up(3.2), 4, "round_up()")
    check_equal(m.round_down(3.8), 3, "round_down()")
    check_almost_equal(m.circle_area(1), math.pi, "circle_area(1)")
    check_equal(m.hypotenuse(3, 4), 5.0, "hypotenuse(3, 4)")


def run_week4_day02():
    m = importlib.import_module("week04.day02_classes_objects")
    dog = m.make_dog("Buddy")
    check_true(isinstance(dog, m.Dog), "make_dog() must return a Dog")
    check_equal(m.dog_name(dog), "Buddy", "dog_name()")
    renamed = m.rename_dog(dog, "Max")
    check_equal(m.dog_name(renamed), "Max", "rename_dog()")
    point = m.make_point(2, 3)
    check_true(isinstance(point, m.Point), "make_point() must return a Point")
    check_equal(point.x, 2, "Point.x")
    check_equal(point.y, 3, "Point.y")


def run_week4_day03():
    m = importlib.import_module("week04.day03_class_fields")
    m.Player.player_count = 0
    m.Player.team_name = "Tigers"
    a = m.make_player("Ada")
    check_equal(a.name, "Ada", "player.name")
    check_equal(m.get_lives(a), 3, "get_lives(default)")
    check_equal(m.Player.player_count, 1, "player_count after 1")
    b = m.make_player("Grace", lives=2)
    check_equal(m.get_lives(b), 2, "get_lives(custom)")
    check_equal(m.Player.player_count, 2, "player_count after 2")
    check_equal(m.lose_life(a), 2, "lose_life()")
    check_equal(m.lose_life(a), 1, "lose_life() again")
    # drain to zero and ensure no negative
    m.lose_life(a)
    check_equal(m.lose_life(a), 0, "lose_life() floor at 0")
    check_equal(m.get_team_name(), "Tigers", "get_team_name()")
    check_equal(m.set_team_name("Lions"), "Lions", "set_team_name()")
    check_equal(m.get_team_name(), "Lions", "get_team_name() after change")


def run_week4_day04():
    m = importlib.import_module("week04.day04_class_functions")
    d = m.make_dog("Buddy", energy=1)
    check_true(isinstance(d, m.Dog), "make_dog() must return a Dog")
    check_equal(d.bark(), "Buddy says woof", "bark()")
    check_equal(d.play(), "fun", "play(fun)")
    check_equal(d.energy, 0, "energy after play")
    check_equal(d.play(), "tired", "play(tired)")
    check_equal(m.Dog.species(), "dog", "species()")
    check_equal(m.Dog.describe_age(3), "Age: 3", "describe_age()")


def run_week4_day05():
    m = importlib.import_module("week04.day05_hierarchy")
    animal = m.Animal("X")
    check_equal(animal.speak(), "...", "Animal.speak()")
    check_equal(animal.label(), "X the animal", "Animal.label()")
    dog = m.Dog("Buddy")
    check_true(isinstance(dog, m.Animal), "Dog should be an Animal")
    check_equal(dog.speak(), "woof", "Dog.speak()")
    check_equal(dog.label(), "Buddy the dog", "Dog.label()")
    cat = m.Cat("Misty")
    check_equal(cat.speak(), "meow", "Cat.speak()")
    check_equal(cat.label(), "Misty the cat", "Cat.label()")
    zoo = m.make_zoo()
    check_equal(len(zoo), 2, "make_zoo() length")
    check_true(isinstance(zoo[0], m.Dog), "make_zoo()[0] should be Dog")
    check_true(isinstance(zoo[1], m.Cat), "make_zoo()[1] should be Cat")
    check_equal(zoo[0].name, "Buddy", "zoo dog name")
    check_equal(zoo[1].name, "Misty", "zoo cat name")


def run_week4_day06():
    toolbox = importlib.import_module("week04.toolbox")
    check_equal(toolbox.double(5), 10, "toolbox.double()")
    check_equal(toolbox.shout("hi"), "HI", "toolbox.shout()")
    check_equal(toolbox.add_exclaim("hi"), "hi!", "toolbox.add_exclaim()")
    m = importlib.import_module("week04.day06_cross_file")
    check_equal(m.double_list([1, 2, 3]), [2, 4, 6], "double_list()")
    check_equal(m.loud_greeting("Jeremy"), "HELLO JEREMY!", "loud_greeting()")
    check_equal(
        m.scoreboard([1, 2, 3]),
        {"raw": [1, 2, 3], "doubled": [2, 4, 6]},
        "scoreboard()",
    )


def run_week4_day07():
    m = importlib.import_module("week04.day07_review")
    rect = m.Rectangle(2, 3)
    check_equal(rect.area(), 6, "Rectangle.area()")
    check_equal(rect.perimeter(), 10, "Rectangle.perimeter()")
    sq = m.Square(4)
    check_true(isinstance(sq, m.Rectangle), "Square should be a Rectangle")
    check_equal(sq.area(), 16, "Square.area()")
    check_equal(sq.perimeter(), 16, "Square.perimeter()")
    check_almost_equal(m.circle_circumference(1), 2 * math.pi, "circle_circumference()")
    check_equal(m.describe_shape(rect), "area=6", "describe_shape()")


WEEK_TESTS = {
    1: {
        1: ("Day 1 — Numbers", run_week1_day01),
        2: ("Day 2 — Strings", run_week1_day02),
        3: ("Day 3 — If-Else", run_week1_day03),
        4: ("Day 4 — Lists", run_week1_day04),
        5: ("Day 5 — Loops", run_week1_day05),
        6: ("Day 6 — Review Part 1", run_week1_day06),
        7: ("Day 7 — Review Part 2", run_week1_day07),
    },
    2: {
        1: ("Day 1 — 2-D Lists", run_week2_day01),
        2: ("Day 2 — Dicts", run_week2_day02),
        3: ("Day 3 — Nested Loops", run_week2_day03),
        4: ("Day 4 — Basic Algorithms", run_week2_day04),
        5: ("Day 5 — Functions Basics", run_week2_day05),
        6: ("Day 6 — Function Parameters", run_week2_day06),
        7: ("Day 7 — Review", run_week2_day07),
    },
    3: {
        1: ("Day 1 — Files and Folders", run_week3_day01),
        2: ("Day 2 — Reading Files", run_week3_day02),
        3: ("Day 3 — Pull", run_week3_day03),
        4: ("Day 4 — Commit", run_week3_day04),
        5: ("Day 5 — Push", run_week3_day05),
        6: ("Day 6 — Branches", run_week3_day06),
        7: ("Day 7 — Review", run_week3_day07),
    },
    4: {
        1: ("Day 1 — Libraries", run_week4_day01),
        2: ("Day 2 — Classes and Objects", run_week4_day02),
        3: ("Day 3 — Class Fields", run_week4_day03),
        4: ("Day 4 — Class Functions", run_week4_day04),
        5: ("Day 5 — Hierarchy", run_week4_day05),
        6: ("Day 6 — Cross-File", run_week4_day06),
        7: ("Day 7 — Review", run_week4_day07),
    },
}


def run_week(week_number, day_number=None):
    if week_number not in WEEK_TESTS:
        print("No acceptance tests for week {0}.".format(week_number))
        print("Available weeks: {0}".format(", ".join(str(w) for w in sorted(WEEK_TESTS))))
        return 1

    days = WEEK_TESTS[week_number]
    if day_number is not None:
        if day_number not in days:
            print("Week {0} has no day {1}.".format(week_number, day_number))
            return 1
        selected = {day_number: days[day_number]}
    else:
        selected = days

    passed = 0
    failed = 0

    print("=" * 50)
    print("Week {0} acceptance tests".format(week_number))
    print("=" * 50)

    for number in sorted(selected.keys()):
        title, func = selected[number]
        try:
            func()
            print("[PASS] {0}".format(title))
            passed += 1
        except TestFailure as err:
            print("[FAIL] {0}".format(title))
            print("       {0}".format(err))
            failed += 1
        except Exception as err:
            print("[FAIL] {0}".format(title))
            print("       Unexpected error: {0}".format(err))
            print("       (Did you forget to replace `pass` with real code?)")
            if os.environ.get("SHOW_TRACEBACK") == "1":
                traceback.print_exc()
            failed += 1

    print("-" * 50)
    print("Passed: {0}  Failed: {1}".format(passed, failed))
    if failed == 0:
        print("Nice work! All selected tests passed.")
        return 0
    print("Fix the failing functions, then run this again.")
    return 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Run acceptance tests for the Python summer course."
    )
    parser.add_argument(
        "week",
        nargs="?",
        type=int,
        default=1,
        help="Week number to test (default: 1)",
    )
    parser.add_argument(
        "--day",
        type=int,
        default=None,
        help="Optional day number (1-7). If omitted, runs the whole week.",
    )
    args = parser.parse_args(argv)
    return run_week(args.week, args.day)


if __name__ == "__main__":
    sys.exit(main())
