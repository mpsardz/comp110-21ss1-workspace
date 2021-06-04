"""Repeating a beat in a loop."""

__author__ = "730004269"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))

repeat: int = int(input("How many times do you want to repeat it? "))

i: int = 1
while i <= repeat:
    print(beat)
    i += 1
if repeat <= 1:
    print("No beat...")