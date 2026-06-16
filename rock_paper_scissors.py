import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)


def decide_winner(user, computer):

    if user == computer:
        print("It's a tie!")

    elif user == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("Computer wins!")

    elif user == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("Computer wins!")

    elif user == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("Computer wins!")

    else:
        print("Invalid input!")


def play_game():

    user_choice = input("Enter rock, paper or scissors: ").lower()

    computer_choice = get_computer_choice()

    print("Your choice:", user_choice)
    print("Computer choice:", computer_choice)

    decide_winner(user_choice, computer_choice)


play_game()