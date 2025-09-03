# Visualizations for this module
# IMPORTANT: Use matplotlib only; no seaborn; no style settings or explicit colors unless asked.

import matplotlib.pyplot as plt

def demo_plot():
    xs = list(range(1, 6))
    ys = [x**2 for x in xs]
    plt.figure()
    plt.plot(xs, ys, marker='o')
    plt.title("Example Visualization")
    plt.xlabel("x")
    plt.ylabel("x^2")
    plt.show()

if __name__ == "__main__":
    demo_plot()
