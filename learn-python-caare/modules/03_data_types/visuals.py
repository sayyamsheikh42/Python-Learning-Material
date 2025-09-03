# Visualizations for Data Types & Immutability
import matplotlib.pyplot as plt

def visualize_truthiness():
    labels = ["0","1","''","'hi'","[]","[0]","{}","{'x':1}","None"]
    values = [0,1,"","hi",[],[0],{},{"x":1},None]
    truth = [bool(v) for v in values]

    plt.figure()
    plt.bar(range(len(labels)), [1 if t else 0 for t in truth))
    plt.xticks(range(len(labels)), labels, rotation=45)
    plt.title("Truthiness of Common Python Values")
    plt.ylabel("Truth value (1=True, 0=False)")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_truthiness()
