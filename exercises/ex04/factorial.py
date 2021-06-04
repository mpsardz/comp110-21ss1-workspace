"""An exercise in computing the factorial of an int."""

__author__ = "730004269"


# Begin your solution here...

some_int: int = int(input("Choose a number: "))

i: int = 1
total: int = 1
while i <= some_int:
    total *= i
    i += 1

print("Factorial: " + str(total))
