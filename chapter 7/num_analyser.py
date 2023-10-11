# File: num_analyser.py
# Description: Design a program that asks the user to enter a series of 20 numbers
# Assignment Name and Number: Number Analysis Program #4
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

numbers = []

for n in range(20):
    try:
        number = float(input(f'Enter number {n + 1}: '))
        numbers.append(number)
    except ValueError:
        print('Invalid input. Please enter a valid number.')

if numbers:
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print('Lowest number:', lowest)
    print('Highest number:', highest)
    print('Total of the numbers:', total)
    print('Average of the numbers:', average)


