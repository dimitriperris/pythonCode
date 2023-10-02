# File: rock_paper_scissors.py
# Description: Write a function that accepts an object's falling time in seconds. 
# Assignment Name and Number: Rock, Paper, Scissors Game #21
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random 

def find_computer_choice():
    computer_choice= random.randint(1,3)
    if computer_choice == 1: 
        print('Rock')
    elif computer_choice == 2:
        print('Paper')
    else: 
        print('Scissors')

def find_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win, rock beats scissors.') 
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win, scissors bat paper.') 
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win, paper beats rock.') 
    else:
        print('Computer wins!') 

def main():
    user_choice = input('Enter rock, paper, or scissors: ')
    computer_choice = find_computer_choice()
    print('Computer chooses', computer_choice)
    
    result = find_winner(computer_choice, user_choice)
    print(result)

main()


    
