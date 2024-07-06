import random

options = ["rock", "paper", "scissor"]
# defining the options

win = 0  # Defining number of wins as 0
loss = 0  # Defining number of losses as 0

for i in range(5):  # USing for loop for playing 5 games
    user_choice = input("Choose an option-rock or paper or scissor: ")
    # asking input from the user
    computer_choice = random.choice(options)
    print("Computers choice:", computer_choice)
    # asking choice of the computer

    # Determining the winner
    if (user_choice == computer_choice):
        print("It's a tie")
    elif (
            user_choice == "rock" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "scissor" or user_choice == "scissor" and computer_choice == "rock"):
        print("You loose!")
        loss += 1
    elif (user_choice == "rock" and computer_choice == "scissor" or
          user_choice == "paper" and computer_choice == "rock" or
          user_choice == "scissor" and computer_choice == "paper"):
        print("You win!")
        win += 1
# number of winnings and loosings
print("You lost", loss, "times")
print("You won", win, "times")
print("You draw ", (5 - (loss + win)), "times")

# Final declaration of the winner
print("Declaration of final winner")
if (win > loss):
    print("You won the game!")
elif (win < loss):
    print("You lost the game!")
else:
    print("It's a draw!")
