# File: rainfall.py
# Description: Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# Assignment Name and Number: Rainfall Statistics #3
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

rainfall_data = []

for month in range(1, 13):
    rainfall = float(input(f'Enter rainfall for month {month}:'))
    rainfall_data.append(rainfall)

total_rainfall = sum(rainfall_data)
max_month = rainfall_data.index(max(rainfall_data)) + 1
min_month = rainfall_data.index(min(rainfall_data)) + 1

average_rainfall = total_rainfall / 12

print('Yearly Rainfall Statistics:')
print('Total Rainfall', total_rainfall, 'inches')
print('Average Monthly Rainfall', average_rainfall, 'inches')
print('Month with Highest Rainfall: Month', max_month)
print('Month with Lowest Rainfall: Month', min_month)

