# Visualizations for OOP Core
import matplotlib.pyplot as plt

def class_vs_instance_plot():
    # Simulate increments from two instances to visualize totals
    instance_a = [0,1,2,3]
    instance_b = [0,1,1,2]
    total = [a+b for a,b in zip(instance_a, instance_b)]
    plt.figure()
    plt.plot(range(len(instance_a)), instance_a, marker='o', label='A.value')
    plt.plot(range(len(instance_b)), instance_b, marker='o', label='B.value')
    plt.plot(range(len(total)), total, marker='o', label='Counter.total')
    plt.title("Instance vs Class Accumulation")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    class_vs_instance_plot()
