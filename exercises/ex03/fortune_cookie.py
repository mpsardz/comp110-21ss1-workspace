"""Program that outputs one of at least four random, good fortunes."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...


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