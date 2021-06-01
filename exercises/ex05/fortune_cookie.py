"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print("Now, go spread positive vibes!")

print("Your fortune cookie says...")

x = randint(1,4)

if x == 1:
    print("You will have the best day ever!")
elif x == 2:
    print ("There is a wonderful surprsing waiting for you around the corner!")
elif x == 3:
    print ("You will soon accomplish something great!")
else:
    print("Life is about to get a little twisted!")

print("Now, go spread positive vibes!")
# TODO 1: Define your fortune_cookie function here.


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()