import random
number = random.randint(1, 10)
while True:
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == number:
        print("Correct! You won!")
        break
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
