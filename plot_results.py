import pandas as pd
import matplotlib.pyplot as plt

def plot():
    df = pd.read_csv('results/results.csv')
    print("Data loaded:")
    print(df.head())
    for size in df['Size'].unique():
        print(f"Plotting size: {size}")
        subset = df[df['Size'] == size]
        plt.figure(figsize=(10, 6))
        for algo in subset['Algorithm'].unique():
            print(f"  Algorithm: {algo}")
            data = subset[subset['Algorithm'] == algo]
            plt.plot(data['Distribution'], data['Time'], marker='o', label=algo)
        plt.title(f'Sorting Time for {size} Elements')
        plt.xlabel('Data Distribution')
        plt.ylabel('Time (seconds)')
        plt.legend()
        plt.savefig(f'graphs/sort_{size}.png')
        plt.show()

plot()