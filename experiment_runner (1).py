from algorithms import quick_sort, merge_sort, heap_sort
from data_generator import generate_data
import time
import csv
import os

algorithms = {
    'Quick Sort': quick_sort,
    'Merge Sort': merge_sort,
    'Heap Sort': heap_sort
}

distributions = ['random', 'sorted', 'reversed', 'nearly_sorted']
sizes = [1000, 10000, 100000]
results = []

print("Running experiments...")

for size in sizes:
    for dist in distributions:
        data = generate_data(size, dist)
        for name, func in algorithms.items():
            data_copy = data.copy()
            start = time.time()
            func(data_copy)
            end = time.time()
            elapsed = end - start
            results.append([name, dist, size, elapsed])
            print(f"{name} | {dist} | {size} → {elapsed:.4f}s")

# Save results
os.makedirs("results", exist_ok=True)
with open("results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Algorithm", "Distribution", "Size", "Time"])
    writer.writerows(results)

print("\n✅ Results saved to results/results.csv")
