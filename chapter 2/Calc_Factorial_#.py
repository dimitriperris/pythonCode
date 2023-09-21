# File: Calc_Factorial_#.py
# Description: Calculate the factorial of a nonngeative number.  
# Assignment Name and Number: Calculate the Factorial of a Number #12
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

number = int(input("Enter a positive integer:"))
factorial = 1

if number >= 0:
    for i in range(1, number + 1):
        factorial *= i
    print('=',factorial)
else:
    print("Please enter a nonnegative integer.")
