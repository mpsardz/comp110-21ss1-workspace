"""An example function definition."""

def my_max(a: int, b: int) -> int:
    """Returns the largest parameter."""
    if a >= b: 
        return a
    else:
        return b


arg_1: int = int(input("First arg: "))
arg_2: int = int(input("Second arg: "))
print(my_max(arg_1, arg_2))


 