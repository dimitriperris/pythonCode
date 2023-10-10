# File: valid_number_info.py
# Description: Design a function that uses a list that contains the numbers 0 to 100 from the given list. 
# Assignment Name and Number: Valid Number Information #1
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.


numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

valid_numbers = [num for num in numbers if 0 <= num <= 100]

total = sum(valid_numbers)
average = total / len(valid_numbers) if valid_numbers else 0

print('Valid Numbers:', valid_numbers)
print('Total of Valid Numbers:', total)
print('Average of Valid Numbers:', average)

