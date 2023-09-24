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
