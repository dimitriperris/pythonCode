
pocket_number = int(input('Enter a pocket number (0-36): '))

if 0 <= pocket_number <= 36:
    if pocket_number == 0:
        print('Pocket', pocket_number, 'is green.')
    elif 1 <= pocket_number <= 10 or 19 <= pocket_number <= 28:
        if pocket_number % 2 == 1:
            print('Pocket', pocket_number, 'is red.')
        else:
            print('Pocket', pocket_number, 'is black.')
    elif 11 <= pocket_number <= 18 or 29 <= pocket_number <= 36:
        if pocket_number % 2 == 1:
            print('Pocket", pocket_number, "is black.')
        else:
            print('Pocket', pocket_number, 'is red.')
else:
    print('Error: Pocket number must be between 0 and 36.')
