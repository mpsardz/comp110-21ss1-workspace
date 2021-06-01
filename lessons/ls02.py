

print("Guess a number!")


guess: int = int(input("Guess: "))

if guess == 8:
    print("correct")
elif guess == 7:
    print("SO close, add 1!")
elif guess > 8:
    print("Lower!")
else: 
    print("higher")

print("Game over")

