"""
Acceptance tests for this Python course.

How to use (from the project root folder):

  python3 tests/run_acceptance.py 1           # all Week 1 days
  python3 tests/run_acceptance.py 1 --day 3   # only Day 3
  python3 tests/run_acceptance.py             # same as week 1 for now

Your older brother can run the same commands after you push to GitHub.
"""

from __future__ import print_function

import argparse
import importlib
import os
import sys
import traceback


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


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


def run_day01():
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


def run_day02():
    m = importlib.import_module("week01.day02_strings")
    check_equal(m.make_greeting(), "Hello, Python!", "make_greeting()")
    check_equal(m.greet("Jeremy"), "Hello, Jeremy!", "greet('Jeremy')")
    check_equal(m.greet("Ada"), "Hello, Ada!", "greet('Ada')")
    check_equal(m.full_name("Ada", "Lovelace"), "Ada Lovelace", "full_name()")
    check_equal(m.shout("hello"), "HELLO", "shout('hello')")
    check_equal(m.whisper("HELLO"), "hello", "whisper('HELLO')")
    check_equal(m.count_characters("python"), 6, "count_characters('python')")
    check_equal(m.count_characters(""), 0, "count_characters('')")


def run_day03():
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


def run_day04():
    m = importlib.import_module("week01.day04_lists")
    check_equal(m.make_number_list(), [1, 2, 3, 4, 5], "make_number_list()")
    check_equal(m.first_item(["a", "b", "c"]), "a", "first_item()")
    check_equal(m.last_item(["a", "b", "c"]), "c", "last_item()")
    check_equal(m.list_length(["a", "b", "c"]), 3, "list_length()")
    check_equal(m.add_favorite(["pizza"], "tacos"), ["pizza", "tacos"], "add_favorite()")
    check_equal(m.second_item(["red", "green", "blue"]), "green", "second_item()")


def run_day05():
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


def run_day06():
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


def run_day07():
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


WEEK_TESTS = {
    1: {
        1: ("Day 1 — Numbers", run_day01),
        2: ("Day 2 — Strings", run_day02),
        3: ("Day 3 — If-Else", run_day03),
        4: ("Day 4 — Lists", run_day04),
        5: ("Day 5 — Loops", run_day05),
        6: ("Day 6 — Review Part 1", run_day06),
        7: ("Day 7 — Review Part 2", run_day07),
    }
}


def run_week(week_number, day_number=None):
    if week_number not in WEEK_TESTS:
        print("No acceptance tests for week {0} yet.".format(week_number))
        print("Right now only Week 1 is ready.")
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
