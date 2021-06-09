"""A problematic function!"""

def f(a: int) -> str:
    if a >= 2:
        print("Hi")
        if a % 2 == 0:
            return "yay its even"

    return "unreachable"
 