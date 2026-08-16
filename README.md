# 🔢 Sorting Algorithm Benchmarker

A terminal-based tool for benchmarking and comparing classic sorting algorithms across different dataset types and sizes. Get clean, visual, ranked results with relative performance bars right in your console.

## Features

- **7 classic sorting algorithms**: Bubble, Selection, Insertion, Shell, Merge, Quick, and Heap Sort
- **5 dataset types**: Random, Sorted, Reversed, Nearly Sorted, and datasets with many duplicates
- **4 benchmark modes**:
  - **Quick Benchmark** — run all algorithms on random data of a chosen size
  - **Custom Benchmark** — pick specific algorithms, a dataset type, and a size
  - **Full Comparison** — every algorithm against every dataset type, with an overall summary
  - **Head-to-Head** — race two algorithms directly against each other across all dataset types
- Results are ranked with medal emojis (🥇🥈🥉🐢) and rendered as relative performance bars
- Each timing is the best of 3 runs to reduce measurement noise
- Custom dataset sizes supported (10 – 50,000 elements)

## Requirements

- Python 3.6+
- No external dependencies (uses only the standard library: `time`, `random`)

## Usage

Run the script from your terminal:

```bash
python main.py
```

You'll be presented with a menu:

```
MAIN MENU
  [1] Quick benchmark  (random data, choose size)
  [2] Custom benchmark (choose algo + size + data)
  [3] Full comparison  (all datasets, all algos)
  [4] Head-to-head     (two algorithms, race!)
  [Q] Quit
```

Follow the prompts to select algorithms, dataset sizes, and dataset types.

### Preset dataset sizes

| Option | Size    |
|--------|---------|
| 1      | 100     |
| 2      | 500 *(recommended start)* |
| 3      | 1,000   |
| 4      | 5,000   |
| C      | Custom (10 – 50,000) |

### Dataset types

| Type          | Description                                  |
|---------------|-----------------------------------------------|
| Random        | Uniformly random values                       |
| Sorted        | Already in ascending order                     |
| Reversed      | Fully descending order (worst case for many algorithms) |
| Nearly Sorted | Sorted with a small number of random swaps     |
| Many Dupes    | Values drawn from a small range, so lots of repeats |

## Example Output

```
    ⏳  Bubble Sort         120.4 ms
    ⏳  Quick Sort          0.812 ms

  RANK  ALGORITHM          TIME         BAR (relative)
  🥇    Quick Sort         0.812 ms     █░░░░░░░░░░░░░░░░░░░  148.3x faster than slowest
  🐢    Bubble Sort        120.4 ms     ████████████████████
```

## How It Works

- Each algorithm sorts a **copy** of the generated dataset so runs don't affect each other.
- `benchmark()` times each algorithm 3 times and keeps the fastest run.
- Results are sorted by time and rendered with a proportional bar (`make_bar`) relative to the slowest result in that comparison.
- In **Full Comparison** mode, per-dataset results are also averaged into an overall summary ranking.

## Notes on Performance

Simple O(n²) algorithms (Bubble, Selection, Insertion Sort) will be dramatically slower on larger datasets — expect multi-second runtimes at 5,000+ elements. Start with smaller sizes (100–500) if you're including these algorithms, or stick to Shell/Merge/Quick/Heap Sort for larger comparisons.