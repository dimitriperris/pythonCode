# File: pennies_day.py
# Description: Calculate the amount of money a person would earn over a period of time in pennies. 
# Assignment Name and Number: Pennies for Pay #7
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

number_of_days= int(input('Enter the number of days worked.:'))
salary= 0.01

for day in range(1, number_of_days + 1):
    salary *= 2.0
    print('Day', day, 'salary $', salary)
print('Your salary on day', number_of_days, 'would be $', salary)
          

