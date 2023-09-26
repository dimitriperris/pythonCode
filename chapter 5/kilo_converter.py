# File: kilo_converter.py
# Description: Convert kilometers to miles using the given formula. 
# Assignment Name and Number: Kilometer Converter #1
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def kilo_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

def main():
    try:
        kilometers = float(input('Enter a distance in kilometers: '))
        miles = kilo_miles(kilometers)
        print('Kilometers', kilometers, 'is equal to miles', miles)
    except ValueError:
        print('Error. Please enter a correct number for kilometers.')

main()
