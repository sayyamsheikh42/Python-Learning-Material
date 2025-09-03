# Modern Python Libraries — Examples (Dataclasses demo)
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    id: int
    name: str

if __name__ == "__main__":
    u = User(1, "Aisha")
    print(u)
