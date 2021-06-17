"""An exercise with functions and lists."""

__author__ = "730004269"


def main() -> None:
    """The entrypoint of the program, when run as a module."""

def is_prime(a: int) -> bool:
    i = 2
    while a > i:
        if a % i == 0:
            return(False)
        i += 1
    return True

def list_primes(b: int, c: int) -> list[int]:
    
    prime = list[int]
    for num in range(b, c):
        if all(num % i != 0 for i in range(2, num)):
            prime.append(num)
    return prime

    
if __name__ == "__main__":
    main()
