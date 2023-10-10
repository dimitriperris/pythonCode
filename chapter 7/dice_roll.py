import random

def roll(number_of_throws):
    return sorted([random.randint(1, 6) 
    for n in range(number_of_throws)])

number_of_throws = int(input('Enter the number of throws: '))
    
if number_of_throws > 0:
    random_numbers = roll(number_of_throws)
    print('Sorted list of random numbers', random_numbers)
else:
    print('Enter a positive integer.')

