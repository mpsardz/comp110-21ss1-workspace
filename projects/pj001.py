""" project 00 """

__author__: str = "730004269"

from random import randint


def main () -> None:
    points : int = 0
    player : str = input("What is your name?  ")
    happy : str = "\U0001f600"
    print(happy)
    greet(player)
    print(happy)
    choice : str = input("Would you like to go down the skittles trail, the snickers trail, or the chocolate trail? Type skittles, snickers, or chocolate?")
    if choice == "skittles":
        skittles(points, player)
    elif choice == "snickers":
        snickers(points)
    elif choice == "chocolate":
        chocolate(points, player)
    else:
        print("Please pick one of the three.")
        main()


def skittles(y: int, t: str) -> int:
    y += 1
    print(f"Congrats! { t }  Your total number of candy coins is now { y }")
    part1: str = input("There is a monster in your way. Do you wish to fight it, let it pass, or run? Types fight, pass, or run.")
    if part1 == "fight":
        print( "Yay! You beat the monster and earned another candy coin!")
        y += 1
        return snickers(y)
    else:
        the_end: str = input("Would you like to play again? Types yes or no.")
    if the_end == "yes":
        main()
    else:
        print("Come play again soon!")


def snickers(z: int) -> int:
    z = z + 1
    print(f"Congrats! Your total number of candy coins is now { z }")
    print("Now you must look behind the tree and....")
    r: int = randint(0,3)
    print("And your lucky number is...." + str(r) + "!!!!")
    if r == 0:
        print("you rolled a 0!")
    elif r == 1:
        print("You rolled a 1!")
    elif r == 2:
        print("You rolled a 2!")
    else: 
        print("Oh no - You rolled a 3....You did not make it to the candy castle.")
        print(f"You ended with  { z }  points")
    the_end: str = input("Would you like to play again? Types yes or no.")
    if the_end == "yes":
        main()
    else:
        print("Come play again soon!")

def chocolate(d: int) -> None:
    print( " Oh no! You got stuck in the chocolate river")
    print(f"You ended with { d }  points")
    the_end: str = input("Would you like to play again? Types yes or no.")
    if the_end == "yes":
        main()
    else:
        print("Come play again soon!")

def greet(c: str) -> None:
    print(f"Hello { c } ! It is time to start your adventure through the candy forest and hopefully you can make it to the candy castle!! Everytime you pass an obstacle, you will be given a point. You will start with 0 points. Lets go!")

if __name__ == "__main__":
   main()
