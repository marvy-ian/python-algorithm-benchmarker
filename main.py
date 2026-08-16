import time
import random

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    a = arr[:]
    _quick_sort_helper(a, 0, len(a) - 1)
    return a

def _quick_sort_helper(a, low, high):
    if low < high:
        pi = _partition(a, low, high)
        _quick_sort_helper(a, low, pi - 1)
        _quick_sort_helper(a, pi + 1, high)

def _partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def heap_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        _heapify(a, i, 0)
    return a

def _heapify(a, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l] > a[largest]: largest = l
    if r < n and a[r] > a[largest]: largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        _heapify(a, n, largest)


def shell_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a


def gen_random(n):     return random.sample(range(n * 10), n)
def gen_sorted(n):     return list(range(n))
def gen_reversed(n):   return list(range(n, 0, -1))
def gen_nearly(n):
    a = list(range(n))
    swaps = max(1, n // 20)
    for _ in range(swaps):
        i, j = random.randrange(n), random.randrange(n)
        a[i], a[j] = a[j], a[i]
    return a
def gen_dupes(n):      return [random.randint(0, n // 10) for _ in range(n)]


ALGORITHMS = [
    ("Bubble Sort",    bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Shell Sort",     shell_sort),
    ("Merge Sort",     merge_sort),
    ("Quick Sort",     quick_sort),
    ("Heap Sort",      heap_sort),
]

DATASETS = [
    ("Random",        gen_random),
    ("Sorted",        gen_sorted),
    ("Reversed",      gen_reversed),
    ("Nearly Sorted", gen_nearly),
    ("Many Dupes",    gen_dupes),
]

SIZES = [100, 500, 1000, 5000]

BAR_CHARS = "█▉▊▋▌▍▎▏"


def benchmark(algo_fn, data, runs=3):
    best = float("inf")
    for _ in range(runs):
        d = data[:]
        t0 = time.perf_counter()
        algo_fn(d)
        best = min(best, time.perf_counter() - t0)
    return best


def make_bar(value, max_value, width=20):
    if max_value == 0:
        return "░" * width
    ratio = value / max_value
    filled = int(ratio * width)
    remainder = ratio * width - filled
    bar = "█" * filled
    if filled < width:
        idx = int(remainder * len(BAR_CHARS))
        bar += BAR_CHARS[idx] if idx < len(BAR_CHARS) else " "
        bar += "░" * (width - filled - 1)
    return bar[:width]


def fmt_time(t):
    if t < 0.001:   return f"{t*1000:.3f} ms"
    if t < 1:       return f"{t*1000:.1f} ms"
    return f"{t:.2f} s"


def rank_label(rank, total):
    if rank == 1:     return "🥇"
    if rank == 2:     return "🥈"
    if rank == 3:     return "🥉"
    if rank == total: return "🐢"
    return f"#{rank} "


W = 62

def header(text):
    print()
    print("╔" + "═" * (W - 2) + "╗")
    print("║" + text.center(W - 2) + "║")
    print("╚" + "═" * (W - 2) + "╝")

def section(text):
    pad = W - 4 - len(text)
    print(f"\n  ┌─ {text} " + "─" * pad + "┐")

def divider():
    print("  " + "─" * (W - 2))


def run_single_benchmark(size, dataset_name, dataset_fn, selected_algos):
    data = dataset_fn(size)
    results = []

    print(f"\n  Benchmarking {len(selected_algos)} algorithms on {size:,} elements...")
    print()

    for name, fn in selected_algos:
        print(f"    ⏳  {name:<18}", end="", flush=True)
        t = benchmark(fn, data)
        results.append((name, t))
        print(f"  {fmt_time(t)}")

    results.sort(key=lambda x: x[1])
    max_t = results[-1][1]

    print()
    divider()
    print(f"  {'RANK':<5} {'ALGORITHM':<18} {'TIME':<12} {'BAR (relative)'}")
    divider()

    for i, (name, t) in enumerate(results):
        bar     = make_bar(t, max_t)
        rank    = rank_label(i + 1, len(results))
        speedup = results[-1][1] / t if t > 0 else 1
        note    = f"  {speedup:.1f}x faster than slowest" if i == 0 and len(results) > 1 else ""
        print(f"  {rank:<5} {name:<18} {fmt_time(t):<12} {bar}{note}")

    divider()
    print(f"  🏆  Winner: {results[0][0]}  ({fmt_time(results[0][1])})")
    return results


def run_full_comparison(size, selected_algos):
    header(f"  FULL COMPARISON — {size:,} ELEMENTS  ")

    all_results = {}
    for name, _ in selected_algos:
        all_results[name] = []

    for ds_name, ds_fn in DATASETS:
        section(ds_name)
        data = ds_fn(size)
        row = []
        for name, fn in selected_algos:
            t = benchmark(fn, data)
            all_results[name].append(t)
            row.append((name, t))
        row.sort(key=lambda x: x[1])
        print()
        for i, (name, t) in enumerate(row):
            bar = make_bar(t, row[-1][1], width=14)
            rnk = rank_label(i + 1, len(row))
            print(f"  {rnk:<5} {name:<18} {fmt_time(t):<12} {bar}")

    header("  OVERALL SUMMARY (avg across all datasets)  ")
    summary = [(name, sum(times) / len(times)) for name, times in all_results.items()]
    summary.sort(key=lambda x: x[1])
    max_avg = summary[-1][1]

    print()
    divider()
    print(f"  {'RANK':<5} {'ALGORITHM':<18} {'AVG TIME':<12} {'BAR (relative)'}")
    divider()
    for i, (name, avg) in enumerate(summary):
        bar  = make_bar(avg, max_avg)
        rank = rank_label(i + 1, len(summary))
        print(f"  {rank:<5} {name:<18} {fmt_time(avg):<12} {bar}")
    divider()
    print()


def pick_algorithms():
    print("\n  Available algorithms:\n")
    for i, (name, _) in enumerate(ALGORITHMS, 1):
        print(f"    [{i}] {name}")
    print(f"    [A] All algorithms")
    print()
    choice = input("  Select algorithms (e.g. 1 3 5  or  A): ").strip().upper()

    if choice == "A" or choice == "":
        return ALGORITHMS[:]

    selected = []
    for c in choice.split():
        try:
            idx = int(c) - 1
            if 0 <= idx < len(ALGORITHMS):
                selected.append(ALGORITHMS[idx])
        except ValueError:
            pass
    return selected if selected else ALGORITHMS[:]


def pick_size():
    print("\n  Dataset size:\n")
    for i, s in enumerate(SIZES, 1):
        note = "  ← recommended start" if i == 2 else ""
        print(f"    [{i}] {s:,} elements{note}")
    print(f"    [C] Custom size")
    print()
    choice = input("  Select size [1-4 or C]: ").strip().upper()

    if choice == "C":
        try:
            n = int(input("  Enter size (100 – 50000): ").strip())
            return max(10, min(50000, n))
        except ValueError:
            return 1000
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(SIZES):
            return SIZES[idx]
    except ValueError:
        pass
    return 1000


def pick_dataset():
    print("\n  Dataset type:\n")
    for i, (name, _) in enumerate(DATASETS, 1):
        print(f"    [{i}] {name}")
    print(f"    [A] All (full comparison)")
    print()
    choice = input("  Select dataset [1-5 or A]: ").strip().upper()

    if choice == "A" or choice == "":
        return None
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(DATASETS):
            return DATASETS[idx]
    except ValueError:
        pass
    return None


def main():
    header("   SORTING ALGORITHM BENCHMARKER   ")
    print("""
  Compare 7 classic sorting algorithms across different
  dataset types and sizes. All times show the best of
  3 runs to reduce noise.
""")

    while True:
        print("\n  ══════════════════════════════════════")
        print("  MAIN MENU")
        print("  ══════════════════════════════════════")
        print("    [1] Quick benchmark  (random data, choose size)")
        print("    [2] Custom benchmark (choose algo + size + data)")
        print("    [3] Full comparison  (all datasets, all algos)")
        print("    [4] Head-to-head     (two algorithms, race!)")
        print("    [Q] Quit")
        print()
        choice = input("  Your choice: ").strip().upper()

        if choice == "Q":
            print("\n  Goodbye! Happy sorting. 👋\n")
            break

        elif choice == "1":
            size = pick_size()
            header(f"   QUICK BENCHMARK — RANDOM DATA, {size:,} ELEMENTS   ")
            run_single_benchmark(size, "Random", gen_random, ALGORITHMS)

        elif choice == "2":
            algos   = pick_algorithms()
            size    = pick_size()
            dataset = pick_dataset()
            if dataset is None:
                run_full_comparison(size, algos)
            else:
                ds_name, ds_fn = dataset
                header(f"   CUSTOM BENCHMARK — {ds_name.upper()}, {size:,} ELEMENTS   ")
                run_single_benchmark(size, ds_name, ds_fn, algos)

        elif choice == "3":
            size = pick_size()
            run_full_comparison(size, ALGORITHMS)

        elif choice == "4":
            print("\n  Pick two algorithms to race:\n")
            for i, (name, _) in enumerate(ALGORITHMS, 1):
                print(f"    [{i}] {name}")
            print()
            try:
                a_idx = int(input("  First algorithm  [1-7]: ").strip()) - 1
                b_idx = int(input("  Second algorithm [1-7]: ").strip()) - 1
                if not (0 <= a_idx < len(ALGORITHMS) and 0 <= b_idx < len(ALGORITHMS)):
                    raise ValueError
            except ValueError:
                print("  Invalid choice.")
                continue

            duo = [ALGORITHMS[a_idx], ALGORITHMS[b_idx]]
            size = pick_size()
            header(f"   HEAD-TO-HEAD: {duo[0][0].upper()} vs {duo[1][0].upper()}   ")

            wins = {duo[0][0]: 0, duo[1][0]: 0}
            for ds_name, ds_fn in DATASETS:
                print(f"\n  Dataset: {ds_name}")
                results = []
                data = ds_fn(size)
                for name, fn in duo:
                    t = benchmark(fn, data)
                    results.append((name, t))
                results.sort(key=lambda x: x[1])
                winner, wt = results[0]
                loser,  lt = results[1]
                wins[winner] += 1
                ratio = lt / wt if wt > 0 else 1
                print(f"    🏆 {winner} wins  ({fmt_time(wt)} vs {fmt_time(lt)}, {ratio:.1f}x faster)")

            print()
            divider()
            a, b = duo[0][0], duo[1][0]
            print(f"  Final score:  {a} {wins[a]}  –  {wins[b]} {b}")
            overall_winner = a if wins[a] > wins[b] else (b if wins[b] > wins[a] else "TIE")
            if overall_winner == "TIE":
                print("  It's a TIE! Very evenly matched.")
            else:
                print(f"  Overall winner: 🏆 {overall_winner}")
            divider()

        else:
            print("  Unknown choice. Please try again.")


if __name__ == "__main__":
    main()