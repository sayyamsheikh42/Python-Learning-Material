# OOP Core — Examples

class Counter:
    total = 0  # class attribute
    
    def __init__(self, start=0):
        self.value = start
    
    def inc(self):
        self.value += 1
        Counter.total += 1
    
    def __repr__(self):
        return f"Counter(value={self.value})"

class LoudCounter(Counter):
    def inc(self):
        super().inc()
        print("Incremented!")

def encapsulation_demo():
    class Secret:
        def __init__(self):
            self.public = "pub"
            self._protected = "prot"
            self.__private = "priv"
        def reveal_private(self):
            return self.__private
    s = Secret()
    print("public:", s.public)
    print("_protected:", s._protected)
    print("private (via method):", s.reveal_private())

if __name__ == "__main__":
    c = Counter()
    c.inc(); c.inc()
    print(c, "total=", Counter.total)
    lc = LoudCounter()
    lc.inc()
    encapsulation_demo()
