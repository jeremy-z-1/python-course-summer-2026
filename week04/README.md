# Week 4: OOP (Object-Oriented Programming)

Final week! You'll use libraries, build classes, and split code across files.

## Daily plan (~10–20 minutes each)

| Day | File | Topic |
|-----|------|--------|
| 1 | `day01_libraries.py` | Libraries (`import math`, …) |
| 2 | `day02_classes_objects.py` | Creating a class and object |
| 3 | `day03_class_fields.py` | Class fields (instance vs shared) |
| 4 | `day04_class_functions.py` | Class functions (methods vs static) |
| 5 | `day05_hierarchy.py` | Hierarchical classes (inheritance) |
| 6 | `day06_cross_file.py` + `toolbox.py` | Cross-file programming |
| 7 | `day07_review.py` | Review |

## How to do each day

1. Open that day's `.py` file.
2. Fill in `# >>> YOUR CODE HERE`.
3. On Day 6, also fill in `toolbox.py` — then import it from `day06_cross_file.py`.
4. Test from the project root:

```bash
python3 tests/run_acceptance.py 4
```

One day:

```bash
python3 tests/run_acceptance.py 4 --day 2
```

5. Commit and push when you're done.

## Tips

- A **class** is the blueprint; an **object** (instance) is one real thing made from it.
- **Instance** fields/methods belong to one object (`self`).
- **Shared / static-style** data can live on the class itself.
- Inheritance: a child class can reuse a parent class (`class Dog(Animal):`).
