"""Defining a simple class."""

class Person:
    """Representation of a person."""
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name 
        self.age = age
    
    def __repr__(self) -> str:
        """Provides a string representation of a person object."""
        representation: str = f"{self.name} is a person who is {self.age} years old."
        return representation

kaki: Person = Person("kaki", 72)
print(kaki)
melanie: Person = Person("Melanie", 40)
print(melanie)




