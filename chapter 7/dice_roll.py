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
    throws = []
    for i in range(number_of_throws):
        throws.append(random.randint(1, 6))
    return throws

n = int(input("Enter number of throws: "))  
print(roll(n))
