# File: lottery_number_gen.py
# Description: Design a program that generates a seven-digit lottery number. 
# Assignment Name and Number: Lottery Number Generator #2
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

lottery_numbers = []

for n in range(7):
    random_number = random.randint(0, 9)
    lottery_numbers.append(random_number)

print('Lottery Numbers:', end='')
for number in lottery_numbers:
    print(number, end='')

print()  
