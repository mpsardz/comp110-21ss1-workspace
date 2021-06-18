"""A program to determine names over 21."""

__author__ = "730004269"


def main() -> None:
    """The entrypoint of the program, when run as a module."""


# TODO 1: Define the over_21 function, and its logic, here.
def over_21(kids: dict[str, int]) -> list[str]:
    result: list[str] = []
    for kid in kids:
        if kids[kid] < 2001:
            result.append(kid)
    return result


if __name__ == "__main__":
    main()
