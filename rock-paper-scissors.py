import random
user = input("Make Your Move(rock/paper/scissors):").lower()
options = ["rock", "paper", "scissors"]
computer = random.choice(options)
print("Your Choice:", user)
print("Computer Choice:", computer)
if user == computer:
    print("Tie!")
elif user == "rock" and computer == "scissors":
    print("Great job! You Won!")
elif user == "paper" and computer == "rock":
    print("Great job! You Won!")
elif user == "scissors" and computer == "paper":
    print("Great job! You Won!")
elif user in options:
    print("Better Luck Next Time!")
else:
    print("Invalid Input!")
