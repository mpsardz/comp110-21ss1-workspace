"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730004269"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print(fortune_cookie())

def fortune_cookie() -> str:
    x = randint(1,4)
    if x == 1:
        return("You will have the best day ever!")
    elif x == 2:
        return ("There is a wonderful surprsing waiting for you around the corner!")
    elif x == 3:
        return ("You will soon accomplish something great!")
    else:
        return("Life is about to get a little twisted!")

if __name__ == "__main__":
    main()