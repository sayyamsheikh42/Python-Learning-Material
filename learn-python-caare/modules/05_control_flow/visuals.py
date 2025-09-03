# Visualizations for Control Flow
import matplotlib.pyplot as plt

def branching_bar():
    counts = {"if": 5, "elif": 2, "else": 3}
    names = list(counts.keys())
    vals = list(counts.values())
    plt.figure()
    plt.bar(names, vals)
    plt.title("Branching Blocks Example Counts")
    plt.ylabel("Count")
    plt.show()

if __name__ == "__main__":
    branching_bar()
