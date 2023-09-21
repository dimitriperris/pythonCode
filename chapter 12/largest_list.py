# File: largest_list.py
# Description: Determine the largest item out of the given list using recursive. 
# Assignment Name and Number: Largest List Item #4
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def find_largest(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    first = numbers[0]
    rest = numbers[1:]
    largest_in_all = find_largest(rest)
    
    if first > largest_in_all:
        return first
    else:
        return largest_in_all

def main():
    numbers = (1, 24, 37, 41, 11, 67, 32, 81,)
    largest = find_largest(numbers)
    print('The largest value in the list is:', largest)


# Call the main function. 
main()
