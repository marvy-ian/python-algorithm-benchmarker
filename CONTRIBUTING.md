# Contributing to Sorting Algorithm Benchmarker

Thanks for your interest in contributing! This is a small, single-file CLI tool, so contributions are easy to make and easy to review. This guide covers how to get set up and what we look for in a good pull request.

## Getting Started

1. **Fork** the repository and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. **No dependencies to install** — the project uses only the Python standard library (`time`, `random`). Just make sure you have Python 3.6+:
   ```bash
   python --version
   ```
3. Run the script to confirm everything works:
   ```bash
   python main.py
   ```

## Ways to Contribute

- **Add a new sorting algorithm** (e.g. Radix Sort, Tim Sort, Cocktail Sort)
- **Add a new dataset generator** (e.g. all-equal values, few-unique values, already-almost-sorted-in-reverse)
- **Improve output formatting** (tables, colors, export to CSV/JSON)
- **Fix bugs** in timing, ranking, or menu navigation
- **Improve documentation** (README, code comments, examples)
- **Add tests** — the project currently has none, and test coverage is very welcome

## Adding a New Algorithm

To add a new sorting algorithm:

1. Write a function following the existing pattern — it must **not mutate the input list**:
   ```python
   def my_sort(arr):
       a = arr[:]
       # ... sort `a` in place or however you like ...
       return a
   ```
2. Register it in the `ALGORITHMS` list:
   ```python
   ALGORITHMS = [
       ...
       ("My Sort", my_sort),
   ]
   ```
3. That's it — it will automatically appear in all menus (Quick, Custom, Full Comparison, Head-to-Head).

## Adding a New Dataset Type

1. Write a generator function that takes an integer `n` and returns a list of length `n`:
   ```python
   def gen_my_dataset(n):
       return [...]
   ```
2. Register it in the `DATASETS` list:
   ```python
   DATASETS = [
       ...
       ("My Dataset", gen_my_dataset),
   ]
   ```

## Code Style

- Follow the existing style in `main.py` — plain, readable Python, no external formatting tools required.
- Keep functions small and focused, consistent with the current sort/generator/display separation.
- Use descriptive names; match the existing naming conventions (`gen_*` for dataset generators, `_snake_case` for private helpers).
- Prefer clarity over cleverness — this project is partly educational, so readable implementations are valued over micro-optimized ones.

## Testing Your Changes

There's no formal test suite yet, but before submitting a PR please manually verify:

- The script runs without errors: `python main.py`
- Each menu option (`1`–`4`) works correctly
- New algorithms produce **correctly sorted output** — an easy way to check:
  ```python
  from main import my_sort
  assert my_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]
  assert my_sort([]) == []
  assert my_sort([1]) == [1]
  ```
- New algorithms and datasets don't crash on edge cases: empty lists, single-element lists, and lists with duplicate values

If you add a test suite (e.g. with `pytest` or `unittest`), that's a welcome contribution on its own — feel free to open a PR just for that.

## Submitting a Pull Request

1. Create a branch for your change:
   ```bash
   git checkout -b feature/my-new-algorithm
   ```
2. Make your changes and commit with a clear, descriptive message:
   ```bash
   git commit -m "Add radix sort algorithm"
   ```
3. Push to your fork and open a pull request against `main`.
4. In your PR description, include:
   - What you changed and why
   - Any new algorithm's time complexity (best/average/worst case)
   - How you tested it

## Reporting Bugs

If you find a bug, please open an issue with:

- A short description of the problem
- Steps to reproduce it (menu choices, dataset size, etc.)
- What you expected to happen vs. what actually happened

## Code of Conduct

Be respectful and constructive. This is a small learning-oriented project — questions and beginner-friendly PRs are welcome.

## Questions?

If anything in this guide is unclear, feel free to open an issue and ask.