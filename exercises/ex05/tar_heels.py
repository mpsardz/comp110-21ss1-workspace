"""Tar Heels exercise redux as a structured program."""

__author__ = "730004269"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))

def tar_heels(choice: int) -> str:
    if (choice % 2 == 0 and choice % 7 == 0):
        return("TAR HEELS")
    elif (choice % 2 == 0):
        return("TAR")
    elif (choice % 7 == 0):
        return ("HEELS")
    else:
        return("CAROLINA")

if __name__ == "__main__":
    main()