"""An exercise in remainders and boolean logic."""

__author__ = "730004269"


# Begin your solution here...


some_int: int = int(input("Enter an int: "))
if (some_int % 2 == 0 and some_int % 7 == 0):
    print("TAR HEELS")
elif (some_int % 2 == 0):
    print("TAR")
elif (some_int % 7 == 0):
    print ("HEELS")
else:
    print("CAROLINA")
