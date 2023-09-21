# File: recursive.py
# Description: Use recursive language that accepts two arguments into x and y. 
# Assignment Name and Number: Recursive Multiplication #2
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    x = 7
    y = 5
    product = recursive_multiply(x, y)
    print('{x} * {y} = {product}')

def recursive_multiply(x, y):
    if y == 1:
        return x
    else:
        return x + recursive_multiply(x, y - 1)

# Call the main function. 
main()
