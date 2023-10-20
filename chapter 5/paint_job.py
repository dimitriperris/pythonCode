# File: paint_job.py
# Description: Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon 
# Assignment Name and Number: Paint Job Estimator #8
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

import math

def main():
    sqr_ft = float(input('Enter the square feet of wall space to be painted: '))
    paint_price = float(input('Enter the price of paint per gallon: '))

    results(sqr_ft, paint_price)

def results(sqr_ft, paint_price):
    gallons_required = sqr_ft / 112
    hours_required = gallons_required * 8
    paint_cost = gallons_required * paint_price
    labor_charges = hours_required * 35
    total_cost = paint_cost + labor_charges

    print('Gallons of paint required', format(gallons_required, '.2f'))
    print('Hours of labor required', format(hours_required, '.2f'))
    print('Cost of the paint', format(paint_cost, '.2f'))
    print('Labor charges', format(labor_charges, '.2f'))
    print('Total cost of the paint job', format(total_cost, '.2f'))

main()


