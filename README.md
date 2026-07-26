# Python Summer Course 2026 — Jeremy

A beginner Python course for summer. Work **one day at a time**. Your older brother can review your code on GitHub after you push.

## What's in this repo

| Folder / file | What it is |
|---------------|------------|
| `week01/` | Week 1 — Fundamentals 1 (7 daily assignments) |
| `week02/` | Week 2 — Fundamentals 2 (7 daily assignments) |
| `week03/` | Week 3 — Organization / files + Git (7 daily assignments) |
| `week04/` | Week 4 — OOP (7 daily assignments) |
| `tests/run_acceptance.py` | Checks your answers automatically |
| `Jeremy Python Course.docx` | Original course outline |

---

## Course overview (from the course doc)

### Week 1: Fundamentals 1
1. Integers vs doubles vs floats  
2. Strings  
3. If-else  
4. Arrays (in Python: **lists**)  
5. Loops  
6. Review (Part 1)  
7. Review (Part 2)

### Week 2: Fundamentals 2
1. 2-D lists  
2. Dicts  
3. Nested loops  
4. Basic algorithms  
5. Functions 1 (basics and main)  
6. Functions 2 (parameters and arguments)  
7. Review

### Week 3: Organization
1. Files and folders (`.py` vs `.ipynb`) & csv/txt  
2. Reading from a file  
3. Pull  
4. Commit  
5. Push  
6. Version control (branches)  
7. Review

### Week 4: OOP
1. Libraries  
2. Creating a class and object  
3. Changing class fields (static vs dynamic)  
4. Class functions (static vs dynamic)  
5. Hierarchical classes  
6. Cross-file programming  
7. Review

---

## How to do a week

1. Open that week's folder README (example: `week02/README.md`).
2. Each day, open that day's file (example: `week02/day01_2d_lists.py`).
3. Read the comments. Find `# >>> YOUR CODE HERE` and write your code there.
4. Save the file.
5. From the project root, run the tests for that week:

```bash
python3 tests/run_acceptance.py 2
```

Only one day:

```bash
python3 tests/run_acceptance.py 2 --day 1
```

Swap `2` for `1`, `3`, or `4` depending on the week.

6. When tests pass (or even if you're stuck and want help), **upload to GitHub** so your brother can check your work.

---

## How to upload your work to GitHub

You already connected this folder to:

**https://github.com/jeremy-z-1/python-course-summer-2026**

### Every time you finish work (the habit)

Open the terminal in Cursor (make sure you are in this project folder), then run these three commands:

```bash
git add .
git commit -m "Describe what you finished, like: Finish day 1 numbers"
git push
```

What those mean:

1. **`git add .`** — stage all your changed files (get them ready)  
2. **`git commit -m "..."`** — save a snapshot with a short message  
3. **`git push`** — upload that snapshot to GitHub  

Then your brother can open the GitHub website and see your latest code.

### If Git asks you to log in

Use your GitHub username. For the password, GitHub often wants a **Personal Access Token**, not your normal password. Ask your brother or a parent to help create one if needed, or use **GitHub Desktop** (easier clicks): https://desktop.github.com

### Check that it worked

1. Go to https://github.com/jeremy-z-1/python-course-summer-2026  
2. Refresh the page  
3. You should see your folders (`week01`–`week04`, `tests`, etc.)

---

## How your brother can check your work

1. Open the repo on GitHub (or `git pull` on his computer).  
2. Run the week you want to check:

```bash
python3 tests/run_acceptance.py 1
python3 tests/run_acceptance.py 2
python3 tests/run_acceptance.py 3
python3 tests/run_acceptance.py 4
```

3. Look at the day files and leave comments on GitHub if he wants.

### Share the repo with your brother

Someone with access to the repo (you or a parent) should:

1. Open https://github.com/jeremy-z-1/python-course-summer-2026  
2. Click **Settings** → **Collaborators**  
3. Click **Add people**  
4. Type your brother's **GitHub username** and send the invite  
5. He accepts the email / notification  

**Tell me his GitHub username** and I can help walk through inviting him (or try to invite him if the GitHub tools are set up).

---

## Quick start today

```bash
# See the week's README, then open that day's .py file
python3 tests/run_acceptance.py 1 --day 1
```

You should see failures at first — that's normal! Replace each `pass` with real code until you get `[PASS]`.

Have fun. One day at a time.
