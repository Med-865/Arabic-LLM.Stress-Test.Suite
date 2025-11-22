import os
import glob

import matplotlib.pyplot as plt
import pandas as pd


RESULTS_DIR = "results"


def get_latest_results_file():
    files = glob.glob(os.path.join(RESULTS_DIR, "results_*.csv"))
    if not files:
        raise FileNotFoundError("No results_*.csv files found in 'results/' directory.")
    files.sort()
    return files[-1]


def main():
    latest = get_latest_results_file()
    print(f"Loading results from: {latest}")
    df = pd.read_csv(latest)

    summary = df.groupby("category")["score"].mean().reset_index()

    print("\nCategory scores:")
    print(summary)

    plt.figure(figsize=(8, 4))
    plt.bar(summary["category"], summary["score"])
    plt.ylim(0, 1)
    plt.title("ALSTS Category Scores")
    plt.xlabel("Category")
    plt.ylabel("Mean Score")
    plt.tight_layout()
    plt.show()


