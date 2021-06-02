"""A problematic function!"""

def f(a: int) -> str:
    if a >= 2:
        return"Greater than or eq to 2"
    else:
        return "less than"
    return "unreachable"