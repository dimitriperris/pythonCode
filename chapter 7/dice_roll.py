# File: dice_roll.py
# Description: Write a function named roll that accepts an integer argument number_of_throws. 
# Assignment Name and Number: Dice Rolling Function #6
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

def roll(number_of_throws):
    return sorted([random.randint(1, 6) 
    for n in range(number_of_throws)])

number_of_throws = int(input('Enter the number of throws: '))
    
if number_of_throws > 0:
    random_numbers = roll(number_of_throws)
    print('Sorted list of random numbers', random_numbers)
else:
    print('Enter a positive integer.')

