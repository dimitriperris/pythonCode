# File: largest_list.py
# Description: Determine the largest number in a list. 
# Assignment Name and Number: Largest List Item #4
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def find_largest(list):
    max_value = list[0]
    for value in list:
        if value > max_value:
            max_value = value
    return max_value

def main():
    grades = [63, 92, 57, 84]
    
    largest = find_largest(grades)
    print('Largest number in the list:', largest)

main()

