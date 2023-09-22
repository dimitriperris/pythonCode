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
    x = 4
    y = 5

def func(x,y):
    if x>0:
        return y + func(x-1,y)
    else:
        return 0
    
main()