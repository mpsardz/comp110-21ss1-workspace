"""Examples of vectorized operations."""

from __future__ import annotations
from typing import Union

class StrArray:
    """Utility class for common string operations."""
    values: list(str)

    def __init__(self, v: list[str]):
        """Init a StrArray object."""
        self.values = v

    def __repr__(self) -> str:
        """String representaion of a StrArray object."""
        return f"StrArray({self.values})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        print(f"__add__ is being called {self} and {rhs}")
        new_values:  list[str] = []
        if isinstance(rhs, str):
            for item in self.values:
                new_values.append(item + rhs)
        else:
            assert len(self.value) == len(rhs.values)
            #new_values: list[str] = []
            for i in range(len(self.values)):
                new_values.append(self.values[i] + rhs.values[i])
            return StrArray(new_values)


s: StrArray = StrArray(["a", "b", "c"])
t: StrArray = StrArray(["d", "e", "f"])
print(s)

print(s + "!")
print(s + t)

first = StrArray(["Kris", "Kaki", "Claire", "Marc"])
last = StrArray(["Jordan", "Ryan", "Helms", "Lewis"])
full_name = last + "," + first
print(full_name)

