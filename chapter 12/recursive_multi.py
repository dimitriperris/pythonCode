# File: recursive_multi.py
# Description: Use recurisve to multiply two arguments. 
# Assignment Name and Number: Recursive Multiplication #2
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def multiply_recursive(x, y):
    if y == 1:
        return x
    else:
        return x + multiply_recursive(x, y - 1)
    
result = multiply_recursive(9, 4)
print('The result of multiplication is:', result)
