# Data Types & Immutability — Examples

def identity_vs_equality():
    a = [1,2,3]
    b = [1,2,3]
    c = a
    print("a == b:", a == b)     # values equal
    print("a is b:", a is b)     # different objects
    print("a is c:", a is c)     # same object

def boolean_truthiness():
    values = [0, 1, "", "hi", [], [0], {}, {"x": 1}, None]
    for v in values:
        print(repr(v).ljust(8), "=>", bool(v))

def immutability():
    t = (1,2,3)
    try:
        t[0] = 9
    except TypeError as e:
        print("Tuples are immutable:", e)

if __name__ == "__main__":
    identity_vs_equality()
    boolean_truthiness()
    immutability()
