import random

def get_user_choice():
    return input("Enter your choice (rock, paper, or scissors): ").lower()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie!'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'You win! Rock beats scissors.'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'You win! Scissors beats paper.'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'You win! Paper beats rock.'
    else:
        return "Computer wins! {computer_choice} beats {user_choice}."

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print("You chose {user_choice}.")
    print("Computer chose {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
