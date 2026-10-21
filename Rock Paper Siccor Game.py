import random
choices = ("rock", "paper", "scissors")
while True:
    user = input("Choose rock, paper, scissors or exit: ").lower()
    if user == "exit":
        print("Exit")
        break
    if user not in choices:
        print("Invalid choice")
        continue
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
