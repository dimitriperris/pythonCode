# File: cal_fat_carbs.py
# Description: Make calculations converting calories from fat and carbs. 
# Assignment Name and Number: Calories from Fat and Carbohydrates #6
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def calc_calories_to_fat(fat_grams):
    return fat_grams * 9

def calc_calories_to_carbs(carb_grams):
    return carb_grams * 4

def main():
    try:
        fat_grams = float(input('Enter the number of fat grams consumed in a day: '))
        carb_grams = float(input('Enter the number of carbohydrate grams consumed in a day: '))
        
        calories_from_fat = calc_calories_to_fat(fat_grams)
        calories_from_carbs = calc_calories_to_carbs(carb_grams)
        
        print('Calories from fat', calories_from_fat, 'calories.')
        print('Calories from carbohydrates', calories_from_carbs,'calories.')
    except ValueError:
        print('Error. Please enter the correct number for fat and carbohydrate grams.')

main()
