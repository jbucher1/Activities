import random

# define the possible choices
choices = ["rock", "paper", "scissors"]

# ask the user to input their choice
user_choice = input("Enter your choice (rock/paper/scissors): ")

# generate a random choice for the computer
computer_choice = random.choice(choices)

# print the computer's choice
print(f"Computer chose {computer_choice}.")

# determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice. Please try again.")