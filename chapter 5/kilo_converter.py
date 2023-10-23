# File: kilo_converter.py
# Description: Convert kilometers to miles using the given formula. 
# Assignment Name and Number: Kilometer Converter #1
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    global kilo
    kilo = float(input('Enter the distance in kilometers: '))
    final= kilo_miles()

    print('The conversion of', kilo, 'kilometers to miles is', final, 'miles.')

def kilo_miles():
    miles = kilo * 0.6214
    return miles

main()