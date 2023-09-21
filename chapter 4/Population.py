# File: Population.py
# Description: Calculate the average size of a population of organisms.  
# Assignment Name and Number: Population #13
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

num_organism = int(input('Enter the starting number of organisms:'))
daily_Inc = float(input('Enter the average daily increase:'))  
days_Multiply = int(input('Enter the number of days to multiply:'))

day = 1
population = num_organism

print('Each days approximate population.')

while day <= days_Multiply:
    print(day, population)
    population += population * (daily_Inc / 100) 
    day += 1

