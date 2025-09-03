# Typing & Static Analysis — Examples
from typing import List, Protocol, TypeVar, Generic

T = TypeVar('T')

class Adder(Protocol):
    def add(self, x: int, y: int) -> int: ...

class IntAdder:
    def add(self, x: int, y: int) -> int:
        return x + y

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item

def sum_list(xs: List[int]) -> int:
    return sum(xs)

if __name__ == "__main__":
    print(sum_list([1,2,3]))
    print(IntAdder().add(2,3))
    print(Box[int](5).item)
