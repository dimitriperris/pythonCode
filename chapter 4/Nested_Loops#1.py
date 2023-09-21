# File: Nested_Loops#1.py
# Description: Use nested to loops to draw a specific pattern.  
# Assignment Name and Number: Nested Lopps #14
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

Base_S = 7  

for row in range(Base_S, 0, -1):
    for column in range(row):
        print('*', end='')
    print()
