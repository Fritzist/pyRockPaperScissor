import random

def checkWin(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"

    elif player_choice == "scissor":
        if computer_choice == "rock":
            return "You lose!"
        elif computer_choice == "paper":
            return "You win!"

    elif player_choice == "rock":
        if computer_choice == "paper":
            return "You lose!"
        elif computer_choice == "scissor":
            return "You win!"

    elif player_choice == "paper":
        if computer_choice == "scissor":
            return "You lose!"
        elif computer_choice == "rock":
            return "You win!"

def compChoose():
    comChoice = random.choice(["scissor", "rock", "paper"])
    return comChoice

print("Welcome to 'Rock, Paper, Scissor'!")

while True:
    player_choice = input("You choose: ").lower()

    if player_choice not in ["scissor", "rock", "paper"]:
        print("Invalid input. Please choose scissor, rock or paper.")
        continue

    computer_choice = compChoose()

    print(f"Computer chooses: {computer_choice}")

    result = checkWin(player_choice, computer_choice)
    print(f"Result: {result}\n")

    play_again = input("Do you want to play again? (yes/y/no/n): ").lower()
    if play_again == "no" or play_again == "n":
        print("thanks for playing!")
        break